from sqlalchemy import Column, Integer, String

from db import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Integer, nullable=False)
    type = Column(String, nullable=False)
