*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}   http://www.practiceselenium.com/practice-form.html
${browser}      chrome

*** Test Cases ***
droplist
    open browser    ${url}      ${browser}
    maximize browser window
    set selenium implicit wait  5

    select from list by label  continents   USA
    select from list by index  continents   4

    select from list by label  selenium_commands    Switch Commands
    unselect from list by label  selenium_commands    Switch Commands
    sleep   3
    select from list by index  selenium_commands    3
    click button    xpath://*[@id="submit"]

    close browser
*** Keywords ***

