*** Settings ***
Library     SeleniumLibrary

*** Variables ***


*** Test Cases ***
forloop1range
    FOR    ${i}    IN RANGE   1     10
    log to console    ${i}
    END

forloopnos
    FOR     ${i}    IN    1  2  3  4  5  6  7  8
    log to console    ${i}
    END

forlooplist
    @{items}    create list     1   2   3   4   5   6   7   8   9
    FOR     ${i}    IN      @{items}
    log to console      ${i}
    END

forloopstring
    FOR     ${i}    IN  Harsha  Vardhan    Patnaik
    log to console  ${i}
    END

forloopstrinlist
    @{items}    create list  harsha  vardhan  patnaik  python  selenium
    FOR     ${i}    IN      @{items}
    log to console  ${i}
    END

forloopconditionexit
    @{items}    create list     1   2   3   4   5   6   7   8   9
    FOR     ${i}    IN      @{items}
    log to console  ${i}
    exit for loop if  ${i}==5
    END



*** Keywords ***

