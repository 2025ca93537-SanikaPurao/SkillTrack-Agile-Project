from flask import Flask, render_template
from flask_login import LoginManager

from config import Config
from models import db
from models.user import User
from models.profile import Profile
from models.skill import Skill
from routes.skill import skill

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from routes.auth import auth
from routes.profile import profile
from routes.project import project
from routes.dashboard import dashboard
from models.project import Project

app.register_blueprint(auth)
app.register_blueprint(profile)
app.register_blueprint(project)
app.register_blueprint(dashboard)
app.register_blueprint(skill)

@app.route("/")
def home():
    return render_template("index.html")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)