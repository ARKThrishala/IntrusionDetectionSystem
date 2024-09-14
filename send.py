from twilio.rest import Client
account_sid = 'UWT81B1WLXRAFQKTZFFR144D'
auth_token = '7e4c5c0fabae1d5f7dcda83bf2b5b965'
client = Client(account_sid, auth_token)
def sendSms():
    message = client.messages.create(
    from_='9121563315',
    body='Alert ',
    to='+917670890705'
    )

    print(message.sid)

