*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${page url}     https://opensource-demo.orangehrmlive.com
${browser}      chrome

*** Test Cases ***

browseropen
    open browser    ${page url}     ${browser}
    maximize browser window
    ${title_tr}=     get title
    title should be     ${title_tr}
    ${var}=  set variable   id:txtUsername
    element should be visible     ${var}
    element should be enabled       id:txtPassword
    input text      id:txtUsername      harsha
    sleep      3
    clear element text      id:txtUsername
    input text      id:txtUsername      Admin
    input text      id:txtPassword      admin123
    click button    id:btnLogin
    close browser
*** Keywords ***

