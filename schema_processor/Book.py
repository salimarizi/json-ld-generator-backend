from schema.Book import BookSchema
from calamus.schema import INCLUDE
from schema_processor.Author import authorLD
from schema_processor.Publisher import publisherLD

class bookLD:
    def main(self, request):
        author_dict = authorLD().main(request)
        publisher_dict = publisherLD().main(request)

        return BookSchema.schema().load({
            "isbn":  request.form['isbn'],
            "bookEdition":  request.form['book_edition'],
            "bookFormat":  request.form['book_format'],
            "numberOfPages":  request.form['number_of_page'],
            "about":  request.form['about'],
            "abstract":  request.form['abstract'],
            "abridged":  True if (request.form['abridged'] == "yes") else False,
            "illustrator": author_dict,
            "publisher": publisher_dict
        }, unknown = INCLUDE).dump()
