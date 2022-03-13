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
                              job_name="Rejareja login",
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

    # 2. Click 'Login'
    login = driver.find_element(By.ID,
                                "com.dukatech.digiduka.onboarding:id/buttonLogin")
    login.click()

    # 3. Click 'Agree'
    agree = driver.find_element(By.ID,
                                "com.dukatech.digiduka:id/btDgPhonePolicyActionAgree")
    agree.click()

    # 4. Click '0712345678'
    _0712345678 = driver.find_element(By.ID,
                                      "com.dukatech.digiduka.onboarding:id/editTextPhone")
    _0712345678.click()

    # 5. Type '723107746' in '0712345678'
    _0712345678 = driver.find_element(By.ID,
                                      "com.dukatech.digiduka.onboarding:id/editTextPhone")
    _0712345678.send_keys("723107746")

    # 6. Click 'com.dukatech.digiduka.onboarding:id/l...'
    com_dukatech_digiduka_onboarding_colon_id_slash_l_ = driver.find_element(By.ID,
                                                                             "com.dukatech.digiduka.onboarding:id/loginPinView")
    com_dukatech_digiduka_onboarding_colon_id_slash_l_.click()

    # 7. Type '2580' in 'com.dukatech.digiduka.onboarding:id/l...'
    com_dukatech_digiduka_onboarding_colon_id_slash_l_ = driver.find_element(By.ID,
                                                                             "com.dukatech.digiduka.onboarding:id/loginPinView")
    com_dukatech_digiduka_onboarding_colon_id_slash_l_.send_keys("2580")

    # 8. Click 'Navigate up'
    navigate_up = driver.find_element(By.XPATH,
                                      "//android.widget.ImageButton[@content-desc = 'Navigate up']")
    navigate_up.click()

    # 9. Does 'Version: 2.1.4.26' contain 'Version: 2.1.4.26'?
    version_colon_2_1_4_26 = driver.find_element(By.ID,
                                                 "com.dukatech.digiduka:id/textViewVersion")
    step_output = version_colon_2_1_4_26.text
    assert step_output and ("Version: 2.1.4.26" in step_output)

    # 10. Click 'Version: 2.1.4.26'
    version_colon_2_1_4_26 = driver.find_element(By.ID,
                                                 "com.dukatech.digiduka:id/textViewVersion")
    version_colon_2_1_4_26.click()

    # 11. Is 'Version: 2.1.4.26' present?
    driver.find_element(By.ID, "com.dukatech.digiduka:id/textViewVersion")
