*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}      https://www.countries-ofthe-world.com/flags-of-the-world.html
${browser}  chrome

*** Test Cases ***
scrolling
    browserlogin
    execute javascript  window.scrollTo(0, 1000)
    sleep   3
    execute javascript  window.scrollTo(0, 2000)
    sleep  3
    execute javascript  window.scrollTo(0, 5000)
    sleep   3

    execute javascript     window.scrollTo(0, -document.body.scrollHeight)
    sleep   3
    execute javascript      window.scrollTo(0,document.body.scrollHeight)
    sleep   3
    execute javascript     window.scrollTo(0, -document.body.scrollHeight)
    sleep   3
    scroll element into view  xpath://*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img
    sleep   3
    close browser

*** Keywords ***
browserlogin
    open browser    ${url}          ${browser}
    maximize browser window
