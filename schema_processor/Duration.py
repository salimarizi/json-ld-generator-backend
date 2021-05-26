from schema.Duration import DurationSchema
from calamus.schema import INCLUDE

class durationLD:
    def main(self, request):
        return DurationSchema.schema().load({
            "name": request.form['duration_name']
        }, unknown = INCLUDE).dump()
