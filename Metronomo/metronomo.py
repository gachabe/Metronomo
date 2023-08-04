import time
import pygame


def cambiar_tono(sonido, factor_tono):
    sonido.set_volume(factor_tono)
def metronomo(tempo, beats_per_measure=4, sound_file="sounds\\sound-1.mp3"):
    pygame.init()
    pygame.mixer.init()

    # Cargar el archivo de sonido para el clic del metrónomo
    sound = pygame.mixer.Sound(sound_file)

    # Cálculo del tiempo entre clics (en segundos) según el tempo
    interval = 60.0 / tempo

    running = True
    beat_count = 0

    while running:
        try:
            if beat_count == 0:
                cambiar_tono(sound,4.0)
                sound.play()
            elif beat_count ==1:
                cambiar_tono(sound, 0.25)
                sound.play()
            else:
                sound.play()
            # Contar los beats
            beat_count += 1

            # Si se completa una medida, reiniciar el contador
            if beat_count == beats_per_measure:
                beat_count = 0

            # Esperar antes del próximo clic
            time.sleep(interval)

        except KeyboardInterrupt:
            running = False

    pygame.quit()
