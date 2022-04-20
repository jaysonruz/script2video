# Import API class from pexels_api package
from pexels_api import API

import requests
import shutil
import os

from dotenv import load_dotenv
from requests import patch
load_dotenv()

PEXELS_API_KEY = os.environ.get("PEXELAPIKEY")# API Key

def pexelsearch(keyword,IMAGES_DIR):
    # Create API object
    api = API(PEXELS_API_KEY)
    # Search five 'kitten' photos
    api.search(keyword, page=1, results_per_page=30)
    # Get photo entries
    photos = api.get_entries()
    if len(photos)<1:
        print("IMAGES NOT FOUND FOR GIVEN KEYWORD!!!")
    else:
        # Loop the five photos
        for photo in photos:
            # if photo.width > photo.height: #landscape photo
            print(photo.height/photo.width)
            print(16/9)
            print("\n")
            if photo.width/photo.height > 1.4: #16/9: #aspect ratio
            # Print photographer
                print('\n\nPhotographer: ', photo.photographer)
            # Print url
                print('Photo url: ', photo.url)
            # Print original size url
                print('Photo original size: ', photo.original)

                print(f"size is {photo.width}X{photo.height}")

                r = requests.get(photo.original,stream=True, headers={'User-agent': 'Mozilla/5.0'})
                if r.status_code == 200:
                    with open(str(IMAGES_DIR/str(keyword+".png")), 'wb') as f:
                        r.raw.decode_content = True
                        shutil.copyfileobj(r.raw, f)
                break

if __name__ == "__main__":
    from pathlib import Path
    BASE_DIR=Path.cwd()
    IMAGES_DIR = BASE_DIR/"images"
    pexelsearch("dogo",IMAGES_DIR)