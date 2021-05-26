from schema.Address import AddressSchema
from calamus.schema import INCLUDE

class addressLD:
    def main(self, request):
        return AddressSchema.schema().load({
            "streetAddress": request.form['address'],
            "addressLocality": request.form['city'],
            "postOfficeBoxNumber": request.form['po_box'],
            "addressRegion": request.form['region'],
            "postalCode": request.form['postal_code'],
            "addressCountry": request.form['country']
        }, unknown = INCLUDE).dump()
