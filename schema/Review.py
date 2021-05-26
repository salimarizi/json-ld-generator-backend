from calamus import fields
from calamus.schema import JsonLDAnnotation

schema = fields.Namespace("http://schema.org/")

class ReviewSchema(metaclass = JsonLDAnnotation):
    itemReviewed = fields.Dict(schema.itemReviewed)
    about = fields.String(schema.about)
    reviewAspect = fields.String(schema.reviewAspect)
    reviewBody = fields.String(schema.reviewBody)
    reviewRating = fields.Dict(schema.reviewRating)
    author = fields.Dict(schema.author)

    class Meta:
        rdf_type = schema.Review
