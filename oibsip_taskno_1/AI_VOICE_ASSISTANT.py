# Name:- Somesh Ramdas Jatti
# Task 3:- Voice Assistant

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import pyaudio
import smtplib


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")
    print('I am Jarvis Sir.')

def takeCommand():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

            try:
                statement = r.recognize_google(audio, language='en-in')
                print(f"user said:{statement}\n")

            except Exception as e:
                speak("Pardon me, please say that again")
                return "None"
            return statement


wishMe()
speak('I am Jarvis Sir')

def send_email(recipient, subject, message):
    # Set up your email server and login credentials
    email_address = 'ternacity5@gmail.com'
    password = 'terna12345@'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_address, password)

    # Create and send the email
    email_text = f'Subject: {subject}\n\n{message}'
    server.sendmail(email_address, recipient, email_text)

    # Close the server connection
    server.quit()


# Function to get a trivia question from the Open Trivia Database
def get_trivia_question():
    response = requests.get("https://opentdb.com/api.php?amount=1&type=multiple")
    data = response.json()
    question = data['results'][0]['question']
    options = data['results'][0]['incorrect_answers']
    correct_answer = data['results'][0]['correct_answer']
    return question, options, correct_answer

# Function to set a reminder
def set_reminder(event, date_time):
    try:
        date_time = datetime.datetime.strptime(date_time, "%d-%m-%Y %H:")
        now = datetime.datetime.now()
        time_difference = (date_time - now).total_seconds()

        if time_difference <= 0:
            speak("Invalid date or time. Please provide a future date and time.")
            return

        # Calculate the time to sleep in seconds
        sleep_time = time_difference.total_seconds()
        time.sleep(sleep_time)
        speak(f"Reminder: {event} at {date_time}")
    except Exception as e:
        speak(str(e))


if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant SpeakSage is shutting down,Good bye')
            print('your personal assistant SpeakSage is shutting down,Good bye')
            break



        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                current_temperature_in_celsius = current_temperature - 273.15
                speak(" Temperature is " +
                      str(round(current_temperature_in_celsius, 2)) + " degrees Celsius" +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature = " +
                      str(round(current_temperature_in_celsius, 2)) + " degrees Celsius" +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%I:%M:%S %p")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Jarvis version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Somesh")
            print("I was built by Somesh")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)


        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "send email" in statement:
            speak("To whom do you want to send the email?")
            recipient = takeCommand().lower()
            speak("What's the subject of the email?")
            subject = takeCommand().lower()
            speak("What should be the content of the email?")
            message = takeCommand().lower()

            try:
                send_email(recipient, subject, message)
                speak("Email sent successfully.")
            except Exception as e:
                speak("Sorry, I couldn't send the email. Please try again later.")

        if 'trivia' in statement:
            question, options, correct_answer = get_trivia_question()
            speak(question)
            print(question)
            for i, option in enumerate(options):
                speak(f"Option {i + 1}: {option}")
                print(f"Option {i + 1}: {option}")
            speak("What's your answer?")
            user_answer = takeCommand().lower()
            if user_answer == correct_answer.lower():
                speak("Correct! Well done.")
            else:
                speak("Sorry, that's incorrect. The correct answer is: " + correct_answer)

        elif 'set reminder' in statement:
            speak("Sure, what's the event?")
            event = takeCommand()
            speak("When should I remind you? Please specify the date and time.")
            date_time = takeCommand()
            set_reminder(event, date_time)

time.sleep(3)










