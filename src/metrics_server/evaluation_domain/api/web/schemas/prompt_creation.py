from marshmallow import fields, Schema

class PromptCreationSchema(Schema):        
    Context = fields.String(required=True)
    Question = fields.String(required=True)
    Type = fields.String(required=True)
    LlmModel = fields.String(required=True)