from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
import datetime

driver = None


def initDriver(profile):
    global driver
    driver = webdriver.Firefox(profile)
    driver.maximize_window()

def getTimestamp():
    nowStamp = datetime.datetime.now().timetuple()
    dateStamp = str(nowStamp.tm_year) + str(nowStamp.tm_mon) + str(nowStamp.tm_mday) + str(nowStamp.tm_hour) + str(
        nowStamp.tm_min) + str(nowStamp.tm_sec)
    return dateStamp

def selectByValue(value):
    return driver.selectByValue(value)

def sleepFor(secs):
    time.sleep(secs)


def loadUrl(url):
    driver.get(url)

def verticalScroll(y):
    if y is None or y==0:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    else:
        driver.execute_script("window.scrollTo(0,y);")

def findByCssSelector(selector):
    return driver.find_element_by_css_selector(selector)


def findMoreByXpath(tag):
    return driver.find_elements_by_xpath(tag)

def findMoreByTag(tag):
    return driver.find_elements_by_tag_name(tag)

def processBrowserAlertYesNo(yesOrNo, secs):
    try:
        webEle = waitForVisibilityOfBrowserAlert(secs)
        if webEle is not None:
            alert = driver.switch_to_alert()
            if yesOrNo == True:
                alert.accept()
            else:
                alert.dismiss()
    except:
        raise

def findMoreByCssSelector(selector):
    return driver.find_elements_by_css_selector(selector)

def findById(id):
    return driver.find_element_by_id(id)

def findMoreById(id):
    return driver.find_elements_by_id(id)

def findByName(name):
    return driver.find_element_by_name(name)


def findByxPath(xpath):
    return driver.find_element_by_xpath(xpath)


def findByclassName(className):
    return driver.find_element_by_class_name(className)


def waitForVisibilityOf(secs, selector):
    return WebDriverWait(driver, secs).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))


def waitForVisibilityOfMore(secs, selector):
    return WebDriverWait(driver, secs).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))

def waitForPresenceOf(secs,selector):
    return WebDriverWait(driver, secs).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
    
def waitForVisibilityOfId(secs, id):
    elem = WebDriverWait(driver, secs).until(EC.presence_of_element_located((By.ID, id)))
    return elem

def waitForVisibilityOfBrowserAlert(secs):
    elem = WebDriverWait(driver, secs).until(EC.alert_is_present(), 'Confirmation popup to appear.')
    return elem

def waitForVisibilityOfName(secs, name):
    return WebDriverWait(driver, secs).until(EC.visibility_of_element_located((By.NAME, name)))

def clearTextElement(elem):
    elem.clear()

def clickAlert():
    driver.switch_to_alert().accept()

def quitBrowser():
    if driver is not None:
        driver.quit()

def hover(self,element):
    wd = driver.connection
    hov = ActionChains(wd).move_to_element(element)
    hov.perform()

def waitForVisibilityOfXPath(secs, xpath):
    elems = WebDriverWait(driver, secs).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    return elems


def pageRefresh():
    driver.refresh()
