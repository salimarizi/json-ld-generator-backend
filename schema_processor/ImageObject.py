from schema.ImageObject import ImageObjectSchema
from calamus.schema import INCLUDE

class imageObjectLD:
    def main(self, request):
        return ImageObjectSchema.schema().load({
            "name": request.form['image_object_name'],
            "url": request.form['image_object_url'],
            "caption": request.form['image_object_caption']
        }, unknown = INCLUDE).dump()
