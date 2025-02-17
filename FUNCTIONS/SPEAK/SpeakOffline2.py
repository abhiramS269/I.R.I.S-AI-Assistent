import os
import pygame
import re

def remove_special_chars(text):
    # Define the regex pattern to remove special characters
    pattern = r'[^a-zA-Z0-9.@&\'"\s.]'
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text



def Speak(data:str):
    data=remove_special_chars(data)
    
    #pygame.init()
    command = f'edge-tts --voice "en-CA-LiamNeural" --pitch=+5Hz --rate=+22% -t "{data}" --write-media "temp/data.mp3"'
    while 1:
        try:
            os.system(command)
            pygame.mixer.init()
            pygame.mixer.music.load(r"temp/data.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            return
        except Exception as e:
            print(e)
        finally:
            pygame.mixer.music.stop()
            pygame.mixer.quit()

if __name__=="__main__":
    Speak(remove_special_chars ("unrecognized arguments: send me the news headlines and I'll handle the rest."))