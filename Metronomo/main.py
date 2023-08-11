import interfaz

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
       interfaz.app.mainloop()
    except KeyboardInterrupt:
        print("\nMetrónomo detenido por el usuario.")


