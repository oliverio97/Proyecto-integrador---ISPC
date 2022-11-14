 # CONEXION CON LA BASE DE DATOS
 
import mysql.connector


conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="123654", 
                                  port= 3306,
                                  database="profesionales")
cursor1=conexion1.cursor()
cursor1.execute("show tables")
for tabla in cursor1:
    print(tabla)
conexion1.close()    

# LISTAR PSICOLOGO

import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  port= 3306,
                                  passwd="123654", 
                                  database="profesionales")
cursor1=conexion1.cursor()
cursor1.execute("select id, Nombre, Apellido from psicologos")
for fila in cursor1:
    print(fila)
conexion1.close()    

# ACTUALIZAR PSICOLOGO

import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root",
                                  port=3306, 
                                  password="123654", 
                                  database="profesionales")

#CREAR PSICOLOGO

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="123654",
                                  port= 3306, 
                                  database="profesionales")
cursor1=conexion1.cursor()
sql="insert into psicologos(Nombre, Apellido) values (%s,%s)"
datos=("Pedro", "Almaraz")
cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close()   

# BORRAR PSICOLOGO

import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root",
                                  password="123654",
                                  port= 3306,  
                                  database="profesionales")
cursor1=conexion1.cursor()
cursor1.execute("delete from psicologos where id=2")
for fila in cursor1:
    print(fila)
conexion1.close()   


