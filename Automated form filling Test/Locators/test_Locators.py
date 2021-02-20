class TestLocators():
    # homepage
    FirstName_textbox_id = "firstName"
    LastName_textbox_id = "lastName"
    Email_textbox_id = "userEmail"
    Gender_radio_css_selector = "div.body-height:nth-child(2) div.container.playgound-body div.row " \
                                "div.col-12.mt-4.col-md-6:nth-child(2) div.practice-form-wrapper form:nth-child(2) " \
                                "div.mt-2.row:nth-child(3) div.col-md-9.col-sm-12 " \
                                "div.custom-control.custom-radio.custom-control-inline:nth-child(1) > " \
                                "label.custom-control-label "
    Mobile_number_textbox_xpath = "//input[@id='userNumber' and @maxlength='10']"
    Date_calendar_id = "dateOfBirthInput"
    Subjects_textbox_class_name = "subjects-auto-complete__value-container " \
                                  "subjects-auto-complete__value-container--is-multi css-1hwfws3 "
    Hobbies_sports_checkbox_xpath = "//label[contains(text(),'Sports')]"
    Hobbies_reading_checkbox_xpath = "//label[contains(text(),'Reading')]"
    Address_textbox_xpath = "//textarea[@id='currentAddress']"
    Submit_button_id = "submit"
    Close_button_id = "closeLargeModal"







