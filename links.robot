*** Settings ***
Library     SeleniumLibrary
*** Variables ***

*** Test Cases ***
getlinks
    open browser    https://www.google.com/   chrome
    maximize browser window
    ${links}=   get element count   xpath://a
    log to console  ${links}

#    @{linkitems}    create list
    FOR     ${i}    IN RANGE   1   ${links}+1
    ${getlinks}=    get text  xpath:(//a)[${i}]

    log to console  ${getlinks}
    END
    close browser

*** Keywords ***

