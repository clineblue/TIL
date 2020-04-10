from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = '홈페이지에서 받은 시드값'
auth_token = '홈페이지에서 받은 토큰 값'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="보낼 메시지",
                     from_='+14439917448',
                     to='+82전화번호'
                 )

print(message.sid)
