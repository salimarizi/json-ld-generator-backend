from calamus import fields
from calamus.schema import JsonLDAnnotation

schema = fields.Namespace("http://schema.org/")

class LocationSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    address = fields.Dict(schema.address)

    class Meta:
        rdf_type = schema.Place
