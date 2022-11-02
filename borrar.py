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