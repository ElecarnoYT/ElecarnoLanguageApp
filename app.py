import tkinter as tk
import tkinter.font as font
from random import randint
root = tk.Tk()
root.config(bg="#4a4a4a")
root.resizable(width=False, height=False)
root.title("Elecarno's Language Learning App")

print("---------------------------------------")

# dictionary
words_library_spanish = [
    "Espanol",
    "los ojos",
    "el perro",
    "la piscina",
    "una camisa",
    "los zapatos",
    "llevo",
    "llevamos",
    "tengo",
    "tiene",
    "un vestido",
    "un abrigo",
    "una falda",
    "una camiseta",
    "una bufanda",
    "una corbata",
    "una gorra",
    "unos pantalones",
    "unos pantalones cortos",
    "unos vaqueros",
    "unos calcetines",
    "una botas",
    "unas zapatillas de deporte",
    "unas gafas",
    "negro",
    "blanco",
    "verde",
    "rojo",
    "rosa",
    "morado",
    "gris",
    "amarillo",
    "naranja",
    "azul",
    "llevas",
    "lleva",
    "llevais",
    "llevan"
]

words_library_english = [
    "Spanish",
    "eyes",
    "the dog",
    "the swimming pool",
    "a shirt",
    "the shoes",
    "I wear",
    "we wear",
    "I have",
    "you have",
    "a dress",
    "a coat",
    "a skirt",
    "a T-shirt",
    "a scarf",
    "a tie",
    "a cap",
    "trousers",
    "shorts",
    "jeans",
    "socks",
    "boots",
    "trainers",
    "glasses",
    "black",
    "white",
    "green",
    "red",
    "pink",
    "purple",
    "grey",
    "yellow",
    "orange",
    "blue",
    "you wear",
    "is wearing",
    "you wear",
    "they wear"
]

# colours & other definitions
bg_colour = "#4a4a4a"
panel_colour = "#666666"
font_colour = "#c4c4c4"
button_colour = "#595959"
main_font = font.Font(family="Helvetica", size=30)

# define canvas
canvas = tk.Canvas(root, height=512, width=512, bg=bg_colour)
canvas.pack()

# define textbox
answer = tk.Entry(bg=panel_colour, bd=0, font=main_font, justify="center", fg=font_colour)
answer.place(x=32, y=310, width=448, height=76)

# define word value
word_value = randint(1, len(words_library_spanish))
used_words = []

if word_value not in used_words:
    word_to_display = words_library_spanish[word_value - 1]
    used_words.append(word_value)

correct = 0
incorrect = 0
print("The word is: " + word_to_display)


def set_word_value():
    global word_value
    global word_to_display
    word_value = randint(0, len(words_library_spanish))
    word_to_display = words_library_spanish[word_value - 1]
    print("---------------------------------------")
    print("The word is: " + word_to_display)
    word = tk.Label(bg=bg_colour, text=word_to_display, font=main_font, fg=font_colour, justify="center", bd=0)
    word.place(x=32, y=218, width=448, height=76)
    if word_value not in used_words:
        word_to_display = words_library_spanish[word_value - 1]
        used_words.append(word_value)
    else:
        set_word_value()


# define label
word = tk.Label(bg=bg_colour, text=word_to_display, font=main_font, fg=font_colour, justify="center", bd=0)
word.place(x=32, y=218, width=448, height=76)


# define button
def check_word():
    global answer
    global correct
    global incorrect
    global used_words
    correct_word = words_library_english[word_value - 1]
    answer_value = answer.get()
    if answer_value == correct_word:
        print("\"" + answer_value + "\"" + " is correct")
        print(used_words)
        set_word_value()
        correct + 1
        answer.delete(0, "end")
    else:
        print("\"" + answer_value + "\"" + " is incorrect")
        print(used_words)
        set_word_value()
        incorrect + 1
        answer.delete(0, "end")


def callback(event):
    check_word()


root.bind('<Return>', callback)

enter_button = tk.Button(bg=button_colour, text="Check", font=main_font, fg=font_colour, justify="center", bd=0, command=check_word)
enter_button.place(x=121, y=401, width=270, height=76)

root.mainloop()
