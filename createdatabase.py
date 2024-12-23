from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the database URL and create the engine
DATABASE_URL = 'sqlite:///database.db'
engine = create_engine(DATABASE_URL)

# Define metadata and Base
metadata = MetaData(bind=engine)
Base = declarative_base(bind=engine)

# Define the User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

# Create tables
Base.metadata.create_all()

# Start local session
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Add sample users to the database
sample_users = [
    {"id": 1, "username": "Tommy", "password": "password1"},
    {"id": 2, "username": "Jimmy", "password": "password2"},
]

for user_data in sample_users:
    user = User(id= user_data["id"],username=user_data["username"], password=user_data["password"])
    session.add(user)

session.commit()
session.close()

print("Sample users added to the database.")