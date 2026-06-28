import os

class Config:
    SECRET_KEY = "skilltrack_secret_key"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/skilltrack"

    SQLALCHEMY_TRACK_MODIFICATIONS = False