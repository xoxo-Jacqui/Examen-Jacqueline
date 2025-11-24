from flask import Flask, render_template, request

app = Flask(__name__)


# Página principal con menú (dos botones)
@app.route("/")
def index():
    return render_template("index.html")


# EJERCICIO 1: Pinturas
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None

    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        cantidad_tarros = int(request.form["cantidad_tarros"])

        precio_unitario = 9000
        total_sin_descuento = cantidad_tarros * precio_unitario

        # Cálculo del descuento según la edad
        descuento = 0
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        monto_descuento = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - monto_descuento

        resultado = {
            "nombre": nombre,
            "edad": edad,
            "cantidad_tarros": cantidad_tarros,
            "total_sin_descuento": total_sin_descuento,
            "descuento_porcentaje": int(descuento * 100),
            "total_con_descuento": total_con_descuento
        }

    return render_template("ejercicio1.html", resultado=resultado)


# EJERCICIO 2: Login simple
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = None

    # Usuarios “registrados”
    usuarios = {
        "juan": "admin",
        "pepe": "user"
    }

    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]

        if usuario in usuarios and password == usuarios[usuario]:
            if usuario == "juan":
                mensaje = f"Bienvenido administrador {usuario}"
            elif usuario == "pepe":
                mensaje = f"Bienvenido usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template("ejercicio2.html", mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True)
