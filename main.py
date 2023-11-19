import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Instantiate options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Instantiate driver
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
money = 0
check_pane_time = time.time() + 5
stop_time = time.time() + 5 * 60
stop = False


def check_pane():
    for index in range(len(store_items_costs)):
        item_cost = int(store_items_costs[index].split("-")[1].strip())
        if money >= item_cost:
            store_items[index].click()
            break


while not stop:
    cookie.click()

    money = int(driver.find_element(By.ID, "money").text.replace(",", ""))

    store = driver.find_element(By.ID, "store")
    store_items = store.find_elements(By.CSS_SELECTOR, "div b")
    if store_items[len(store_items) - 1]:
        store_items.remove(store_items[len(store_items) - 1])
    store_items.reverse()

    store_items_costs = [item.text.replace(",", "") for item in store_items]

    if time.time() > check_pane_time:
        check_pane()
        check_pane_time = time.time() + 5
    if time.time() > stop_time:
        cookies_per_sec = driver.find_element(By.ID, "cps").text
        print(cookies_per_sec)
        stop = True
