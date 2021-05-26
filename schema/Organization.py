from calamus import fields
from calamus.schema import JsonLDAnnotation

schema = fields.Namespace("http://schema.org/")

class OrganizationSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    logo = fields.String(schema.logo)
    image = fields.String(schema.image)
    description = fields.String(schema.description)
    address = fields.Dict(schema.address)
    email = fields.String(schema.email)
    telephone = fields.String(schema.telephone)

    class Meta:
        rdf_type = schema.Organization

class CorporationSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    logo = fields.String(schema.logo)
    image = fields.String(schema.image)
    description = fields.String(schema.description)
    address = fields.Dict(schema.address)
    email = fields.String(schema.email)
    telephone = fields.String(schema.telephone)

    class Meta:
        rdf_type = schema.Corporation

class EducationalOrganizationSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    logo = fields.String(schema.logo)
    image = fields.String(schema.image)
    description = fields.String(schema.description)
    address = fields.Dict(schema.address)
    email = fields.String(schema.email)
    telephone = fields.String(schema.telephone)

    class Meta:
        rdf_type = schema.EducationalOrganization

class GovernmentOrganizationSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    logo = fields.String(schema.logo)
    image = fields.String(schema.image)
    description = fields.String(schema.description)
    address = fields.Dict(schema.address)
    email = fields.String(schema.email)
    telephone = fields.String(schema.telephone)

    class Meta:
        rdf_type = schema.GovernmentOrganization

class LocalBusinessSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    logo = fields.String(schema.logo)
    image = fields.String(schema.image)
    description = fields.String(schema.description)
    address = fields.Dict(schema.address)
    email = fields.String(schema.email)
    telephone = fields.String(schema.telephone)

    class Meta:
        rdf_type = schema.LocalBusiness

class NGOSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    logo = fields.String(schema.logo)
    image = fields.String(schema.image)
    description = fields.String(schema.description)
    address = fields.Dict(schema.address)
    email = fields.String(schema.email)
    telephone = fields.String(schema.telephone)

    class Meta:
        rdf_type = schema.NGO

class PerformingGroupSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    logo = fields.String(schema.logo)
    image = fields.String(schema.image)
    description = fields.String(schema.description)
    address = fields.Dict(schema.address)
    email = fields.String(schema.email)
    telephone = fields.String(schema.telephone)

    class Meta:
        rdf_type = schema.PerformingGroup

class SportsTeamSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    logo = fields.String(schema.logo)
    image = fields.String(schema.image)
    description = fields.String(schema.description)
    address = fields.Dict(schema.address)
    email = fields.String(schema.email)
    telephone = fields.String(schema.telephone)

    class Meta:
        rdf_type = schema.SportsTeam
