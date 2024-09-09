from twilio.rest import Client
account_sid = 'AC260b53286d7f7e12b7ab3f19663e76b4'
auth_token = '4f44eeab64250b14949342449dbf60ca'
client = Client(account_sid, auth_token)
message = client.messages.create(
  messaging_service_sid='MGad478fcec26cc94799067d502d9160f6',
  body='This is working just fine!!!',
  to='+40725929880'
)
print(message.sid)