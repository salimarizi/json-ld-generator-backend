from schema.VideoObject import VideoObjectSchema, SimpleVideoObjectSchema
from calamus.schema import INCLUDE
from schema_processor.Actor import actorLD
from schema_processor.Director import directorLD
from schema_processor.MusicGroup import musicGroupLD
from schema_processor.ImageObject import imageObjectLD

class videoObjectLD:
    def main(self, request, type = ""):
        video_object = {
            "name": request.form['video_name'],
            "description": request.form['video_description'],
            "uploadDate": request.form['upload_date'],
            "caption": request.form['video_caption'],
            "transcript": request.form['transcript'],
            "videoFrameSize": request.form['frame_size'],
            "videoQuality": request.form['quality'],
            "bitrate": request.form['bitrate'],
            "contentURL": request.form['content_url'],
            "embedUrl": request.form['embed_url'],
            "thumbnailUrl": request.form['image_object_url']
        }

        if type != "":
            return SimpleVideoObjectSchema.schema().load(video_object, unknown = INCLUDE).dump()

        video_object["actor"] = actorLD().main(request)
        video_object["director"] = directorLD().main(request)
        video_object["musicBy"] = musicGroupLD().main(request)
        video_object["thumbnail"] = imageObjectLD().main(request)

        return VideoObjectSchema.schema().load(video_object, unknown = INCLUDE).dump()
