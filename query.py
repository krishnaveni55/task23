import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
paths = r"C:\Users\HP\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://jqueryui.com/droppable/")
time.sleep(3)
iframe = driver.find_element(By.CSS_SELECTOR, ".demo-frame")
driver.switch_to.frame(iframe)
draggable = driver.find_element(By.ID, "draggable")
droppable = driver.find_element(By.ID, "droppable")
actions = ActionChains(driver)
actions.drag_and_drop(draggable, droppable).perform()
time.sleep(5)
print("Drag and drop operation performed successfully.")
driver.quit()
