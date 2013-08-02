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

Ahora nuestra proyecto se ve más o menos como esto
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

Crearemos nuestro primer modelo editando el archivo _models.py_ y
agregaremos este código:

    from django.db import models

    class URLShorter(models.Model):
        url = models.CharField(max_length=500, verbose_name="URL")
        shorter = models.CharField(max_length=8, verbose_name="Shorter")
    
        class Meta:
            verbose_name="URLSorter"
            verbose_name_plural="URLSorters"


##Corriendo muestra aplicación

Agregamos nuestra aplicacion a las _INSTALLED_APPS_ en el archivo _djaus/settings.py_ agregando esta linea

        'urlshorter',

Tambien debemos establecer los datos de nuestra conexiòn a base de datos 

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/path/to/my_database.sqlite',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }

He usado SQLite pero uds pueden usar la base de datos que mas se ajuste a sus requerimientos.
Ahora syncronizamos nuestra base de datos.

    python manage.py syncdb

Habilitemos la administración y registremos nuestro modelo en el admin.
Modifiquemos nuestro archivo _djaus/urls.py_ y descomentamos unas lineas, y quedara mas o menoas así:

    from django.conf.urls import patterns, include, url

    # Uncomment the next two lines to enable the admin:
    from django.contrib import admin
    admin.autodiscover()

    urlpatterns = patterns('',
        # Examples:
        # url(r'^$', 'djaus.views.home', name='home'),
        # url(r'^djaus/', include('djaus.foo.urls')),

        # Uncomment the admin/doc line below to enable admin documentation:
        # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

        # Uncomment the next line to enable the admin:
        url(r'^admin/', include(admin.site.urls)),
    )

Creara las tablas necesarias y pedira los datos para crear un super usuario. 
Ahora ya podemos ejecutar nuestra aplicación, para lo que usaremos el servidor de pruebas
que viene integrado con django.

    python manage.py runserver

Con esto ya deberiamos tener corriendo nuestro servidor de pruebas, accedamos a la administración de Django.
En nuestro navegador favorito vallamos ahora a la siguiente direccón web [servidor de pruebas](http://localhost:8000/admin):

    http://localhost:8000/admin

Ingresemos el usuario y clave que hemos configurado previamente.

##Otros temas
