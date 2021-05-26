from calamus import fields
from calamus.schema import JsonLDAnnotation

schema = fields.Namespace("http://schema.org/")

class LocalBusinessSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    logo = fields.String(schema.logo)
    image = fields.String(schema.image)
    description = fields.String(schema.description)
    address = fields.Dict(schema.address)
    telephone = fields.String(schema.telephone)
    contactPoint = fields.Dict(schema.contactPoint)
    openingHours = fields.String(schema.openingHours)
    priceRange = fields.String(schema.priceRange)

    class Meta:
        rdf_type = schema.LocalBusiness

class AutomotiveBusinessSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    logo = fields.String(schema.logo)
    image = fields.String(schema.image)
    description = fields.String(schema.description)
    address = fields.Dict(schema.address)
    telephone = fields.String(schema.telephone)
    contactPoint = fields.Dict(schema.contactPoint)
    openingHours = fields.String(schema.openingHours)
    priceRange = fields.String(schema.priceRange)

    class Meta:
        rdf_type = schema.AutomotiveBusiness

class EntertainmentBusinessSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    logo = fields.String(schema.logo)
    image = fields.String(schema.image)
    description = fields.String(schema.description)
    address = fields.Dict(schema.address)
    telephone = fields.String(schema.telephone)
    contactPoint = fields.Dict(schema.contactPoint)
    openingHours = fields.String(schema.openingHours)
    priceRange = fields.String(schema.priceRange)

    class Meta:
        rdf_type = schema.EntertainmentBusiness

class HealthAndBeautyBusinessSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    logo = fields.String(schema.logo)
    image = fields.String(schema.image)
    description = fields.String(schema.description)
    address = fields.Dict(schema.address)
    telephone = fields.String(schema.telephone)
    contactPoint = fields.Dict(schema.contactPoint)
    openingHours = fields.String(schema.openingHours)
    priceRange = fields.String(schema.priceRange)

    class Meta:
        rdf_type = schema.HealthAndBeautyBusiness

class HomeAndConstructionBusinessSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    logo = fields.String(schema.logo)
    image = fields.String(schema.image)
    description = fields.String(schema.description)
    address = fields.Dict(schema.address)
    telephone = fields.String(schema.telephone)
    contactPoint = fields.Dict(schema.contactPoint)
    openingHours = fields.String(schema.openingHours)
    priceRange = fields.String(schema.priceRange)

    class Meta:
        rdf_type = schema.HomeAndConstructionBusiness

class HVACBusinessSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    logo = fields.String(schema.logo)
    image = fields.String(schema.image)
    description = fields.String(schema.description)
    address = fields.Dict(schema.address)
    telephone = fields.String(schema.telephone)
    contactPoint = fields.Dict(schema.contactPoint)
    openingHours = fields.String(schema.openingHours)
    priceRange = fields.String(schema.priceRange)

    class Meta:
        rdf_type = schema.HVACBusiness

class LodgingBusinessSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    logo = fields.String(schema.logo)
    image = fields.String(schema.image)
    description = fields.String(schema.description)
    address = fields.Dict(schema.address)
    telephone = fields.String(schema.telephone)
    contactPoint = fields.Dict(schema.contactPoint)
    openingHours = fields.String(schema.openingHours)
    priceRange = fields.String(schema.priceRange)

    class Meta:
        rdf_type = schema.LodgingBusiness

class RestaurantSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    logo = fields.String(schema.logo)
    image = fields.String(schema.image)
    description = fields.String(schema.description)
    address = fields.Dict(schema.address)
    telephone = fields.String(schema.telephone)
    contactPoint = fields.Dict(schema.contactPoint)
    openingHours = fields.String(schema.openingHours)
    priceRange = fields.String(schema.priceRange)
    servesCuisine = fields.String(schema.servesCuisine)

    class Meta:
        rdf_type = schema.Restaurant
