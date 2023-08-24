import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, FLOAT
from sqlalchemy import types
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine



Base = declarative_base()
# engine = create_engine('sqlite:///reactions2.db', echo = True)

# Session = sessionmaker(bind=engine)

class Reactions(Base):
    __tablename__ = 'reactions'
    # Here we define columns for the table grid_info
    # Notice that each column is also a normal Python instance attribute.
    number = Column(Integer, primary_key=True)
    temperature = Column(Integer, nullable=False)
    treatment = Column(String(255), nullable=False)
    plate = Column(Integer, nullable=False)
    row = Column(String(40),nullable=False)
    column = Column(String(40), nullable=False)
    electrophile = Column(String(255), nullable=False)
    electrophile_conc = Column(types.Numeric, nullable=False)
    nucleophile = Column(String(255), nullable=False)
    nucleophile_conc = Column(types.Numeric, nullable=False)
    product = Column(String(255), nullable=False)
    catalyst = Column(String(255), nullable=False)
    catalyst_smiles = Column(String(255), nullable=False)
    catalyst_conc = Column(types.Numeric, nullable=False)
    base = Column(String(255), nullable=False)
    base_smiles = Column(String(255), nullable=False)
    base_conc = Column(types.Numeric, nullable=False)
    solvent = Column(String(255), nullable=False)
    analytical_method = Column(String(255), nullable=False)
    output_value = Column(types.Numeric, nullable=False)
    group = Column(String(255), nullable=False)
    reaction_name = Column(String(255), nullable=False)

# Base.metadata.create_all(engine)