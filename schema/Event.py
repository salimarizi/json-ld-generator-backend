from calamus import fields
from calamus.schema import JsonLDAnnotation

schema = fields.Namespace("http://schema.org/")

class EventSchema(metaclass = JsonLDAnnotation):
    _id = fields.Id()
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    description = fields.String(schema.description)
    startDate = fields.String(schema.startDate)
    endDate = fields.String(schema.endDate)
    location = fields.Dict(schema.location)
    offers = fields.Dict(schema.offers)
    eventAttendanceMode = fields.String(schema.eventAttendanceMode)
    eventStatus = fields.String(schema.eventStatus)
    image = fields.String(schema.image)

    class Meta:
        rdf_type = schema.Event

class BusinessEventSchema(metaclass = JsonLDAnnotation):
    _id = fields.Id()
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    description = fields.String(schema.description)
    startDate = fields.String(schema.startDate)
    endDate = fields.String(schema.endDate)
    location = fields.Dict(schema.location)
    offers = fields.Dict(schema.offers)
    eventAttendanceMode = fields.String(schema.eventAttendanceMode)
    eventStatus = fields.String(schema.eventStatus)
    image = fields.String(schema.image)

    class Meta:
        rdf_type = schema.BusinessEvent

class ChildrenEventSchema(metaclass = JsonLDAnnotation):
    _id = fields.Id()
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    description = fields.String(schema.description)
    startDate = fields.String(schema.startDate)
    endDate = fields.String(schema.endDate)
    location = fields.Dict(schema.location)
    offers = fields.Dict(schema.offers)
    eventAttendanceMode = fields.String(schema.eventAttendanceMode)
    eventStatus = fields.String(schema.eventStatus)
    image = fields.String(schema.image)

    class Meta:
        rdf_type = schema.ChildrensEvent

class ComedyEventSchema(metaclass = JsonLDAnnotation):
    _id = fields.Id()
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    description = fields.String(schema.description)
    startDate = fields.String(schema.startDate)
    endDate = fields.String(schema.endDate)
    location = fields.Dict(schema.location)
    offers = fields.Dict(schema.offers)
    eventAttendanceMode = fields.String(schema.eventAttendanceMode)
    eventStatus = fields.String(schema.eventStatus)
    image = fields.String(schema.image)

    class Meta:
        rdf_type = schema.ComedyEvent

class DanceEventSchema(metaclass = JsonLDAnnotation):
    _id = fields.Id()
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    description = fields.String(schema.description)
    startDate = fields.String(schema.startDate)
    endDate = fields.String(schema.endDate)
    location = fields.Dict(schema.location)
    offers = fields.Dict(schema.offers)
    eventAttendanceMode = fields.String(schema.eventAttendanceMode)
    eventStatus = fields.String(schema.eventStatus)
    image = fields.String(schema.image)

    class Meta:
        rdf_type = schema.DanceEvent

class EducationalEventSchema(metaclass = JsonLDAnnotation):
    _id = fields.Id()
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    description = fields.String(schema.description)
    startDate = fields.String(schema.startDate)
    endDate = fields.String(schema.endDate)
    location = fields.Dict(schema.location)
    offers = fields.Dict(schema.offers)
    eventAttendanceMode = fields.String(schema.eventAttendanceMode)
    eventStatus = fields.String(schema.eventStatus)
    image = fields.String(schema.image)

    class Meta:
        rdf_type = schema.EducationEvent

class FestivalSchema(metaclass = JsonLDAnnotation):
    _id = fields.Id()
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    description = fields.String(schema.description)
    startDate = fields.String(schema.startDate)
    endDate = fields.String(schema.endDate)
    location = fields.Dict(schema.location)
    offers = fields.Dict(schema.offers)
    eventAttendanceMode = fields.String(schema.eventAttendanceMode)
    eventStatus = fields.String(schema.eventStatus)
    image = fields.String(schema.image)

    class Meta:
        rdf_type = schema.Festival

class FoodEventSchema(metaclass = JsonLDAnnotation):
    _id = fields.Id()
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    description = fields.String(schema.description)
    startDate = fields.String(schema.startDate)
    endDate = fields.String(schema.endDate)
    location = fields.Dict(schema.location)
    offers = fields.Dict(schema.offers)
    eventAttendanceMode = fields.String(schema.eventAttendanceMode)
    eventStatus = fields.String(schema.eventStatus)
    image = fields.String(schema.image)

    class Meta:
        rdf_type = schema.FoodEvent

class LiteraryEventSchema(metaclass = JsonLDAnnotation):
    _id = fields.Id()
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    description = fields.String(schema.description)
    startDate = fields.String(schema.startDate)
    endDate = fields.String(schema.endDate)
    location = fields.Dict(schema.location)
    offers = fields.Dict(schema.offers)
    eventAttendanceMode = fields.String(schema.eventAttendanceMode)
    eventStatus = fields.String(schema.eventStatus)
    image = fields.String(schema.image)

    class Meta:
        rdf_type = schema.LiteraryEvent

class MusicEventSchema(metaclass = JsonLDAnnotation):
    _id = fields.Id()
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    description = fields.String(schema.description)
    startDate = fields.String(schema.startDate)
    endDate = fields.String(schema.endDate)
    location = fields.Dict(schema.location)
    offers = fields.Dict(schema.offers)
    eventAttendanceMode = fields.String(schema.eventAttendanceMode)
    eventStatus = fields.String(schema.eventStatus)
    image = fields.String(schema.image)

    class Meta:
        rdf_type = schema.MusicEvent

class SalesEventSchema(metaclass = JsonLDAnnotation):
    _id = fields.Id()
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    description = fields.String(schema.description)
    startDate = fields.String(schema.startDate)
    endDate = fields.String(schema.endDate)
    location = fields.Dict(schema.location)
    offers = fields.Dict(schema.offers)
    eventAttendanceMode = fields.String(schema.eventAttendanceMode)
    eventStatus = fields.String(schema.eventStatus)
    image = fields.String(schema.image)

    class Meta:
        rdf_type = schema.SaleEvent

class SocialEventSchema(metaclass = JsonLDAnnotation):
    _id = fields.Id()
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    description = fields.String(schema.description)
    startDate = fields.String(schema.startDate)
    endDate = fields.String(schema.endDate)
    location = fields.Dict(schema.location)
    offers = fields.Dict(schema.offers)
    eventAttendanceMode = fields.String(schema.eventAttendanceMode)
    eventStatus = fields.String(schema.eventStatus)
    image = fields.String(schema.image)

    class Meta:
        rdf_type = schema.SocialEvent

class SportsEventSchema(metaclass = JsonLDAnnotation):
    _id = fields.Id()
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    description = fields.String(schema.description)
    startDate = fields.String(schema.startDate)
    endDate = fields.String(schema.endDate)
    location = fields.Dict(schema.location)
    offers = fields.Dict(schema.offers)
    eventAttendanceMode = fields.String(schema.eventAttendanceMode)
    eventStatus = fields.String(schema.eventStatus)
    image = fields.String(schema.image)

    class Meta:
        rdf_type = schema.SportsEvent

class TheaterEventSchema(metaclass = JsonLDAnnotation):
    _id = fields.Id()
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    description = fields.String(schema.description)
    startDate = fields.String(schema.startDate)
    endDate = fields.String(schema.endDate)
    location = fields.Dict(schema.location)
    offers = fields.Dict(schema.offers)
    eventAttendanceMode = fields.String(schema.eventAttendanceMode)
    eventStatus = fields.String(schema.eventStatus)
    image = fields.String(schema.image)

    class Meta:
        rdf_type = schema.TheaterEvent

class UserInteractionSchema(metaclass = JsonLDAnnotation):
    _id = fields.Id()
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    description = fields.String(schema.description)
    startDate = fields.String(schema.startDate)
    endDate = fields.String(schema.endDate)
    location = fields.Dict(schema.location)
    offers = fields.Dict(schema.offers)
    eventAttendanceMode = fields.String(schema.eventAttendanceMode)
    eventStatus = fields.String(schema.eventStatus)
    image = fields.String(schema.image)

    class Meta:
        rdf_type = schema.UserInteraction

class VisualArtsEventSchema(metaclass = JsonLDAnnotation):
    _id = fields.Id()
    name = fields.String(schema.name)
    url = fields.String(schema.url)
    description = fields.String(schema.description)
    startDate = fields.String(schema.startDate)
    endDate = fields.String(schema.endDate)
    location = fields.Dict(schema.location)
    offers = fields.Dict(schema.offers)
    eventAttendanceMode = fields.String(schema.eventAttendanceMode)
    eventStatus = fields.String(schema.eventStatus)

    class Meta:
        rdf_type = schema.VisualArtsEvent
