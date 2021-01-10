# backend-test-enviame
## Instrucciones para ejecutado en la máquina local

### Requisitos
- Tener instalada la versión 3.9 de Python 
- Tener levantada un servidor local de SQL 
- Ejecutar el ambiente virtual de Python 
  
### Pasos para ejecutar ambiente virtual de Python
  - Navegar hasta el directorio donde se encuentra "my_venv" 
  - Ejecutar en la linea de comandos:
  ##### Para Linux:
     [server]$ source my_venv/Scripts/activate
  ##### Para Windows:
     ..\prueba> my_venv\Scripts\activate 
    
  Posterior a la ejecución del comando, se mostrará
  ##### Para Linux:
    (my_venv) [server]$ 
  ##### Para Windows:
    (my_venv) ..\prueba> 
    
## Ejecución Ejercicio 3:
- Navegar hasta el directorio donde se encuentra el ejecutable __Ejercicio_3.py__ 
- Ejecutar en la linea de comandos:
##### Para Linuxs o Windows:
	$ python Ejercicio_3.py 
	
Con esto se ejecutará el Script y mostrará los resultados por pantalla

#### Este Proceso se repite para los Ejercicios 5 y 6

## Ejecución Ejercicio 4:
- Navegar hasta el directorio donde se encuentra el ejecutable __Ejercicio_4.py__ 
- Ejecutar en la linea de comandos:
##### Para Linuxs o Windows:
	$ python Ejercicio_4.py 
	
Con esto se ejecutará el Script y en el directorio donde se encuentra el ejecutable __Ejercicio_4.py__, se creará un archivo __"data.txt"__ que contiene la respuesta del endpoint

## Ejecución Ejercicio 7
- Ejecutar la creación de Tablas e inserción de los datos a la Base de datos con los Script dados por la prueba
- Utilizando un cliente de Base de Datos como DBeaver
  1. Conectarse al servidor local 
  2. Abrir un Editor SQL para la ejecución de la query
  3. Pegar el contenido del archivo llamado __Script_Ejercicio_7.sql__
  4. Ejecutar el script
 
 O a través de la linea de comandos que provee el motpr de base de datos ejecytar el script apuntando a la base de datos que ya contiene los datos:.
 ##### Por ejemplo para mysql:
     shell> mysql db_name < Script_Ejercicio_7.sql
     
     
