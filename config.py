from dotenv import load_dotenv
import os
load_dotenv()

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql://admin:Mani$2004@infosys.c7uwqq6e2cfz.ap-south-1.rds.amazonaws.com:3306/infosys'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    GOOGLE_OAUTH_CLIENT_ID = '541441980761-tmhlqs9pt59a43vicec0lc9o7j09rtsl.apps.googleusercontent.com'
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
    GOOGLE_OAUTH_REDIRECT_URI = 'http://127.0.0.1:5000/google/login'
    
