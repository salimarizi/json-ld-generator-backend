from calamus import fields
from calamus.schema import JsonLDAnnotation

schema = fields.Namespace("http://schema.org/")

class PersonSchema(metaclass = JsonLDAnnotation):
    _id = fields.Id()
    name = fields.String(schema.name)
    jobTitle = fields.String(schema.jobTitle)
    url = fields.String(schema.url)
    address = fields.Dict(schema.address)
    email = fields.String(schema.email)
    telephone = fields.String(schema.telephone)
    birthDate = fields.String(schema.birthDate)

    class Meta:
        rdf_type = schema.Person

class SimplePersonSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    email = fields.String(schema.email)
    telephone = fields.String(schema.telephone)

    class Meta:
        rdf_type = schema.Person
