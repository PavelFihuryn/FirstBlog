class Configuration(object):
    DEBUG = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:My-N7w_And.5ecure-P@s5w0rd@localhost/test1'

    SECRET_KEY = 'very secret'

    ### Security

    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'bcrypt'
