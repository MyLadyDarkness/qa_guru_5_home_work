import os.path
from selene import browser, by, have, command


def test_demoqa():
    browser.open("/automation-practice-form")
    browser.element("#firstName").type("Oleg")
    browser.element("#lastName").type("Teplov")
    browser.element("#userEmail").type("oteplov@gmail.com")
    browser.element(".custom-radio>input[value='Other']+label").click()
    browser.element("#userNumber").type("7123456789")

    browser.element("#dateOfBirthInput").perform(command.js.click)
    browser.element(".react-datepicker__year-select").click().element("option[value='1981']").click()
    browser.element(".react-datepicker__month-select").click().element("option[value='3']").click()
    browser.element(".react-datepicker__day--014").click()

    browser.element('#subjectsInput').type("Hindi").press_enter()

    browser.element(".custom-checkbox>input[value='2']+label").click()

    browser.element("#uploadPicture").send_keys(os.path.abspath("picture.jpg"))

    browser.element("#currentAddress").type("Some address")

    browser.element('#state').perform(command.js.scroll_into_view)
    browser.element('#state').click().element(by.text('NCR')).click()
    browser.element('#city').click().element(by.text('Noida')).click()

    browser.element("#submit").click()

    browser.element(".modal-title").should(have.text("Thanks for submitting the form"))
    browser.element(".table").all("td").even.should(
        have.exact_texts(
            "Oleg Teplov",
            "oteplov@gmail.com",
            "Other",
            "7123456789",
            "14 April,1981",
            "Hindi",
            "Reading",
            "picture.jpg",
            "Some address",
            "NCR Noida"
        )
    )

