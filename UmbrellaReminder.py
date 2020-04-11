from bs4 import BeautifulSoup
import smtplib
import requests as rq


url=rq.get('https://forecast.weather.gov/MapClick.php?lat=40.71455000000003&lon=-74.00713999999994')

soup=BeautifulSoup(url.text,'html.parser')

weather= (soup.select('#current_conditions-summary p')[0]).text
temperature= (soup.select('#current_conditions-summary p')[1]).text



if weather == 'Raining' or weather == 'Overcast':
    server = smtplib.SMTP('smtp.gmail.com', 587)
    print(server.ehlo())
    print(server.starttls())

    server.login('awish4alll@gmail.com', 'cqtzjhqeqafahmvs')

    subject = "Umbrella Reminder"
    body = f"Take an umbrella with you. Weather condition for today is {weather} and temperature is {temperature} in New York."

    msg = f"Subject:{subject}\n\n{body}\n\nRegards,\nVishal".encode('utf-8')
    print(msg)

    server.sendmail('awish4alll@gmail.com', 'vishal.sharma5181@gmail.com', msg)

    print("Email Sent!")

    server.quit()
else:
    print("There is going to be {} and temperature is {} in New York".format(weather,temperature))


