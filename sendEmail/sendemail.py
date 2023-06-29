# =============================================================================
# Imports
# =============================================================================
import smtplib

# =============================================================================
# SET EMAIL LOGIN REQUIREMENTS
# =============================================================================
gmail_user = 'zerotoskyemail@gmail.com'
gmail_app_password = 'xpiuzwzhmcksapck'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_app_password)
    server.sendmail(sent_from, sent_to, email_text)
    server.close()

    print('Email sent!')
except Exception as exception:
    print("Error: %s!\n\n" % exception)