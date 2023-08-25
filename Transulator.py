
print("Please check your internet Support if it is in on ")
while 1:
    e=input("Enter ""OK or DONE"":")

    if(e==('ok' or 'done' or 'OK' or 'DONE' or 'Ok' or 'Done' or 'done')):
        import gtts  
        from playsound import playsound
        t1 = gtts.gTTS("Welcome to my Transulator")
        t1.save("welcome.mp3")
        playsound("welcome.mp3")
        import googletrans

       # print(googletrans.LANGUAGES)
        from googletrans import Translator
        
        while True:
            import os
            translator = Translator()
            a=input("Enter the input language:")
            b=input("Enter the required language:")
            c=input("Enter the Text:")
            result = translator.translate(c, src=a, dest=b)

            print(result.src)
            print(result.dest)
            print(result.text)
            d=(result.text)
            
            import gtts  
            from playsound import playsound
            t1 =gtts.gTTS(d)
        
            t1.save("welcome1.mp3")
            playsound("welcome1.mp3")
            os.remove("welcome1.mp3")

    else:
        print("Connect to internet")

