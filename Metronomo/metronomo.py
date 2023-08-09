import time
import pygame
import threading


def cambiar_tono(sonido, factor_tono):
    sonido.set_volume(factor_tono)

def metronomo(tempo, beats_per_measure=4, sound_file="sounds\\sound-1.mp3"):
    pygame.init()
    pygame.mixer.init()

    # Cargar el archivo de sonido para el clic del metrónomo
    sound = pygame.mixer.Sound(sound_file)

    # Cálculo del tiempo entre clics (en segundos) según el tempo
    interval = 60.0 / tempo

    beat_count = 0

    # Crear un objeto de bloqueo para controlar la ejecución
    running_event = threading.Event()
    running_event.set()  # Inicialmente, permitir la ejecución

    def metronomo_thread():
        beat_count = 0
        while running_event.is_set():
            try:
                if beat_count == 0:
                    cambiar_tono(sound, 4.0)
                    sound.play()
                elif beat_count == 1:
                    cambiar_tono(sound, 0.25)
                    sound.play()
                else:
                    sound.play()

                beat_count += 1

                if beat_count == beats_per_measure:
                    beat_count = 0

                time.sleep(interval)
            except KeyboardInterrupt:
                break

    # Crear y comenzar el hilo del metrónomo
    metronomo_thread = threading.Thread(target=metronomo_thread)
    metronomo_thread.start()

    return running_event


