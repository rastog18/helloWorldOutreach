# 📊 LinkedIn Outreach Automation Tool

This Python script uses Selenium to automate the process of:
- Logging into LinkedIn
- Searching companies from a list
- Navigating to their LinkedIn pages
- Scraping the top 6 recruiters (e.g. "Campus Recruiter")
- Saving their name, LinkedIn URL, and designation into a CSV file

---

## 🔧 Requirements

### ✅ Python Libraries
Install them using pip:

```bash
pip install selenium
```

### ✅ Additional Requirements
- [Google Chrome](https://www.google.com/chrome/)
- [ChromeDriver](https://chromedriver.chromium.org/downloads) (Make sure it's compatible with your Chrome version and in your PATH)

---

## 📁 Files Overview

| File                | Purpose |
|---------------------|---------|
| `main_script.py`    | The main automation script (the one you pasted) |
| `Companies.txt`     | Contains a list of companies (one per line, can be numbered like `1. Adobe`) |
| `Outreach.csv`      | The final output with names, LinkedIn URLs, and roles |

---

## ✏️ Setup

1. **Create a `Companies.txt` file**
   - Example:
     ```
     1. Adobe
     2. Databricks
     3. Palantir
     ```

2. **Update your LinkedIn credentials**
   Inside the script, set:
   ```python
   USRNAME = "your_email@example.com"
   PASS = "your_password"
   ```

3. **Customize the search keyword**
   Default is:
   ```python
   KEYWORD = "Campus Recruiter"
   ```
   You can change it to things like `"University Recruiting"`, `"Talent Acquisition"` etc.

---

## 🚀 How to Run
- Option 1: Using PyCharm I personally run this project using PyCharm. Just open the project folder in PyCharm and click the green "Run" button near the main_script.py (or whichever file holds the object.main() call).
This is the most convenient way, especially since the script pauses for manual input during login.
- Option 2: Terminal
```bash
python main_script.py
```

- The browser will open and log you into LinkedIn.
- Once the script opens the LinkedIn login page and enters your credentials, you will be prompted in the terminal:
``` Do the security check for me!```
- At this point, complete any CAPTCHA, 2FA, or LinkedIn verification manually in the browser.
- After you're done, return to the terminal and press Enter. The script is waiting for this input to continue.
- After that, it will start scraping.
- Output will be saved in `Outreach.csv`.

---

## 📌 Notes

- The script scrapes **up to 6 people** per company.
- Make sure your LinkedIn account has access to view the company pages and people tabs.
- This is for educational or internal outreach research only — do not use it for spamming or mass unsolicited outreach.

---

## 🧼 To Reset

If you want to rerun and start fresh:
- Delete `Outreach.csv`
- Re-run the script
