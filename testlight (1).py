# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 23:23:50 2020

@author: dell
"""

import speech_recognition as sr 
import datetime
import wikipedia
import pyttsx3
import webbrowser
import random
import os
import calendar
from datetime import date
import time
import subprocess
import requests
from bs4 import BeautifulSoup 
#from newspaper import Article
from GoogleNews import GoogleNews
#import speedtest
from num2words import num2words
from covid import Covid
import platform
import socket as s
#import sports
#from pynotifier import Notification
import bs4
#import pyjokes
#from translate import Translator
#import pyautogui as p

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
#engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',100)

#engine.say("tell me which voice do you prefer , male  or  female")
#here audio is var which contain text
def speak(audio):  
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("good morning sir i am light")
    elif hour>=12 and hour<18:
        speak("good afternoon sir i am light ") 
    else:
        speak("good evening sir i am light ") 
        
def weather():
     quer="bareilly up"
     search="weather in {}".format(quer)
     URL= "https://www.google.com/search?q={}".format(search)
     req=requests.get(URL)
     sav=BeautifulSoup(req.text,"html.parser")
     update=sav.find("div",class_="BNeawe").text
     speak("today bareilly has temperature of")
     speak(update) 
     
     
def calendr():
     today=date.today()
     t=time.localtime()
     c_t=time.strftime("%H:%M:%S", t)
     today=date.today()
     bn= datetime.datetime.strptime(str(today), '%Y-%m-%d').weekday()
     yd=calendar.day_name[bn]
     speak(" if we talk about todays calendar then")
     speak("date is") 
     speak(today)
     speak("time is ")
     speak(c_t)
     speak("and day is")
     speak(yd)
     
     
def speed():
    test=speedtest.Speedtest()
    download=test.download()
    upload=test.upload()
    speak(" download speed is {} bytes \n upload speed is {} bytes".format(int(download),int(upload)))
    
def malevoice():
    engine.setProperty('voice',voices[0].id)
    
def femalevoice():
    engine.setProperty('voice',voices[1].id)
    
    
     

#now convert audio to text 
def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listning....")
        audio = r.listen(source)
    try:
        print("Recognising.") 
        text = r.recognize_google(audio,language='en-in')
        print(text)
    except Exception:                #For Error handling
        speak("error...")
        print("Network connection error") 
        return "none"
    return text


#voice selection 
# speak("tell me which voice do you prefer , man  or  female")
# q=takecom().lower()
# if "man" in q:
#     malevoice()
# if "female" in q:
#     femalevoice()
    
    
#for main function                               
if __name__ == "__main__":
    # wish()
    # weather()
    # calendr()
   # speed()
  
    speak(" what can i do for you , tell me , i am listening")
    while True:
        query = takecom().lower()

        if "wikipedia" in query or "who is" in query:
            speak("searching details....Wait")
            query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        elif "weather" in query or " temperature " in query :
            speak("please tell me the name of the place ")
            quer=takecom().lower()
            search="weather in {}".format(quer)
            URL= "https://www.google.com/search?q={}".format(search)
            req=requests.get(URL)
            sav=BeautifulSoup(req.text,"html.parser")
            update=sav.find("div",class_="BNeawe").text
            speak(update)
            
        # elif 'joke' in query:
        #     sy=pyjokes.get_joke()
        #     translator=Translator(to_lang="Hindi")
        #     tra=translator.translate(sy)
            
        #     translator=Translator(to_lang="english")
        #     trp=translator.translate(tra)
        #     print(tra)
        #     speak(trp)
            #speak("if you didnot understand then look at the screen  ")
            
            
        elif "screenshot" in query:
            ss=p.screenshot()
            ss.save('ss.png')
            speak("screenshot taken ")
            
        elif "translate" in query:
            speak("tell me the language in which you want to translate .")
            tr=takecom().lower()
            translator=Translator(to_lang=tr)
            speak("what you want to translate please speak ")
            q=takecom().lower()
            translation=translator.translate(q)
            speak("look at the screen for results please")
            print(translation)
       
        elif 'open youtube' in query or "open video online" in query:
            webbrowser.open("https://www.youtube.com")
            speak("opening youtube")
        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")  
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")      
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")    
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("opening google")
            
        elif 'open yahoo' in query:
            webbrowser.open("https://www.yahoo.com")
            speak("opening yahoo")
            
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail") 
            
        elif 'open snapdeal' in query:
            webbrowser.open("https://www.snapdeal.com") 
            speak("opening snapdeal")  
             
        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")
        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("opening flipkart")   
        elif 'open ebay' in query:
            webbrowser.open("https://www.ebay.com")
            speak("opening ebay")
        elif 'music from pc' in query:
            speak("ok i am playing music")
            music_dir = './music'
            musics = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,musics[0]))
        elif 'video from pc' in query:
            speak("ok i am playing videos")
            video_dir = './video'
            videos = os.listdir(music_dir)
            os.startfile(os.path.join(video_dir,videos[0]))
        elif query == 'none':
            continue 
        elif "music" in query:
            speak("tell me the name of the song")
            quer=takecom().lower()
            webbrowser.open("https://www.jiosaavn.com/search/"+quer)  
            
        elif "video" in query:
            speak("tell me the name of the vedio") 
            quer=takecom().lower()
            webbrowser.open("https://www.youtube.com/results?search_query="+quer)  
        elif 'good bye' in query:
            speak("good bye")
            exit()
        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s')            
        elif "restart" in query:
            speak("restarting...")
            os.system('shutdown /r')
        elif 'news' in query:
            speak("tell me the area of news, sir")
            topic=takecom().lower()
            googlenews=GoogleNews()
            googlenews=GoogleNews("en","d")
            googlenews.search("{}".format(topic))
            googlenews.result()
            googlenews.getpage(2)
            q=googlenews.gettext()
            speak(q)
            print(q)

        elif  'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            ans_take_from_user_how_are_you = takecom()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('okey..')  
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')  
        elif 'make you' in query or 'created you' in query or 'develop you' in query:
            ans_m = " For your information Paritosh and his team Created me ! I give Lot of Thannks to Him "
            print(ans_m)
            speak(ans_m)
        elif "who are you" in query or "what can you do" in query or "your details" in query:
            about = "I am light and  I am based on computer program but i can help you as much as i can ! i promise you ! try to give  commands ! like playing music or video from your directory i also play video and song from web or online ! i can also entertain you so i hope  you Understand me ! ok Lets Start "
            print(about)
            speak(about)
        elif "hello" in query or "hello light" in query:
            hel = "soo ! How May i Help you.."
            print(hel)
            speak(hel)
        elif "your name" in query or "sweat name" in query:
            na_me = "Thanks for Asking  ,   myself light"  
            print(na_me)
            speak(na_me)
        elif "open executables" in query:
            speak('which executable file do you want me to run')
            query1=takecom()
            print(query1+'.exe')
            os.system(query1+'.exe')
        elif "open shortcut files" in query:
            speak('which shortcut file do you want me to run')
            query1=takecom()
            print(query1+'.lnk')
            os.system(query1+'.lnk')
        elif "you feeling" in query:
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you") 
        elif query == 'none':
            continue 
        elif 'exit' in query or 'thank you' in query or 'stop' in query or 'bye' in query or 'quit' in query :
            ex_exit = 'have a good time , Humans  '
            speak(ex_exit)
            exit()
        elif 'close browser' in query:
            subprocess.call("taskkill /IM chrome.exe")
            speak("closing browser")
        elif "date" in query:
            today=date.today()
            print(today)
            speak(today)
        elif "time" in query:
            t=time.localtime()
            c_t=time.strftime("%H:%M:%S", t)
            print(c_t)
            speak(c_t)
        elif "day" in query:
            bn= datetime.datetime.strptime(str(today), '%Y-%m-%d').weekday()
            yd=calendar.day_name[bn]
            print(yd)
            speak(yd)
        elif "system information" in query:
            speak(" system is")
            speak(platform.system())
            speak("version is")
            speak(platform.version())
            speak("machine is")
            speak(platform.machine())
            speak("platform is")
            speak(platform.platform())
            speak("processor is of ")
            speak(platform.processor())   
            
        elif "live score" in query:
           link='https://www.cricbuzz.com/live-cricket-scorecard/31647/3rd-test-india-tour-of-australia-2020-21'
           res=requests.get(link)
           soup=bs4.BeautifulSoup(res.text,'html.parser')
           updat=soup.find("div",class_="cb-col cb-col-100 cb-scrd-hdr-rw").text    
           print(updat) 
           speak(updat)
            # matchinfo=sports.get_sport(sports.BASKETBALL)
            # Notification(title="LIVE SCORE", description=str(matchinfo),duration=40).send()
            
        elif "hostname" in query:
            host=s.gethostname()
            IPAD=s.gethostbyname(host)
            speak(IPAD)
            print(IPAD)


        # elif "corona update" in query:
        #     r=requests.get("https://covid-19tracker.milkeninstitute.org/")
        #     soup=BeautifulSoup(r,'html.parser')
        #     res=soup.find_all("div",class_="is_h5-2 is_developer w-richtext")
        #     print(str(res[279:305]))

        # elif "coronavirus" or "pandemic" in query:
        #     covi=Covid()
        #     p=covi.get_total_active_cases()
        #     pr=covi.get_total_deaths()
        #     pri=covi.get_total_confirmed_cases()
        #     #print(p)
        #     speak("active cases are ")
        #     speak(num2words(p,to="ordinal"))
        #     speak("total deaths are ")
        #     speak(num2words(pr,to="ordinal"))
        #     speak("confirmed cases are ")
        #     speak(num2words(pri,to="ordinal"))
            
        else:
            speak("No result found! Do u want me to search it on Google")   #ask for google search
            query1 = takecom().lower()
            if "yes" in query1:
                temp = query.replace(' ','+')
                g_url="https://www.google.com/search?q="    
                res_g = 'searching your query on google'
                print(res_g)
                speak(res_g)
                webbrowser.open(g_url+temp)     
            if "no" in query1:
                speak("ok now what")
                continue