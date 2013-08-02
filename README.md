#Introducción a Django

Esto inicio como un evento que pensábamos para compartir con nuestros
compañeros de trabajo interesado en aprender acerca de _Django_ y _Python_. Nos
pareció muy buena idea crear un evento que les daría una introducción breve a
esta tecnología.

##Preparando el ambiente

Aunque yo en lo personal prefiero utilizar el gestor de paquetes del sistema
por acá les dejo una [guía](https://www.evernote.com/shard/s88/sh/76cdad6a-e3c0-4f73-aa8a-d2d703e01513/ca0d052b74ccc2e0227534c7b679a9d3) que crearon uno compañeros para instalar de forma
local lo que necesitan para trabajar.



Si ya tienen _Python_ instalado necesitaran primeramente instalar _pip_, y
configurar su ambiente virtual. Bien pueden trabajar sin esto; pero facilita
mucho al desarrollar mantener ambientes aislados con diferentes paquetes o
versiones de paquetes para distintos proyectos o grupos de proyectos.

		python-pip install virtualenv --user
 
 Esto instalara virtualenv en $HOME/.local/bin/

 Una herramienta muy útil y que facilita el lidiar con los ambientes virtuales
 de python es [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/index.html)

		python-pip install virtualenvwrapper --user

 Creamos el directorio donde se crearan los ambientes virtuales
 
		mkdir ~/virtualenv

 Agregamos estas lineas a nuestro _.bashrc_

		export WORKON_HOME=$HOME/virtualenv
		source $HOME/.local/bin/virtualenvwrapper.sh

Abrimos una nueva terminal o corremos esto en la actual

		source ~/.bashrc

Ya podemos crear nuestro primer ambiente virtual que acá llamaremos _djaus_ e
instalamos _Django_ usando el _pip_ del virtrualenv

		mkvirtualen virtualenv_name
		pip install django

En este repositorio he agregado un archivo _requirements.txt_ en el que podemos
definir todas las dependencias de nuestro proyecto e instalarlas todas con la
siguiente instrucción.

		pip install -r requirements.txt

##Iniciando nuestro proyecto

Ahora nos movemos a donde estará nuestro proyecto e iniciamos un nuevo proyecto
al que llamaremos _djaus_.

		cd /path/to/project_root
		django-admin.py startproject djaus

Ahora nuestra proyecto se ve más o menos como esto:
    .
	└── djaus
	    ├── __init__.py
	    ├── settings.py
	    ├── urls.py
	    └── wsgi.py

##Nuestra primer aplicación

Ahora crearemos nuestra primer aplicación. Intentaremos crear un url shorter
que ya verán no es algo muy complejo.

		cd djaus
		python manage.py startapp urlshorter

Que ha de parecerse un tanto a esto:
    urlshorter/
	├── __init__.py
	├── models.py
	├── tests.py
	└── views.py

Ahora crearemos nuestro primer modelo editando el archivo _models.py_ y
agregaremos este código:

    from django.db import models

    class URLShorter(models.Model):
        url = models.CharField(max_length=500, verbose_name="URL")
        shorter = models.CharField(max_length=8, verbose_name="Shorter")
    
        class Meta:
            verbose_name="URLSorter"
            verbose_name_plural="URLSorters"


