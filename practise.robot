*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/PractiseResources.robot


*** Variables ***
${browser}  chrome
#${url}  https://opensource-demo.orangehrmlive.com

#${url}  https://www.seleniumeasy.com/test/basic-radiobutton-demo.html
#${url}  http://practiceselenium.com/practice-form.html
#${url}  http://demo.automationtesting.in/Windows.html

#${url}  https://testautomationpractice.blogspot.com/

#${url}  https://seleniumhq.github.io/selenium/docs/api/java/index.html
${url}  https://opensource-demo.orangehrmlive.com
#${url}  https://swisnl.github.io/jQuery-contextMenu/demo.html

#${url}  https://www.countries-ofthe-world.com/flags-of-the-world.html



*** Test Cases ***
#TC1-InputBox
#    open browser  ${url}    ${browser}
#    maximize browser window
#    element should be visible  id:txtUsername
#    element should be enabled  id:txtUsername
#    input text      id:txtUsername   Admin
#    input text      id:txtPassword      admin123
#    clear element text  id:txtUsername
#    sleep   2
#    input text      id:txtUsername   Admin
#    click button  id:btnLogin
#    ${title}=   get title
#    title should be  ${title}
#
#
#    sleep   3
#    close browser

#TC2-Radiobutton
#    open browser  ${url}    ${browser}
#    select radio button  optradio  Male
#    sleep   3
#    select radio button  ageGroup   15 - 50
#    sleep   3
#    close browser

#TC3-Checkbox
#    open browser  ${url}    ${browser}
#    maximize browser window
#    select checkbox  name:BlackTea
#    select checkbox  name:tool
#    unselect checkbox  name:RedTea
#    sleep   2
#    close browser

#TC4-Dropdown
#    open browser  ${url}    ${browser}
#    maximize browser window
#    select from list by label  name:continents  Asia
#    select from list by label  name:continents  USA
#    sleep   3
#
#    select from list by index   name:continents      6
#    set selenium speed       2
#
#    select from list by value  name:continents      South America
#
#    sleep   3
#    close browser

#TC5-ListBox
#    open browser  ${url}    ${browser}
#    maximize browser window
#    select from list by label  name:selenium_commands   Browser Commands
#    unselect from list by label  name:selenium_commands   Browser Commands
#
#    select from list by label  name:selenium_commands   Wait Commands
#    select from list by label  name:selenium_commands   Navigation Commands
#
#    sleep   3
#
#    close browser
#TC6-SeleniumSpeed
#    open browser  ${url}    ${browser}
#    maximize browser window
#    set selenium timeout  10 seconds
#    ${speed}=   get selenium timeout
#    log to console  ${speed}
#    wait until page contains  Practice Form
#
#
#    ${speed}=   get selenium timeout
#    log to console  ${speed}
##    set selenium speed  4 seconds
##    ${speed}=   get selenium speed
##    log to console  ${speed}
#    select from list by label  name:selenium_commands   Browser Commands
#    unselect from list by label  name:selenium_commands   Browser Commands
#    ${speed}=   get selenium timeout
#    log to console  ${speed}
#    set selenium implicit wait  5 seconds
#
#
#    select from list by label  name:selenium_commands   Wait Commands
#    select from list by label  name:selenium_commands   Navigation Commands
#
#    sleep   3
#
#    close browser

#TC7-CloseSingleAndMultipleBrowsers
#    open browser  ${url}    ${browser}
#    maximize browser window
#
#    open browser  https://testautomationpractice.blogspot.com/  ${browser}
#    maximize browser window
#
#    close browser

#TC8-HandleAlerts
#    open browser  ${url}    ${browser}
#    maximize browser window
#    set selenium speed  4
#    click button  xpath://button[contains(text(),'Click Me')]
#    handle alert  ACCEPT
#    page should contain  You pressed OK!
#    click button  xpath://button[contains(text(),'Click Me')]
#    handle alert  DISMISS
#    page should contain     You pressed Cancel!
#    click button  xpath://button[contains(text(),'Click Me')]
#    handle alert  leave
#
#    close browser

#TC9-HandleFrames
#    open browser  ${url}    ${browser}
#    maximize browser window
#    set selenium speed  3
#    click link  xpath://header/nav[1]/div[1]/div[2]/ul[1]/li[1]/a[1]
#    select frame  packageListFrame
#    click link  xpath://body/main[1]/ul[1]/li[1]/a[1]
#
#    unselect frame
#
#    select frame  packageFrame
#    click link  xpath:/html/body/main/div/section[1]/ul/li[1]/a/span
#
#    unselect frame
#
#    select frame  classFrame
#    input text  xpath://*[@id="search"]     helloworld
#
#    unselect frame
#
#    close browser

#TC10-HandleTabbedWindows
#    open browser  ${url}    ${browser}
#    maximize browser window
#    set selenium speed  2 seconds
#    click button  xpath://*[@id="Tabbed"]/a/button
#    select window  SeleniumHQ Browser Automation
#    page should contain  Follow us on twitter to keep up-to-date with all Selenium development and community activity!
#    close browser

#TC11-HandleBrowserwindows
#    open browser  http://demo.automationtesting.in/Windows.html     ${browser}
#    maximize browser window
#    set selenium speed      2seconds
#    open browser  https://seleniumhq.github.io/selenium/docs/api/java/index.html    ${browser}
#    maximize browser window
#
#    switch browser  1
#    click button  xpath://*[@id="Tabbed"]/a/button
#    select window  SeleniumHQ Browser Automation
#    page should contain  Follow us on twitter to keep up-to-date with all Selenium development and community activity!
#
#    switch browser  2
#    page should contain  Packages
#
#    close all browsers

#TC12-NavigationalCommands
#    open browser  https://www.google.com/    chrome
#    maximize browser window
#    ${pageurl}=     get location
#    log to console  ${pageurl}
#
#    go to  https://www.facebook.com/
#    maximize browser window
#    ${pageurl}=     get location
#    log to console  ${pageurl}
#
#    go back
#    ${pageurl}=     get location
#    log to console  ${pageurl}
#    close browser

#TC13-captureScreenshot
#    open browser  ${url}    ${browser}
#    maximize browser window
#    capture element screenshot  xpath://*[@id="divLogo"]/img    ../Elementss.png
#    input text  id:txtUsername  Admin
#    input password  id:txtPassword  admin123
#    click button    id:btnLogin
#    capture page screenshot  ../pagess.png
#    close browser

#TC14-MouseActions
#    open browser  ${url}    ${browser}
#    maximize browser window
#    open context menu  xpath:/html/body/div/section/div/div/div/p/span
#    sleep   3
#
#    go to   https://testautomationpractice.blogspot.com/
#    double click element  xpath://*[@id="HTML10"]/div[1]/button
#
#    sleep  3
#
#    drag and drop  xpath://*[@id="draggable"]/p     //*[@id="droppable"]
#    sleep   3
#    close browser

#TC15-UserDefinedKeywords
#    open browser  ${url}    ${browser}
#    maximize browser window
#    ${output}=  userdefinedwithoutargs  Admin   admin123
#    log to console  ${output}
#    close browser

#TC16-ScrollingWebpage
#    open browser  ${url}    ${browser}
#    maximize browser window
#    execute javascript  window.scrollTo(0,5000)
#    scroll element into view  xpath://*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[30]/td[2]
#    execute javascript  window.scrollTo(0,document.body.scrollHeight)
#    close browser

#TC17-ForLoop
#    FOR     ${i}    IN RANGE    1   100
#    log to console  ${i}
#    END
#    FOR     ${i}    IN  RANGE   1  2  3  4  5  6  6  7
#    log to console  ${i}
#    END

#     @{items}   create list     1  2  3  4  Harsha
#     FOR    ${i}   IN  @{items}
#     log to console  ${i}
#     END

#      FOR   ${i}    IN  1  2  3  4  5  Harsha
#      log to console  ${i}
#      exit for loop if  ${i}==3
#      END

#TC18-ExtractLinks
#    open browser  https://en-gb.facebook.com/   ${browser}
#    maximize browser window
#    ${element_count}=   get element count  xpath://a
#    log to console  ${element_count}
#
#    FOR     ${i}    IN      ${element_count}+1
#    ${link_text}=   get text  xpath:(//a)[${i}]
#    log to console  ${link_text}
#    END
#    close browser

#TC19-HTML Table
#    open browser  ${url}    ${browser}
#    maximize browser window
#    ${row_count}=   get element count  xpath://*[@id="HTML1"]/div[1]/table/tbody/tr
#    log to console  ${row_count}
#
#    ${col_count}=   get element count  xpath://*[@id="HTML1"]/div[1]/table/tbody/tr/th
#    log to console  ${col_count}
#
#    ${data}=    get text  xpath://tbody/tr[3]/td[1]
#    log to console  ${data}
#    close browser

TC20-Datadriven
datascript




*** Keywords ***
datascript
    [Arguments]     ${user}     ${pwd}
    username  ${user}
    password  ${pwd}
    login
    invalidmsg





