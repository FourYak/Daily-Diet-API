from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.Meal import Meal
from schemas.MealSchema import MealSchema
from datetime import datetime
from database import db

# Initialize the meal schema
meal_schema = MealSchema()
meals_schema = MealSchema(many=True)

# Initialize meal routes
def init_meal_routes(app):
    # READ route - to get all meals for the current user
    @app.route('/meals', methods=['GET'])
    @jwt_required()
    def get_meals():
        current_user_id = get_jwt_identity()
        meals = Meal.query.filter_by(user_id=current_user_id).all()
        return jsonify(meals_schema.dump(meals))
    
# READ route - to get a specific meal by ID for the current user  
    @app.route('/meals/<int:id>', methods=['GET'])
    @jwt_required()
    def get_meal(id):
        current_user_id = get_jwt_identity()
        meal = Meal.query.filter_by(id=id, user_id=current_user_id).first_or_404()
        return jsonify(meal_schema.dump(meal))
    
# CREATE route - to add a new meal   
    @app.route('/meals', methods=['POST'])
    @jwt_required()
    def add_meal():
        current_user_id = get_jwt_identity()
        data = request.get_json()
        errors = meal_schema.validate(data)

        if errors:
            return jsonify({"errors": errors}), 400
        
        meal = Meal(
            name=data['name'],
            description=data.get('description'),
            date_time=datetime.fromisoformat(data['date_time']),
            is_in_diet=data['is_in_diet'],
            user_id=current_user_id
        )
        db.session.add(meal)
        db.session.commit()
        return jsonify(meal_schema.dump(meal)), 201
    
# UPDATE route - to update a meal    
    @app.route('/meals/<int:id>', methods=['PUT'])
    @jwt_required()
    def update_meal(id):
        current_user_id = get_jwt_identity()
        meal = Meal.query.filter_by(id=id, user_id = current_user_id).first_or_404()
        data = request.json
        errors = meal_schema.validate(data)
        if errors:
            return jsonify({"errors": errors}), 400
        
        meal.name = data['name']
        meal.description = data.get('description')
        meal.date_time = datetime.fromisoformat(data['date_time'])
        meal.is_in_diet = data['is_in_diet']
        db.session.commit()
        return jsonify(meal_schema.dump(meal))

# DELETE route - for deleting a meal
    @app.route('/meals/<int:id>', methods=['DELETE'])
    @jwt_required()
    def delete_meal(id):
        current_user_id = get_jwt_identity()
        meal = Meal.query.filter_by(id=id, user_id = current_user_id).first_or_404()
        db.session.delete(meal)
        db.session.commit()
        return jsonify({"message": "Meal deleted successfully"}), 200


        


        
