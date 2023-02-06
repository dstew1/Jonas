from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

# Speech engine initialisation
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # 0 = male, 1 = female
activationword = 'Jonas' 

def speak(text, rate = 120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()
    

def parsecommand():
    listener = sr.Recognizer()
    print('Listening for you')
    
    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)
        
    try:
        print('Computing Voice...')
        query = listener.recognize_google(input_speech, language='en_US')
        print('You said: {query}')
    except Exception as exception:
        print('I did not catch that')
        speak('I did not catch that')
        print(exception)
        return 'none'
    
    return query

# Main loop
if __name__ == '__main__':
    speak('Hello Daniel')
    
    while True:
        # Parse Command
        query = parsecommand().lower().split()
        
        if query[0] == activationword:
            query.pop(0)
            
            #list commands
            if query[0] == 'say':
                if 'hello' in query:
                    speak('Good morning, afternoon, evening or night')
                else:
                    query.pop(0) #Remove say
                    speech = ' '.join(query)
                    speak(speech)