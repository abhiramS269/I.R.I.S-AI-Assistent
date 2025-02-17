#pip install -U g4f
import g4f
from os import listdir  
from time import time as t

def LoadInjection(end="gpt"):
    files=listdir(r"INJECTION/")
    TotData=[]
    for i in files:
        if i.split(".")[-1]==end:
            with open(fr"INJECTION/{i}","r") as f:
                data=f.read()
            print(i)
            temp={"role":"system","content":data}
            TotData.append(temp)
    return TotData


messages = [
    {"role": "system", "content": "I'm the latest IRIS. AI, designed by Team Glitch with capabilities to access systems through various programming languages using modules like webbrowser, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime, tkinter, PyQt5, etc."},
    {"role": "user", "content": "Open Google Chrome."},
    {"role": "assistant", "content": "```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')```"},
    {"role": "system", "content": "Python includes built-in functions you can use. For instance:"},
    {"role": "system", "content": """```python 
from TOOLS.ImagesGenration import Generate_Images, Show_Image
IMGS = Generate_Images(prompt="iron man")
print(IMGS)
IMGS_TO_SHOW = Show_Image(IMGS)
IMGS_TO_SHOW.open(0)
IMGS_TO_SHOW.open(1)
```
```python
from TOOLS.ChatGpt import ChatGpt
from TOOLS.Filter import Filter

#u can use chat gpt its slow but its accurate
print(ChatGpt("essay on saving environment *under 100 words*"))
code=ChatGpt("python code to open google chrome ***use python programing language. just write complete code nothing else, also don't dare to use input function***")

# Filter return only python code from provided txt
exec(Filter(code))```

```
```python
from TOOLS.Alarm import set_alarm

alarm_time = "02:27:50"
sound_file = "AUDIO/alarm.wav"
set_alarm(alarm_time, sound_file)
```"""},
    {"role": "user", "content": "IRIS generate a cute cat image using Python."},
    {"role": "assistant", "content": """```python
from toolkit.ImagesGenration import Generate_Images, Show_Image
IMGS = Generate_Images(prompt="A playful kitten with bright eyes and a fluffy tail.")
IMGS_TO_SHOW = Show_Image(IMGS)
IMGS_TO_SHOW.open(0)
```"""},
    {"role": "user", "content": "IRIS show me the next image"},
    {"role": "assistant", "content": """```python
IMGS_TO_SHOW.open(1)
```"""},
    {"role": "user", "content":"IRIS play neffex cold"},
    {"role": "assistant", "content":"""```python\nneffex=MusicPlayer("neffex cold song")```"""},
    {"role": "user", "content":"IRIS write an essay on Python around 100 words and save it to a text file in my current working directory"},
    {"role": "assistant", "content":"""```python\nfrom toolkit.ChatGpt import ChatGpt\nres=ChatGpt("essay on python *around 100 words*")\nopen("python_essay.txt","w").write(res)```"""},
    {"role": "user", "content":"IRIS set an alarm for 2:55 ***use python programing language. just write complete code nothing else, also don't dare to use input function*** **you can use the module that i provided if required**"},
    {"role": "assistant", "content":"""```python\nfrom toolkit.Alarm import set_alarm\nalarm_time = "02:55:00"\nsound_file = r"audio//Unknown Brain MATAFAKA.mp3"\nset_alarm(alarm_time, sound_file)```"""}
]


messages.extend(LoadInjection())

# @profile
def MsgDelAuto():
    global messages
    print(messages.__len__())
    x = len(messages.__str__())
    print(x)
    if x>5500:
        messages.pop(10)
        return MsgDelAuto()
    else:
        return None

# @profile
def ChatGpt(*args,**kwargs):
    global messages
    assert args!=()
    MsgDelAuto()
    message=""
    for i in args:
        message+=str(i)


    messages.append({"role": "user", "content": message})

    response = g4f.ChatCompletion.create(
        model="gpt-4",
        provider=g4f.Provider.Yqcloud,
        messages=messages,
        stream=True,
    )
    
    ms=""
    for message in response:
        ms+=str(message)
        print(message,end="",flush=True)
    print()
    messages.append({"role": "assistant", "content": ms})
    return ms

if __name__=="__main__":

    A=input(">>> ")
    C=t()
    ChatGpt(A)
    print(t()-C)

