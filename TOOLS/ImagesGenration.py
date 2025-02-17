import asyncio
import requests
import os
from random import randint
from PIL import Image
from io import BytesIO
import time

API_URL = "https://api.stability.ai/v2beta/stable-image/generate/sd3"
headers = {"Authorization": f"Bearer {open('KEYS//huggingface2').read().strip()}"}

# Ensure the output directory exists
if not os.path.exists("output"):
    os.makedirs("output")

async def query(payload):
    """ Sends a request to the API and returns the image bytes. """
    response = await asyncio.to_thread(requests.post, API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        if 'image' in response.headers.get('Content-Type', ''):
            return response.content
        else:
            print("Response is not an image.")
            return None
    elif response.status_code == 429:
        print("Rate limit reached. Retrying in 60 seconds...")
        time.sleep(60)  # Wait for 60 seconds
        return await query(payload)  # Retry the request
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

async def generate_images(prompt: str):
    """ Generates 4 images asynchronously and saves them. """
    tasks = []
    for _ in range(4):
        payload = {
            "inputs": f"{prompt} seed={randint(0, 100000)}",
        }
        task = asyncio.create_task(query(payload))
        tasks.append(task)

    image_bytes_list = await asyncio.gather(*tasks)

    filenames = []
    for i, image_bytes in enumerate(image_bytes_list):
        if image_bytes:  # Only save valid images
            filename = f"output/image_{i + 1}.jpg"
            with open(filename, "wb") as f:
                f.write(image_bytes)
            filenames.append(filename)
        else:
            print(f"Skipping corrupted image {i + 1}")

    return filenames

def Generate_Images(prompt: str):
    """ Runs the image generation synchronously and returns the last 4 valid image filenames. """
    return asyncio.run(generate_images(prompt))

class Show_Image:
    """ Class to display images from the output directory. """
    def _init_(self, li: list) -> None:
        self.listd = li

    def open(self, no):
        """ Opens the image by index number. """
        if no >= len(self.listd):
            print("No more valid images to show.")
            return

        try:
            img = Image.open(self.listd[no])
            img.show()
        except Exception as e:
            print(f"Error opening image {self.listd[no]}: {e}")
            self.open(no + 1)  # Try the next image

    def close(self, no):
        """ Placeholder for closing the image. """
        pass  # TODO: Implement closing logic if needed

if __name__ == "__main__":
    images = Generate_Images("iron man")
    print("Generated images:", images)

   