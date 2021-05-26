from schema.Location import LocationSchema
from calamus.schema import INCLUDE
from schema.Event import EventSchema, BusinessEventSchema, ChildrenEventSchema, ComedyEventSchema, DanceEventSchema, EducationalEventSchema, FestivalSchema, FoodEventSchema, LiteraryEventSchema, MusicEventSchema, SalesEventSchema, SocialEventSchema, SportsEventSchema, TheaterEventSchema, UserInteractionSchema, VisualArtsEventSchema
from schema_processor.Location import locationLD
from schema_processor.Offer import offerLD

class eventLD:
    def main(self, request):
        location_dict = locationLD().main(request)
        offer_dict = offerLD().main(request)

        events = {
            "_id": request.form['id'],
            "name": request.form['name'],
            "url": request.form['url'],
            "description": request.form['description'],
            "startDate": request.form['start_date'],
            "endDate": request.form['end_date'],
            "location": location_dict,
            "offers": offer_dict,
            "eventAttendanceMode": request.form['attendance_mode'],
            "eventStatus": request.form['event_status'],
            "image": request.form['image']
        }

        event_type = request.form['event_type']
        if event_type == "Event":
            event_dict = EventSchema.schema().load(events, unknown = INCLUDE).dump()
        if event_type == "BusinessEvent":
            event_dict = BusinessEventSchema.schema().load(events, unknown = INCLUDE).dump()
        if event_type == "ChildrenEvent":
            event_dict = ChildrenEventSchema.schema().load(events, unknown = INCLUDE).dump()
        if event_type == "ComedyEvent":
            event_dict = ComedyEventSchema.schema().load(events, unknown = INCLUDE).dump()
        if event_type == "DanceEvent":
            event_dict = DanceEventSchema.schema().load(events, unknown = INCLUDE).dump()
        if event_type == "EducationalEvent":
            event_dict = EducationalEventSchema.schema().load(events, unknown = INCLUDE).dump()
        if event_type == "Festival":
            event_dict = FestivalSchema.schema().load(events, unknown = INCLUDE).dump()
        if event_type == "FoodEvent":
            event_dict = FoodEventSchema.schema().load(events, unknown = INCLUDE).dump()
        if event_type == "LiteraryEvent":
            event_dict = LiteraryEventSchema.schema().load(events, unknown = INCLUDE).dump()
        if event_type == "MusicEvent":
            event_dict = MusicEventSchema.schema().load(events, unknown = INCLUDE).dump()
        if event_type == "SalesEvent":
            event_dict = SalesEventSchema.schema().load(events, unknown = INCLUDE).dump()
        if event_type == "SocialEvent":
            event_dict = SocialEventSchema.schema().load(events, unknown = INCLUDE).dump()
        if event_type == "SportsEvent":
            event_dict = SportsEventSchema.schema().load(events, unknown = INCLUDE).dump()
        if event_type == "TheaterEvent":
            event_dict = TheaterEventSchema.schema().load(events, unknown = INCLUDE).dump()
        if event_type == "UserInteraction":
            event_dict = UserInteractionSchema.schema().load(events, unknown = INCLUDE).dump()
        if event_type == "VisualArtsEvent":
            event_dict = VisualArtsEventSchema.schema().load(events, unknown = INCLUDE).dump()

        return event_dict
