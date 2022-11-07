import mysql.connector

class Conexion():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 4000,
                user = 'root',
                password = 'Contadores2',
                db = 'ISPC_PF'

            )
        except mysql.connector.Error as descripcionError:
            print("Fallo en la conexión a la base de datos:",descripcionError)

#Función Inserción Simple

    def InsertarRegistro(self,tipo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL= "INSERT INTO genero (tipo) VALUES(%s)"
                datos= ([tipo])

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
                sentenciaSQL= "INSERT INTO clientes(dni,nombre,apellido,contraseña,fecha_nacimiento,email,direccion,ubicacion_id,genero_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"                
                cursor.executemany(sentenciaSQL,data)
                self.conexion.commit()
                self.conexion.close()

            except Exception as descripcionError:
                print("Error en la inserción múltiple de datos:", descripcionError)
   
#Función Select

    def BuscarRegistros(self,nombre):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL= f"SELECT * from clientes where nombre = '{nombre}'"
                cursor.execute(sentenciaSQL)
                resultadoSelect = cursor.fetchall()
                self.conexion.close()
                return resultadoSelect

            except Exception as descripcionError:
                print("Error en la lectura de datos:", descripcionError)

#Función Select con JOIN

    def BuscarRegistrosJOIN(self,tipo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL= f"""select clientes.DNI, clientes.nombre, clientes.apellido, genero.tipo from
                clientes INNER JOIN genero on clientes.genero_id = genero.id where genero.tipo='{tipo}'"""
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
                sentenciaSQL = f"DELETE from clientes where nombre = '{nombre}'"
                cursor.execute(sentenciaSQL)
                self.conexion.commit()                
                self.conexion.close()
            except Exception as descripcionError:
                print("Error en la eliminación de datos:",descripcionError)

#Creación de objeto

conexion1 = Conexion() 

#Consulta Inserción Simple

conexion1.InsertarRegistro("Femenino",30)

#Consulta Inserción Múltiple

data=[(411111,"Julian","Meneses","asdas","1997-06-19","asdas333","asdas",1,1),
(40333,"Julian","Meneses","asdas","1997-06-19","asdassdsd3","asdas222",1,1)]
conexion1.InsertarMultiplesRegistros(data)

#Consulta Select

print(conexion1.BuscarRegistros("Julian"))

#Consulta Select con JOIN

print(conexion1.BuscarRegistrosJOIN("masculino"))

#Consulta Update

conexion1.ActualizarRegistros("Alvaro","Julian")

#Consulta Delete

conexion1.EliminarRegistros("Alvaro")



