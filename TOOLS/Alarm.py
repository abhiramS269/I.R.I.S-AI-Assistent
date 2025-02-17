import time
import pygame
from threading import Thread

def set_set_alarm(alarm_time, sound_file):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time >= alarm_time:
            print("Time's up!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            break
        time.sleep(1)  # Check the time every second

def set_alarm(alarm_time,sound_file="AUDIO/alarm.wav"):
    print("ALARM STARTED")
    Thread(target=set_set_alarm,args=(alarm_time, sound_file)).start()


