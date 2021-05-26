from schema.Audience import AudienceSchema
from calamus.schema import INCLUDE

class audienceLD:
    def main(self, request):
        return AudienceSchema.schema().load({
            "audienceType": request.form['audience_type']
        }, unknown = INCLUDE).dump()
