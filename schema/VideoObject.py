from calamus import fields
from calamus.schema import JsonLDAnnotation

schema = fields.Namespace("http://schema.org/")

class VideoObjectSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    description = fields.String(schema.description)
    uploadDate = fields.String(schema.uploadDate)
    actor = fields.Dict(schema.actor)
    caption = fields.String(schema.caption)
    director = fields.Dict(schema.director)
    musicBy = fields.Dict(schema.musicBy)
    thumbnail = fields.Dict(schema.thumbnail)
    thumbnailUrl = fields.String(schema.thumbnailUrl)
    transcript = fields.String(schema.transcript)
    videoFrameSize = fields.String(schema.videoFrameSize)
    videoQuality = fields.String(schema.videoQuality)
    bitrate = fields.String(schema.bitrate)
    contentURL = fields.String(schema.contentURL)
    embedUrl = fields.String(schema.embedUrl)

    class Meta:
        rdf_type = schema.VideoObject

class SimpleVideoObjectSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    description = fields.String(schema.description)
    uploadDate = fields.String(schema.uploadDate)
    caption = fields.String(schema.caption)
    transcript = fields.String(schema.transcript)
    videoFrameSize = fields.String(schema.videoFrameSize)
    videoQuality = fields.String(schema.videoQuality)
    bitrate = fields.String(schema.bitrate)
    contentURL = fields.String(schema.contentURL)
    embedUrl = fields.String(schema.embedUrl)
    thumbnailUrl = fields.String(schema.thumbnailUrl)

    class Meta:
        rdf_type = schema.VideoObject
