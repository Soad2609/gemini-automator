from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Load prompts
with open("prompts.txt", "r", encoding="utf-8") as file:
    prompts = [line.strip() for line in file if line.strip()]

# Connect to the open Chrome with remote debugging
options = Options()
options.debugger_address = "127.0.0.1:9222"
driver = webdriver.Chrome(options=options)

# Go to Gemini
driver.get("https://gemini.google.com")
time.sleep(5)  # Let the page load for a few seconds

# Wait until the input area is visible
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
input_area = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.ql-editor")))

# Loop through prompts
for i, prompt in enumerate(prompts):
    print(f"\n🟢 Prompt {i+1}: {prompt}")
    
    try:
        # Clear the input field
        input_area.clear()

        # Type each character quickly with minimal delay
        for char in prompt:
            input_area.send_keys(char)
            time.sleep(random.uniform(0.00005, 0.0001))  # Faster typing speed (reduced delay)

        # Press Enter to submit
        input_area.send_keys(Keys.RETURN)

        # Wait for the response to appear (adjust time as necessary)
        response_area = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.attachment-container.generated-images")))  # Adjust selector based on actual response element
        
        # Optionally, wait for a few more seconds to ensure the response is fully loaded
        time.sleep(random.uniform(3, 5))  # Adjust time based on response time

        # Check if the image has been generated and extract its URL
        image_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "img.loaded")))  # Adjust selector if needed
        image_url = image_element.get_attribute("src")
        print(f"Image generated successfully for Prompt {i+1}. Image URL: {image_url}")

        # Scroll to ensure the page is fully loaded
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    except Exception as e:
        print(f"❌ Error with prompt {i+1}: {e}")

print("\n✅ Done.")
