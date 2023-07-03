from sqlalchemy import Column, Integer, String
from database.sqldatabase import Base, Model


class Project(Base,Model):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    

    # def __str__(self):
    #     return f'{self.name}'

    
    




