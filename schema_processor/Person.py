from schema.Person import PersonSchema
from calamus.schema import INCLUDE
from schema_processor.Address import addressLD

class personLD:
    def main(self, request):
        address_dict = addressLD().main(request)

        return PersonSchema.schema().load({
            "_id": request.form['id'],
            "name": request.form['name'],
            "jobTitle": request.form['job_title'],
            "url": request.form['url'],
            "address": address_dict,
            "email": request.form['email'],
            "telephone": request.form['phone'],
            "birthDate": request.form['birth_date']
        }, unknown = INCLUDE).dump()
