import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os.path
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WEBPAGE = "https://www.thesoftwarereport.com/the-top-100-software-companies-of-2023/"
LINKELDN = "https://www.linkedin.com/mynetwork/"
COMPANY = "https://www.linkedin.com/company/"
OUTPUT = "Outreach.csv"
USRNAME = ""
PASS = ""
KEYWORD = "Campus Recruiter"


class Linkedln_Follower():

    def __init__(self, *args, **kwargs):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.connections_made = 0
        self.listOfCompanies = None
        self.fileName = None

    def get_list(self):
        try:
            with open("Companies.txt", "r", encoding="utf-8") as file:
                self.listOfCompanies = []
                for line in file:
                    line = line.strip()
                    if not line:
                        continue  # Skip empty lines
                    # Split by '.', then take the part after the number
                    if '.' in line:
                        parts = line.split('.', 1)
                        name = parts[1].strip()
                        self.listOfCompanies.append(name)
                    else:
                        self.listOfCompanies.append(line)
            print(f"[INFO] Loaded {len(self.listOfCompanies)} companies.")
        except FileNotFoundError:
            print("[ERROR] File 'companies.txt' not found.")
            self.listOfCompanies = []

    def login(self):
        self.driver.get(LINKELDN)
        time.sleep(3)
        username = self.driver.find_element(By.ID, "username")
        username.send_keys(USRNAME)
        password = self.driver.find_element(By.ID, "password")
        password.send_keys(PASS, Keys.ENTER)
        input("Do the security check for me!")
        time.sleep(3)
        return

    def create_csv_file(self):
        with open(self.fileName, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "LinkedIn URL", "Designation"])
            writer.writerow("")

    def writeToCsv(self, name, link=None, desig=None):
        file_exists = os.path.isfile(self.fileName)

        with open(self.fileName, mode="a", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([name, link, desig])


    def search_companies(self, comName):
        comLink = COMPANY + comName
        self.driver.get(comLink)
        try:

            # Look for People
            people = self.driver.find_element(By.LINK_TEXT, "People")
            people.click()
            time.sleep(3)
            search = self.driver.find_element(By.ID, "people-search-keywords")
            search.send_keys(KEYWORD, Keys.ENTER)
            time.sleep(6)
            self.driver.execute_script("window.scrollTo(0, 600)")
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(600, 1200)")
            time.sleep(2)

            # extract top 6 people
            wait = WebDriverWait(self.driver, 10)
            people_cards = wait.until(EC.presence_of_all_elements_located((
                By.XPATH,
                "//li[starts-with(@class, 'grid') and contains(@class, 'org-people-profile-card__profile-card-spacing')]"
            )))
            top6 = people_cards[:6]

            for card in top6:
                try:
                    # Name
                    name_elem = card.find_element(By.XPATH, ".//div[contains(@class, 'lt-line-clamp--single-line')]")
                    name = name_elem.text.strip()

                    # Title / Role
                    title_elem = card.find_element(By.XPATH, ".//div[contains(@class, 'lt-line-clamp--multi-line')]")
                    title = title_elem.text.strip()

                    # LinkedIn profile URL
                    link_elem = card.find_element(By.XPATH, ".//a[contains(@href, '/in/')]")
                    profile_url = link_elem.get_attribute("href")

                    # Write to csv
                    self.writeToCsv(name, profile_url, title)

                    print(f"Name: {name}")
                    print(f"Title: {title}")
                    print(f"Profile URL: {profile_url}")
                    print("-" * 50)

                except Exception as e:
                    print(f"[WARN] Could not extract data from a card: {e}")
                    continue
        except Exception as e:
            return
        return None

    def main(self):
        self.fileName = OUTPUT
        self.create_csv_file()
        self.get_list()
        self.login()
        for comp in self.listOfCompanies:
            self.writeToCsv(comp)
            self.search_companies(comp)
        self.driver.close()

object = Linkedln_Follower()
object.main()
