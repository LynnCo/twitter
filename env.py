import os
import dotenv

dotenv.load_dotenv('.env')

ENV = {
    'API_KEY':      os.environ['API_KEY'],
    'API_SECRET':   os.environ['API_SECRET'],
    'ACCESS_TOKEN': os.environ['ACCESS_TOKEN'], # user context
    'TOKEN_SECRET': os.environ['TOKEN_SECRET'], # user context
    'ROOT':         os.environ['ROOT'],
    'PORT':         os.environ['PORT'],         # local only
    'SECRET_KEY':   os.environ['SECRET_KEY'],
}
