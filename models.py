from database import Base
from sqlalchemy import Column, String, Integer

class Usuario(Base):
    __tablename__ = 'TUsuario'
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(25))
    sobrenome = Column(String(25)) 
    email = Column(String(150), unique=True)
    login = Column(String(20), unique=True)
    senha = Column(String(10))

    def __init__(self, nome, sobrenome, email, login, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.login = login
        self.senha = senha