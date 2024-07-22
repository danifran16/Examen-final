from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('inicio.html')

# Calculos
def promedioNotas(n1,n2,n3):
    return (n1 + n2 + n3)

@app.route('/ejercicio1',methods=['GET','POST'])
def formulario1():
    if request.method == 'POST':
        nota1 = request.form['nota1']
        nota2 = request.form['nota1']
        nota3 = request.form['nota3']
        asistencia = request.form['asistencia']

        nota1 = int(nota1)
        nota2 = int(nota2)
        nota3 = int(nota3)
        asistencia = int(asistencia)

        pro = promedioNotas(nota1, nota2, nota3)/3

        if pro >= 40 and asistencia >= 75:
            asis = "Aprobado"
            return render_template('Ejercicio1.html', promedio=pro, asistencia=asis)
        else:
            asis = "Reprobado"
            return render_template('Ejercicio1.html', promedio=pro, asistencia=asis)
    return render_template('Ejercicio1.html')


@app.route('/ejercicio2',methods=['GET','POST'])
def formulario2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        n1L = len(nombre1)
        n2L = len(nombre2)
        n3L = len(nombre3)

        if n1L > n2L and n1L > n3L:
            return render_template('Ejercicio2.html', nombre='El nombre con mayor cantidad de caracteres es: '+ nombre1, caracteres= 'el nombre tiene: ' + str(n1L) + ' caracteres')
        if n2L > n1L and n2L > n3L:
            return render_template('Ejercicio2.html', nombre='El nombre con mayor cantidad de caracteres es: '+ nombre2, caracteres= 'el nombre tiene: ' + str(n2L) + ' caracteres')
        else:
            return render_template('Ejercicio2.html', nombre='El nombre con mayor cantidad de caracteres es: '+ nombre3, caracteres= 'el nombre tiene: ' + str(n3L) + ' caracteres')
    return render_template('Ejercicio2.html')

if __name__== '__main__':
    app.run()