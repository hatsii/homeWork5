import os
import time
import pytest
from selene import browser, have, command

#Тест на заполнение формы регистрации студента
def test_form(browser_open_page):
    # ФИ студента
    browser.element("#firstName").type("Vadim")
    browser.element("#lastName").type("Tatarnikov")

    browser.element("#userEmail").type("exampleemail@mail.ru")
    #Пол студента
    browser.element('label[for="gender-radio-1"]').click()
    # Номер телефона студента
    browser.element("#userNumber").type("3467823467")

    #Дата рождения студента
    browser.element("#dateOfBirthInput").click()
    browser.element('.react-datepicker__year-select').element('option[value="2003"]').click()
    browser.element('.react-datepicker__month-select').element('option[value="3"]').click()
    browser.element('.react-datepicker__day--023').click()

    #Предмет студента

    browser.element('#subjectsInput').type('Maths').press_enter()

    #Хобби студента(чекбоксы)
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element('label[for="hobbies-checkbox-3"]').click()

    #Загрузка фотографии
    browser.element('#uploadPicture').set_value(os.path.abspath('exampleImage.jpg'))

    #Адресс студента
    browser.element('#currentAddress').type('example street')

    #Штат и город студента
    browser.element('#state').click()
    browser.element("//div[text()='Haryana']").click()
    browser.element('#city').click()
    browser.element("//div[text()='Karnal']").click()

    #Отправка формы и ее проверка на отправленные данные
    browser.element("#submit").perform(command.js.click)
    browser.element("#example-modal-sizes-title-lg").should(have.text('Thanks for submitting the form'))
    browser.all('td').should(have.texts([
        'Student Name', 'Vadim Tatarnikov',
        'Student Email', 'exampleemail@mail.ru',
        'Gender', 'Male',
        'Mobile', '3467823467',
        'Date of Birth', '23 April,2003',
        'Subjects', 'Maths',
        'Hobbies', 'Sports, Reading, Music',
        'Picture', 'exampleImage.jpg',
        'Address', 'example street',
        'State and City', 'Haryana Karnal'
    ]))
