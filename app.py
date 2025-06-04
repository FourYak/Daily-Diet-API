from flask import Flask
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os
from database import db
from routes.auth_routes import init_auth_routes
from routes.meal_routes import init_meal_routes

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///daily_diet.db'
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

init_auth_routes(app)  # Register authentication routes
init_meal_routes(app)  # Register meal management routes
# Registration of routes

# Initialize database
db.init_app(app)
jwt = JWTManager(app)

# Create the database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)