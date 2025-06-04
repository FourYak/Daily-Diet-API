from marshmallow import Schema, fields

class MealSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    date_time = fields.DateTime(required=True)
    is_in_diet = fields.Boolean(required=True)
    user_id = fields.Int(dump_only=True)