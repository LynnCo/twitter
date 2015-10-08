import os
import dotenv

dotenv.load_dotenv('.env')

ENV = {
    'API_KEY':      os.environ['API_KEY'],
    'API_SECRET':   os.environ['API_SECRET'],
    'ROOT':         os.environ['ROOT'],
    'PORT':         os.environ['PORT'],
    'SECRET_KEY':   os.environ['SECRET_KEY'],
}
