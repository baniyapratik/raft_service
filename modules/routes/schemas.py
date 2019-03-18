from marshmallow import fields, Schema


class NeighborSchema(Schema):
    host = fields.Str()
    port = fields.Integer()