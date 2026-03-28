import tkinter as tk
from chatbot_model import chatbot_response

def send_message(event=None):
    user_input = entry.get()

    if user_input.strip() == "":
        return

    chat_box.insert(tk.END, "You: " + user_input + "\n")

    response = chatbot_response(user_input)
    chat_box.insert(tk.END, "Bot: " + response + "\n\n")

    entry.delete(0, tk.END)

# Window
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("400x500")

# Chat display
chat_box = tk.Text(root)
chat_box.pack(pady=10)

# Input area
frame = tk.Frame(root)
frame.pack()

entry = tk.Entry(frame, width=30)
entry.pack(side=tk.LEFT)

send_button = tk.Button(frame, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

entry.bind("<Return>", send_message)

root.mainloop()