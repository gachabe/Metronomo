import customtkinter as ctk
from PIL import Image
from metronomo import metronomo


rboton = 1
play = ctk.CTkImage(Image.open("image\\play.ico"))
ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green



app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

valor_tempo = ctk.IntVar(value = 50)
play_boton = ctk.BooleanVar()

def button_function():


    if play_boton.get():
        play_boton.set(False)
    else:
        play_boton.set(True)
    print(play_boton.get())
    metronomo(valor_tempo.get(),running = play_boton.get())


def slider_event(value):
    value_label.configure(text=valor_tempo.get())


value_label = ctk.CTkLabel(app, textvariable=valor_tempo)
value_label.pack()




# Use CTkButton instead of tkinter Button
button = ctk.CTkButton(master=app, image=play, text="", height=rboton, width=rboton, corner_radius=75,
                       command=button_function)
button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)


slider = ctk.CTkSlider(master = app,from_ = 50, to = 200, command=slider_event, variable=valor_tempo)
slider.pack()

app.mainloop()
