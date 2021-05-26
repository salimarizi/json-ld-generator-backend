from schema.Movie import MovieSchema
from calamus.schema import INCLUDE
from schema_processor.Actor import actorLD
from schema_processor.Director import directorLD
from schema_processor.MusicGroup import musicGroupLD
from schema_processor.Organization import organizationLD
from schema_processor.Country import countryLD
from schema_processor.VideoObject import videoObjectLD
from schema_processor.ImageObject import imageObjectLD

class movieLD:
    def main(self, request):
        actor_dict = actorLD().main(request)
        director_dict = directorLD().main(request)
        country_dict = countryLD().main(request)
        music_group_dict = musicGroupLD().main(request)
        organization_dict = organizationLD().main(request)
        video_object_dict = videoObjectLD().main(request, "simple")
        image_object_dict = imageObjectLD().main(request)

        return MovieSchema.schema().load({
            "name": request.form['movie_name'],
            "about": request.form['movie_about'],
            "actor": actor_dict,
            "director": director_dict,
            "countryOfOrigin": country_dict,
            "musicBy": music_group_dict,
            "duration": request.form['duration'],
            "productionCompany": organization_dict,
            "subtitleLanguage": request.form['subtitle_language'],
            "titleEIDR": request.form['title_eidr'],
            "trailer": video_object_dict,
            "image": image_object_dict,
            "dateCreated": request.form['date_created']
        }, unknown = INCLUDE).dump()
