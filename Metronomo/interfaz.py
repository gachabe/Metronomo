import customtkinter as ctk
from PIL import Image
from metronomo import metronomo
rboton=1
play = ctk.CTkImage(Image.open("image\\play.ico"))
ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = ctk.CTkButton(master=app,image= play,text="",height=rboton,width=rboton, corner_radius=75, command=button_function)
button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
def slider_event(value):
    metronomo(value)

slider = ctk.CTkSlider(app, from_=50, to=200, command=slider_event)
slider.pack()

app.mainloop()