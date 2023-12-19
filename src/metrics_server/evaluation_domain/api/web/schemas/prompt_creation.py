from marshmallow import fields, Schema
from marshmallow import INCLUDE


class PromptCreationSchema(Schema):        
    prompt = fields.String(required=True)
    metrics = fields.List(fields.String(), required=True)
    llm_models = fields.String(required=True)
    class Meta:
        unknown = INCLUDE