from schema.MusicGroup import MusicGroupSchema
from calamus.schema import INCLUDE

class musicGroupLD:
    def main(self, request):
        return MusicGroupSchema.schema().load({
            "name": request.form['music_group_name'],
            "url": request.form['music_group_url'],
            "genre": request.form['music_group_genre']
        }, unknown = INCLUDE).dump()
