from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import smtplib
from email.mime.text import MIMEText

adminEmail = 'zerotoskyemail@gmail.com'
gmailUser = 'zerotoskyemail@gmail.com'
gmailAppPassword = 'xpiuzwzhmcksapck'


class EmailView(APIView):
    def post(self, request):

        emailReqBody = request.data
        subject = emailReqBody['subject']
        message = emailReqBody['message']
        userEmail = emailReqBody['userEmail']

        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = userEmail
        msg['To'] = adminEmail

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmailUser, gmailAppPassword)
        server.sendmail(userEmail, adminEmail,  msg.as_string())

        # to admin
        # to user as ack
        msg = MIMEText(
            'Thanks! For Contacting legal, We will shortly reply to you response.')
        msg['Subject'] = 'No Reply - Your Booking is Successful'
        msg['From'] = adminEmail
        msg['To'] = userEmail
        server.sendmail(adminEmail, userEmail, msg.as_string())
        server.close()
        return Response({'message': "Message Send Successfully"}, status=status.HTTP_200_OK)
