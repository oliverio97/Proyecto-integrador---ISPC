# CONEXION CON LA BASE DE DATOS

import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="1234", 
                                  port= 3307,
                                  database="clientes")
cursor1=conexion1.cursor()
cursor1.execute("show tables")
for tabla in cursor1:
    print(tabla)
conexion1.close()    

#  ********CRUD************

# LISTAR PACIENTES

import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  port= 3307,
                                  passwd="1234", 
                                  database="clientes")
cursor1=conexion1.cursor()
cursor1.execute("select id, nombre, apellido from pacientes")
for fila in cursor1:
    print(fila)
conexion1.close()    

#CREAR PACIENTES

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="1234",
                                  port= 3307, 
                                  database="clientes")
cursor1=conexion1.cursor()
sql="insert into pacientes(nombre, apellido) values (%s,%s)"
datos=("rodrigo", "alvarez")
cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close()   

# ACTUALIZAR PACIENTES

import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root",
                                  port=3307, 
                                  password="1234", 
                                  database="clientes")

cursor1=conexion1.cursor()
cursor1.execute("update pacientes set nombre='Noelia' where id=7")
conexion1.commit()
for fila in cursor1:
    print(fila)
conexion1.close()   


# BORRAR PACIENTES

import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  
                                  password="1234", 
                                  database="clientes")
cursor1=conexion1.cursor()
cursor1.execute("delete from pacientes where id=7")
for fila in cursor1:
    print(fila)
conexion1.close()   





