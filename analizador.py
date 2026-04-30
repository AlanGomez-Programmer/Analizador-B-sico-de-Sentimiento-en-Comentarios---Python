palabras_positivas = ["ama", "gusta", "genial", "excelente", "bueno", "encanto"]
palabras_negativas = ["odio", "malo", "terrible", "decepcionado", "decepcionada", "decepcionante", "pésimo", "no"]

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
        cantidad_palabras = len(comentario)

        for i in range(cantidad_palabras):
            palabra_por_palabra = comentario[i]
            if palabra_por_palabra in palabras_positivas:
                contador_p += 1

            if palabra_por_palabra in palabras_negativas:
                contador_n += 1
            
        
        if contador_p > contador_n:
            print("Comentario positivo")
        elif contador_n > contador_p:
            print("Comentario negativo")
        else:
            print("Comentario Neutro")
            
               

       


analizador()

    