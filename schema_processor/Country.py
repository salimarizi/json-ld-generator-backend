from schema.Country import CountrySchema
from calamus.schema import INCLUDE

class countryLD:
    def main(self, request):
        return CountrySchema.schema().load({
            "name": request.form['country_name']
        }, unknown = INCLUDE).dump()
