from schema.Location import LocationSchema
from calamus.schema import INCLUDE
from schema_processor.Address import addressLD

class locationLD:
    def main(self, request):
        address_dict = addressLD().main(request)

        return LocationSchema.schema().load({
            "name": request.form['venue_name'],
            "url": request.form['venue_url'],
            "address": address_dict
        }, unknown = INCLUDE).dump()
