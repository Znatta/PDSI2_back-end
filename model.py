from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.sql import text
from database import Base

class Model_Mensagem(Base):
    __tablename__ = 'teste'

    id = Column(Integer, primary_key = True, nullable = False)
    titulo = Column(String, nullable = False)
    conteudo = Column(String, nullable = False)
    publicada = Column(Boolean, server_default = 'True' , nullable = False)
    created_at = Column(TIMESTAMP(timezone = True), server_default = text('now()'), nullable = False)

class Model_Webscraping(Base):
    __tablename__ = 'webscraping'

    id = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    menuNav = Column(String, nullable = False)
    link = Column(String, nullable = False)
    created_at = Column(TIMESTAMP(timezone = True), server_default = text('now()'), nullable = False)