from schema.Article import ArticleSchema
from calamus.schema import INCLUDE
from schema_processor.Author import authorLD
from schema_processor.Organization import organizationLD

class articleLD:
    def main(self, request):
        author_dict = authorLD().main(request)
        organization_dict = organizationLD().main(request)

        return ArticleSchema.schema().load({
            "name": request.form['article_name'],
            "articleBody": request.form['article_body'],
            "articleSection": request.form['article_section'],
            "headline": request.form['headline'],
            "datePublished": request.form['date_published'],
            "image": request.form['image'],
            "backstory": request.form['backstory'],
            "pageStart": request.form['page_start'],
            "pageEnd": request.form['page_end'],
            "pagination": request.form['pagination'],
            "about": request.form['about'],
            "wordCount": request.form['word_count'],
            "author": author_dict,
            "publisher": organization_dict
        }, unknown = INCLUDE).dump()
