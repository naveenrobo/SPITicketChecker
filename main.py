import requests
from twilio.rest import Client

# declare variables here
account_sid = "<twilio sid>"
auth_token = "<twilio auth token>"
numbers = ["+91xxxxxxxxxx", "+91xxxxxxxxxx"]
debug = "+91xxxxxxxxxx"

url = "https://www.spicinemas.in/chennai/now-showing"


def whatsapp(to, message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                                from_='whatsapp:+14155238886',
                                body=message,
                                to='whatsapp:'+to
                            )
    print(message.sid)

print("Running 5 mins script")

# do the stuffs here
try:
    r = requests.get(url)
    if(r.status_code == 200):
        try:
            print("getting content")
            content = r.text.lower()
            if "avengers" in content:
                print("Booking opened")
                for number in numbers:
                    whatsapp(number,"Bookings opened in SPI Cinemas. Hurry!!!😀😀")
        except Exception as e:
            print("Exception!!!")
            whatsapp(debug,"Exception in your script. Idiot 😐😐"+e)
            print(e)
    else:
        print("error while loading page")
        whatsapp(debug,"Error while loading the page. 😐😐")
except Exception as e:
    whatsapp(debug,"Exception in your script. Idiot 😐😐."+e)

