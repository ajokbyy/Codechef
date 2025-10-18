from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

chrome_options = Options()
# Comment out below line for debugging
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(), options=chrome_options)

url = "https://www.mohanfoundation.org/ngos-list.asp"
driver.get(url)

# Wait for browser view and visually check content
time.sleep(10)

# Take screenshot to verify page state
driver.save_screenshot("debug_screen.png")

# Extra scroll, may help reveal lazy content
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

cards = driver.find_elements(By.CSS_SELECTOR, ".col-md-6")
print(f"Found {len(cards)} cards detected.")

ngos = []

for card in cards:
    try:
        ngo_name = card.find_element(By.TAG_NAME, "b").text.strip()
    except:
        continue
    lines = [line.strip() for line in card.text.split('\n') if line.strip()]
    ngo = {
        "name": ngo_name,
        "address": None,
        "state": None,
        "pincode": None,
        "phone": None,
        "email": None,
        "website": None,
    }
    for line in lines:
        if "Pincode" in line:
            ngo["pincode"] = line.split("-")[-1].strip()
        elif "Phone:" in line:
            ngo["phone"] = line.replace("Phone:", "").strip()
        elif "Email:" in line:
            ngo["email"] = line.replace("Email:", "").strip()
        elif "Website:" in line:
            ngo["website"] = line.replace("Website:", "").strip()
        elif any(state in line for state in ["Maharashtra", "West Bengal", "Delhi NCR", "Tamil Nadu", "Karnataka", "Gujarat"]):
            ngo["state"] = line.strip()
        elif any(word in line for word in ["Plot", "House", "Road", "Street", "Lane"]):
            ngo["address"] = line.strip()
    ngos.append(ngo)

if ngos:
    with open("ngos.json", "w", encoding="utf-8") as f:
        json.dump(ngos, f, indent=4, ensure_ascii=False)

driver.quit()
print(f"💾 Saved {len(ngos)} NGOs to ngos.json")
