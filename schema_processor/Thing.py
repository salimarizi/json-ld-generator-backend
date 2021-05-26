from schema.Thing import ThingSchema
from calamus.schema import INCLUDE

class thingLD:
    def main(self, request, brand = ""):
        return ThingSchema.schema().load({
            "name": request.form['item_name'] if brand == "" else brand['alternateName'],
            "url": request.form['item_url'] if brand == "" else brand['logo'],
            "description": request.form['item_description'] if brand == "" else brand['description']
        }, unknown = INCLUDE).dump()
