from schema.Offer import OfferSchema
from calamus.schema import INCLUDE

class offerLD:
    def main(self, request):
        return OfferSchema.schema().load({
            "description": request.form['offer_description'],
            "url": request.form['offer_url'],
            "price": request.form['offer_price'],
            "priceCurrency": request.form['offer_price_currency'],
            "availability": "http://schema.org/" + request.form['offer_availability'],
            "validFrom": request.form['offer_valid_from']
        }, unknown = INCLUDE).dump()
