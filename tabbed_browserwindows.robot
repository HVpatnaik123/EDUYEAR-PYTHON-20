*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
tabbedbrowser
    open browser  http://demo.automationtesting.in/Windows.html     chrome
    maximize browser window
    click button  xpath://*[@id="Tabbed"]/a/button

    sleep   3
    select window  title=Frames & windows
    click link  xpath=/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a
    sleep   3
    select window  title=SeleniumHQ Browser Automation
    page should contain  BLACK LIVES MATTER

    close browser
