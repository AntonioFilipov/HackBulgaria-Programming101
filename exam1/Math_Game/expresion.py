from sqlalchemy import Column, Integer, String, Float
from connect import Base


class Expression(Base):
    __tablename__ = "expression"
    id = Column(Integer, primary_key=True)
    left_operand = Column(Integer)
    right_operand = Column(Integer)
    sign = Column(String)
    result = Column(String)


    def __str__(self):
        return "{} {} {} = ?".format(int(self.left_operand), self.sign, int(self.right_operand))

    def __repr__(self):
        return self.__str__()
