*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/datadrivenresources.robot
Suite Setup         openmybrowser
Suite Teardown      closebrowser
Test Template       Invalidlogin

*** Variables ***

*** Test Cases ***          user            pswd

wuwp    dsgjd                   jfhsj
ruwp    admin@yourstore.com     dwddw
wuep    csdcs                   ${EMPTY}
wurp    dwed                    admin
ruep    admin@yourstore.com     ${EMPTY}




*** Keywords ***
Invalidlogin
    cleardata
    [Arguments]  ${user}    ${pswd}
    inpuser  ${user}
    inppswd  ${pswd}
#    clicklogin
    errormsg
#validlogin
#    cleardata
#    [Arguments]  ${user}    ${pswd}
#    inpuser  ${user}
#    inppswd  ${pswd}
#    clicklogin
#    loginsuccess