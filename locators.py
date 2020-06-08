from selenium.webdriver.common.by import By

class MainPageLocators():

    SIGN_IN_BTN = (By.CLASS_NAME, 'login')

class AuthenticationPageLocators():

    EMAIL_INPUT = (By.CSS_SELECTOR, '#email_create')
    CREATE_ACCOUNT_BTN = (By.CSS_SELECTOR, '#SubmitCreate')

class CreateAnAccountPageLocators():

    # YOUR PERSONAL INFORMATION:
    MRS_RADIO_BTN = (By.CSS_SELECTOR, '#uniform-id_gender2')
    FIRST_NAME_INPUT1 = (By.CSS_SELECTOR, '#customer_firstname')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '#customer_lastname')
    PASSWD_INPUT = (By.CSS_SELECTOR, '#passwd')
    EMAIL_INPUT = (By.ID, 'email')
    # DATE OF BIRTH:
    DATE = (By.CSS_SELECTOR, '#days')
    MONTH = (By.CSS_SELECTOR, '#months')
    YEAR = (By.CSS_SELECTOR, '#years')
    # YOUR ADDRESS:
    POSTAL_CODE_INPUT = (By.ID, 'postcode')
    CITY_INPUT = (By.ID, 'city')
    ADDITIONAL_INF_INPUT = (By.ID, 'other')
    MOBILE_PHONE_INPUT = (By.ID, 'phone_mobile')
    ADDRESS_INPUT = (By.CSS_SELECTOR, '#address1')
    STATE_SELECT = (By.ID, 'id_state')
    SUBMIT_BTN = (By.ID, 'submitAccount')