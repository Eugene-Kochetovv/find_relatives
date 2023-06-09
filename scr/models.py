

from sqlalchemy import Column, String, ForeignKey, Boolean, Date, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, declarative_base, Mapped

import uuid



Base = declarative_base()

class Link(Base):
    __tablename__ = "link"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'))
    relatives_id = Column(UUID(as_uuid=True), ForeignKey('relatives.id'))


class User(Base):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    username = Column(String(128), nullable=False)
    email = Column(String(64), unique=True, nullable=False)
    hashed_password = Column(String(128), nullable=False, index=True)
    active = Column(Boolean(), nullable=False, default=False)
    relatives = relationship("Relatives", secondary="link", back_populates='users')


class Relatives(Base):
    __tablename__ = "relatives"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    last_name = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    surname = Column(String(128), nullable=True)
    birth_data = Column(Date(), nullable=True)
    death_data = Column(Date(), nullable=True)
    sity = Column(String(128), nullable=False)
    users = relationship("User", secondary="link", back_populates='relatives')
