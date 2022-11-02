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