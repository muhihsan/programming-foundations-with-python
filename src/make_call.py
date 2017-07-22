from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)

call = client.calls.create(to="",
                           from_="",
                           url="http://demo.twilio.com/docs/voice.xml")

print(call.sid)
