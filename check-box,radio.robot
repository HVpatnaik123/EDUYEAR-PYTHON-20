*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}      http://www.practiceselenium.com/practice-form.html
${browser}      chrome

*** Test Cases ***
checkboxwork
    open browser    ${url}      ${browser}
    maximize browser window
    select checkbox  BlackTea
    select checkbox  RedTea
    select radio button     sex     Female

    unselect checkbox  RedTea
    sleep   2
    close browser


*** Keywords ***

