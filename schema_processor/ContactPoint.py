from schema.ContactPoint import ContactPointSchema
from calamus.schema import INCLUDE

class contactPointLD:
    def main(self, request):
        return ContactPointSchema.schema().load({
            "contactType": request.form['contact_type']
        }, unknown = INCLUDE).dump()
