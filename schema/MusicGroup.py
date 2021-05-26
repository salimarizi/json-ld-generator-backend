from calamus import fields
from calamus.schema import JsonLDAnnotation

schema = fields.Namespace("http://schema.org/")

class MusicGroupSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    genre = fields.String(schema.genre)

    class Meta:
        rdf_type = schema.MusicGroup
