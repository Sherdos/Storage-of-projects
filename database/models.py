from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqldb import Base
from sqlalchemy import create_engine


def get_session():
    engine = create_engine("sqlite:///database.db", echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        return session

class Object():

    def __init__(self, obj):
        self.obj = obj

    def create(self, **kwargs):
        with get_session() as session:
            obj = self.obj(**kwargs)
            session.add(obj)
            session.commit()
            return obj

    def all(self):
        with get_session() as session:
            objects = session.query(self.obj).all()
            return objects

    def filter(self, *args, **kwargs):
        with get_session() as session:
            objects = session.query(self.obj).filter_by(*args, **kwargs).all()
            return objects
    
    def save(self, obj):
        session = get_session()
        session.add(obj)
        session.commit()

class Model():
    @classmethod
    @property
    def object(cls):
        return Object(cls)


class Project(Base,Model):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def __str__(self):
        return f'{self.name}'

    
    
# Base.metadata.create_all(engine)
project = Project.object.all()
print(project)
# project.name = 'Updated Project'
# Project.object.save(project)




