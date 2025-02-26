import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://neonDB_owner:YOUR_PASSWORD@ep-hidden-leaf-a25em0f.eu-central-1.aws.neon.tech/mop_alias_thorn_845685?sslmode=require"


db = SQLAlchemy(app)

from taskmanager import routes  # noqa