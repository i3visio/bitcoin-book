# -*- coding: utf-8 -*-
#!/usr/bin/env python3
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

import sys

# Definimos la API URL base donde está localizado el servicio
BASE_URL = 'http://localhost:5000/api/geolocate/'

# Importando las librerías...
from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

# Creando un cliente de bitrequest para gestionar transparentemente las peticiones...
wallet = Wallet()
requests = BitTransferRequests(wallet)

# Comprando la petición
def buyGeolocateAPI(ip):
    try:    
        response = requests.get( url = BASE_URL + ip )
        print(response.text)
        print(“¡Pago realizado!)
    except Exception as e:
        print("¡Oops! Algo ha pasado...")
        print(str(e))

def showHelp():
    print("client.py <IP> [<IP> <IP> ...]")
    sys.exit()

if __name__ == "__main__":
    # Verificando si se han facilitado argumentos suficientes
    if len(sys.argv) >= 2:
        for ip in sys.argv[1:]:
            buyGeolocateAPI(ip)
    else:
        showHelp()
