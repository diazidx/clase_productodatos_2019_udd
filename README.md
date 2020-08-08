
# Laboratorio: MODELO DE DEEP LEARNING PARA DETERMINAR LA EDAD DE UNA PERSONA

Proyecto 1 para el ramo de Productos de Datos del Magister en Data Science de la Universidad del Desarrollo. 
Elaborado por: Israel Diaz G.

La aplicación se encuentra disponible en https://5e18ebada7ab.ngrok.io/

## Recursos utilizados

- El código en este repositorio se ha ejecutado en una maquina virtual de GCP con 8 nucleos, si la maquina utiliza menos de 8 nuclos podría presentar problemas con la librería OpenCV. 
- Librerías: opencv-contrib-python, numpy, flask, dlib.
- ngrok tunnel.

## Instalación de librerías necesarias

### Numpy
```
pip install numpy
```

### dlib 
Para linux, se requieren las siguientes librerias del sistema:
```
sudo apt-get update
sudo apt-get install build-essential cmake
sudo apt-get install libopenblas-dev liblapack-dev 
sudo apt-get install libx11-dev libgtk-3-dev
sudo apt-get install python python-dev python-pip
sudo apt-get install python3 python3-dev python3-pip
```
Luego se puede instalar dlib
```
pip install dlib
```

### OpenCV
```
pip install opencv-contrib-python
```

### Flask
```
pip install Flask
```

### ngrok
Ngrok es una aplicación para crear un tunnel que permita acceder a la url localhost de una maquina. Para realizar el setup de esta app se recomienda seguir las instrucciones en la documentación de https://ngrok.com/

### Se recomienda el uso de un ambiente dedicado. Ver: https://medium.com/@m.monroyc22/configurar-entorno-virtual-python-a860e820aace


## Construcción del Modelo de Deep Learning

- Los detalles del modelo utilizado se explica en detalle en el siguiente articulo web: https://www.pyimagesearch.com/2020/04/13/opencv-age-detection-with-deep-learning/.


## Levantar 

Para levantar el servidor flask, se debe establecer la app y el ambiente:

En linux:
```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

En otra terminal, se debe ejecutar el tunnel ngrok
```
./ngrok http 5000
```
Este comando devuelve una url a la que se puede acceder para tener acceso a la aplicación.

## ENJOY!

## Créditos

- El modelo se ha desarrollado utilizando la metodología presentada en PyImageSearch.com

