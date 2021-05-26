from calamus import fields
from calamus.schema import JsonLDAnnotation

schema = fields.Namespace("http://schema.org/")

class BookSchema(metaclass = JsonLDAnnotation):
    isbn = fields.String(schema.isbn)
    bookEdition = fields.String(schema.bookEdition)
    bookFormat = fields.String(schema.bookFormat)
    numberOfPages = fields.String(schema.numberOfPages)
    about = fields.String(schema.about)
    abstract = fields.Boolean(schema.abstract)
    abridged = fields.String(schema.abridged)
    illustrator = fields.Dict(schema.illustrator)
    publisher = fields.Dict(schema.publisher)

    class Meta:
        rdf_type = schema.Book
