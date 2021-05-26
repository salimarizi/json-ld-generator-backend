from calamus import fields
from calamus.schema import JsonLDAnnotation

schema = fields.Namespace("http://schema.org/")

class OfferSchema(metaclass = JsonLDAnnotation):
    description = fields.String(schema.description)
    url = fields.String(schema.url)
    price = fields.String(schema.price)
    priceCurrency = fields.String(schema.priceCurrency)
    availability = fields.String(schema.availability)
    validFrom = fields.String(schema.validFrom)

    class Meta:
        rdf_type = schema.Offer
