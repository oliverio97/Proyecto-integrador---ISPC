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