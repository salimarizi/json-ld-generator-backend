from calamus import fields
from calamus.schema import JsonLDAnnotation

schema = fields.Namespace("http://schema.org/")

class ImageObjectSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    caption = fields.String(schema.caption)

    class Meta:
        rdf_type = schema.ImageObject
