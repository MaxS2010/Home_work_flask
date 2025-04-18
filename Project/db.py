import flask_sqlalchemy as sqlalchemy
import flask_migrate as migrate
import os
from .settings import project

DATABASE = sqlalchemy.SQLAlchemy(app = project)

MIGRATE = migrate.Migrate(
    app= project,
    db= DATABASE,
    directory= os.path.abspath(os.path.join(__file__, "..", "migrations"))
)
