# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDefaultSuite():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_upr(self):
    self.driver.get("https://pup.staging.hieraug.fr/login")
    self.driver.set_window_size(1536, 920)
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("upr")
    self.driver.find_element(By.ID, "password").send_keys("upr")
    self.driver.find_element(By.XPATH, "//div[@id=\'root\']/form/main/div[2]/div/div[2]/button").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'root\']/div/main/div[2]/div/div/div/div/button")))
    self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/main/div[2]/div/div/div/div/button").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID, ":r1q:")))
    self.driver.find_element(By.ID, ":r1q:").click()
    self.driver.find_element(By.ID, ":r1k:").send_keys("0002-09-29")
    self.driver.find_element(By.ID, ":r1k:").send_keys("0020-09-29")
    self.driver.find_element(By.ID, ":r1k:").send_keys("0202-09-29")
    self.driver.find_element(By.ID, ":r1k:").send_keys("2024-09-29")
    self.driver.find_element(By.ID, ":r1l:").click()
    self.driver.find_element(By.ID, ":r1l:-option-1").click()
    self.driver.find_element(By.ID, ":r1r:").click()
    self.driver.find_element(By.ID, ":r1r:-option-3").click()
    self.driver.find_element(By.ID, ":r1p:").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiStack-root:nth-child(3) > .MuiButtonBase-root").click()
    self.driver.find_element(By.ID, ":r1t:").click()
    self.driver.find_element(By.ID, ":r1t:").send_keys("2")
    self.driver.find_element(By.ID, ":r1u:").click()
    self.driver.find_element(By.ID, ":r1u:").send_keys("2")
    element = self.driver.find_element(By.XPATH, "//div[2]/div/div[3]/div/div/div")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    self.driver.find_element(By.CSS_SELECTOR, "body").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiMenuItem-root:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiMenuItem-root:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiBackdrop-root").click()
    element = self.driver.find_element(By.XPATH, "//div[4]/div/div/div")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    self.driver.find_element(By.CSS_SELECTOR, "body").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiMenuItem-root:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiMenuItem-root:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiList-padding > .MuiButtonBase-root:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiBackdrop-root").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiStack-root:nth-child(5) > .MuiButtonBase-root").click()
    self.driver.find_element(By.ID, ":r1v:").click()
    self.driver.find_element(By.ID, ":r1v:").send_keys("2")
    element = self.driver.find_element(By.XPATH, "//div[3]/div/div[2]/div/div/div")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    self.driver.find_element(By.CSS_SELECTOR, "body").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiMenuItem-root:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiMenuItem-root:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiBackdrop-root").click()
    element = self.driver.find_element(By.XPATH, "//div[3]/div/div[3]/div/div/div")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    self.driver.find_element(By.CSS_SELECTOR, "body").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiMenuItem-root:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiMenuItem-root:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiList-padding > .MuiButtonBase-root:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiBackdrop-root").click()
    self.driver.find_element(By.ID, ":r1q:").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(1) > .MuiButtonBase-root path").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".MuiDataGrid-columnHeader:nth-child(1) .MuiDataGrid-columnHeaderTitle").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiDataGrid-columnHeader:nth-child(1) .MuiDataGrid-columnHeaderTitleContainer .MuiSvgIcon-root").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiDataGrid-columnHeader:nth-child(1) .MuiDataGrid-columnHeaderTitleContainer .MuiSvgIcon-root")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiDataGrid-row:nth-child(1) .MuiButtonBase-root").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.ID, "simple-tab-1").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-sizeMedium").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(2) > .MuiButtonBase-root .MuiSvgIcon-root").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(3) .MuiListItemIcon-root").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(1) > .MuiButtonBase-root path").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div[2]/div/div/div/div/div[1]/div[2]/nav/button").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiStack-root").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiMenuItem-root > .MuiSvgIcon-root").click()
  
  def test_spf(self):
    self.driver.get("https://pup.staging.hieraug.fr/login")
    self.driver.set_window_size(1536, 920)
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("spf")
    self.driver.find_element(By.ID, "password").send_keys("spf")
    self.driver.find_element(By.ID, ":r2:").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".MuiDataGrid-columnHeader:nth-child(1) .MuiDataGrid-columnHeaderTitleContainer").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiDataGrid-columnHeader:nth-child(1) .MuiDataGrid-columnHeaderTitleContainer .MuiSvgIcon-root").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiDataGrid-columnHeader:nth-child(1) .MuiDataGrid-columnHeaderTitleContainer path")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiDataGrid-row:nth-child(1) .MuiButtonBase-root").click()
    self.driver.find_element(By.ID, "simple-tab-1").click()
    self.driver.find_element(By.ID, "simple-tab-2").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-textSizeMedium").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(2) > .MuiButtonBase-root .MuiSvgIcon-root").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(3) > .MuiButtonBase-root path:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(4) > .MuiButtonBase-root .MuiSvgIcon-root").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(5) .MuiSvgIcon-root").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(1) > .MuiButtonBase-root .MuiSvgIcon-root").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".MuiMenuItem-root").click()
  
  def test_partnerorange(self):
    self.driver.get("https://pup.staging.hieraug.fr/login")
    self.driver.set_window_size(1536, 920)
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("orange")
    self.driver.find_element(By.ID, "password").send_keys("orange")
    self.driver.find_element(By.ID, ":r2:").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".MuiDataGrid-columnHeader:nth-child(1) .MuiDataGrid-columnHeaderTitleContainer").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiDataGrid-columnHeader:nth-child(1) .MuiDataGrid-columnHeaderTitleContainer path")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiDataGrid-columnHeader:nth-child(1) .MuiDataGrid-columnHeaderTitleContainer path").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiDataGrid-columnHeader:nth-child(1) .MuiDataGrid-columnHeaderTitleContainer path")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiDataGrid-row:nth-child(1) .MuiButtonBase-root").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.ID, "simple-tab-1").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-textSizeMedium").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".MuiIconButton-colorInherit > .MuiSvgIcon-root").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(2) .MuiTypography-root").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(3) > .MuiButtonBase-root").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(4) .MuiTypography-root").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(5) .MuiTypography-root").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(6) .MuiTypography-root").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(1) > .MuiButtonBase-root .MuiTypography-root").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".MuiMenuItem-root > .MuiSvgIcon-root").click()
  
  def test_immersion(self):
    self.driver.get("https://pup.staging.hieraug.fr/login")
    self.driver.set_window_size(1536, 920)
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("immersion")
    self.driver.find_element(By.ID, "password").send_keys("immersion")
    self.driver.find_element(By.ID, ":r2:").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div[2]/div/div/div/div/div[1]/div[2]/nav/button").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(1) > .MuiButtonBase-root .MuiSvgIcon-root").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(2) .MuiListItemIcon-root").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(1) > .MuiButtonBase-root > .MuiListItemIcon-root").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiListItem-root:nth-child(1)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiDataGrid-columnHeader:nth-child(4) .MuiDataGrid-columnHeaderTitleContainer").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiDataGrid-row:nth-child(1) .MuiButton-containedPrimary").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-text").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".MuiMenuItem-root path").click()
  
