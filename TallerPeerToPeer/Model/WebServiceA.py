import json
import requests
from flask import Flask, jsonify, request, render_template, flash, redirect, url_for
from NodoA import NodoA
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = 'SECRETO'

n = NodoA()
nodo = 'Nodo A'
lista = n.num
print(f'bandera estado inicial ', n.bandera)

@app.route('/')
def inicio():
    suma_nodo = n.sumatoria()
    datos = {
        'nombre': nodo,
        'lista': lista,
        'total': suma_nodo
    }

    return render_template('index.html', datos=datos)


@app.route('/guardar', methods=['get', 'post'])
def guardar():

    if request.method == 'POST':
        numero = request.form['numero']
        num = int(numero)
        n.num.append(num)
        flash(f'El numero guardado es : {num}')
        return redirect(url_for('inicio'))

    return render_template('index.html')



# ----------------------Servicio del nodo----------------------------------
@app.route('/total')
def suma_nodo():
    if n.bandera == 0:
        suma_vec = sumatoria()
        print(f'bandera estado en entrega de datos : ', n.bandera)
        suma_vec = suma_vec.json
        print(f'suma vecinos : {suma_vec}')
    else:
        suma_vec = 0
    return jsonify(suma_vec)


# ----------------------Reseteo  del nodo----------------------------------
@app.route('/reset', methods=['get', 'post'])
def reset():
    for i in n.vecinos.values():
        response = requests.get(url=f"{i}/cambiarflag")
        print(response.status_code)
        if response.status_code == 200:
            mensaje = {'mensaje ': 'OK'}
        else:
            mensaje = {'mensaje ': 'OK'}

    return mensaje

@app.route('/cambiarflag')
def cambiar_flag():
    if n.bandera ==1:
        n.bandera =0
        rta = reset()
        print(rta)
        print(f'estado actual de bandera', n.bandera)
    return rta



# -----------------Web service cliente ------------------------------------
@app.route('/sumatoria')
def sumatoria():
    valor = 0
    n.bandera = 1
    print(f'bandera estado cuando solicito data : ', n.bandera)
    for i in n.vecinos.values():
        print(i)
        response = requests.get(url=f"{i}/total")
        data = response.content
        data = data.decode()
        data = json.loads(data)
        print('->', data)
        valor += data
    suma = n.suma_vecinos(valor)
    print(f'Yo : {n.sumatoria()}')

    return jsonify(suma)

@app.route('/redsum' ,methods=['post','get'])
def redsum():
    red = sumatoria()
    sum= red.json
    print(sum)
    suma_nodo = n.sumatoria()
    datos = {
        'nombre': nodo,
        'lista': lista,
        'total': suma_nodo,
        'red': sum
    }

    return render_template('index.html', datos= datos)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
