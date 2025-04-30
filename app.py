"""<made by: givemetocode-net-hk/powerpointGPTwithGemini email: info@givemetocode.com >"""

import tkinter as tk
import requests
import json


def send_message():
    user_message = user_input.get()
    if user_message:
        messages = [
            {"role": "system", "content": "You are a powerpoint GPT trained by givemetocode.net and name is powerpointGPT."},
            {"role": "user", "content": user_message}
        ]
        
        api_url = "https://pptai-for-tcps-v1.deno.dev/v1/chat/completions"
        headers = {
            "Authorization": "Bearer AIzaSyArFHUgs0FlUoE2OkVQLEfqi0s6mWKhbAA",
            "Content-Type": "application/json"
        }
        payload = {
            "messages": messages,
            "model": "gemini-2.0-flash-exp"
        }
        
        response = requests.post(api_url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            reply = response.json().get('choices')[0]['message']['content']
            chat_window.insert(tk.END, f"User: {user_message}\n")
            chat_window.insert(tk.END, f"GPT: {reply}\n")
        else:
            chat_window.insert(tk.END, "Error: Unable to get response from API.\n")
        
        user_input.delete(0, tk.END)


root = tk.Tk()
root.title("powerpointgpt v1.0.0.0 alpha")


chat_window = tk.Text(root, wrap=tk.WORD)
chat_window.pack(padx=10, pady=10)


user_input = tk.Entry(root, width=50)
user_input.pack(padx=10, pady=10)


send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)


root.mainloop()