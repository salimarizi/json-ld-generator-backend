from schema.LocalBusiness import LocalBusinessSchema, AutomotiveBusinessSchema, EntertainmentBusinessSchema, HealthAndBeautyBusinessSchema, HomeAndConstructionBusinessSchema, HVACBusinessSchema, LodgingBusinessSchema, RestaurantSchema
from calamus.schema import INCLUDE
from schema_processor.Address import addressLD
from schema_processor.ContactPoint import contactPointLD

class localBusinessLD:
    def main(self, request):
        address_dict = addressLD().main(request)
        contact_point_dict = contactPointLD().main(request)

        local_business = {
            "name": request.form['name'],
            "url": request.form['url'],
            "logo": request.form['logo'],
            "image": request.form['image'],
            "description": request.form['description'],
            "address": address_dict,
            "telephone": request.form['telephone'],
            "contactPoint": contact_point_dict,
            "openingHours": request.form['opening_hours'],
            "priceRange": request.form['price_range']
        }

        business_type = request.form['business_type']
        if business_type == "LocalBusiness":
            local_business_dict = LocalBusinessSchema.schema().load(local_business, unknown = INCLUDE).dump()
        if business_type == "AutomotiveBusiness":
            local_business_dict = AutomotiveBusinessSchema.schema().load(local_business, unknown = INCLUDE).dump()
        if business_type == "EntertainmentBusiness":
            local_business_dict = EntertainmentBusinessSchema.schema().load(local_business, unknown = INCLUDE).dump()
        if business_type == "HealthAndBeautyBusiness":
            local_business_dict = HealthAndBeautyBusinessSchema.schema().load(local_business, unknown = INCLUDE).dump()
        if business_type == "HomeAndConstruction":
            local_business_dict = HomeAndConstructionBusinessSchema.schema().load(local_business, unknown = INCLUDE).dump()
        if business_type == "HVACBusiness":
            local_business_dict = HVACBusinessSchema.schema().load(local_business, unknown = INCLUDE).dump()
        if business_type == "LodgingBusiness":
            local_business_dict = LodgingBusinessSchema.schema().load(local_business, unknown = INCLUDE).dump()
        if business_type == "Restaurant":
            local_business["servesCuisine"] = request.form['serves_cuisine']
            local_business_dict = RestaurantSchema.schema().load(local_business, unknown = INCLUDE).dump()

        return local_business_dict
