# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Faecher(db.Model):
    __tablename__ = 'faecher'

    Faecher_Id = db.Column(db.Integer, primary_key=True, unique=True)
    Bzeichnung = db.Column(db.String(128))
    Farbe = db.Column(db.String(64))
    description = db.Column(db.Text)
    Lehrraum = db.Column(db.Integer)



class Lehrer(db.Model):
    __tablename__ = 'lehrer'

    Lehrer_Id = db.Column(db.Integer, primary_key=True, unique=True)
    Vorname = db.Column(db.String(128))
    Nachname = db.Column(db.String(128))
    Faecher_Unterrichtet = db.Column(db.Text)
    Anzahl_Klassen = db.Column(db.Integer)



class LehrerFach(db.Model):
    __tablename__ = 'lehrer_fach'

    Lehrer_Fach = db.Column(db.Integer, primary_key=True, unique=True)
    Lehrer_Id = db.Column(db.ForeignKey('lehrer.Lehrer_Id'), index=True)
    Faecher_Id = db.Column(db.ForeignKey('faecher.Faecher_Id'), index=True)

    faecher = db.relationship('Faecher', primaryjoin='LehrerFach.Faecher_Id == Faecher.Faecher_Id', backref='lehrer_faches')
    lehrer = db.relationship('Lehrer', primaryjoin='LehrerFach.Lehrer_Id == Lehrer.Lehrer_Id', backref='lehrer_faches')



class School(db.Model):
    __tablename__ = 'school'

    school_Id = db.Column(db.Integer, primary_key=True, unique=True)
    Adresse = db.Column(db.String(255))
    Anzahl_Schüler = db.Column(db.Integer)
    Name_Schule = db.Column(db.String(255))
    Schulart = db.Column(db.String(255))



class SchuleLehrer(db.Model):
    __tablename__ = 'schule_lehrer'

    Schule_Lehrer_Id = db.Column(db.Integer, primary_key=True, unique=True)
    school_Id = db.Column(db.ForeignKey('school.school_Id'), index=True)
    Lehrer_Id = db.Column(db.ForeignKey('lehrer.Lehrer_Id'), index=True)

    lehrer = db.relationship('Lehrer', primaryjoin='SchuleLehrer.Lehrer_Id == Lehrer.Lehrer_Id', backref='schule_lehrers')
    school = db.relationship('School', primaryjoin='SchuleLehrer.school_Id == School.school_Id', backref='schule_lehrers')



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
