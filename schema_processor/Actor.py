from schema.Person import SimplePersonSchema
from calamus.schema import INCLUDE

class actorLD:
    def main(self, request):
        return SimplePersonSchema.schema().load({
            "name": request.form['actor_name'],
            "url": request.form['actor_url'],
            "email": request.form['actor_email'],
            "telephone": request.form['actor_phone']
        }, unknown = INCLUDE).dump()
