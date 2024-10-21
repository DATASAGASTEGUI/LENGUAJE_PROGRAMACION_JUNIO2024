DROP TABLE IF EXISTS Persona;

CREATE TABLE IF NOT EXISTS Persona (
    id_persona INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nombre     TEXT    NOT NULL,
    apellido   TEXT    NOT NULL,
    sexo       CHAR(1) NOT NULL
);

INSERT INTO Persona(nombre,apellido,sexo) VALUES('Luis','Roncal','H');

SELECT * FROM Persona;