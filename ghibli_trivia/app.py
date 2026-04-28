from flask import Flask, render_template, request, redirect, url_for, session
from services.api import obtener_peliculas
from services.preguntas import generar_preguntas

app = Flask(__name__)
app.secret_key = "clave_secreta"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start", methods=["POST"])
def start():
    peliculas = obtener_peliculas()
    preguntas = generar_preguntas(peliculas)

    session["preguntas"] = preguntas
    session["puntaje"] = 0
    session["actual"] = 0

    return redirect(url_for("game"))


@app.route("/game", methods=["GET", "POST"])
def game():
    if request.method == "POST":
        respuesta = request.form["respuesta"]
        actual = session["actual"]
        preguntas = session["preguntas"]

        if respuesta == preguntas[actual]["respuesta"]:
            session["puntaje"] += 1

        session["actual"] += 1

        if session["actual"] >= 10:
            return redirect(url_for("resultado"))

    actual = session["actual"]
    pregunta = session["preguntas"][actual]

    return render_template("game.html", pregunta=pregunta, numero=actual+1)


@app.route("/resultado")
def resultado():
    puntaje = session["puntaje"]
    return render_template("result.html", puntaje=puntaje)


if __name__ == "__main__":
    app.run(debug=True)