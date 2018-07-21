import json

from sqlalchemy import Column, Integer, String

from database import Base


class Spot(Base):
    __tablename__ = 'spots'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    lat = Column(String(10))
    lng = Column(String(10))

    def __init__(self, name='', lat=0.0, lng=0.0):
        self.name = name
        self.lat = '%s' % lat
        self.lng = '%s' % lng


