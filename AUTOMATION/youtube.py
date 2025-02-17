from youtube_transcript_api import YouTubeTranscriptApi
from keyboard import press,press_and_release
import pyperclip
from time import sleep
# Get the clipboard data


def GetTranscript():
    clipboard_data=""
    for i in range(5):
        press("f6")
        sleep(1)
        press_and_release("ctrl + c")
        sleep(1)
        clipboard_data = pyperclip.paste()
        if  "https://www.youtube.com/watch?" in  clipboard_data:
            break
        else:
            sleep(1)
    
    url= clipboard_data.removeprefix("https://www.youtube.com/watch?v=").split("&")[0]
    try:
        new=""
        for i in YouTubeTranscriptApi.get_transcript(url,languages=("en","hi")):
            new+=i["text"]
        #print(new)
        return new
    except:
        return None
