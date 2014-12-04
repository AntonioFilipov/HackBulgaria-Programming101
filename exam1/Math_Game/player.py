from sqlalchemy import Column, Integer, String, Float
from connect import Base


class Player(Base):
    __tablename__ = "player"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    high_score = Column(Integer)

    def __str__(self):
        return "{} with {} scores".format(self.name, self.high_score)

    def __repr__(self):
        return self.__str__()
