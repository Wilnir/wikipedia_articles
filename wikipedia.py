from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal")

total_articles = driver.find_elements(By.CSS_SELECTOR, ".hp-statistieken div p")

for article in total_articles:
    number = article.get_attribute("innerText")
    print(number)

driver.quit()
