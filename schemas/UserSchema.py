from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=8, max=30))
    password = fields.Str(required=True, load_only=True, validate=validate.Length(min=6))
    