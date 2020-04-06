from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC61f682127809466145c8d416aed0ae6e'
auth_token = 'be7288eb387df031d7b61ff6417c8790'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hi. this is text message test.",
                     from_='+14439917448',
                     to='+821035337121'
                 )

print(message.sid)