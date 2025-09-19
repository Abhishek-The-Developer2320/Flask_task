from flask import Flask, render_template
from myproject.extensions import db, login_manager, migrate  # Use the single db instance from extensions

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "Hello"
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/flaskdb"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from myproject.users import bp as users_bp
    from myproject.projects import bp as projects_bp
    from myproject.tasks import bp as tasks_bp

    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(projects_bp, url_prefix="/projects")
    app.register_blueprint(tasks_bp, url_prefix="/tasks")

    @app.route("/")
    def home():
        return render_template("home.html")

    return app
