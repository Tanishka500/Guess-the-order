import tkinter as tk
import random

colors = ['Black', 'Red', 'Yellow', 'Green', 'Blue']
hidden_sequence = []
guess_sequence = []
score = 0

def generateSequence():
    global hidden_sequence
    hidden_sequence = random.sample(colors, 5)

def startGame(event):
    global score
    if not hidden_sequence:
        generateSequence()
    displayCups()

def drawGlass(canvas, color):
    width, height = 60, 100
    canvas.create_rectangle(10, 10, width, height, fill=color, outline='black', width=2)
    canvas.create_rectangle(10, height - 10, width, height, fill='white', outline='black', width=2)

def displayCups():
    global color_buttons
    for widget in color_frame.winfo_children():
        widget.destroy()
    for widget in guessed_colors_frame.winfo_children():
        widget.destroy()

    color_buttons = []
    for color in colors:
        canvas = tk.Canvas(color_frame, width=100, height=150, bg='lightgrey')
        canvas.pack(side=tk.LEFT, padx=5)
        drawGlass(canvas, color)
        
        button = tk.Button(color_frame, text=color, command=lambda c=color: addToGuess(c), bg='darkgrey', fg='black', font=('Times New Roman', 12))
        button.pack(side=tk.LEFT, pady=5)
        color_buttons.append(button)

    global guessed_colors_canvas
    guessed_colors_canvas = tk.Canvas(guessed_colors_frame, width=800, height=120, bg='lightgrey')
    guessed_colors_canvas.pack(pady=10)

    global guess_sequence
    guess_sequence = []

    instructions.config(text="Arrange the cups in the order you think is under the cart:")

def addToGuess(color):
    global guess_sequence
    if len(guess_sequence) < 5:
        guess_sequence.append(color)
        updateGuessedColors()
    if len(guess_sequence) == 5:
        checkGuess()

def updateGuessedColors():
    global guessed_colors_canvas
    guessed_colors_canvas.delete("all")
    width, height = 60, 100
    for i, color in enumerate(guess_sequence):
        x = i * (width + 10) + 10
        guessed_colors_canvas.create_rectangle(x, 10, x + width, height, fill=color, outline='black', width=2)
        guessed_colors_canvas.create_rectangle(x, height - 10, x + width, height, fill='white', outline='black', width=2)

def checkGuess():
    global score
    correct_count = sum(1 for i in range(5) if guess_sequence[i] == hidden_sequence[i])
    
    if correct_count == 5:
        score += 1
        result_label.config(text=f"Congratulations! You guessed correctly! Score: {score}")
        instructions.config(text="You guessed correctly! Press Enter to play again.")
    else:
        result_label.config(text=f"Correctly placed colors: {correct_count}/5. Score: {score}. Try again!")

    guess_sequence.clear()
    updateGuessedColors()

def resetGame(event):
    global hidden_sequence
    if not hidden_sequence:
        generateSequence()
    displayCups()

root = tk.Tk()
root.title("Color Guessing Game")
root.geometry("800x500")
root.configure(bg='lightgrey')

instructions = tk.Label(root, text="Press Enter to start", font=('Times New Roman', 12), bg='lightgrey', fg='black')
instructions.pack(pady=10)

result_label = tk.Label(root, text="", font=('Times New Roman', 12), bg='lightgrey', fg='black')
result_label.pack(pady=10)

color_frame = tk.Frame(root, bg='lightgrey')
color_frame.pack(pady=10)

guessed_colors_frame = tk.Frame(root, bg='lightgrey')
guessed_colors_frame.pack(pady=10)

guess_label = tk.Label(root, text="", font=('Times New Roman', 24), bg='lightgrey', fg='black')
guess_label.pack(pady=10)

guessed_colors_canvas = tk.Canvas(guessed_colors_frame, width=800, height=120, bg='lightgrey')
guessed_colors_canvas.pack(pady=10)

root.bind('<Return>', lambda event: startGame(event) if hidden_sequence else resetGame(event))

root.focus_set()
color_buttons = []

root.mainloop()
