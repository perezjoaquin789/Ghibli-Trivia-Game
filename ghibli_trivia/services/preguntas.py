import random

def generar_preguntas(peliculas):
    preguntas = []

    for _ in range(10):
        peli = random.choice(peliculas)
        tipo = random.choice(["director", "anio", "score"])

        if tipo == "director":
            correcta = peli["director"]
            opciones = list(set([p["director"] for p in peliculas]))
            pregunta = f"¿Quién dirigió {peli['title']}?"

        elif tipo == "anio":
            correcta = peli["release_date"]
            opciones = list(set([p["release_date"] for p in peliculas]))
            pregunta = f"¿En qué año se lanzó {peli['title']}?"

        else:
            correcta = peli["rt_score"]
            opciones = list(set([p["rt_score"] for p in peliculas]))
            pregunta = f"¿Cuál es el score de {peli['title']}?"

        opciones = random.sample(opciones, 4)

        if correcta not in opciones:
            opciones[random.randint(0, 3)] = correcta

        preguntas.append({
            "pregunta": pregunta,
            "opciones": opciones,
            "respuesta": correcta
        })

    return preguntas