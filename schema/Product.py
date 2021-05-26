from calamus import fields
from calamus.schema import JsonLDAnnotation

schema = fields.Namespace("http://schema.org/")

class ProductSchema(metaclass = JsonLDAnnotation):
    brand = fields.Dict(schema.brand)
    name = fields.String(schema.name)
    image = fields.String(schema.image)
    description = fields.String(schema.description)
    productID = fields.String(schema.productID)
    url = fields.String(schema.url)
    audience = fields.Dict(schema.audience)
    offers = fields.Dict(schema.offers)

    class Meta:
        rdf_type = schema.Product

class ProductWithReviewSchema(metaclass = JsonLDAnnotation):
    brand = fields.Dict(schema.brand)
    name = fields.String(schema.name)
    image = fields.String(schema.image)
    description = fields.String(schema.description)
    productID = fields.String(schema.productID)
    url = fields.String(schema.url)
    audience = fields.Dict(schema.audience)
    offer = fields.Dict(schema.offers)
    review = fields.Dict(schema.review)

    class Meta:
        rdf_type = schema.Product
