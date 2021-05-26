from schema.Brand import BrandSchema, BrandWithRatingSchema
from calamus.schema import INCLUDE
from schema_processor.Rating import ratingLD

class brandLD:
    def main(self, request):
        brand = {
            "logo": request.form['brand_logo'],
            "slogan": request.form['brand_slogan'],
            "description": request.form['brand_description'],
            "alternateName": request.form['brand_alternate_name']
        }

        brand_dict = BrandSchema.schema().load(brand, unknown = INCLUDE).dump()

        if "rating_value" in request.form:
            brand["aggregateRating"] = ratingLD().main(request, "aggregate", brand)
            brand_dict = BrandWithRatingSchema.schema().load(brand, unknown = INCLUDE).dump()

        return brand_dict
