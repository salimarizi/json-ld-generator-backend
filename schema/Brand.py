from calamus import fields
from calamus.schema import JsonLDAnnotation

schema = fields.Namespace("http://schema.org/")

class BrandSchema(metaclass = JsonLDAnnotation):
    logo = fields.String(schema.logo)
    slogan = fields.String(schema.slogan)
    description = fields.String(schema.description)
    alternateName = fields.String(schema.alternateName)

    class Meta:
        rdf_type = schema.Brand

class BrandWithRatingSchema(metaclass = JsonLDAnnotation):
    logo = fields.String(schema.logo)
    slogan = fields.String(schema.slogan)
    description = fields.String(schema.description)
    alternateName = fields.String(schema.alternateName)
    aggregateRating = fields.Dict(schema.aggregateRating)

    class Meta:
        rdf_type = schema.Brand
