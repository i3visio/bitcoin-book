
#Descarga de Node
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.4/install.sh | bash

# Configuración de variables de entorno
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" # This loads nvm

# Instalación de la versión 4 de Node
nvm install v4

# Resolución de dependencias adicionales
sudo apt-get install libzmq3-dev build-essential

# Instalación de bitcore-node usando NPM
npm install -g bitcore-node
bitcore-node create mynode
cd mynode

# Instalación de la API
bitcore-node install insight-api
# Instalación de la interfaz gráfica
bitcore-node install insight-ui
# Arrancamos el servicio
bitcore-node start
