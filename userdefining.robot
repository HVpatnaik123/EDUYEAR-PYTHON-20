*** Settings ***

Library     SeleniumLibrary
Resource  ../Resources/userdefiningresources.robot

*** Variables ***
${url}  https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407
${browser}      chrome

*** Test Cases ***
user1
    ${printing}=    logincase   ${url}  ${browser}
    input text      name:RESULT_TextField-1    Harsha
    log to console  ${printing}
    close browser

*** Keywords ***
