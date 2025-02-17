import edge_tts
import asyncio
from pydub import AudioSegment
from pydub.playback import play
import colorama
from colorama import Fore

# Initialize colorama
colorama.init(autoreset=True)

async def _SpeakAsync(text):
    voice = "en-GB-SoniaNeural"
    output_file = "speech.mp3"

    # Print the text in cyan color
    print(Fore.CYAN + text)
    print()

    # Generate speech file
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)

    # Play the MP3 file with high quality
    audio = AudioSegment.from_file(output_file, format="mp3")
    play(audio)  # Smooth, high-quality playback

def Speak(*args):
    # Combine all arguments into a single string
    text = " ".join(args)
    
    # Run the asynchronous function
    asyncio.run(_SpeakAsync(text))
