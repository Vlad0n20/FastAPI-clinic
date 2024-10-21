from decouple import config

class Config:
    DEBUG = config('DEBUG', default=False, cast=bool)
    TESTING = config('TESTING', default=False, cast=bool)
    CSRF_ENABLED = config('CSRF_ENABLED', default=True, cast=bool)
    SECRET_KEY = config('SECRET_KEY', default='SECRET')
    JWT_TOKEN_SECRET = config('JWT_TOKEN_SECRET', default='JWT_TOKEN_SECRET')
    RESET_PASSWORD_TOKEN_SECRET = config('RESET_PASSWORD_TOKEN_SECRET', default='RESET_PASSWORD_TOKEN_SECRET')
    VERIFICATION_TOKEN_SECRET = config('VERIFICATION_TOKEN_SECRET', default='VERIFICATION_TOKEN_SECRET')

    DB_URI = config('DB_URI', default='sqlite+aiosqlite:///db.sqlite') # if use default value you will need to install aiosqlite




