import os
import sys
from dotenv import load_dotenv
import openai
from openai import OpenAI

# access openai key from .env in root folder
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))
openai_key = os.getenv('OPENAI_SECRET')

client = OpenAI(
    api_key=openai_key #,...
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message.content)