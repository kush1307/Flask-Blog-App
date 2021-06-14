import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY_FLASK')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    GOOGLE_CLIENT_ID = "505904973836-o3g1u9ggvhlu14l0mgsevve9cd61lfmk.apps.googleusercontent.com"
    GOOGLE_CLIENT_SECRET = "0ca7CGGQn2HGw9Yge6FPw83p"

