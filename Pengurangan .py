from appium import webdriver
import time
from appium.webdriver.common.appiumby import AppiumBy

desired_cap = {
        "platformName": "Android",
        "appium:platformVersion": "11.0",
        "appium:deviceName": "sdk_gphone_x86",
        "appium:automationName": "uiautomator2",
        "appium:app": "C:\\Users\\Mazway\\Desktop\\appium\\calculator.apk",
        "appium:appPackage": "com.google.android.calculator",
        "appium:noReset": "true"
        }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)

#click '8'
driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_8").click()
#click 'minus'
driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/op_sub").click()
#click '5'
driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_5").click()
#click 'equals'
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(18)").click()

time.sleep(2)

driver.quit()
