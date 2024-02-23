import tkinter as tk
import random

class ChatBotApp:
    def __init__(self, master):
        self.master = master
        master.title("Random ChatBot")

        self.chat_history = tk.Text(master, state=tk.DISABLED)
        self.chat_history.pack(padx=10, pady=10)

        self.user_input = tk.Entry(master)
        self.user_input.pack(padx=10, pady=10, fill=tk.X)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=10)

    def send_message(self):
        message = self.user_input.get()
        self.user_input.delete(0, tk.END)
        self.display_message("You: " + message)

        response = self.generate_response(message)
        self.display_message("Bot: " + response)

    def generate_response(self, message):
        # Define some sample responses
        def generate_random_sentence():
            subjects = ["I", "You", "He", "She", "They", "We"]
            verbs = ["am", "are", "is", "was", "were"]
            objects = ["happy", "sad", "hungry", "thirsty", "tired", "excited"]

            subject = random.choice(subjects)
            verb = random.choice(verbs)
            obj = random.choice(objects)

            sentences_01= f"{subject} {verb} {obj}."

            return sentences_01

        responses = [
            generate_random_sentence(),     
            "That's interesting!",
            "I'm not sure I understand.",
            "Tell me more.",
            "What do you think about that?",
            "I see.",
            "Could you elaborate?",
            "Interesting, tell me more about it.",
            "I'm sorry, I don't have an answer for that right now."
        ]

        # Select a random response
        return random.choice(responses)

    def display_message(self, message):
        self.chat_history.config(state=tk.NORMAL)
        self.chat_history.insert(tk.END, message + '\n')
        self.chat_history.config(state=tk.DISABLED)
        self.chat_history.see(tk.END)

def main():
    root = tk.Tk()
    app = ChatBotApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()