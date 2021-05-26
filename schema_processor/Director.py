from schema.Person import SimplePersonSchema
from calamus.schema import INCLUDE

class directorLD:
    def main(self, request):
        return SimplePersonSchema.schema().load({
            "name": request.form['director_name'],
            "url": request.form['director_url'],
            "email": request.form['director_email'],
            "telephone": request.form['director_phone']
        }, unknown = INCLUDE).dump()
