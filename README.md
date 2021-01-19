# Invera ToDo-List Challenge (Python/Django Jr-SSr)

Instrucciones:
-De no tener, descargar python...

    https://www.python.org/downloads/

-Clonar este repositorio para tener una copia local...

    https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository 

-Crear un entorno virtual...

    Abrir la consola, luego con 'cd' indicamos la ruta donde crearemos el entorno (ej: cd C:\Users\User_Name\Desktop\InveraToDoApp\todo-challenge)
    Una vez en el lugar, crear el entorno con los comandos: python -m venv myvenv
    'myvenv' es el nombre que le otorgamos al entorno.
    Ahora activarlo: 
        
        Colocarnos dentro de la carpeta Scripts (ej: cd C:\Users\User_Name\Desktop\InveraToDoApp\todo-challenge\myvenv\Scripts)
        En la consola ejecutar: activate

-Instalar los requerimientos...

    Dentro de la carpeta del projecto clonado (ej: cd C:\Users\User_Name\Desktop\InveraToDoApp\todo-challenge), ejecutar en la consola (con el entorno activado): pip install -r requirements.txt

-Migraciones...

    Dentro de la carpeta del projecto clonado, ejecutar en la consola (con el entorno activado): python manage.py migrate

-Listo...

    Ejecutar en la consola (con el entorno activado): python manage.py runserver


Para visualizar la página, abrir un navegador y colocar en la barra de navegación: http://127.0.0.1:8000/

https://github.com/spedreira/eon-rad/blob/main/Imagenes/HomeToDo.jpg?raw=true

-Para realizar los tests...

    Ejecutar en la consola (con el entorno activado): python manage.py test

