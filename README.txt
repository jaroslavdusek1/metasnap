EXIF Metadata Extractor

Description:
This Python script downloads images from a specified URL and extracts available EXIF metadata. The script is designed to support images that contain EXIF metadata, displaying the results as key-value pairs.

Usage:
Execute the script with an image URL as an argument.
Example: python3.10 extract_exif_info.py https://raw.githubusercontent.com/ianare/exif-samples/master/jpg/Canon_40D.jpg

Dependencies:

Pillow: A Python Imaging Library, used for handling images and EXIF data extraction.
requests: Used for downloading images from URLs.
Features:

Downloads images from URLs.
Extracts and displays EXIF metadata from images.
Supports various image formats that contain EXIF data.
External Resources:
The script utilizes sample images from the 'ianare/exif-samples' repository on GitHub for testing and demonstration purposes.

Maintainer:
jd

Date:
October 5, 2023

Notes:
The script's effectiveness depends on the presence of EXIF metadata in the target image. It's designed to inform the user when no EXIF data is found or if the image format does not support EXIF metadata.
