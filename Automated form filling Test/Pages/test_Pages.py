
from Project_05.Locators.test_Locators import TestLocators


class TestPages():

    def __init__(self, driver):
        self.driver = driver
        self.FirstName_textbox_id = TestLocators.FirstName_textbox_id
        self.LastName_textbox_id = TestLocators.LastName_textbox_id
        self.Email_textbox_id = TestLocators.Email_textbox_id
        self.Gender_radio_css_selector = TestLocators.Gender_radio_css_selector
        self.Mobile_number_textbox_xpath = TestLocators.Mobile_number_textbox_xpath
        self.Date_calendar_id = TestLocators.Date_calendar_id
        self.Hobbies_sports_checkbox_xpath = TestLocators.Hobbies_sports_checkbox_xpath
        self.Hobbies_reading_checkbox_xpath = TestLocators.Hobbies_reading_checkbox_xpath
        self.Address_textbox_xpath = TestLocators.Address_textbox_xpath
        self.Submit_button_id = TestLocators.Submit_button_id
        self.Close_button_id = TestLocators.Close_button_id

    def enter_firstname(self, first_name):
        self.driver.find_element_by_id(self.FirstName_textbox_id).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element_by_id(self.LastName_textbox_id).send_keys(last_name)

    def enter_email(self, email):
        self.driver.find_element_by_id(self.Email_textbox_id).send_keys(email)

    def click_gender(self):
        self.driver.find_element_by_css_selector(self.Gender_radio_css_selector).click()

    def enter_mobile_number(self, mobile_number):
        self.driver.find_element_by_xpath(self.Mobile_number_textbox_xpath).send_keys(mobile_number)

    def click_date(self):
        self.driver.find_element_by_id(self.Date_calendar_id).clear()
        self.driver.find_element_by_id(self.Date_calendar_id).send_keys("18 May 2005")

    def click_hobbies(self):
        self.driver.find_element_by_xpath(self.Hobbies_sports_checkbox_xpath).click()
        self.driver.find_element_by_xpath(self.Hobbies_reading_checkbox_xpath).click()

    def enter_address(self, address):
        self.driver.find_element_by_xpath(self.Address_textbox_xpath).send_keys(address)

    def click_submit(self):
        self.driver.find_element_by_id(self.Submit_button_id).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_close(self):
        self.driver.find_element_by_id(self.Close_button_id).click()
