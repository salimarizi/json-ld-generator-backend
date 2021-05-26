from calamus import fields
from calamus.schema import JsonLDAnnotation

schema = fields.Namespace("http://schema.org/")

class ThingSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    description = fields.String(schema.description)

    class Meta:
        rdf_type = schema.Thing
