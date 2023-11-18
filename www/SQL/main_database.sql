-- Run it in MySQL Workbench

CREATE DATABASE T_VALL;

USE T_VALL;

CREATE TABLE Professor(
    id_professor INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    senha VARCHAR(50) NOT NULL,
    PRIMARY KEY(id_professor)
);

CREATE TABLE Aluno(
    id_aluno INT NOT NULL AUTO_INCREMENT, -- Pode ser usado como RA
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    senha VARCHAR(50) NOT NULL,
    PRIMARY KEY(id_aluno)
);

CREATE TABLE Disciplina(
    id_disciplina INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    PRIMARY KEY(id_disciplina)
);

CREATE TABLE Turma(
    id_turma INT NOT NULL AUTO_INCREMENT,
    id_disciplina INT NOT NULL,
    id_professor INT NOT NULL,
    PRIMARY KEY(id_turma),
    FOREIGN KEY(id_disciplina) REFERENCES Disciplina(id_disciplina),
    FOREIGN KEY(id_professor) REFERENCES Professor(id_professor)
);

CREATE TABLE Aluno_Turma(
    id_aluno INT NOT NULL,
    id_turma INT NOT NULL,
    PRIMARY KEY(id_aluno, id_turma),
    FOREIGN KEY(id_aluno) REFERENCES Aluno(id_aluno),
    FOREIGN KEY(id_turma) REFERENCES Turma(id_turma)
);

CREATE TABLE Aula(
    id_aula INT NOT NULL AUTO_INCREMENT,
    id_turma INT NOT NULL,
    id_professor INT NOT NULL,
    data DATE NOT NULL,
    PRIMARY KEY(id_aula),
    FOREIGN KEY(id_turma) REFERENCES Turma(id_turma)
    FOREIGN KEY(id_professor) REFERENCES Professor(id_professor)
);

CREATE TABLE Frequencia(
    id_aluno INT NOT NULL,
    id_aula INT NOT NULL,
    presenca BOOLEAN NOT NULL,
    PRIMARY KEY(id_aluno, id_aula),
    FOREIGN KEY(id_aluno) REFERENCES Aluno(id_aluno),
    FOREIGN KEY(id_aula) REFERENCES Aula(id_aula)
);

CREATE TABLE Nota(
    id_aluno INT NOT NULL,
    id_turma INT NOT NULL,
    nota INT NOT NULL,
    PRIMARY KEY(id_aluno, id_turma),
    FOREIGN KEY(id_aluno) REFERENCES Aluno(id_aluno),
    FOREIGN KEY(id_turma) REFERENCES Turma(id_turma)
);

