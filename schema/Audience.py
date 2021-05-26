from calamus import fields
from calamus.schema import JsonLDAnnotation

schema = fields.Namespace("http://schema.org/")

class AudienceSchema(metaclass = JsonLDAnnotation):
    audienceType = fields.String(schema.audienceType)

    class Meta:
        rdf_type = schema.Audience
