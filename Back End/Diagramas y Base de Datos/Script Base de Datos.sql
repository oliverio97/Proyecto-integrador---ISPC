create database ispc_pf;

use ispc_pf;

create table IF NOT EXISTS cursos(
id INT PRIMARY KEY AUTO_INCREMENT,
fecha_inicio date,
fecha_finalizacion date,
fecha_insercion datetime,
fecha_actualizacion datetime,
estado varchar(10)
);

create table IF NOT EXISTS clientes(
DNI INT PRIMARY KEY,
nombre char(40),
apellido char(40),
contraseña char(100),
fecha_nacimiento date,
email char(100) unique,
direccion char(80),
fecha_insercion datetime,
fecha_actualizacion datetime,
estado char(10),
ubicacion_id INT,
genero_id INT,
foreign key (ubicacion_id) references Ubicacion (id),
foreign key (genero_id) references Genero (id)
);

create table IF NOT EXISTS psicologos(
DNI INT PRIMARY KEY,
nombre char(40),
apellido char(40),
contraseña char(100),
fecha_nacimiento date,
email char(100) unique,
direccion_consultorio char(80),
telefono char(50),
matricula INT,
fecha_insercion datetime,
fecha_actualizacion datetime,
estado char(10),
ubicacion_id INT,
genero_id INT,
modalidad_id INT,
especialidad_id INT,
orientacion_id INT,
foreign key (orientacion_id) references Orientacion (id),
foreign key (ubicacion_id) references Ubicacion (id),
foreign key (genero_id) references Genero (id),
foreign key (modalidad_id) references Modalidad (id),
foreign key (especialidad_id) references Especialidad (id)
);

create table IF NOT EXISTS clientes_cursos(
id INT PRIMARY KEY AUTO_INCREMENT,
fecha_insercion datetime,
fecha_actualizacion datetime,
estado char(10),
clientes_dni INT,
charlas_talleres_id INT,
foreign key (clientes_dni) references Clientes (dni),
foreign key (cursos_id) references Cursos (id)
);

create table IF NOT EXISTS clientes_psicologos(
id INT PRIMARY KEY AUTO_INCREMENT,
honorarios INT,
fecha_insercion datetime,
fecha_actualizacion datetime,
estado char(10),
psicologos_dni INT,
clientes_dni INT,
foreign key (psicologos_dni) references Psicologos (dni),
foreign key (clientes_dni) references Clientes (dni)
);

create table IF NOT EXISTS orientacion(
id INT PRIMARY KEY AUTO_INCREMENT,
nombre char(40),
fecha_insercion datetime,
fecha_actualizacion datetime,
estado char(10)
);

create table IF NOT EXISTS especialidad(
id INT PRIMARY KEY AUTO_INCREMENT,
nombre char(40),
fecha_insercion datetime,
fecha_actualizacion datetime,
estado char(10)
);

create table IF NOT EXISTS genero(
id INT PRIMARY KEY AUTO_INCREMENT,
tipo char(10),
fecha_insercion datetime,
fecha_actualizacion datetime,
estado char(10)
);

create table IF NOT EXISTS libros(
id INT PRIMARY KEY AUTO_INCREMENT,
nombre char(50),
autor char(50),
fecha_insercion datetime,
fecha_actualizacion datetime,
estado char(10)
);

create table IF NOT EXISTS libros_clientes(
id INT PRIMARY KEY AUTO_INCREMENT,
fecha_insercion datetime,
fecha_actualizacion datetime,
estado char(10),
clientes_dni INT,
libros_id INT,
foreign key (clientes_dni) references Clientes (dni),
foreign key (libros_id) references Libros (id)
);

create table IF NOT EXISTS modalidad(
id INT PRIMARY KEY AUTO_INCREMENT,
tipo char(10),
fecha_insercion datetime,
fecha_actualizacion datetime,
estado char(10)
);

create table IF NOT EXISTS obra_social(
id INT PRIMARY KEY AUTO_INCREMENT,
nombre char(10),
fecha_insercion datetime,
fecha_actualizacion datetime,
estado char(10)
);

create table IF NOT EXISTS psicologos_obra_social(
id INT PRIMARY KEY AUTO_INCREMENT,
fecha_insercion datetime,
fecha_actualizacion datetime,
estado char(10),
psicologos_dni INT,
obra_social_id INT,
foreign key (psicologos_dni) references Psicologos (dni),
foreign key (obra_social_id) references Obra_social (id)
);

create table IF NOT EXISTS ubicacion(
id INT PRIMARY KEY AUTO_INCREMENT,
ciudad char(30),
provincia char(30),
fecha_insercion datetime,
fecha_actualizacion datetime,
estado char(10)
)






  
