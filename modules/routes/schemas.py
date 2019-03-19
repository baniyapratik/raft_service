from marshmallow import fields, Schema


class NeighborSchema(Schema):
    host = fields.Str()
    port = fields.Integer()


class NeighborUpdateSchema(Schema):
    nodeid = fields.Integer()
    isAlive = fields.Str(required=True, allow_none=False)
    node_address = fields.Nested(NeighborSchema, required=True)

class NeighborAddSchema(Schema):
    neighbors = fields.Dict(fields.Nested(NeighborUpdateSchema), required=True)