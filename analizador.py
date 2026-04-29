palabras = {
    "Positivas": ["ama", "gusta", "genial", "excelente", "bueno"],
    "Negativas": ["odio", "malo", "terrible", "decepcionado", "decepcionada", "decepcionante", "pésimo"]
}


def validar_palabras():

    palabras = input("Ingrese el comentario: ").strip().lower()

    palabras_separadas = palabras.split(" ")

    return palabras_separadas
    

def analizador():
    while True:

        print("--- ANALIZADOR DE COMENTARIOS ---")
        comentario = validar_palabras()

        contador_p = 0
        contador_n = 0

        print(comentario)

        cantidad_palabras = len(comentario)

        print(cantidad_palabras)

        for i in range(cantidad_palabras):
            for llave, palabra in palabras.items():
                print(llave, palabra)

       


analizador()

    