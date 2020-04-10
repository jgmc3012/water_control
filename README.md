# water_control
Sistema de administracion y control para una central de distribucion de agua

En la app podras:
- Crear y modificar Usuarios
- Registrar locales/casas a las cuales se les suministra agua
- Actulizar periodicamente el medidor de agua de la casa/local. Este creara automaticamente un recibo con su respectivo valor
- Registrar el pago de los recibos. Y se le enviara un correo al usuario detallando el pago(Aun no esta habilidatado)
- Lista por, dia, mes o año los pagos y deudas de las facturas registradas en esa fecha.

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

# API
La documentacion de la API se puede encontrar en este [link](https://www.getpostman.com/collections/4de493acc29b6b17c7a3)

# Credenciales
## Usuario de pruebas para utilizar en la web.
Usuario = user.test
Contraseña = 1q2w3e4r5t

**PD:** Una vez concluida la pureba para la cual se realizo esta app. La Base De datos, se eliminara al llegar a los 10Mb.