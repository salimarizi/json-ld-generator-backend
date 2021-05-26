from schema.Product import ProductSchema, ProductWithReviewSchema
from calamus.schema import INCLUDE
from schema_processor.Audience import audienceLD
from schema_processor.Brand import brandLD
from schema_processor.Review import reviewLD
from schema_processor.Offer import offerLD

class productLD:
    def main(self, request):
        brand_dict = brandLD().main(request)
        audience_dict = audienceLD().main(request)
        offer_dict = offerLD().main(request)

        product = {
            "brand": brand_dict,
            "name": request.form['name'],
            "image": request.form['image'],
            "description": request.form['description'],
            "productID": request.form['product_id'],
            "url": request.form['url'],
            "audience": audience_dict,
            "offers": offer_dict
        }
        product_dict = ProductSchema.schema().load(product, unknown = INCLUDE).dump()

        if "rating_value" in request.form:
            product["review"] = reviewLD().main(request, product_dict)
            product_dict = ProductWithReview.schema().load(product, unknown = INCLUDE).dump()

        return product_dict
