*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***

alertframes
#    open browser  https://testautomationpractice.blogspot.com/  chrome
#    maximize browser window
#    click button  xpath://*[@id="HTML9"]/div[1]/button
#    handle alert  accept
#
#    sleep   3
#    click button  xpath://*[@id="HTML9"]/div[1]/button
#    set selenium speed  3seconds
#    handle alert  dismiss
#    sleep   3
#
#
#    click button  xpath://*[@id="HTML9"]/div[1]/button
#    alert should be present  Press a button!
#    sleep   3
#    click button  xpath://*[@id="HTML9"]/div[1]/button
#    handle alert  leave
#    close browser

    open browser  https://seleniumhq.github.io/selenium/docs/api/java/index.html    chrome
    click link  xpath:/html/body/header/nav/div[1]/div[2]/ul[1]/li[1]/a
    sleep  3
    select frame  packageListFrame
    click link  xpath:/html/body/main/ul/li[7]/a
    unselect frame

    select frame  packageFrame
    click link     xpath:/html/body/main/div/section[1]/ul/li[2]/a
    unselect frame
    sleep   3

    select frame  classFrame
    input text  xpath://*[@id="search"]     hello
    sleep   3
    clear element text  //*[@id="search"]
    click link  xpath:/html/body/header/nav/div[1]/div[2]/div[2]/ul[1]/li[5]/a


    close browser