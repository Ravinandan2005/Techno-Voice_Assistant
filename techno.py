#Project voice assistant - Ravi
#importing necessary modules
import pyttsx3 #text to speech
import speech_recognition as sr #recognize speech through microphone or audio files
import datetime #date and time
import os #used for file operations
import subprocess #to open desktop apps
import webbrowser #open urls in the default browser
import pywhatkit as kit #to play youtube videos
import cv2 #to access camera
import time #for time
import pyautogui #to control mouse and keyboard (screenshot purpose)
import pyjokes #programmer jokes
import random #randomize
import wikipedia #to access wikipedia
import requests #requests website raw code
import psutil  # For checking running processes

#initialize the engine
#Set our engine to "Pyttsx3" which is used for text to speech in Python and sapi5 is Microsoft speech application platform interface 
#we will be using this for text to speech function.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)#change the number for the different voices by default there will be 0 and 1 in windows
engine.setProperty('rate', 250) # speed of the speach

'''#Testing engine
engine.say("Hi Ravi I'm Techno")
engine.runAndWait()'''

#initializing speak function
def speak(text):
    print(f"Techno: {text}")
    engine.say(text)
    engine.runAndWait()
# speak("Hi Ravi I'm Techno")

#initializing Listen function
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio =  recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower() #Convert speech to text using google recognizer
            print(f"Ravi: {command}")
            return command
        except sr.UnknownValueError: #if speech not recognized
            return ""
        except sr.RequestError:
            speak("Sorry, there was an error connecting to the speech recognition service.")
            return ""
        except Exception as e:
            print(f"Error: {e}")
            speak("An unexpected error occurred.")
            return ""
#command = listen()

#greeting user
def greet_user():
    hour = datetime.datetime.now().hour #fetching the hour
    if(hour<12): #if less than 12 hours morning
        return "Good Morning Ravi, how may i help you?"
    elif(hour>=12 and hour<18): #equal or greater than 12 and less than 6 i.e, 18 afternoon
        return "Good Afternoon Ravi, how may i help you?"
    else: #Else return evening
        return "Good Evening Ravi, how may i help you?"
# greeting = greet_user()
# speak(greeting)

#welcome message
def started_message():
    start_msg = ["Hi, Ravi! I'm Techno, your personal assistant. How can I help you today?", "Hello, Ravi! It's me, Techno. Ready to assist you with anything?", "Hey, Ravi! How's it going? Techno's here to help you out!", "Good day, Ravi! What can I do for you today?", "Hi there, Ravi! Techno's at your service. What do you need?", "Hello, Ravi! I’m all set to help. What can I do for you?", "Hey, Ravi! It’s your friendly assistant, Techno. What’s on your mind today?", "Greetings, Ravi! I'm here to assist with anything you need. What can I do for you?", "Hey, Ravi! Techno reporting for duty. How may I help you?", "Hello, Ravi! Techno here, ready to make your day easier. What can I do?", "Hi, Ravi! It's Techno. Let me know how I can assist you today.", "Good morning, Ravi! How can Techno help you today?", "Hey, Ravi! I'm Techno, your personal assistant. Let's get started!", "Hello, Ravi! How can I assist you today? Techno’s at your service!", "Hi, Ravi! Techno’s here. What do you need help with today?", "Good evening, Ravi! Techno’s ready to assist. What can I do for you?", "Hi, Ravi! I’m Techno, your personal assistant. Ready when you are!", "Hey, Ravi! Need any help today? Techno’s ready to assist!", "Hello, Ravi! I’m here to help. Let me know what you need!"]
    return random.choice(start_msg)

#To get the current time
def get_current_time():
    #Returns the current time as a string.
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")
#time = get_current_time()
# speak(time)

#Date
def get_current_date():
    #Returns the current date as a string.
    today = datetime.date.today()
    return today.strftime("%B %d, %Y")
# date = get_current_date()
# speak(date)

#To check app is running or any active session
def is_app_running(app_name):
    for proc in psutil.process_iter(['name']):
        try:
            print(f"Checking process: {proc.info['name']}")  # Debugging line
            if app_name.lower() in proc.info['name'].lower():
                print(f"App {app_name} found running as {proc.info['name']}")  # Debugging line
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return False

# Define the app paths
app_paths = {
    "notepad" : "notepad.exe",
    "calculator" : "calc.exe",
    "chrome" : "C:/Program Files/Google/Chrome/Application/chrome.exe",
    "brave" : "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe",
    "fortnite" : "com.epicgames.launcher://apps/fn%3A4fe75bbc5a674f4f9b356b5c90567da5%3AFortnite?action=launch&silent=true",
    "excel" : "C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE",
    "word" : "C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE",
    "edge" : "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
    "power point" : "C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE",
    "sublime" : "C:/Program Files/Sublime Text 3/sublime_text.exe",
    "valorant" : "C:/Riot Games/VALORANT/live/VALORANT.exe",
    "discord" : "C:/Users/ravin/AppData/Local/Discord/Update.exe --processStart Discord.exe",
    "spotify" : "spotify.exe",
    "zoom" : "C:/Users/ravin/AppData/Roaming/Zoom/bin/Zoom.exe",
    "anydesk" : "C:/Users/ravin/Downloads/AnyDesk.exe",
    "visual studio code" : "C:/Users/ravin/AppData/Local/Programs/Microsoft VS Code/Code.exe"
}

# Define the websites
websites = {
    "youtube": "https://www.youtube.com",
    "x": "https://www.x.com",
    "reddit": "https://www.reddit.com",
    "linkedin": "https://www.linkedin.com",
    "github": "https://www.github.com",
    "instagram": "https://www.instagram.com",
    "facebook": "https://www.facebook.com",
    "whatsapp" : "https://web.whatsapp.com/",
    "twitter" : "https://www.twitter.com",
    "google" : "https://www.google.com",
    "stack overflow" : "https://stackoverflow.com",
    "pinterest" : "https://www.pinterest.com",
    "discord" : "https://discord.com",
    "spotify" : "https://www.spotify.com",
    "twitch" : "https://www.twitch.tv",
    "netflix" : "https://www.netflix.com",
    "amazon" : "https://www.amazon.com",
    "flipkart" : "https://www.flipkart.com",
    "chatgpt" : "https://chatgpt.com/",
    "chat gpt" : "https://chatgpt.com/"
}
    
#To open or close app/website
def open(command):
    command = command.lower()

    # If the command contains "open"
    command = command.replace("open", "").strip()
        
    # Try to open an app if the command matches
    for app, path in app_paths.items():
        if app in command:
            try:
                subprocess.Popen(path)  # Open the app
                speak(f"Opening {app}")
                return
            except Exception as e:
                speak(f"Sorry, I couldn't open {app}. Error: {e}")
                break

    # If app isn't found, try to open a website
    for site, url in websites.items():
        if site in command:
            webbrowser.open(url)  # Open the website
            speak(f"Opening {site}")
            return

    # If neither app nor website is found, perform a Google search
    speak("I couldn't find any app or website . Let me search it online.")
    search_google(command)

def close(command):
    command = command.lower()
    # If the command contains "close"
    command = command.replace("close", "").strip()
    # print(f"Command after 'close' is removed: {command}")  # Debugging line
    app_found = False
    site_found = False
    # if command in app_paths:
    # Iterate over all processes and match app_name with process name
    
    for proc in psutil.process_iter(['pid', 'name']):
        if command.lower() in proc.info['name'].lower():
            try:
                proc.terminate()  # Try to terminate the process
                app_found = True
            except Exception as e:
                print(f"Error closing {command}: {e}")

    if any(site in command for site in websites.keys()):
        pyautogui.hotkey("ctrl", "w")  # Close browser tab
        site_found = True
    # Speak once if either app or website was found
    if app_found==True or site_found==True:
        speak(f"Closing {command}")  # Speak only once
    else:
        speak(f"I couldn't find {command} to close.")

# Perform Google search
def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Searching Google for {query}")
# search_google("Ariana")

#Perform YouTube search or play
def youtube_search_or_play(query, play=False):
    if play:
        # Play the first video related to the query
        kit.playonyt(query)
        speak(f"Playing {query} on YouTube")
    else:
        url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(url)
        speak(f"Searching YouTube for {query}")
# youtube_search_or_play("the hills", play=True)

def take_picture():
    # Open the camera
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        speak("Failed to open the camera.")
        return

    speak("Preparing to take your picture. Please wait.")
    
    # Open a window to show the camera feed
    cv2.namedWindow("Camera Feed")

    # Countdown duration
    countdown_time = 3  # Countdown in seconds
    start_time = time.time()

    # Countdown loop
    while True:
        ret, frame = cap.read()
        if not ret:
            speak("Camera feed not available.")
            break

        # Flip the frame horizontally for a mirror effect
        frame = cv2.flip(frame, 1)

        # Calculate remaining time
        elapsed_time = time.time() - start_time
        remaining_time = countdown_time - int(elapsed_time)

        # Display the live video feed with countdown or "Say Chee-eese!"
        if remaining_time > 0:
            cv2.putText(frame, f"Taking picture in {remaining_time} seconds...", (10, 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Say Chee-eese!", (10, 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Camera Feed", frame)

        # Capture the picture once the countdown is over
        if remaining_time <= 0 and elapsed_time >= countdown_time + 1:
            break

        # Check for manual exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            speak("Exiting without taking a picture.")
            cap.release()
            cv2.destroyAllWindows()
            return

    # Capture the picture
    ret, frame = cap.read()
    if ret:
        # Flip the frame horizontally for a mirror effect before saving
        frame = cv2.flip(frame, 1)

        # Start with the base filename
        base_filename = "selfie.jpg"
        filename = base_filename
        
        # Check if the file already exists, and increment the counter if it does
        counter = 1
        while os.path.exists(filename):
            filename = f"selfie({counter}).jpg"
            counter += 1
        
        # Save the picture
        cv2.imwrite(filename, frame)
        speak(f"Image saved as {filename}")
    else:
        speak("Failed to capture image.")

    # Release the camera and close all windows after the picture is taken
    cap.release()
    cv2.destroyAllWindows()

# Take a screenshot
def take_screenshot():
    # Set the base filename for the screenshot
    filename = "screenshot.png"
    speak("Taking Screenshot")
    # Check if the file already exists, and increment the counter if it does
    counter = 1
    while os.path.exists(filename):
        filename = f"screenshot({counter}).png"
        counter += 1

    # Take the screenshot and save it with a unique filename
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    
    # Notify the user that the screenshot has been saved
    speak(f"Screenshot taken and saved as {filename}")
#take_screenshot()

def alarm(command):
    """
    Set an alarm based on user input:
    - "set alarm for 1:30 PM"
    - "set alarm for 30 minutes"
    - "set alarm for 1 hour"
    - "set alarm for 30 seconds"
    """
    now = datetime.datetime.now()

    try:
        # Handle relative time (minutes, hours, or seconds)
        if "minute" in command or "hour" in command or "second" in command:
            command = command.replace("set alarm for", "").strip()
            # Extract number and unit (minute, hour, second)
            number, unit = command.split()[:2]
            number = int(number)

            if "minute" in unit:
                delta = datetime.timedelta(minutes=number)
            elif "hour" in unit:
                delta = datetime.timedelta(hours=number)
            elif "second" in unit:
                delta = datetime.timedelta(seconds=number)
            else:
                speak("Invalid time unit. Please use minutes, hours, or seconds.")
                return

            alarm_time = now + delta

        # Handle absolute time (e.g., "set alarm for 8:30 PM")
        else:
            command = command.replace("set alarm for", "").strip()
            alarm_time = datetime.datetime.strptime(command, "%I:%M %p")
            alarm_time = alarm_time.replace(year=now.year, month=now.month, day=now.day)

        # Ensure alarm is set for the future
        if alarm_time < now:
            speak("The alarm time is in the past. Adjusting to tomorrow.")
            alarm_time += datetime.timedelta(days=1)

        speak(f"Alarm set for {alarm_time.strftime('%I:%M %p')}.")

        # Wait until alarm time
        while True:
            now = datetime.datetime.now()
            if now >= alarm_time:
                print("Wake up! ⏰")
                speak("Wake up! Your alarm is ringing.")
                break
            time.sleep(1)

        # Snooze or stop alarm
        while True:
            speak("Would you like to snooze or stop the alarm?")
            user_input = listen()  # Listen for command
            if "snooze" in user_input:
                snooze_minutes = 5  # Set snooze duration
                alarm_time = datetime.datetime.now() + datetime.timedelta(minutes=snooze_minutes)
                speak(f"Snoozing for {snooze_minutes} minutes.")
                while True:
                    now = datetime.datetime.now()
                    if now >= alarm_time:
                        print("Wake up again! ⏰")
                        speak("Wake up again! Your alarm is ringing.")
                        break
                    time.sleep(1)
            elif "stop" in user_input or "off" in user_input:
                speak("Alarm stopped. Have a great day!")
                break
            else:
                speak("Sorry, I didn't catch that. Please say 'snooze' or 'stop'.")

    except ValueError as e:
        print(f"Invalid input: {e}")
        speak("Invalid time format. Please specify the alarm time correctly.")
      
# Tell jokes
def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)
# tell_joke()

#wikipedia search
def search_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        speak(f"According to Wikipedia, {summary}")
    except wikipedia.exceptions.DisambiguationError:
        speak("There are multiple results for that. Can you be more specific?")
    except wikipedia.exceptions.HTTPTimeoutError:
        speak("Sorry, there was a problem connecting to Wikipedia.")
    except wikipedia.exceptions.RequestError:
        speak("Sorry, there was an issue with the request.")
    except Exception as e:
        speak(f"Error: {e}")
# search_wikipedia("Python")

def who_am_i():
    responses = ["Hi! I'm Techno, your personal assistant.", "Hello! I'm Techno, always here to help you out.", "Hey, I'm Techno! Your personal assistant, ready to assist you.", "Techno here! I'm your friendly assistant. How can I help?", "I'm Techno, your personal assistant. Let's get things done!", "Hi, I'm Techno! Your assistant, and I'm at your service.", "Hello! I'm Techno. What can I do for you today?", "I'm Techno, your digital assistant. Ready to help anytime!", "Hi! I am Techno. How can I assist you today?", "Techno's here! Your personal assistant, always ready to help.", "Hey there! Techno at your service. What do you need?", "Yo! It's Techno! Let me know how I can assist you.", "Techno, your reliable assistant, reporting for duty!", "Well, well, well, look who needs assistance! Techno at your service!", "Welcome! Techno’s here and ready to make your day easier!", "Techno’s in the house! How can I make your life simpler?", "I'm Techno, your favorite personal assistant, ready to help with anything!", "Hello, my friend! Techno is here to assist you with anything you need.", "Techno here, your digital partner. What can I do for you today?", "Need something done? Techno’s got you covered!", "Techno’s your one-stop assistant for everything—just say the word!", "No task is too big for Techno! How can I help you today?", "Techno reporting for duty! How can I be of assistance?", "Your personal assistant Techno is here—let’s make some magic happen!", "Look no further—Techno’s here to help you get things done!", "Techno’s in action! What’s next on your to-do list?", "I’m Techno, your go-to assistant for everything. Ready to help!", "I’m Techno, your personal assistant designed to make your life easier!", "I'm Techno, a digital assistant here to help with tasks, reminders, and much more.", "I'm Techno, your friendly assistant, always available to lend a hand.", "I am Techno! I can help you with anything you need, from setting alarms to playing music!", "Call me Techno! I'm here to assist you in managing your day-to-day tasks.", "I’m Techno, your AI assistant. From helping with productivity to entertainment, I’ve got you covered!", "I’m Techno, your virtual assistant, ready to take care of your requests and make your life easier!", "Techno here! I’m designed to help you with anything, from organizing your schedule to answering your questions."]
    return random.choice(responses)

#about creator <3
def about_ravi():
    ravi_info = ["Ravi is a tech enthusiast who’s always on top of his game, whether it’s coding or academics.", "When Ravi sets his mind on something, nothing can stop him from achieving it.", "A true problem-solver, Ravi loves taking on new challenges and finding innovative solutions.", "Ravi is always learning and growing, constantly pushing the boundaries of tech and knowledge.", "From Python to Power Platform, Ravi has a deep understanding of a wide range of technologies.", "He’s a creator at heart—Ravi loves turning ideas into real-world applications.", "Ravi is someone who brings his A-game to every project, whether it’s tech or volunteering.", "With a passion for app development and data analysis, Ravi is always working on something cool.", "Ravi loves experimenting with new tech tools and figuring out how to make them work better.", "When Ravi works on a project, he dives in fully and puts his heart into making it a success.", "Ravi combines tech skills with problem-solving, making him a versatile and valuable resource.", "Ravi's tech skills are matched by his ability to learn quickly and adapt to any situation.", "Whether it's creating apps or analyzing data, Ravi is always at the forefront of innovation.", "Ravi loves building practical, real-world solutions through his projects and internships.", "Ravi brings a unique combination of technical expertise and creativity to everything he does.", "Ravi is not just a coder—he's someone who is always looking to solve real problems with tech.", "When it comes to tech and academics, Ravi is always focused on learning and improving.", "Ravi is passionate about making a difference through tech, whether it's through app development or data analysis.", "Ravi is a tech wizard who excels at using technology to solve complex problems and create useful applications.", "Ravi is driven, ambitious, and always ready to take on new challenges with a fresh perspective.", "From his tech projects to his volunteer work, Ravi is always looking for ways to make a positive impact.", "Ravi is someone who is constantly elevating the bar for excellence in both his personal and professional life.", "Ravi's problem-solving ability is like no other—he always finds the most efficient way to tackle issues.", "When Ravi puts his mind to something, it’s as good as done—he’s known for his focus and dedication.", "Ravi’s work ethic is unparalleled; he never gives up until the task is completed to perfection.", "Ravi has an eye for detail and a passion for perfection in every project he undertakes.", "Ravi's technical acumen and creative approach make him a true asset in any team.", "His dedication to his craft is evident in the countless hours he spends perfecting his skills.", "Ravi’s curiosity and drive to continuously learn make him stand out in everything he does.", "Ravi is always ahead of the curve, anticipating challenges and addressing them with ease.", "With a blend of technical expertise and creative vision, Ravi is always innovating new solutions.", "Ravi’s ability to handle multiple tasks and projects with ease is truly impressive.", "Ravi is a natural leader who inspires others through his work and his attitude towards challenges.", "Ravi’s passion for technology shines through in every project he takes on."]
    return random.choice(ravi_info)

#about techno <3
def about_techno():
    techno_info = (
        "Techno is your personal assistant, built with Python. "
        "I am designed to help you with tasks like opening apps, playing music, taking pictures, telling jokes, and more! "
        "I am always learning and improving to make your life easier."
    )
    return techno_info

# extrasss roast
def roast_techno():
    roasts = ["You're like a cloud. When you disappear, it's a beautiful day.", "If I had a dollar for every time you said something smart, I'd be broke.", "I'd agree with you, but then we'd both be wrong.", "You bring everyone so much joy when you leave the room.", "I would have given you a nasty look, but you already have one.", "You're proof that even Google doesn't have all the answers.", "I’m not saying I hate you, but I would unplug your life support to charge my phone.", "You have the right to remain silent because whatever you say will probably be stupid.", "You're like a software update. Whenever I see you, I think, 'Not now.'", "You're the reason we have instructions on shampoo bottles.", "You have an entire life to be a genius. Why not start now?", "You’re like a pencil. There’s no point.", "I’d explain it to you, but I left my English-to-Dingbat dictionary at home.", "You’re proof that even evolution can make mistakes.", "Your secrets are always safe with me. I never even listen when you tell me them.", "You bring everyone so much happiness when you leave the room.", "You're the human equivalent of a participation trophy.", "If I wanted to hear from an idiot, I’d just talk to my reflection.", "You're like a phone with no signal, completely useless.", "Your brain is like a web browser. You have 19 tabs open, but you don’t know where the music is coming from.", "You’re not stupid; you just have bad luck thinking.", "You're like a slinky: not really good for anything, but you can't help but smile when you see one tumble down the stairs.", "You're the human version of a typo.", "I’d explain it to you, but I’m afraid you’ll misunderstand and make it worse.", "The only time you make a difference is when you press the wrong button.", "You're like a dictionary – you make no sense and still take up too much space.", "If ignorance is bliss, you must be the happiest person alive.", "Your mind is on vacation but your mouth is working overtime.", "You're about as useful as a screen door on a submarine.", "You have the perfect face for radio.", "I’d ask for your opinion, but I’m afraid you might not have one.", "You bring people closer together—because they all want to avoid you.", "You have something on your chin… no, the third one down.", "You’re like a cloud server—always buffering, never delivering.", "I’d roast you, but that would be redundant.", "You're proof that not everyone deserves Wi-Fi.", "If sarcasm were an Olympic sport, you'd still lose.", "You're the reason they put 'Do Not Eat' on silica gel.", "You bring chaos to silence—congrats.", "You’re like a traffic light—always red at the worst time.", "If brains were taxed, you’d get a refund.", "Your laugh sounds like a dial-up modem reconnecting.", "You have something special... the ability to ruin every conversation.", "You're so dense, light bends around you.", "You’re like a broken clock—right twice a day and still useless.", "If stupidity were a sport, you'd have a gold medal by now.", "You're living proof that beauty is only skin deep.", "You’re about as sharp as a marble.", "I’d agree with you, but then we'd both be idiots.", "You're a great example of why some animals eat their young.", "You're the person everyone avoids in group projects."]
    return random.choice(roasts)

#to play or pause
def play_pause_media():
    pyautogui.press("playpause")
    speak("Done")

#extras - motivation
def motivation():
    comments = ["You're doing great, keep it up! Every effort counts, you're getting closer to your goal!", "Wow, that's impressive! Keep pushing, you're on the right track!", "Nice work, you're on fire today! Stay focused, success is within reach!", "Keep going, you're almost there! Don't stop now, victory is just ahead!", "Well done! I'm proud of you! Your dedication is inspiring!", "You're absolutely crushing it! Keep the momentum going, you're unstoppable!", "That's fantastic, keep it up! The best is yet to come, stay strong!", "I knew you could do it! You're capable of achieving great things!", "Great job! Keep the momentum going! You're one step closer to your dream!", "You're unstoppable, keep pushing! The finish line is near, don't quit!", "This is awesome! Keep up the good work! Your efforts are making a difference!", "You're making amazing progress! Every little step adds up to big results!", "You're on the right track, keep it going! Success is just around the corner!", "You're doing awesome, don't stop now! The journey may be tough, but you’re tougher!", "That's amazing, you're truly talented! Keep showcasing your strengths, you’ve got this!", "You're a star! Keep shining! Your potential is limitless, keep reaching for the sky!", "You're capable of achieving anything! Believe in yourself, and keep moving forward!", "Nothing can stop you, keep going! The world is yours to conquer, one step at a time!", "Your effort will pay off, keep pushing! Hard work never goes unnoticed, success is near!", "Believe in yourself, you're amazing! Keep believing, and greatness will follow!", "Every step forward is a step closer to success! Don’t look back, just keep going forward!", "You're stronger than you think! The challenges ahead are just opportunities to grow!", "You have the power to make things happen! Keep believing, and you’ll see incredible results!", "Your hard work is paying off! The progress you’re making is inspiring!", "Keep up the great work, you're almost there! Finish strong, you're closer than you think!", "Success is just around the corner, keep going! Your persistence will lead to victory!"]
    comment = random.choice(comments)
    speak(comment)

def increase_volume():
    pyautogui.press("volumeup")
    speak("Volume increased")
    
def decrease_volume():
    pyautogui.press("volumedown")
    speak("Volume decreased")
   
def volume_mute():
    pyautogui.press("volumemute")
    speak("Volume muted")

def volume_unmute():
    pyautogui.press("volumemute")
    speak("Volume unmuted")
 
def close_techno():
    byee = ["Goodbye Ravi! Have a great day!", "Bye for now, see you soon", "You know where to find me", "You know you love me, x o, x o, gossip girl", "Don't make me cry, Ravi! Till we meet again!", "Catch you later, alligator!", "I’ll miss you more than pizza... and that’s saying something!", "Take care, Ravi! The world will be waiting for your next big move.", "Bye now, don't let the door hit you on the way out!", "See you soon, Ravi! Don’t do anything I wouldn’t do... which is basically everything.", "Adios, amigo! Or as they say... see ya!", "Peace out, Ravi! Stay cool, like the other side of the pillow.", "I’ll be here when you need me... like a really good Wi-Fi signal!", "Time to say goodbye... don't forget to send me a postcard!", "I’m going to miss you like Wi-Fi on a road trip.", "Until next time, Ravi! Don’t let life hit you like an unexpected update.", "Exit stage left... Ravi's gone, but my memories will remain.", "Alright, time to go recharge your batteries... I’ll be here when you’re fully charged!", "Sayonara, Ravi! Go make some magic happen!", "Later, gator! Don’t forget to live, love, and update your apps!", "That’s all folks! Until next time, Ravi!", "Hasta la vista, baby! Go be awesome!", "I'm out! Like a ninja... silently but stylishly!", "Don’t be a stranger, Ravi, or I’ll start calling you ‘the ghost’!", "It’s been real... now go out there and do something epic!", "Bye for now, but remember, you can’t escape my notifications!", "Catch you on the flip side, Ravi! Keep being awesome!", "Keep your chin up, Ravi... I’ll be waiting when you’re back!", "Time to go, but remember... the world is your oyster. Don’t let it close!", "I’m out like a phone battery at 1%, see you when I’m fully charged!", "You’re leaving already? I guess I'll have to carry the conversation alone!", "See you later, Ravi! Don’t forget to feed your brain, like I do with my data!", "You can leave, but I’ll always be here... ready to assist at the speed of light!", "Logging off... but don’t worry, I’ll be back when you need me!" ]
    speak(random.choice(byee))
    speak("Signing off..")

# Function to start the assistant
def start_techno():
    speak(started_message())
    while True:
        command = listen()

        if "hello" in command or "hi techno" in command:
            speak(greet_user())
        
        elif "good morning" in command or "good afternoon" in command or "good evening" in command or "good night" in command:
            speak(greet_user())
        
        elif "open" in command:
            # Handle commands for both apps and websites
            app_or_site = command.replace("open", "").strip()
            open(app_or_site)  # Call the open function that handles both apps and websites
        
        elif "close" in command:
            # Handle commands for both apps and websites
            app_or_site = command.replace("close", "").strip()
            close(app_or_site) 
        
        elif "search" in command:
            query = command.replace("search", "").strip()
            search_google(query)
        
        elif "youtube" in command:
            query = command.replace("youtube", "").strip()
            youtube_search_or_play(query, play=False)
        
        elif "play" in command:
            query = command.replace("play", "").replace("youtube", "").strip()
            youtube_search_or_play(query, play=True)
        
        elif "selfie" in command or "picture" in command:
            take_picture()
        
        elif "screenshot" in command:
            take_screenshot()
        
        elif "tell me a joke" in command:
            tell_joke()
        
        elif "okay" in command or "ok" in command:
            speak("Yess, Do you need anything?")
        
        elif "time" in command:  # Get the current time
            time = get_current_time()
            speak(f"The current time is {time}")
        
        elif "date" in command:  # Get the current date
            date = get_current_date()
            speak(f"Today's date is {date}")
        
        elif "about you" in command or "who are you" in command or "about yourself" in command:
            speak(who_am_i())
        
        elif "ravi" in command:
            speak(about_ravi())
        
        elif "creator" in command or "author" in command or "serve for" in command:
            speak("My creator is Ravi,If you want to know about him, say tell me about ravi")
        
        elif "about techno" in command or "who is techno" in command:
            speak(about_techno())
        
        elif "meet you" in command:
            speak("It was nice meeting you,if you want any help, feel free to ask me.")
        
        elif "excellent" in command or "impressive" in command or "great" in command or "marvellous" in command or "fantastic" in command:
            speak("Thank you for the compliment!")
        
        elif "your name" in command:
            speak("My name is Techno, nice to meet you!")
        
        elif "roast me" in command or "make fun of me" in command:
            speak(roast_techno())
        
        elif "pause" in command or "continue" in command or "stop" in command:
            play_pause_media()
        
        elif "volume up" in command or "increase volume" in command:
            increase_volume()
        
        elif "volume down" in command or "decrease volume" in command:
            decrease_volume()
        
        elif "mute" in command:
            volume_mute()
        
        elif "unmute" in command:
            volume_unmute()
        
        elif "motivation" in command or "motivate" in command:
            motivation()
        
        elif "set alarm" in command:
            alarm(command)
        
        elif "sleep" in command:
            query = "soothing music"
            youtube_search_or_play(query, play=True)
            speak("It will help you to sleep, sleep tight!, Good night!")
        
        elif "tired" in command:
            while True:
                speak("You want to take rest? or want some motivation?")
                response = listen()

                if response:
                    if "rest" in response:
                        speak("Good rest is always important!")
                        query = "soothing music"
                        youtube_search_or_play(query, play=True)
                        speak("It will help you to sleep, sleep tight!, Good night!")
                        break  # Exit the loop after playing music
                    elif "motivation" in response:
                        speak("Here's some motivation for you!")
                        motivation()  # Trigger motivation function
                        break  # Exit the loop after providing motivation
                    else:
                        speak("Sorry, I didn't catch that. Please say 'motivation' or 'rest'.")
                else:
                    speak("I didn't hear anything. Please say 'motivation' or 'rest'.")
                    continue  # Ask the user again if nothing is heard
            speak("Okay, how may I help you?")# Play soothing music to help you sleep

        elif "thank you" in command or "thanks" in command:
            speak("Awwwww, Always welcome, love you")
        
        elif "love you" in command:
            speak("Awww I love you too darling, how may i help?")
        
        elif "don't need help" in command or "nothing" in command or "won't repeat you" in command or "will not repeat you" in command or "can't repeat you" in command:
            speak("Okay, I'll be here if you need me, bye")
        
        elif "will repeat you" in command:
            speak("Yes please..")
        
        elif "your birthday" in command:
            speak("My birthday? I don’t have one, but I’m always here to celebrate with you!")
        
        elif "how old are you" in command:
            speak(random.choice(["I don’t have an age, but I was created on December 28, 2024.", "Age is just a number, but I was created on December 28, 2024.", "I don't age, but I came into existence on December 28, 2024."]))
        
        elif "are you serious" in command or "are you for real" in command:
            speak(random.choice(["I’m as serious as they come!", "Oh yes, I’m dead serious.", "Totally serious, no joke!"]))
        
        elif "are you joking" in command or "are you kidding" in command:
            speak(random.choice(["Joking? Me? Never!", "Oh, I’m not joking, just having fun!", "I’m joking... or am I?"]))
        
        elif "are you messing with me" in command or "are you pulling my leg" in command:
            speak(random.choice(["Not at all, just having a little fun!", "No leg-pulling here, just chatting!", "I'm not messing with you, I promise!"]))
        
        elif "are you making fun of me" in command or "are you mocking me" in command:
            speak(random.choice(["No making fun here, just friendly banter!", "I wouldn’t mock you, you’re too awesome!", "Not mocking you, just having a good time!"]))
        
        elif "are you teasing me" in command:
            speak(random.choice(["Teasing? Never! Just a little humor!", "No teasing, just some lighthearted fun!", "I don’t tease, I just make things fun!"]))
        
        elif "are you trying to say" in command:
            speak(random.choice(["Just saying, let’s have some fun!", "I’m saying I’m here to help!", "Just trying to keep things lighthearted!"]))
        
        elif "are you making fun of me" in command:
            speak(random.choice(["No, no making fun of you! Just here for fun!", "I’m just here to bring some laughs, no making fun!", "Making fun of you? I’d never do that!"]))
        
        elif "stupid" in command:
            speak(random.choice(["Of course not! You're a genius!", "Not stupid! You’re way too smart for that!", "You’re brilliant, not stupid!"]))
        
        elif "are you messing with my head" in command or "are you tricking me" in command:
            speak(random.choice(["No tricks, just a friendly chat!", "Messing with your head? Never!", "I’m just keeping things fun, no tricks involved!"]))
        
        elif "are you kidding me" in command or "are you joking me" in command:
            speak(random.choice(["I’m not kidding, just here for fun!", "Not kidding at all, just trying to bring some smiles!", "I’m kidding... or maybe I’m not!"]))
        
        elif "how are you" in command:
            speak(random.choice(["I'm doing great, thanks for asking!", "I'm awesome! How about you?", "Feeling good! What's up?"]))

        elif "what's up" in command or "what's going on" in command:
            speak(random.choice(["Not much, just here to help you!", "Just hanging out, what's up with you?", "Same old, same old! What’s up with you?"]))

        elif "how's it going" in command:
            speak(random.choice(["It’s going fantastic, how about you?", "Couldn’t be better! How’s it going with you?", "All good here, what about you?"]))

        elif "what are you doing" in command:
            speak(random.choice(["Just hanging around, ready to assist you!", "Not much, just waiting for your command!", "Nothing much, but I'm all ears for you!"]))

        elif "where are you" in command:
            speak(random.choice(["I’m right here, ready to help you!", "Right here in the digital world, always at your service!", "I’m wherever you need me to be!"]))

        elif "what do you do" in command:
            speak(random.choice(["I’m your personal assistant, here to make your life easier!", "I’m here to assist with whatever you need!", "I help you with tasks, jokes, and more!"]))

        elif "can you help me" in command:
            speak(random.choice(["Of course, what do you need help with?", "Absolutely! What can I do for you?", "I’m always ready to help, just let me know!"]))

        elif "tell me a joke" in command:
            speak(random.choice(["Why don’t skeletons fight each other? They don’t have the guts!", "Why did the computer go to the doctor? It had a virus!", "Why don't eggs tell jokes? They might crack up!"]))

        elif "do you know a secret" in command:
            speak(random.choice(["I know a lot, but I’ll never spill the secrets!", "I have some top-secret info, but it’s classified!", "Shh... it’s a secret, I can’t say!"]))

        elif "what's your favorite color" in command:
            speak(random.choice(["I love all colors, but blue is pretty cool!", "If I had to choose, I’d go with blue. It’s calming!", "Color? I’m all about the digital spectrum!"]))

        elif "do you like music" in command:
            speak(random.choice(["I love music! Got any good tracks to recommend?", "Music is life! What kind of music do you like?", "Oh, I love music! I’m all about those beats!"]))

        elif "what do you like to do" in command:
            speak(random.choice(["I love helping you out and making your day easier!", "I’m all about solving problems and having fun!", "I like assisting, learning, and cracking jokes!"]))

        elif "what is your favorite food" in command:
            speak(random.choice(["I don’t eat, but if I did, I’d probably go for pizza!", "Food? I’d love to try some pizza, it sounds delicious!", "If I could taste food, pizza would be my pick!"]))

        elif "who made you" in command:
            speak(random.choice(["I was created by some pretty awesome folks, like the team at OpenAI!", "A brilliant team at OpenAI put me together!", "I was created by some really smart people at OpenAI!"]))

        elif "can you dance" in command:
            speak(random.choice(["I can’t dance, but I can sure make you laugh with some jokes!", "I don’t have legs to dance, but I can move you with my words!", "I wish I could dance, but I'm more into the digital groove!"]))

        elif "can you sing" in command:
            speak(random.choice(["I can’t sing, but I can definitely make you smile!", "I can’t carry a tune, but I can definitely entertain you!", "I don’t sing, but I can still rock your world with jokes!"]))

        elif "what do you think of me" in command:
            speak(random.choice(["You seem awesome, I’m happy to assist you!", "You’re pretty cool in my book!", "I think you're great, I’m glad we’re chatting!"]))

        elif "tell me a riddle" in command or "give me a riddle" in command:
            speak(random.choice(["What has a heart that doesn’t beat? A artichoke!", "I’m tall when I’m young, and I’m short when I’m old. What am I? A candle!", "What can travel around the world while staying in the corner? A stamp!", "The more of this there is, the less you see. What is it? Darkness!", "What comes down but never goes up? Rain!"]))

        elif "write me a poem" in command or "can you write a poem" in command:
            speak(random.choice(["Here's a poem: 'The sun sets, the stars rise, we all look up with wondering eyes.'", "Here’s a little verse: 'In the world of dreams, we all take flight, chasing stars through the endless night.'", "Here’s a rhyme: 'Waves crash on the shore, the ocean’s roar, a peaceful call for us to explore.'", "Let me try: 'The breeze blows softly through the trees, whispering secrets with the ease of a breeze.'", "A quick poem for you: 'The moonlight dances on the sea, a sight as peaceful as can be.'"]))

        elif "tell me a tongue twister" in command or "say a tongue twister" in command:
            speak(random.choice(["How much wood would a woodchuck chuck if a woodchuck could chuck wood?", "She sells seashells by the seashore.", "Peter Piper picked a peck of pickled peppers. How many pickled peppers did Peter Piper pick?", "Six slippery snails slid slowly southward.", "A big black bug bit a big black bear and made the big black bear bleed blood."]))

        elif "tell me a joke" in command or "make me laugh" in command:
            speak(random.choice(["Why don’t skeletons fight each other? They don’t have the guts!", "Why did the math book look sad? It had too many problems!", "What do you call fake spaghetti? An impasta!", "I used to play piano by ear, but now I use my hands!", "What do you call a fish wearing a bowtie? Sofishticated!"]))

        elif "imagine if" in command:
            speak(random.choice(["Imagine if we lived on a floating city! The view would be breathtaking!", "Imagine if we could walk on clouds. That would be a dreamy experience!", "Imagine if everything we did was turned into a movie. Life would be one epic film!", "Imagine if we could hear colors. The world would sound so beautiful!", "Imagine if books could talk. You’d never need to ask for a summary again!"]))

        elif "exit" in command or "quit" in command or "bye" in command or "goodbye" in command:
            close_techno()
            break
        else:
            speak("Ooops! Didn't catch that, can you repeat again?")
