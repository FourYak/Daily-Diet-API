from flask import request, jsonify
from flask_jwt_extended import create_access_token
from models.User import User
from schemas.UserSchema import UserSchema
from database import db

user_schema = UserSchema()

def init_auth_routes(app):
    # CREATE route - to register a new user
    @app.route('/auth/register', methods=['POST'])
    def register():
        data = request.get_json()
        errors = user_schema.validate(data)
        if errors:
            return jsonify({"errors": errors}), 400
        
        if User.query.filter_by(username=data['username']).first():
            return jsonify({"error": "Username already exists"}), 400
        
        user = User(username=data['username'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "User registered successfully"}), 201
    
# READ route - to login a user    
    @app.route('/login', methods=['POST'])
    def login():
        data = request.json
        user = User.query.filter_by(username=data['username']).first()

        if not user or not user.check_password(data['password']):
            return jsonify({"error": "Invalid credentials"}), 401
        
        access_token = create_access_token(identity=user.id)
        return jsonify({"access_token": access_token}), 200

# POST route - to logout a user
    @app.route('/logout', methods=['POST'])
    def logout():
        # In JWT, logout is typically handled on the client side by deleting the token
        return jsonify({"message": "User logged out successfully"}), 200
                