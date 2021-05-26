from schema.Rating import RatingSchema, AggregateRatingSchema, AggregateRatingWithItemSchema
from calamus.schema import INCLUDE
from schema_processor.Thing import thingLD

class ratingLD:
    def main(self, request, type = "", brand = ""):
        rating = {
            "ratingValue": request.form['rating_value'],
            "ratingExplanation": request.form['explanation'],
            "bestRating": request.form['best_rating'],
            "worstRating": request.form['worst_rating'],
        }

        if brand != "":
            thing_dict = thingLD().main(request, brand)
            rating["itemReviewed"] = thing_dict

        if type == "":
            rating_dict = RatingSchema.schema().load(rating, unknown = INCLUDE).dump()
        else:
            rating["ratingCount"] = request.form['rating_count'] if "rating_count" in request.form else ""
            rating_dict = AggregateRatingWithItemSchema.schema().load(rating, unknown = INCLUDE).dump() if (brand != "") else AggregateRatingSchema.schema().load(rating, unknown = INCLUDE).dump()

        return rating_dict
