*** Settings ***

Library     SeleniumLibrary
*** Variables ***

${browser}  chrome
${url}  https://opensource-demo.orangehrmlive.com

*** Test Cases ***
openbrowserandlogin
    open browser    ${url}  ${browser}
    wait until page contains  LOGIN Panel
    input text  xpath://*[@id="txtUsername"]    Admin
    sleep   2
    input text  xpath://*[@id="txtPassword"]    admin123
    click button  id:btnLogin
    page should contain  Dashboard
    close browser
*** Keywords ***

