CREATE TABLE IF NOT EXISTS Trabajador (
  id_trabajador TEXT NOT NULL PRIMARY KEY,
  nombre        TEXT NOT NULL,
  apellido      TEXT NOT NULL
);

INSERT INTO Trabajador (id_trabajador, nombre, apellido) VALUES (?,?,?);

CREATE TABLE IF NOT EXISTS Directivo (
  id_directivo TEXT     NOT NULL PRIMARY KEY,
  metas        INTEGER  NOT NULL,
  dietas       INTEGER  NOT NULL,
  base         INTEGER  NOT NULL,
               FOREIGN KEY (id_directivo) REFERENCES Trabajador (id_trabajador)
);

INSERT INTO Directivo (id_directivo, metas, diestas, base) VALUES (?,?,?,?)

CREATE TABLE IF NOT EXISTS Secretaria (
  id_secretaria    TEXT    NOT NULL PRIMARY KEY,
  horas_trabajadas INTEGER NOT NULL,
  incentivos       INTEGER NOT NULL,
                   FOREIGN KEY (id_secretaria) REFERENCES Trabajador (id_trabajador)
);

INSERT INTO Secretaria (id_secretaria, horas_trabajadas, incentivos) VALUES (?,?,?)

CREATE TABLE IF NOT EXISTS Conserje (
  id_conserje       TEXT    NOT NULL PRIMARY KEY,
  horas_trabajadas  INTEGER NOT NULL,
                    FOREIGN KEY (id_conserje) REFERENCES Trabajador (id_trabajador)
);

INSERT INTO Conserje (id_conserje, horas_trabajadas) VALUES (?,?)


