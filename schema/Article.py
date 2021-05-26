from calamus import fields
from calamus.schema import JsonLDAnnotation

schema = fields.Namespace("http://schema.org/")

class ArticleSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    articleBody = fields.String(schema.articleBody)
    articleSection = fields.String(schema.articleSection)
    headline = fields.String(schema.headline)
    datePublished = fields.String(schema.datePublished)
    image = fields.String(schema.image)
    backstory = fields.String(schema.backstory)
    pageStart = fields.String(schema.pageStart)
    pageEnd = fields.String(schema.pageEnd)
    pagination = fields.String(schema.pagination)
    about = fields.String(schema.about)
    wordCount = fields.String(schema.wordCount)
    author = fields.Dict(schema.author)
    publisher = fields.Dict(schema.publisher)

    class Meta:
        rdf_type = schema.Article
