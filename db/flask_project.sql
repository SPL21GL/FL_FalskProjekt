create database if not exists Schule;
use Schule;

create table if not exists school (
	school_Id int auto_increment unique key primary key,
    Adresse varchar(255),
    Anzahl_Schueler int,
    Name_Schule varchar(255),
    Schulart varchar(255)
);
	

create table if not exists Lehrer (
	Lehrer_Id int auto_increment unique key primary key,
    Vorname varchar(128),
    Nachname varchar(128),
    Faecher_Unterrichtet text,
    Anzahl_Klassen int
    
);

create table if not exists Schule_Lehrer (
	Schule_Lehrer_Id int auto_increment unique key primary key,
    school_Id int,
    Lehrer_Id int
);


create table if not exists Lehrer_Fach (
	Lehrer_Fach int auto_increment unique key primary key,
    Lehrer_Id int,
    Faecher_Id int
);

create table if not exists Faecher (
	Faecher_Id int auto_increment unique key primary key,
    Bzeichnung varchar(128),
    Farbe varchar(64),
    description text,
    Lehrraum int
);

alter table Lehrer_Fach
ADD CONSTRAINT `LehrerForeignKey` FOREIGN KEY (`Lehrer_Id`) REFERENCES `Lehrer` (`Lehrer_Id`),
ADD Constraint `FaecherForeignKey` FOREIGN KEY (`Faecher_Id`) REFERENCES `Faecher` (`Faecher_Id`);

alter table Schule_Lehrer
ADD CONSTRAINT `schoolForeignKey` FOREIGN KEY (`school_Id`) REFERENCES `school` (`school_Id`),
ADD CONSTRAINT `Lehrer_ForeignKey` FOREIGN KEY (`Lehrer_Id`) REFERENCES `Lehrer` (`Lehrer_Id`)