#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Description:
    A Python script that downloads an image from a provided URL and extracts all available
    EXIF metadata. The script supports images containing EXIF metadata.
    Results are displayed as key-value pairs of all EXIF data found in the image.

Maintainer:
            ::::  ::::::::::::  
            :+:     :+:    :+: 
            +:+     +:+    +:+ 
            +#+     +#+    +:+ 
            +#+     +#+    +#+ 
        #+# #+#     #+#    #+# 
         #####    ############     

Date:
    Oct 05, 2023

Usage:
    python3 extract_exif_info.py [image_url]

Arguments:
    image_url - The URL of the image from which to extract EXIF metadata.

Dependencies:
    - Pillow library for handling images and EXIF data
    - requests library for downloading images

Notes:
    The script relies on the presence of EXIF metadata in the image. If the image at the specified URL
    does not contain EXIF data, the script will report this.
"""

# ascii art welcome
print("""
                           /$$                /$$$$$$                               
                          | $$               /$$__  $$                              
 /$$$$$$/$$$$   /$$$$$$  /$$$$$$    /$$$$$$ | $$  \__/ /$$$$$$$   /$$$$$$   /$$$$$$ 
| $$_  $$_  $$ /$$__  $$|_  $$_/   |____  $$|  $$$$$$ | $$__  $$ |____  $$ /$$__  $$
| $$ \ $$ \ $$| $$$$$$$$  | $$      /$$$$$$$ \____  $$| $$  \ $$  /$$$$$$$| $$  \ $$
| $$ | $$ | $$| $$_____/  | $$ /$$ /$$__  $$ /$$  \ $$| $$  | $$ /$$__  $$| $$  | $$
| $$ | $$ | $$|  $$$$$$$  |  $$$$/|  $$$$$$$|  $$$$$$/| $$  | $$|  $$$$$$$| $$$$$$$/
|__/ |__/ |__/ \_______/   \___/   \_______/ \______/ |__/  |__/ \_______/| $$____/ 
                                                                          | $$      
                                                                          | $$      
                                                                          |__/     
""")

import requests
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from io import BytesIO
import sys

def download_image(url):
    """Downloads an image from a URL and returns an Image object."""
    print("[-] Downloading image...")
    response = requests.get(url)
    if response.status_code == 200:
        print("[-] Image downloaded successfully.")
        return Image.open(BytesIO(response.content))
    else:
        print("Failed to download the image.")
        return None

def get_exif_data(image):
    """Extracts EXIF data from a PIL Image object."""
    print("[-] Extracting EXIF data...")
    exif_data = {}
    if hasattr(image, '_getexif'):
        exif_info = image._getexif()
        if exif_info is not None:
            for tag, value in exif_info.items():
                decoded = TAGS.get(tag, tag)
                exif_data[decoded] = value
        else:
            print("[-] Image does not support EXIF data.")
    return exif_data

def display_exif_data(exif_data):
    """Displays all EXIF metadata."""
    print("[-] Displaying EXIF metadata...")
    if exif_data:
        print("[-] EXIF Metadata:")
        for key, value in exif_data.items():
            print(f"{key}: {value}")
    else:
        print("[-] No EXIF metadata to display.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 extract_exif_info.py [image_url]")
        sys.exit(1)

    image_url = sys.argv[1]
    image = download_image(image_url)

    if image:
        exif_data = get_exif_data(image)
        display_exif_data(exif_data)
    else:
        print("[-] Failed to download the image or invalid image URL.")