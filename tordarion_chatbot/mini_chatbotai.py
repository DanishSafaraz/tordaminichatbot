import openai
import anthropic
import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_claude = os.getenv("API_KEY_CLAUDE")
api_chatgpt = os.getenv("API_KEY_CHATGPT")
api_deepseek = os.getenv("API_KEY_DEEPSEK")

memanggilclaude = anthropic.Anthropic(api_key=api_claude)
memanggilchatgpt = openai.OpenAI(api_key=api_chatgpt)
memanggildeepseek = openai.OpenAI(api_key = api_deepseek, base_url = "https://seekai.cc/v1")

message = []

print("========Torda AI========")
name = str(input("Masukkan nama user:"))
print(f'Halo {name}, selamat datang di mini chatbot Torda AI by RAN Group.')
print('''Model AI:
1. Claude
2. ChatGPT
3. DeepSeek''')

user = int(input("Pilih Model (1/2/3):"))

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

elif user == 3:
    while True:
            chat = input(f'{name}:').lower()
    
            if chat == "q":
                break
    
            message.append({"role": "user", "content": chat})
    
            respon = memanggildeepseek.chat.completions.create(model = "deepseek-v4-flash", 
                                                        messages = message,
                                                        stream=False, 
                                                        reasoning_effort="high", 
                                                        extra_body={"thinking": {"type": "enabled"}})

            jawab = ""

            message.append({"role": "system", "content": jawab})
    
            print("AI:", respon.choices[0].message.content)