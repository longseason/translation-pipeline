from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def load_client():
    client = OpenAI(
        api_key= os.getenv("GEMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    return client

# test function
if __name__ == "__main__":
    client = load_client()

    response = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[
        {   "role": "assistant",
            "content": "You are a helpful translator that translates into english."
        },
        {
            "role": "user",
            "content": "私の体重（おもみ）を、あなたの重荷（おもに）にしないで。"
        }
    ]
)
    print(response.choices[0].message.content)
