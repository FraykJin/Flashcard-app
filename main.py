from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
FONT1 = ('Ariel', 40, 'italic')
FONT2 = ('Ariel', 60, 'bold')
ENGLISH = None

dataframe = pandas.read_csv('./data/french_words.csv')
# french_word = dataframe['French'].tolist()
to_learn = dataframe.to_dict(orient='records')


# Fonctions pour les boutons command=fonction


def change_word():
    global ENGLISH
    random_french_word = random.choice(to_learn)
    canvas.itemconfigure(carte, image=card_front_img)
    canvas.itemconfigure(id_mot, text=f"{random_french_word['French']}")
    canvas.itemconfigure(id_up, text='French')
    ENGLISH = random_french_word['English']
    window.after(3000, change_background)


def change_background():
    canvas.itemconfigure(carte, image=card_back_img)
    canvas.itemconfigure(id_up, text='English')
    canvas.itemconfigure(id_mot, text=f"{ENGLISH}")


# Notre application

window = Tk()
window.title('Flash Card App')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


# Arriere Plan Carte Verte
card_back_img = PhotoImage(file='./images/card_back.png')

# Foreground carte Blanche = la reponse
card_front_img = PhotoImage(file='./images/card_front.png')
carte = canvas.create_image(400, 263, image=card_front_img)

# Button Wrong
image_non = PhotoImage(file='./images/wrong.png')
button_wrong = Button(image=image_non, highlightthickness=0, command=change_word)
button_wrong.grid(row=1, column=0)

# Button Right
image_oui = PhotoImage(file='./images/right.png')
button_right = Button(image=image_oui, highlightthickness=0, command=change_word)
button_right.grid(row=1, column=1)

# Label 1
id_up = canvas.create_text(400, 150, font=FONT1, text='French')

# Mot
id_mot = canvas.create_text(400, 263, font=FONT2, text='mot')

change_word()


window.mainloop()