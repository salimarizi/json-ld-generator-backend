from schema.Person import SimplePersonSchema
from calamus.schema import INCLUDE

class authorLD:
    def main(self, request):
        return SimplePersonSchema.schema().load({
            "name": request.form['author_name'],
            "url": request.form['author_url'],
            "email": request.form['author_email'],
            "telephone": request.form['author_phone']
        }, unknown = INCLUDE).dump()
