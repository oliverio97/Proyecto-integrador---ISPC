create database ispc_pf;

use ispc_pf;

create table IF NOT EXISTS cursos(
id INT PRIMARY KEY AUTO_INCREMENT,
precio INT,
autor char(40),
descripcion char(255),
fecha_inicio date,
fecha_finalizacion date,
fecha_insercion timestamp DEFAULT CURRENT_TIMESTAMP,
fecha_actualizacion timestamp,
estado char(10) DEFAULT "A"
);

create table IF NOT EXISTS orientacion(
id INT PRIMARY KEY AUTO_INCREMENT,
nombre char(40),
fecha_insercion timestamp DEFAULT CURRENT_TIMESTAMP,
fecha_actualizacion timestamp,
estado char(10) DEFAULT "A"
);

create table IF NOT EXISTS especialidad(
id INT PRIMARY KEY AUTO_INCREMENT,
nombre char(40),
fecha_insercion timestamp DEFAULT CURRENT_TIMESTAMP,
fecha_actualizacion timestamp,
estado char(10) DEFAULT "A"
);

create table IF NOT EXISTS genero(
id INT PRIMARY KEY AUTO_INCREMENT,
tipo char(10),
fecha_insercion timestamp DEFAULT CURRENT_TIMESTAMP,
fecha_actualizacion timestamp,
estado char(10) DEFAULT "A"
);

create table IF NOT EXISTS libros(
id INT PRIMARY KEY AUTO_INCREMENT,
precio INT,
nombre char(50),
autor char(50),
editorial char(30),
sinopsis char(255),
paginas INT,
fecha_insercion timestamp DEFAULT CURRENT_TIMESTAMP,
fecha_actualizacion timestamp,
estado char(10) DEFAULT "A"
);

create table IF NOT EXISTS modalidad(
id INT PRIMARY KEY AUTO_INCREMENT,
tipo char(10),
fecha_insercion timestamp DEFAULT CURRENT_TIMESTAMP,
fecha_actualizacion timestamp,
estado char(10) DEFAULT "A"
);

create table IF NOT EXISTS obra_social(
id INT PRIMARY KEY AUTO_INCREMENT,
nombre char(10),
fecha_insercion timestamp DEFAULT CURRENT_TIMESTAMP,
fecha_actualizacion timestamp,
estado char(10) DEFAULT "A"
);

create table IF NOT EXISTS ubicacion(
id INT PRIMARY KEY AUTO_INCREMENT,
ciudad char(30),
provincia char(30),
fecha_insercion timestamp DEFAULT CURRENT_TIMESTAMP,
fecha_actualizacion timestamp,
estado char(10) DEFAULT "A"
);
create table IF NOT EXISTS clientes(
DNI INT PRIMARY KEY,
nombre char(40),
apellido char(40),
contraseña char(100),
fecha_nacimiento date,
email char(100) unique,
direccion char(80),
fecha_insercion timestamp DEFAULT CURRENT_TIMESTAMP,
fecha_actualizacion timestamp,
estado char(10) DEFAULT "A",
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
fecha_insercion timestamp DEFAULT CURRENT_TIMESTAMP,
fecha_actualizacion timestamp,
estado char(10) DEFAULT "A",
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
fecha_insercion timestamp DEFAULT CURRENT_TIMESTAMP,
fecha_actualizacion timestamp,
estado char(10) DEFAULT "A",
clientes_dni INT,
cursos_id INT,
foreign key (clientes_dni) references Clientes (dni),
foreign key (cursos_id) references Cursos (id)
);

create table IF NOT EXISTS clientes_psicologos(
id INT PRIMARY KEY AUTO_INCREMENT,
valoracion char(100),
fecha_insercion timestamp DEFAULT CURRENT_TIMESTAMP,
fecha_actualizacion timestamp,
estado char(10) DEFAULT "A",
psicologos_dni INT,
clientes_dni INT,
foreign key (psicologos_dni) references Psicologos (dni),
foreign key (clientes_dni) references Clientes (dni)
);

create table IF NOT EXISTS libros_clientes(
id INT PRIMARY KEY AUTO_INCREMENT,
clientes_dni INT,
libros_id INT,
fecha_insercion timestamp DEFAULT CURRENT_TIMESTAMP,
fecha_actualizacion timestamp,
estado char(10) DEFAULT "A",
foreign key (clientes_dni) references Clientes (dni),
foreign key (libros_id) references Libros (id)
);

create table IF NOT EXISTS psicologos_obra_social(
id INT PRIMARY KEY AUTO_INCREMENT,
psicologos_dni INT,
obra_social_id INT,
fecha_insercion timestamp DEFAULT CURRENT_TIMESTAMP,
fecha_actualizacion timestamp,
estado char(10) DEFAULT "A",
foreign key (psicologos_dni) references Psicologos (dni),
foreign key (obra_social_id) references Obra_social (id)
);

create table If NOT EXISTS administradores(
DNI INT PRIMARY KEY AUTO_INCREMENT,
email char(100) unique,
contraseña CHAR(40),
fecha_insercion timestamp DEFAULT CURRENT_TIMESTAMP,
fecha_actualizacion timestamp,
estado char(10) DEFAULT "A"
)








  
