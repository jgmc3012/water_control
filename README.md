# water_control
Sistema de administracion y control para una central de distribucion de agua

## Credenciales
Usuario = user.test
Contraseña = 1q2w3e4r5t

# Instalacion
```shell
sudo apt install git python3.7 python3-venv python3.7-venv python3.7-dev

git clone https://github.com/jgmc3012/water_control.git
cd water_control

python3.7 -m venv venv
source venv/bin/acticate
pip install wheel
pip install -r requeriments.txt

cp .env.example .env
# Configurar las Variables de entorno
# hasta ahora es solo el Key de django

#Nota si deseas configurar una base de datos para el proyecto deberias guarte desde otro lugar

python manage.py migrate
python manage.py collectstatic
```