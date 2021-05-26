from calamus import fields
from calamus.schema import JsonLDAnnotation

schema = fields.Namespace("http://schema.org/")

class CountrySchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)

    class Meta:
        rdf_type = schema.Country
