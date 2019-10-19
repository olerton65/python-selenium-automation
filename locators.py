"""

1. Amazon logo: search by XPATH, "//a[@class='a-link-nav-icon']/i"

2. Continue button: search by XPATH, "//span[@class='a-button a-button-span12 a-button-primary']/span"

3. Need help link: search by XPATH, "//span[@class='a-expander-prompt']" OR by XPATH, "//*[contains(text(),
'Need help?')]"

4. Forgot your password link: search by XPATH, "//a[@id='auth-fpp-link-bottom' and @class='a-link-normal']"

5. Other issues with Sign-in link: search by XPATH, "//a[@id='ap-other-signin-issues-link']" OR by XPATH,
"//div[@class='a-expander-content a-expander-inline-content a-expander-inner a-expander-content-expanded']/a[
@href='/gp/help/customer/account-issues/ref=ap_login_with_otp_claim_collection?ie=UTF8']"

6. Create your Amazon account button: search by XPATH, "//span[@id='auth-create-account-link' and @class='a-button
a-button-span12 a-button-base']"

7. Conditions of Use link (at the bottom of the screen): search by XPATH, "//a[@class='a-link-normal' and
@href='/gp/help/customer/display.html/ref=ap_desktop_footer_cou?ie=UTF8&nodeId=508088']"                `

N.B. UNFORTUNATELY I couldn't find XPATH which highlights the link 'Conditions of Use' under the button Continue.
All possible combinations of XPATH highlight the whole element:
 "By continuing, you agree to Amazon's Conditions of
Use and Privacy Notice."

8. Privacy Notice link: search by XPATH, "//*[
@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']//self::a"

"""