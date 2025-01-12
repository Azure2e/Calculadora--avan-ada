import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Super Calculadora Avançada")
        self.root.geometry("400x600")
        self.root.resizable(0, 0)

        self.display = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="ridge", justify="right")
        self.display.pack(expand=True, fill="both")

        self.create_buttons()

    def create_buttons(self):
        button_texts = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*',
            '1', '2', '3', '-', 
            '0', '.', '=', '+'
        ]

        button_frame = ttk.Frame(self.root)
        button_frame.pack(expand=True, fill="both")

        for i, text in enumerate(button_texts):
            button = ttk.Button(button_frame, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=i//4, column=i%4, sticky='nsew')
            button_frame.grid_rowconfigure(i//4, weight=1)
            button_frame.grid_columnconfigure(i%4, weight=1)

    def on_button_click(self, char):
        if char == '=':
            try:
                expression = self.display.get()
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Erro")
        else:
            current_text = self.display.get()
            new_text = current_text + char
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, new_text)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()