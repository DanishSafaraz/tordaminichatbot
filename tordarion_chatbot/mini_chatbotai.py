import openai
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

api_claude = os.getenv("API_KEY_CLAUDE")
api_chatgpt = os.getenv("API_KEY_CHATGPT")

memanggilclaude = anthropic.Anthropic(api_key=api_claude)
memanggilchatgpt = openai.OpenAI(api_key=api_chatgpt)

message = []

print("========Torda AI========")
name = str(input("Masukkan nama user:"))
print(f'Halo {name}, selamat datang di mini chatbot Torda AI by RAN Group.')
print('''Model AI:
1. Claude
2. ChatGPT''')

user = int(input("Pilih Model (1/2):"))

if user == 1:
    while True:
        chat = input(f'{name}:').lower()

        if chat == "q":
            break

        message.append({"role": "user", "content": chat})

        respon = memanggilclaude.messages.create(model = "claude-sonnet-5", max_tokens = 1024, messages = message)

        jawaban = ""

        for block in respon.content:
             if block.type == "text":
                  jawaban += block.text 

        message.append({"role": "assistant", "content": jawaban})

        print("AI:", jawaban)

elif user == 2:
    while True:
            chat = input(f'{name}:').lower()
    
            if chat == "q":
                break
    
            message.append({"role": "user", "content": chat})
    
            respon = memanggilchatgpt.responses.create(model = "gpt-5.6-luna", input = message, store = False)
    
            print("AI:", respon.output_text)