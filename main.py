import base64
import requests
import sys
import os  # Import os module to work with file paths
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')


# Check if the user provided an argument (the image path)
if len(sys.argv) < 2:
    print("Usage: python script.py <image_path>")
    sys.exit(1)  # Exit if no argument is provided

# The first command line argument is the script name, so the second one is your first actual input
image_path = sys.argv[1]  # Use the first argument as the image path

# Function to get the MIME type based on the file extension
def get_mime_type(file_path):
    _, file_ext = os.path.splitext(file_path)
    # Convert extension to lowercase to handle case variations
    file_ext = file_ext.lower()
    if file_ext in [".jpg", ".jpeg"]:
        return "jpeg"
    elif file_ext == ".png":
        return "png"
    elif file_ext == ".gif":
        return "gif"
    else:
        return "octet-stream"  # Default MIME type if unknown

# Function to encode the image
def encode_image(image_path):
    mime_type = get_mime_type(image_path)  # Get the MIME type
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8'), mime_type

# Getting the base64 string and MIME type
base64_image, mime_type = encode_image(image_path)


headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What’s in this image? Describe it in portuguese. if there's text, please transcribe it as is."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/{mime_type};base64,{base64_image}"
                    }
                }
            ]
        }
    ],
    "max_tokens": 300
}

# Since we can't make external requests, this is where the example ends
# You would normally use requests.post here as you had in your original script
response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

# print(response.json())

print(response.json()["choices"][0]["message"]["content"])