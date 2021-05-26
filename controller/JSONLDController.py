from schema_processor.Person import personLD
from schema_processor.Event import eventLD
from schema_processor.Review import reviewLD
from schema_processor.Product import productLD
from schema_processor.Brand import brandLD
from schema_processor.Book import bookLD
from schema_processor.Article import articleLD
from schema_processor.Organization import organizationLD
from schema_processor.VideoObject import videoObjectLD
from schema_processor.Movie import movieLD
from schema_processor.Recipe import recipeLD
from schema_processor.LocalBusiness import localBusinessLD

class ProcessingSchema:
    def main(self, request):
        if request.form['json_type'] == "Person":
            result = personLD()
        if request.form['json_type'] == "Events":
            result = eventLD()
        if request.form['json_type'] == "Review":
            result = reviewLD()
        if request.form['json_type'] == "Product":
            result = productLD()
        if request.form['json_type'] == "Brand":
            result = brandLD()
        if request.form['json_type'] == "Book":
            result = bookLD()
        if request.form['json_type'] == "Article":
            result = articleLD()
        if request.form['json_type'] == "Organization":
            result = organizationLD()
        if request.form['json_type'] == "VideoObject":
            result = videoObjectLD()
        if request.form['json_type'] == "Movie":
            result = movieLD()
        if request.form['json_type'] == "Recipe":
            result = recipeLD()
        if request.form['json_type'] == "LocalBusiness" or request.form['json_type'] == "Restaurant":
            result = localBusinessLD()

        return result.main(request)
