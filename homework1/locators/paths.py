from selenium.webdriver.common.by import By

class ButtonForAuthorization:
    BUTTON_LOGIN = (By.CSS_SELECTOR, "[class*=responseHead-module-button]")
    BUTTON_LOGIN_AFTER_INPUT_DATA = (By.CLASS_NAME, "authForm-module-button-1u2DYF")
    BUTTON_PROFILE = (By.CLASS_NAME, "right-module-userNameWrap-3Odw2D")
    BUTTON_LOGOUT = (By.CSS_SELECTOR, "[href='/logout']")
class ButtonForInputData:
    INPUT_EMAIL = (By.NAME, "email")
    INPUT_PASSWORD = (By.NAME, "password")
    INPUT_NAME = (By.CSS_SELECTOR, "[data-name*='fio'] input")
    INPUT_INN = (By.CSS_SELECTOR, "[data-name*='Inn'] input")
    INPUT_PHONE = (By.CSS_SELECTOR, "[data-name*='phone'] input")

class ButtonForNavigatingPages:
    BUTTON_AUDIENCES = (
        By.CSS_SELECTOR,
        "[class*='center-module-button-14O4yB center-module-segments']",
    )
    BUTTON_BALANCE = (By.CSS_SELECTOR, "[class*='center-module-billing-1cIfj4']")
    BUTTON_STATISTICS = (By.CSS_SELECTOR, "[class*='center-module-statistics-2Wbrwh']")
    BUTTON_PROFILE = (By.CSS_SELECTOR, "[class*='center-module-profile']")
    BUTTON_TOOLS = (By.CSS_SELECTOR, "[class*='center-module-tools']")

class ButtonForSavingChanges:
    SAVE_CHANGE = (By.CSS_SELECTOR, "[class*='submit']")


class Check:
    CURRENT_USERNAME = (By.CSS_SELECTOR, "[class*='right-module-userNameWrap']")
    PAGE_AUDIENCES = (By.CSS_SELECTOR, "[data-class-name*='SegmentsList']")
    PAGE_BALANCE = (By.CSS_SELECTOR, "[class*='autodeposit']")
    PAGE_STATISTICS = (By.CSS_SELECTOR, "[class*=page_statistics]")
    PAGE_PROFILE = (By.CSS_SELECTOR, "[data-translated='Contact information']")
    PAGE_TOOLS = (By.CSS_SELECTOR, "[class*=feeds]")
    ERROR_LOGIN_WITH_INVALID_DATA = (By.CLASS_NAME, "formMsg_title")

