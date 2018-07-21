import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Spot(Base):
    __tablename__ = 'spots'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    lat = Column(String(10))
    lng = Column(String(10))
    history = relationship("History")

    def __init__(self, name='', lat=0.0, lng=0.0):
        self.name = name
        self.lat = '%s' % lat
        self.lng = '%s' % lng


class History(Base):
    __tablename__ = 'history'
    id = Column(Integer, primary_key=True)
    occupied = Column(Boolean)
    working = Column(Boolean)
    time = Column(DateTime, default=datetime.datetime.utcnow)
    spot_id = Column(Integer, ForeignKey('spots.id'))
