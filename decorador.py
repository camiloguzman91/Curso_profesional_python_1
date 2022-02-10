def mayus(func):
    def env(text):
        return func(text).upper()
    return env


@mayus
def mensaje(nombre):
    return f'{nombre}, recibió un mensaje'


print(mensaje('Pepe'))
