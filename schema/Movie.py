from calamus import fields
from calamus.schema import JsonLDAnnotation

schema = fields.Namespace("http://schema.org/")

class MovieSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    about = fields.String(schema.about)
    actor = fields.Dict(schema.actor)
    director = fields.Dict(schema.director)
    countryOfOrigin = fields.Dict(schema.countryOfOrigin)
    musicBy = fields.Dict(schema.musicBy)
    duration = fields.String(schema.duration)
    productionCompany = fields.Dict(schema.productionCompany)
    subtitleLanguage = fields.String(schema.subtitleLanguage)
    titleEIDR = fields.String(schema.titleEIDR)
    trailer = fields.Dict(schema.trailer)
    image = fields.Dict(schema.image)
    dateCreated = fields.String(schema.dateCreated)

    class Meta:
        rdf_type = schema.Movie
