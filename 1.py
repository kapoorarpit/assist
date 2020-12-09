import speech_recognition as sr 
import datetime
import wikipedia
import pyttsx3
import webbrowser
import random
import os
import subprocess 
import pygame 
pygame.init()

win = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Personal assistant")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[2].id)

def speak(audio):  #here audio is var which contain text
    engine.say(audio)
    engine.runAndWait()

def wish():         #edit this as per convenience--------
    hour = int(datetime.datetime.now().hour)
    if hour >=4 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<17:
        speak("good afternoon") 
    elif hour>=17 and hour<20:
        speak("good evening")  
    else:
        speak("good night")
                    #-------------------------------------

#now convert audio to text
# 
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

silver = (192,192,192)
#-------------------------------------
def redrawGameWindow():
    win.fill(silver)
#-------------------------------------

run = True
#for main function                               
if __name__ == "__main__":
    wish()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                run = False
        
        while run:
            query = takecom().lower()

            if "wikipedia" in query:
                speak("searching details....Wait")
                query.replace("wikipedia","")
                results = wikipedia.summary(query,sentences=2)
                print(results)
                speak(results)
            elif 'open youtube' in query or "open video online" in query:
                webbrowser.open("www.youtube.com")
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
            elif 'music from pc' in query or "music" in query:
                speak("ok i am playing music")
                music_dir = './music'
                musics = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,musics[0]))
            elif 'video from pc' in query or "video" in query:
                speak("ok i am playing videos")
                video_dir = './video'
                videos = os.listdir(music_dir)
                os.startfile(os.path.join(video_dir,videos[0]))    
#       elif "music" in query:
#            speak("ok i am playing music")
#            webbrowser.open("https://www.jiosaavn.com/search/"+query)  
#            
#        elif "video" in query:
#            speak("ok i am playing videos")
#          webbrowser.open("https://www.youtube.com/results?search_query="+query)  
            elif 'good bye' in query:
                speak("good bye")
                exit()
            elif "shutdown" in query:
                speak("shutting down")
                os.system('shutdown -s') 
            elif "what\'s up" in query or 'how are you' in query:
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
            elif "who are you" in query or "about you" in query or "your details" in query:
                about = "I am light an A I am based on computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
                print(about)
                speak(about)
            elif "hello" in query or "hello Jarvis" in query:
                hel = "soo ! How May i Help you.."
                print(hel)
                speak(hel)
            elif "your name" in query or "sweat name" in query:
                na_me = "Thanks for Asking my myself light"  
                print(na_me)
                speak(na_me)
            elif "you feeling" in query:
                print("feeling Very sweet after meeting with you")
                speak("feeling Very sweet after meeting with you") 
            
            #forcefull termination(web browser(chrome))------------------------
            elif 'close browser' in query:
                subprocess.call("taskkill /IM chrome.exe")
                speak("closing browser")
            #-----------------------------------------------------------------
            
            #manual-------------------------------------------------------------
            #elif "play starboy" in query:
            #    print("playing starboy")
            #    os.system('starboy.mp4')
            #elif "open power point" in query:
            #    print("opening power point")
            #    os.system('pp.lnk')
            #elif "open Virtual dj" in query:
            #    print("opening Virtual Dj")
            #    os.system('virtualdj8.exe')
            #------------------------------------------------------------------

            #Automated---------------------------------------------------------
            #workspace must contains these query files-------------------------
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
            elif "open a video" in query: #video format mp4 supported
                speak('which shortcut file do you want me to run')
                query1=takecom()
                print(query1+'.mp4')
                os.system(query1+'.mp4')
            #-----------------------------------------------------------------
            
            #forcefull termination(system files)------------------------------


            #-----------------------------------------------------------------
            
            elif query == 'none':
                continue 
            elif 'exit' in query or 'thank you' in query or 'stop' in query or 'bye' in query or 'quit' in query :
                ex_exit = 'I feeling very sweet after meeting with you but you are going! i am very sad'
                speak(ex_exit)
                exit()    
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
                else:
                    continue
        
    redrawGameWindow()

pygame.quit()



