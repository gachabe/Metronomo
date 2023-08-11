import customtkinter as ctk
from PIL import Image
from metronomo import metronomo


rboton = 30
play = ctk.CTkImage(Image.open("image\\play.ico"))
pause = ctk.CTkImage(Image.open("image\\pause.png"))
ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


app = ctk.CTk()  # create CTk window like you do with the Tk window
app.title("Metrónomo")
app.iconbitmap("image\\icono2.ico")
app.geometry("400x240")
app.resizable(False,False)

beats = ctk.IntVar(value = 4)
valor_tempo = ctk.IntVar(value = 50)
play_boton = ctk.BooleanVar(value = False)
prueba = [0]
sonido = ctk.StringVar(value = "sounds\\sound-1.mp3")

def button_function():


    if play_boton.get():
        prueba[0].clear()
        play_boton.set(False)
        button.configure(image=play)
    else:
        prueba[0] = metronomo(valor_tempo.get(),beats.get(),sound_file=sonido.get())
        play_boton.set(True)
        button.configure(image=pause)



def slider_event(value):
    if play_boton.get():
        prueba[0].clear()
        play_boton.set(False)
    value_label.configure(text=valor_tempo.get())


value_label = ctk.CTkLabel(app, textvariable=valor_tempo, font=("Helvetica", 30))
value_label.pack()


button = ctk.CTkButton(master=app, image=play, text="", height=rboton, width=rboton, corner_radius=75,
                       command=button_function)
button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)


slider = ctk.CTkSlider(master = app,from_ = 50, to = 200, command=slider_event, variable=valor_tempo)
slider.pack()

button2 = ctk.CTkButton(master = app, font=("Helvetica", 20), text = "2/4", height= 10, width = 50,
                        command= lambda : beats.set(2))
button3 = ctk.CTkButton(master = app, font=("Helvetica", 20),text = "3/4", height= 10, width = 50,
                        command=lambda: beats.set(3))
button4 = ctk.CTkButton(master = app, font=("Helvetica", 20), text = "4/4", height= 10, width = 50,
                        command=lambda: beats.set(4))
button2.place(relx=0.07, rely=0.3, anchor=ctk.W)
button3.place(relx=0.07, rely=0.5, anchor=ctk.W)
button4.place(relx=0.07, rely=0.7, anchor=ctk.W)

button5 = ctk.CTkButton(master = app, font=("Helvetica", 20), text = "Sound 1", height= 10, width = 50,
                        command= lambda : sonido.set("sounds\\sound-1.mp3"))
button6 = ctk.CTkButton(master = app, font=("Helvetica", 20),text = "Sound 2", height= 10, width = 50,
                        command=lambda: sonido.set("sounds\\sound-2.wav"))
button7 = ctk.CTkButton(master = app, font=("Helvetica", 20), text = "Sound 3", height= 10, width = 50,
                        command=lambda: sonido.set("sounds\\sound-3.mp3"))

button5.place(relx=0.93, rely=0.3, anchor=ctk.E)
button6.place(relx=0.93, rely=0.5, anchor=ctk.E)
button7.place(relx=0.93, rely=0.7, anchor=ctk.E)

app.mainloop()
