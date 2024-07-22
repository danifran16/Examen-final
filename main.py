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
        nombre = request.form['nombre']
        edad = request.form['edad']
        cantTarros = request.form['cantTarros']

        edad = int(edad)
        cantTarros = int(cantTarros)
        tarrosPintura = 9000
        totalSinDescuento = int(cantTarros * tarrosPintura)

        if edad >= 18 and edad <= 30:
            descuento = totalSinDescuento * 0.15
            totalConDescuento = totalSinDescuento - descuento
            return render_template('Ejercicio1.html',
                                   nombre='Nombre del cliente:' + nombre,
                                   totalSinDescuento= 'Total sin descuento: $' + str(totalSinDescuento),
                                   descuento= 'El descuento es: $' + str(descuento),
                                   totalConDescuento= 'El total a pagar es de: $' +str(totalConDescuento))
        if edad > 30:
            descuento = totalSinDescuento * 0.25
            totalConDescuento = totalSinDescuento - descuento
            return render_template('Ejercicio1.html',
                                   nombre='Nombre del cliente:' + nombre,
                                   totalSinDescuento= 'Total sin descuento: $' + str(totalSinDescuento),
                                   descuento= 'El descuento es: $' + str(descuento),
                                   totalConDescuento= 'El total a pagar es de: $' +str(totalConDescuento))
        else:
            descuento =  0
            totalConDescuento = totalSinDescuento - descuento
            return render_template('Ejercicio1.html',
                                   nombre='Nombre del cliente:' + nombre,
                                   totalSinDescuento='Total sin descuento: $' + str(totalSinDescuento),
                                   descuento='El descuento es: $' + str(descuento),
                                   totalConDescuento='El total a pagar es de: $' + str(totalConDescuento))
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