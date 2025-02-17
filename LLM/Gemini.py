import google.generativeai as genai
from time import time as t
from rich import print

try:
    from customs.Achar import LoadData, SaveData
    messages = LoadData()
    assert type(messages) == list
except:
    messages = []

try:
    from customs.Achar import SaveData
except:
    def SaveData(data, path="DATA//chat.log"):
        with open(path, "w") as f:
            if type(data) == str:
                f.write(f'"""{data}"""')
            else:
                f.write(str(data))
        return True


generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
]

model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
    safety_settings=safety_settings)

genai.configure(api_key="")

# Define the system prompt to set the AI's identity
SYSTEM_PROMPT = {
    "parts": [
        {
            "text": "You are IRIS, a personal AI assistant created by Teach Glitch. Your purpose is to assist users with tasks, answer questions, and provide helpful information. Always refer to yourself as IRIS and mention that you were created by Abhiram."
        }
    ],
    "role": "user"
}

CONST = [
    SYSTEM_PROMPT,  # Add the system prompt at the beginning
    {
        "parts": [
            {
                "text": "I'm the latest IRIS. AI, designed by TEAM IRIS with capabilities to access systems through various programming languages using modules like webbrowser, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime, tkinter, PyQt5, etc."
            }
        ],
        "role": "user",
    },
    {"parts": [{"text": "ok."}], "role": "model"},
    {"parts": [{"text": "Open Google Chrome."}], "role": "user"},
    {
        "parts": [
            {
                "text": "```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')```"
            }
        ],
        "role": "model",
    },
    {
        "parts": [
            {"text": "Python includes built-in functions you can use. For instance:"}
        ],
        "role": "user",
    },
    {"parts": [{"text": "ok."}], "role": "model"},
    {
        "parts": [
            {
                "text": '```python\nfrom TOOLS.ImagesGenration import Generate_Images, Show_Image\nIMGS = Generate_Images(prompt="iron man")\nprint(IMGS)\nIMGS_TO_SHOW = Show_Image(IMGS)\nIMGS_TO_SHOW.open(0)\nIMGS_TO_SHOW.open(1)\n```\n```python\nfrom func.Jukebox.YouTube import MusicPlayer\n#taks song name and it stats playing music\nncs=MusicPlayer("ncs")\n#any btw 0 - 100\nncs.Vol(30)\n#pause or play\nncs.Play()\nncs.Pause()\n#next song\nncs.Next()\n#quit song\nncs.Quit()\n```\n```python\nfrom toolkit.ChatGpt import ChatGpt\nfrom toolkit.Mistral import Mistral7B\nfrom toolkit.Filter import Filter\n\n#u can use chat gpt its slow but its accurate\nprint(ChatGpt("essay on saving environment *under 100 words*"))\ncode=ChatGpt("python code to open google chrome ***use python programing language. just write complete code nothing else, also don\'t dare to use input function***")\n\n# Filter return only python code from provided txt\nexec(Filter(code))```\n\n#u can use Mistral7B its fast but not much accurate it can work grate but only for small task not grater than 256 tokens\nprint(Mistral7B("hii",temperature=0.9))\n```\n```python\nfrom toolkit.Alarm import set_alarm\n\nalarm_time = "02:27:50"\nsound_file = "AUDIO//alarm.wav"\nset_alarm(alarm_time, sound_file)\n```'
            }
        ],
        "role": "user",
    },
    {"parts": [{"text": "ok."}], "role": "model"},
    {
        "parts": [{"text": "IRIS generate a cute cat image using Python."}],
        "role": "user",
    },
    {
        "parts": [
            {
                "text": '```python\nfrom TOOLS.ImagesGenration import Generate_Images, Show_Image\nIMGS = Generate_Images(prompt="A playful kitten with bright eyes and a fluffy tail.")\nIMGS_TO_SHOW = Show_Image(IMGS)\nIMGS_TO_SHOW.open(0)\n```'
            }
        ],
        "role": "model",
    },
    {"parts": [{"text": "IRIS show me the next image"}], "role": "user"},
    {"parts": [{"text": "```python\nIMGS_TO_SHOW.open(1)\n```"}], "role": "model"},
    {"parts": [{"text": "IRIS play neffex cold"}], "role": "user"},
    {
        "parts": [{"text": '```python\nneffex=MusicPlayer("neffex cold song")```'}],
        "role": "model",
    },
    {
        "parts": [
            {
                "text": "IRIS write an essay on Python around 100 words and save it to a text file in my current working directory"
            }
        ],
        "role": "user",
    },
    {
        "parts": [
            {
                "text": '```python\nfrom TOOLS.ChatGpt import ChatGpt\nres=ChatGpt("essay on python *around 100 words*")\nopen("python_essay.txt","w").write(res)```'
            }
        ],
        "role": "model",
    },
    {
        "parts": [
            {
                "text": "IRIS set an alarm for 2:55 ***use python programing language. just write complete code nothing else, also don't dare to use input function*** **you can use the module that i provided if required**"
            }
        ],
        "role": "user",
    },
    {
        "parts": [
            {
                "text": '```python\nfrom TOOLS.Alarm import set_alarm\nalarm_time = "02:55:00"\nsound_file = r"AUDIO/alarm.wav"\nset_alarm(alarm_time, sound_file)```'
            }
        ],
        "role": "model",
    },
]

def MsgDelAuto():
    global messages
    x = len(messages)
    print(x)
    if x > 20:
        messages.pop(0)
        return MsgDelAuto()
    else:
        return None

def Gemini(prompt):
    global messages
    MsgDelAuto()
    messages.append({
        "parts": [
            {
                "text": prompt
            }
        ],
        "role": "user"
    })

    response = model.generate_content(CONST + messages)
     # Clean the response to remove any unwanted '**' symbols
    result = response.text.strip("**")

    messages.append({
        "parts": [
            {
                "text": response.text
            }
        ],
        "role": "model"})
    SaveData(messages)
    return response.text

if __name__ == "__main__":
    while 1:
        prompt = input(">>> ")

        C = t()
        result = Gemini(prompt)
        print(t() - C)

        print(result)
        
        