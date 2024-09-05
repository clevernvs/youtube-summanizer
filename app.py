from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# Lê a transcrição no arquivo
with open("transcript.txt", "r") as file:
    transcript = file.read()

# Chama o endpoint com o modelo ChatGPT
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "user",
        "content": f"Summarize the following video transcript.: \n{transcript}"
    }]
)


print(response.choices[0].message.content)
