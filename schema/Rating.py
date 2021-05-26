from calamus import fields
from calamus.schema import JsonLDAnnotation

schema = fields.Namespace("http://schema.org/")

class RatingSchema(metaclass = JsonLDAnnotation):
    ratingValue = fields.String(schema.ratingValue)
    ratingExplanation = fields.String(schema.ratingExplanation)
    bestRating = fields.String(schema.bestRating)
    worstRating = fields.String(schema.worstRating)

    class Meta:
        rdf_type = schema.Rating

class AggregateRatingSchema(metaclass = JsonLDAnnotation):
    ratingValue = fields.String(schema.ratingValue)
    ratingExplanation = fields.String(schema.ratingExplanation)
    bestRating = fields.String(schema.bestRating)
    worstRating = fields.String(schema.worstRating)
    ratingCount = fields.String(schema.ratingCount)

    class Meta:
        rdf_type = schema.AggregateRating

class AggregateRatingWithItemSchema(metaclass = JsonLDAnnotation):
    ratingValue = fields.String(schema.ratingValue)
    ratingExplanation = fields.String(schema.ratingExplanation)
    bestRating = fields.String(schema.bestRating)
    worstRating = fields.String(schema.worstRating)
    itemReviewed = fields.Dict(schema.itemReviewed)
    ratingCount = fields.String(schema.ratingCount)

    class Meta:
        rdf_type = schema.AggregateRating
