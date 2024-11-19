from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejer1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = None
    estado = None

    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        promedio = (nota1 + nota2 + nota3) / 3
        estado = "Aprobado" if promedio >= 40 and asistencia >= 75 else "Reprobado"

    return render_template('ejer1', promedio=promedio, estado=estado)


@app.route('/ejer2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None

    if request.method == 'POST':
        nombres = [
            request.form['nombre_1'],
            request.form['nombre_2'],
            request.form['nombre_3']
        ]
        # Obtener el nombre más largo
        nombre_largo = max(nombres, key=len)
        resultado = {'nombre': nombre_largo, 'longitud': len(nombre_largo)}

    return render_template('ejer2', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
