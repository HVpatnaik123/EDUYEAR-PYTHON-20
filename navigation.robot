*** Settings ***

Library  SeleniumLibrary

*** Test Cases ***
naviga
    open browser  https://www.google.com/   chrome
    ${url}=     get location
    log to console  ${url}

    go to  https://www.facebook.com
    ${url}=     get location
    log to console  ${url}

    go back
    ${url}=     get location
    log to console  ${url}
