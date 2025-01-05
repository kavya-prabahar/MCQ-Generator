import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

def generate_mcq(text,api):
    
    url= f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
  "contents": [{
    "parts":[{"text": f"Generate 10 multiple-choice questions on: {text}"}]
    }]
   }
    
    response = requests.post(url, json = payload, headers = headers)


    if response.status_code == 200:
        data = response.json()

        content = data.get('candidates', [{}])[0].get('content', {})
        text_content = content.get('parts', [{}])[0].get('text', '')

        return text_content
    else:
        return f"Error: {response.status_code} - {response.text}"

    
    