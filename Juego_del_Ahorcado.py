import os
import random

FAILS_MAX = 5
strings = [
    'crema', 'café', 'estrella', 'explosión', 'guitarra', 'plástico',
    'navaja', 'martillo', 'libros', 'lápiz', 'lapicera', 'aluminio',
    'embarcación', 'letra', 'agujeta', 'ventana', 'librería', 'sonido',
    'universidad', 'rueda', 'perro', 'llaves', 'camisa', 'pelo', 'papá',
    'sillón', 'felicidad', 'catre', 'teclado', 'servilleta', 'escuela',
    'pantalla', 'sol', 'codo', 'tenedor', 'estadística', 'mapa', 'agua',
    'mensaje', 'lima', 'cohete', 'rey', 'edificio', 'césped', 'presidencia',
    'hojas', 'parlante', 'colegio', 'granizo', 'pestaña', 'lámpara', 'mano',
    'monitor', 'flor', 'música', 'hombre', 'tornillo', 'habitación', 'velero',
    'abuela', 'abuelo', 'palo', 'satélite', 'templo', 'lentes', 'bolígrafo',
    'plato', 'nube', 'gobierno', 'botella', 'castillo', 'enano', 'casa', 'libro',
    'persona', 'planeta', 'televisor', 'guantes', 'metal', 'teléfono', 'proyector',
    'mono', 'remera', 'muela', 'petróleo', 'percha', 'remate', 'debate', 'anillo',
    'cuaderno', 'ruido', 'pared', 'taladro', 'herramienta', 'cartas', 'chocolate',
    'anteojos', 'impresora', 'caramelos', 'living', 'luces', 'angustia', 'zapato',
    'bomba', 'lluvia', 'ojo', 'corbata', 'periódico', 'diente', 'planta', 'chupetín',
    'buzo', 'oficina', 'persiana', 'puerta', 'tío', 'silla', 'ensalada', 'pradera',
    'zoológico', 'candidato', 'deporte', 'recipiente', 'diarios', 'fotografía',
    'ave', 'hierro', 'refugio', 'pantalón', 'barco', 'carne', 'nieve', 'tecla',
    'humedad', 'pistola', 'departamento', 'celular', 'tristeza', 'hipopótamo', 'sofá',
    'cama', 'árbol', 'mesada', 'campera', 'discurso', 'auto', 'cinturón', 'rúcula',
    'famoso', 'madera', 'lentejas', 'piso', 'maletín', 'reloj', 'diputado', 'cuchillo',
    'desodorante', 'candado', 'luz', 'montañas', 'computadora', 'radio', 'moño', 'cuadro',
    'calor', 'partido', 'teatro', 'bife', 'fiesta', 'bala', 'auriculares'
]


def create_strings():
    string = random.choice(strings)
    secret = '_'*len(string)
    return string, secret

def replace_letter(original, secret, letter):
    amount = original.count(letter)
    start = 0
    for i in range(amount):
        pos = original.find(letter, start)
        secret = secret[:pos] + letter + secret[pos+1:]
        start = pos + 1
    return secret

def run():
    original, secret = create_strings()
    fails = 0
    while secret != original and fails < FAILS_MAX:
        print("Hola, bienvenido al juego del ahorcado. ¡Tienes 5 intentos para ganar!")
        print(f'Palabra: {secret}')
        s = input('¿Cuál letra quieres destapar? ')
        if s in original:
            secret = replace_letter(original, secret, s)
        else:
            fails += 1
            
        os.system("cls")    

    if secret == original:
        print(f'Felicidades, ¡GANASTE! La palabra es {original}')
    else:
        print(f'Tienes {fails} fallos de {FAILS_MAX} oportunidades')
        print(f'Lo siento, la palabra era {original}')



if __name__ == "__main__":
    os.system("cls")
    run()