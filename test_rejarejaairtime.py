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
                              job_name="RejarejaAirtime",
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

    # 8. Click 'Sell'
    sell = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'Sell']")
    sell.click()

    # 9. Click 'Sell1'
    sell1 = driver.find_element(By.XPATH,
                                "//androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[2]//android.widget.ImageView")
    sell1.click()

    # 10. Click '07123456781'
    _07123456781 = driver.find_element(By.ID,
                                       "com.dukatech.digiduka.home:id/editTextPhone")
    _07123456781.click()

    # 11. Type '0715073891' in '07123456781'
    _07123456781 = driver.find_element(By.ID,
                                       "com.dukatech.digiduka.home:id/editTextPhone")
    _07123456781.send_keys("0715073891")

    # 12. Tap at ('1001','2219') with '1' fingers for '100'ms
    driver.tap(positions=[(1001, 2219)], duration=100)

    # 13. Click 'KES. 0.00'
    kes_0_00 = driver.find_element(By.ID,
                                   "com.dukatech.digiduka.home:id/editTextAmount")
    kes_0_00.click()

    # 14. Type '5' in 'KES. 0.00'
    kes_0_00 = driver.find_element(By.ID,
                                   "com.dukatech.digiduka.home:id/editTextAmount")
    kes_0_00.send_keys("5")

    # 15. Tap at ('832','2340') with '1' fingers for '100'ms
    driver.tap(positions=[(832, 2340)], duration=100)

    # 16. Click 'Send'
    send = driver.find_element(By.ID,
                               "com.dukatech.digiduka.home:id/nextButton")
    send.click()

    # 17. Click 'com.dukatech.digiduka.home:id/purchas...'
    com_dukatech_digiduka_home_colon_id_slash_purchas_ = driver.find_element(By.ID,
                                                                             "com.dukatech.digiduka.home:id/purchasePinView")
    com_dukatech_digiduka_home_colon_id_slash_purchas_.click()

    # 18. Type '2580' in 'com.dukatech.digiduka.home:id/purchas...'
    com_dukatech_digiduka_home_colon_id_slash_purchas_ = driver.find_element(By.ID,
                                                                             "com.dukatech.digiduka.home:id/purchasePinView")
    com_dukatech_digiduka_home_colon_id_slash_purchas_.send_keys("2580")

    # 19. Click 'com.dukatech.digiduka.home:id/purchas...'
    com_dukatech_digiduka_home_colon_id_slash_purchas_ = driver.find_element(By.ID,
                                                                             "com.dukatech.digiduka.home:id/purchasePinView")
    com_dukatech_digiduka_home_colon_id_slash_purchas_.click()

    # 20. Click 'Pay'
    pay = driver.find_element(By.ID,
                              "com.dukatech.digiduka.home:id/payButton")
    pay.click()
