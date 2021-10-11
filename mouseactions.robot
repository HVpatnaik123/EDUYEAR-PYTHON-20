*** Settings ***

Library  SeleniumLibrary

*** Test Cases ***

actionsmouse
    open browser  https://swisnl.github.io/jQuery-contextMenu/demo.html     chrome
    maximize browser window
#   right click action
    open context menu   xpath:/html/body/div/section/div/div/div/p/span
    sleep   3
    click link  xpath://li[@class='context-menu-item context-menu-icon context-menu-icon-copy']
#    go to   https://testautomationpractice.blogspot.com/
#    double click element  xpath://*[@id="HTML10"]/div[1]/button
#    ${valu}=     get text  id:field2
#    log to console  ${valu}
#
#    drag and drop  xpath://*[@id="draggable"]/p     //*[@id="droppable"]
#    sleep   3
#    close all browsers