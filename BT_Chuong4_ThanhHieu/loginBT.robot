*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}             https://opensource-demo.orangehrmlive.com/web/index.php/auth/login   
${VALID USER}      Admin
${VALID PASS}      admin123
${INVALID USER}    thnjhjhfsd
${INVALID PASS}    skjgkjsdkjf

*** Test Cases ***
Valid Login
    [Documentation]    Kiểm tra đăng nhập thành công
    Open Browser    ${URL}    chrome
    Wait Until Element Is Visible    xpath=//input[@name="username"]    timeout=10
    Input Text    xpath=//input[@name="username"]    ${VALID USER}
    Input Text    xpath=//input[@name="password"]    ${VALID PASS}
    Click Button    xpath=//button[@type="submit"]
    Wait Until Page Contains Element    xpath=//h6[text()="Dashboard"]    timeout=10
    Page Should Contain    Dashboard
    Log To Console    Đăng nhập thành công
    Close Browser

Invalid Login
    [Documentation]    Kiểm tra đăng nhập thất bại
    Open Browser    ${URL}    chrome
    Wait Until Element Is Visible    xpath=//input[@name="username"]    timeout=10
    Input Text    xpath=//input[@name="username"]    ${INVALID USER}
    Input Text    xpath=//input[@name="password"]    ${INVALID PASS}
    Click Button    xpath=//button[@type="submit"]
    Wait Until Element Is Visible    xpath=//p[contains(@class, "oxd-alert-content-text")]    timeout=15
    Element Text Should Be    xpath=//p[contains(@class, "oxd-alert-content-text")]    Invalid credentials
    Log To Console    Đăng nhập thất bại
    Close Browser

