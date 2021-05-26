from calamus import fields
from calamus.schema import JsonLDAnnotation

schema = fields.Namespace("http://schema.org/")

class NutritionSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    calories = fields.String(schema.calories)

    class Meta:
        rdf_type = schema.NutritionInformation
