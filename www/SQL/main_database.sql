-- Run it in MySQL Workbench
drop database T_VALL;
CREATE DATABASE T_VALL;

USE T_VALL;
CREATE table Instituicao(
    id_instituicao INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    PRIMARY KEY(id_instituicao)
);

insert into Instituicao(nome) values('UNICAMP');
insert into Instituicao(nome) values('USP');
insert into Instituicao(nome) values('UNESP');
insert into Instituicao(nome) values('UNIFESP');
insert into Instituicao(nome) values('UFSCAR');
insert into Instituicao(nome) values('UFABC');
insert into Instituicao(nome) values('UNIFEI');
insert into Instituicao(nome) values('UNICID');
insert into Instituicao(nome) values('UNIP');
insert into Instituicao(nome) values('UNISAL');
insert into Instituicao(nome) values('UNISANTOS');
insert into Instituicao(nome) values('UNIMONTE');
insert into Instituicao(nome) values('UNIMES');
insert into Instituicao(nome) values('UNIBAN');
insert into Instituicao(nome) values('UNIB');
insert into Instituicao(nome) values('UNAERP');
insert into Instituicao(nome) values('UNIARA');
insert into Instituicao(nome) values('UNIARARAS');
insert into Instituicao(nome) values('UNIARA');
insert into Instituicao(nome) values('UNIARARAS');
insert into Instituicao(nome) values('UNIARA');
insert into Instituicao(nome) values('UNIARARAS');
insert into Instituicao(nome) values('UNIARA');
insert into Instituicao(nome) values('UNIARARAS');
insert into Instituicao(nome) values('UNIARA');
insert into Instituicao(nome) values('UNIARARAS');
insert into Instituicao(nome) values('UNIARA');
insert into Instituicao(nome) values('UNIARARAS');
insert into Instituicao(nome) values('UNIARA');
insert into Instituicao(nome) values('UNIARARAS');
insert into Instituicao(nome) values('UNIARA');
insert into Instituicao(nome) values('UNIARARAS');
insert into Instituicao(nome) values('UNIARA');
insert into Instituicao(nome) values('UNIARARAS');

CREATE TABLE Professor(
    id_professor INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    senha VARCHAR(50) NOT NULL,
    CPF VARCHAR(11) NOT NULL,
    CEP VARCHAR(8) NOT NULL,
    Instituicao INT NOT NULL,
    Telefone VARCHAR(11) NOT NULL,
    PRIMARY KEY(id_professor),
    FOREIGN KEY(Instituicao) REFERENCES Instituicao(id_instituicao)
);

CREATE TABLE Aluno(
    id_aluno INT NOT NULL AUTO_INCREMENT, -- Pode ser usado como RA
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    senha VARCHAR(50) NOT NULL,
    CPF VARCHAR(11) NOT NULL,
    CEP VARCHAR(8) NOT NULL,
    Instituicao INT NOT NULL,
    Telefone VARCHAR(11) NOT NULL,
    PRIMARY KEY(id_aluno),
    FOREIGN KEY(Instituicao) REFERENCES Instituicao(id_instituicao)
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
    FOREIGN KEY(id_turma) REFERENCES Turma(id_turma),
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

