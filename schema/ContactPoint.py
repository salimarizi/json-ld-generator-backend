from calamus import fields
from calamus.schema import JsonLDAnnotation

schema = fields.Namespace("http://schema.org/")

class ContactPointSchema(metaclass = JsonLDAnnotation):
    contactType = fields.String(schema.contactType)

    class Meta:
        rdf_type = schema.ContactPoint
