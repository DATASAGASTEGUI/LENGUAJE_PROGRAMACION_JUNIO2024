CREATE TABLE Usuario (
   id_usuario     INTEGER PRIMARY KEY AUTOINCREMENT,
   nombre_usuario TEXT    NOT NULL UNIQUE,  
   contrasena     TEXT    NOT NULL,
   rol            TEXT    NOT NULL CHECK (rol IN ('Administrador','Cajero','Almacén'))
);