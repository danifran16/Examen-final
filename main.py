from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('inicio.html')

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
            descuento = 0
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
        nombreSesion = request.form['nombreSesion']
        contraseña = request.form['contraseña']

        if nombreSesion == "juan" and contraseña == "admin":
            return render_template('Ejercicio2.html',
                                   nombre='Bienvenido administrador '+ nombreSesion)
        elif nombreSesion == "pepe" and contraseña == "user":
            return render_template('Ejercicio2.html',
                                   nombre='Bienvenido usuario '+ nombreSesion)
        else:
            return render_template('Ejercicio2.html',
                                   nombre='Usuario o contraseña incorrectos')
    return render_template('Ejercicio2.html')

if __name__== '__main__':
    app.run()