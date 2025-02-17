from FUNCTIONS.SPEAK.SpeakOnline2 import Speak
from FUNCTIONS.LISTERN.ListenJs import Listen
from FUNCTIONS.ONLINE_DATA.ExecCode import ExecCode
from LLM.Filter import Filter
from LLM.Gemini import Gemini
from LLM.ChatGpt import ChatGpt
from DEFAULT import GoodMsg, KnowApps
from AUTOMATION.youtube import GetTranscript
from POWERPOINT.app import get_bot_response
from TOOLS.ImagesGenration import *
from CUSTOM.Missing import Missing
from CUSTOM.WebsiteInfo import WebsiteInfo
import pyperclip as pi
import random
import pygetwindow as gw
import keyboard
import time
from os import startfile, getcwd
from AUTHENTICATION.FaceAuth import FaceAuth

"""Speak("Face ID required.")
ID = FaceAuth()

if ID is None:  # If no face match is found
    Speak("Face authentication failed. Access denied.")
    exit()  # Terminate the program if the face is not recognized

Speak(f"Login successful with Face ID of {ID}")
"""
if __name__ == "__main__":
    while True:
        Q = Listen()
        QL = Q.lower()
        LQ=len(Q.split(" "))
        SQ=Q.split(" ")[0]
        EQ=Q.split(" ")[-1]
        NQ = Q.lower().removeprefix("IRIS ")
        CURRENT_APP = ""

        try:
            CURRENT_APP = gw.getActiveWindowTitle()
        except:
            CURRENT_APP = ""

        CURRENT_APP_NAME = CURRENT_APP.split(" - ")[-1]

        if NQ in ["optimize this code", "write code for this", "optimise this code"]:
            keyboard.press_and_release("ctrl + c")
            time.sleep(1)
            clipboard_data = pi.paste()
            response = Gemini(f"{clipboard_data} **{NQ}**")
            response = Filter(response)
            if response:
                pi.copy(response)
                keyboard.press_and_release("ctrl + v")
                Speak(random.choice(GoodMsg))
            else:
                Speak("I can't do that, sir.")

        elif "powerpoint" in QL and NQ.startswith("create"):
            path = get_bot_response(Q)
            startfile(f"{getcwd()}\\{path}")
            Speak("Done, sir.")
            Speak(random.choice(GoodMsg))

        elif QL.find("read my selection")==0 or QL.find("read my selected text")==0:
            Speak("Sure sir reading your selected data")
            keyboard.press_and_release("ctrl + c")
            time.sleep(1)
            jo = pi.paste()
            print(jo)
            Speak("data copied")

        elif NQ in ["read this website", "scan this website"]:
            Speak("Scanning this website, sir.")
            keyboard.press("f6")
            time.sleep(1)
            keyboard.press_and_release("ctrl + c")
            time.sleep(1)
            url = pi.paste()
            if "http" in url:
                Gemini(WebsiteInfo(url))
                Speak("Website scanned. Ask me anything about it.")
                
                
        elif "open command prompt" in QL:
            Speak("Opening command prompt")
            os.system('start cmd')

        elif "close command prompt" in QL:
            Speak("Closing command prompt")
            os.system("taskkill /f /im cmd.exe")

        elif "open camera" in QL:
            Speak("Opening camera, sir.")
            sp.run('start microsoft.windows.camera:', shell=True)
        
        elif "close camera" in QL:
            Speak("Closing camera, sir.")
            os.system("taskkill /f /im WindowsCamera.exe")
            
        elif "open notepad" in QL:
            Speak("Opening Notepad for you, sir.")
            notepad_path = "C:\\Windows\\system32\\notepad.exe"
            startfile(notepad_path)
            
        elif "close notepad" in QL:
            Speak("Closing Notepad for you, sir.")
            os.system("taskkill /f /im notepad.exe")
            
        elif "open discord" in QL:
            Speak("Opening Discord for you, sir.")
            discord_path = "C:\\Users\\ASUS\\AppData\\Local\\Discord\\app-1.0.9028\\Discord.exe"
            startfile(discord_path)
            
        elif "close discord" in QL:
            Speak("Closing Discord for you, sir.")
            os.system("taskkill /f /im Discord.exe")

        elif "ip address" in QL:
            ip_address = ExecCode("find_my_ip")
            Speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')                
                
        

        elif any(action in NQ for action in ["summarize", "transcribe", "translate"]) and "video" in NQ:
            transcript = GetTranscript()
            if transcript:
                response = Gemini(f"{transcript} **{NQ.replace('video', 'text')}**")
                Speak(response)
            else:
                Speak("I can't do that, sir.")
                
        elif "iris" == SQ.lower():
            responce = Gemini(f"{Q} ***use python programing language. just write complete code nothing else, also don't dare to use input function*** **you can use the module that i provided if required**")
            code = Filter(responce)
            print(code)
            if code is not None:
                if ("from TOOLS.ImagesGenration import " in code or 
                    "import" not in code or "from TOOLS.Alarm import set_alarm"in code):
                    exec(code)
                else:
                    Done = ExecCode(code)
                    print(Done)
                    if Done:
                        Speak(random.choice(GoodMsg))
                    else:
                        for i in range(3):
                            with open(r"error.log", "r") as f:
                                res = f.read()
                                if res != "":
                                    Gemini(f"{res} /n" + "**fix this and write full code again. with different approach**")
                                    code = Filter(code)
                                    if code is None:
                                        break
                                    Done = ExecCode(code)
                                    if Done:
                                        break
                                    else:
                                        break
                                    Speak("Sorry sir, I can't do that.")
                                else:
                                    Speak(responce)


        elif CURRENT_APP_NAME in KnowApps:
            func = KnowApps[CURRENT_APP_NAME]
            output = func(QL)
            if output:
                keyboard.press_and_release(output)
            else:
                reply = Gemini(f"{Q} ***reply concisely, no code.***")
                Speak(reply)
        
        else:
            reply = Missing([Q, f"{Q} ***reply concisely, no code.***"], [Gemini]).Start()
            Speak(reply)
