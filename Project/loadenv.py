import dotenv
import os

PATH = os.path.abspath(os.path.join(__file__, ".."))
def load_env():
    env_path = os.path.abspath(os.path.join(__file__, "..", "..", ".env"))
    if os.path.exists(env_path):
        dotenv.load_dotenv(env_path)
    if not os.path.exists(os.path.join(PATH, 'migrations')):
        os.system(os.environ["FLASK_APP"])
    os.system(os.environ["FLASK_MIGRATE"])

