from schema.Person import SimplePersonSchema
from calamus.schema import INCLUDE

class publisherLD:
    def main(self, request):
        return SimplePersonSchema.schema().load({
            "name": request.form['publisher_name'],
            "url": request.form['publisher_url'],
            "email": request.form['publisher_email'],
            "telephone": request.form['publisher_phone']
        }, unknown = INCLUDE).dump()
