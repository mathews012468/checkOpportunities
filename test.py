from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

url = "https://www.nyrr.org/getinvolved/volunteer/opportunities?available_only=true&itemId=3EB6F0CC-0D76-4BAF-A894-E2AB244CEB44&limit=8&offset=0&totalItemLoaded=8"
driver.get(url)

while True:
    print("a")
    loadMore = driver.find_element(webdriver.common.by.By.CSS_SELECTOR, "div.button_bar > a")
    print(loadMore.text)
    if "LOAD MORE" not in loadMore.text:
        break

    print("b")
    webdriver.ActionChains(driver).scroll_to_element(loadMore).scroll_by_amount(0,90).perform()
    time.sleep(0.5)
    print("c")
    loadMore.click()
    print("d")
    lastOpportunity = driver.find_elements(webdriver.common.by.By.CSS_SELECTOR, "#results > section")[-1]
    print("e")
    lastDate = lastOpportunity.find_element(webdriver.common.by.By.CSS_SELECTOR, "div > div.role_listing__meta_col > div.role_listing__date")
    print(lastDate.text)
    time.sleep(2)

with open("page_source.html", "w") as page:
    page.write(driver.page_source)
