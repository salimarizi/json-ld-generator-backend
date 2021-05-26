from schema.Review import ReviewSchema
from calamus.schema import INCLUDE
from schema_processor.Author import authorLD
from schema_processor.Rating import ratingLD
from schema_processor.Thing import thingLD

class reviewLD:
    def main(self, request, item_reviewed_dict = ""):
        if item_reviewed_dict == "":
            item_reviewed_dict = thingLD().main(request)

        rating_dict = ratingLD().main(request)
        author_dict = authorLD().main(request)

        return ReviewSchema.schema().load({
            "itemReviewed": item_reviewed_dict,
            "about": request.form['about'],
            "reviewAspect": request.form['review_aspect'],
            "reviewBody": request.form['review_body'],
            "reviewRating": rating_dict,
            "author": author_dict
        }, unknown = INCLUDE).dump()
