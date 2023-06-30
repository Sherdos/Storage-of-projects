from sqlalchemy.ext.declarative import declarative_base
from database.settings import DATABASE_NAME
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

def get_session():
    engine = create_engine(f"sqlite:///{DATABASE_NAME}", echo=True)
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