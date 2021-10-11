*** Settings ***
Library  SeleniumLibrary
*** Variables ***

*** Test Cases ***
htmltables
    open browser    https://testautomationpractice.blogspot.com/    chrome
    maximize browser window
    ${trow}=    get element count  xpath://*[@id="HTML1"]/div[1]/table/tbody/tr
    log to console  ${trow}     No. of rows

    ${tcol}=    get element count  xpath://*[@id="HTML1"]/div[1]/table/tbody/tr[1]/th
    log to console  ${tcol}

    ${tdata}=   get text  xpath://*[@id="HTML1"]/div[1]/table/tbody/tr[3]/td[1]
    log to console  ${tdata}

    table column should contain  xpath://*[@id="HTML1"]/div[1]/table/tbody/tr[1]/th[2]  2   Author
    table row should contain  xpath://*[@id="HTML1"]/div[1]/table/tbody/tr[6]/td[1]     6   Master In Java
    table header should contain  xpath://*[@id="HTML1"]/div[1]/table/tbody/tr[1]/th[3]  Subject
    table header should contain  xpath://*[@id="HTML1"]/div[1]/table/tbody/tr[1]/th[4]  Price
    table cell should contain  xpath://*[@id="HTML1"]/div[1]/table/tbody/tr[5]/td[3]        5       3       Selenium
    close browser
*** Keywords ***

