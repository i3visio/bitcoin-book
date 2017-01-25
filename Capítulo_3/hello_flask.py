# -*- coding: utf-8 -*-
# Copyright (C) 2016,  Félix Brezo @febrezo and Yaiza Rubio @yrubiosec
# 
#  This program is free software: you can redistribute it and/or modify# 
#  it under the terms of the Affero GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the Affero GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import flask

app = flask.Flask(__name__)

# Importamos el nuevo módulo
import requests

# Definimos la URL base
BASEURL = "http://ipinfo.io/"

# Definimos la ruta donde  expondremos la API de geolocalización
@app.route('/api/geolocate/<ip>')
def api_geolocate(ip):
    # Construimos la URL de destino en función de la IP usada
    targetUrl =  BASEURL + ip
    # Visualizamos el contenido como texto preformateado
    return requests.get(targetUrl).text

# Definimos la ruta donde haremos la geolocalización
@app.route('/geolocate/<ip>')
def geolocate(ip):
    # Construimos la URL de destino en función de la IP usada
    targetUrl =  BASEURL + ip
    # Visualizamos el contenido como texto preformateado
    return '\nResultados para ' + ip + ':<pre>' + requests.get(targetUrl).text + '</pre>'

# Definimos la ruta principal y retornamos código HTML arbitrario...
@app.route('/')
def home():
    return '<h1>¡Hola mundo!</h1>Un saludo de Yaiza y Félix. Puedes usar el servicio de geolocalización usando esta ruta: <a href="/geolocate/8.8.8.8">/geolocate/8.8.8.8</a>.'

# Arrancamos el servidor
if __name__ == "__main__":
    app.run()