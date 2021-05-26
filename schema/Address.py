from calamus import fields
from calamus.schema import JsonLDAnnotation

schema = fields.Namespace("http://schema.org/")

class AddressSchema(metaclass = JsonLDAnnotation):
    streetAddress = fields.String(schema.streetAddress)
    addressLocality = fields.String(schema.addressLocality)
    postOfficeBoxNumber = fields.String(schema.postOfficeBoxNumber)
    addressRegion = fields.String(schema.addressRegion)
    postalCode = fields.String(schema.postalCode)
    addressCountry = fields.String(schema.addressCountry)

    class Meta:
        rdf_type = schema.PostalAddress
