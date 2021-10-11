*** Settings ***

Library  SeleniumLibrary

*** Test Cases ***

screeny
    open browser  https://opensource-demo.orangehrmlive.com   chrome
    maximize browser window
    capture page screenshot
    capture element screenshot  xpath://*[@id="divLogo"]/img
    close browser