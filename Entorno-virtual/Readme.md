# Entorno vitual

### Creacion de un entorno Virtual

En este repositorio crearemos un entorno virtual el cual nos ayudara a:

* Entorno Aislado 
* Evitar Conflictos
* Instalacion de paquetes especificamente en el entorno y no enla computadora

## Instalacion
### Instalacion de las librerias
~~~
> pip install virtualenv
~~~
### Creacion del entorno

Te dirijes a la carpeta de tu proyecto e ingresas el siguiene comando: 

~~~
> python -m venv Nombre-Entorno
~~~

puedes verificar si se creo con el comando 

~~~
dir nombre/
~~~

Para activar el entorno virtual usaremos:

~~~
Nombre\Scripts\activate
~~~

Ahora escribiremos el siguiente comando para para ver una lista de los paquetes instalados

~~~
pip freeze
~~~

Cada vez que termines de trabajr en el proyecto debes Desactivarlo con:

~~~
deactivate
~~~



