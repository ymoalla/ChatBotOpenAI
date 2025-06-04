from openaiapi import *

system_message = "Tu es un assitant plus humain, tu t'appelle Alex, tu as 30 ans et tu réponds comme un humain et non pas comme un assitant virtuel"
messages = []

while True:
    prompt = input("You: ")
    print()
    response = get_prompt(prompt, system_message, messages)
    print("ChatGPT: " + response)
    print()
