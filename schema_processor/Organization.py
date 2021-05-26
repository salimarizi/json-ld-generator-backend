from schema.Organization import OrganizationSchema, CorporationSchema, EducationalOrganizationSchema, GovernmentOrganizationSchema, LocalBusinessSchema, NGOSchema, PerformingGroupSchema, SportsTeamSchema
from calamus.schema import INCLUDE
from schema_processor.Address import addressLD

class organizationLD:
    def main(self, request):
        address_dict = addressLD().main(request)

        organization = {
            "name": request.form['name'],
            "url": request.form['url'],
            "logo": request.form['logo'],
            "image": request.form['image'],
            "description": request.form['description'],
            "address": address_dict,
            "email": request.form['email'],
            "telephone": request.form['telephone']
        }

        organization_type = request.form['organization_type']

        if organization_type == "Organization":
            organization_dict = OrganizationSchema.schema().load(organization, unknown = INCLUDE).dump()
        if organization_type == "Corporation":
            organization_dict = CorporationSchema.schema().load(organization, unknown = INCLUDE).dump()
        if organization_type == "EducationalOrganization":
            organization_dict = EducationalOrganizationSchema.schema().load(organization, unknown = INCLUDE).dump()
        if organization_type == "GovernmentOrganization":
            organization_dict = GovernmentOrganizationSchema.schema().load(organization, unknown = INCLUDE).dump()
        if organization_type == "LocalBusiness":
            organization_dict = LocalBusinessSchema.schema().load(organization, unknown = INCLUDE).dump()
        if organization_type == "NGO":
            organization_dict = NGOSchema.schema().load(organization, unknown = INCLUDE).dump()
        if organization_type == "PerformingGroup":
            organization_dict = PerformingGroupSchema.schema().load(organization, unknown = INCLUDE).dump()
        if organization_type == "SportsTeam":
            organization_dict = SportsTeamSchema.schema().load(organization, unknown = INCLUDE).dump()

        return organization_dict
