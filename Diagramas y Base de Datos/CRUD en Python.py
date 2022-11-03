import mysql.connector

class Conexion():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '123654',
                db = 'ispc_pf'

            )
        except mysql.connector.Error as descripcionError:
            print("Fallo en la conexión a la base de datos:",descripcionError)

#Función Inserción Simple

    def InsertarRegistro(self,tipo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL= "INSERT INTO genero (id, tipo, estado) VALUES (%s,%s,%s)"
                datos= (tipo)

                cursor.execute(sentenciaSQL,datos)
                self.conexion.commit()
                self.conexion.close()

            except Exception as descripcionError:
                print("Error en la inserción simple de datos:",descripcionError)

#Función Inserción Múltiple

    def InsertarMultiplesRegistros(self,data):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL= "INSERT INTO clientes (DNI,nombre,apellido,contraseña,fecha_nacimiento,email,direccion,estado,ubicacion_id,genero_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"                
                cursor.executemany(sentenciaSQL,data)
                self.conexion.commit()
                self.conexion.close()

            except Exception as descripcionError:
                print("Error en la inserción múltiple de datos:", descripcionError)
   
#Función Select
    def BuscarRegistros(self, nombre):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                #sentenciaSQL= f"SELECT * from clientes where nombre = '{nombre}'"
                sentenciaSQL = f"select clientes.DNI AS DNI_clientes, clientes.nombre, clientes.apellido, clientes.estado, genero.id AS id_genero, genero.tipo, genero.estado FROM clientes LEFT JOIN genero ON clientes.nombre = genero_id;"
                
                cursor.execute(sentenciaSQL)
                resultadoSelect = cursor.fetchall()
                self.conexion.close()
                return resultadoSelect

            except Exception as descripcionError:
                print("Error en la lectura de datos:", descripcionError)

#Función Update

    def ActualizarRegistros(self,nombreNuevo,nombreActual):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL= f"UPDATE clientes set nombre = '{nombreNuevo}' where nombre = '{nombreActual}'"
                cursor.execute(sentenciaSQL)  
                self.conexion.commit()                           
                self.conexion.close()                             

            except Exception as descripcionError:
                print("Error en la actualización de datos:", descripcionError)        

#Función Delete

    def EliminarRegistros(self,nombre):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = f"DELETE from genero where id = '{nombre}'"
                cursor.execute(sentenciaSQL)
                self.conexion.commit()                
                self.conexion.close()
            except Exception as descripcionError:
                print("Error en la eliminación de datos:",descripcionError)

#Creación de objeto

conexion1 = Conexion() 

Consulta Inserción Simple
datos = (3, 'Femenino', 'A')
conexion1.InsertarRegistro(datos)

#Consulta Inserción Múltiple

data=[(654321,'Ariel',"Ojeda","abc","1995-10-21","ariel@gmail.com","Misiones s/n",'A',1,1),
(123456,"Walter","Gomez","123","1997-05-30","walter@gmail.com","Venezuela s/n",'A',2,2)]
conexion1.InsertarMultiplesRegistros(data)

#Consulta Select

print(conexion1.BuscarRegistros("Ariel"))

#Consulta Update

conexion1.ActualizarRegistros("Juan","Walter")

#Consulta Delete

conexion1.EliminarRegistros(3)



