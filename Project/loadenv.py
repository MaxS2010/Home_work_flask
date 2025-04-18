import dotenv
import os

PATH = os.path.abspath(os.path.join(__file__, ".."))
def load_env():
    commands = {
        "FLASK_APP": "flask --app Project db init",
        "FLASK_MIGRATE": "flask --app Project db migrate",
        "FLASK_UPGRADE": "flask --app Project db upgrade"
    }
    env_path = os.path.abspath(os.path.join(__file__, "..", "..", ".env"))
    if not os.path.exists(env_path):
        with open(env_path, "w") as env_file:
            for key, value in commands.items():
                env_file.write(f"{key}={value}\n")

    
    dotenv.load_dotenv(env_path)
    if not os.path.exists(os.path.join(PATH, 'migrations')):
        os.system(os.environ["FLASK_APP"])
    os.system(os.environ["FLASK_MIGRATE"])
    os.system(os.environ["FLASK_UPGRADE"])

