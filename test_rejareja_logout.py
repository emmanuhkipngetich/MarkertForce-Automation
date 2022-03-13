from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


@pytest.fixture()
def driver():
    capabilities = {
        "platformName": "Android",
        "udid": "R58R61XCMMJ",
        "appPackage": "com.dukatech.digiduka",
        "appActivity": "com.dukatech.digiduka.ui.views.ui.dashboard.DashboardActivity",
    }
    driver = webdriver.Remote(token="FleuoSg2jb_Q_OkT_4gUmMw3_h5z2s7WejhfakYqpsQ",
                              project_name="Zuri_whatsapp",
                              job_name="Rejareja logout",
                              desired_capabilities=capabilities)
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):

    # 1. Reset App
    # Clear application data and restart (Auto-generated)
    driver.reset()

    # 2. Click 'Navigate up'
    navigate_up = driver.find_element(By.XPATH,
                                      "//android.widget.ImageButton[@content-desc = 'Navigate up']")
    navigate_up.click()

    # 3. Click 'Logout'
    logout = driver.find_element(By.XPATH,
                                 "//android.widget.TextView[@text = 'Logout']")
    logout.click()

    # 4. Click 'Yes'
    yes = driver.find_element(By.ID,
                              "com.dukatech.digiduka:id/btDgLogoutActionYes")
    yes.click()
