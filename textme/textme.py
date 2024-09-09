from twilio.rest import Client
account_sid = ''
auth_token =
client = Client(account_sid, auth_token)
message = client.messages.create(
  messaging_service_sid=,
  body='This is working just fine!!!',
  to=
)
print(message.sid)