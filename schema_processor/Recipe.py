from schema.Recipe import RecipeSchema
from calamus.schema import INCLUDE
from schema_processor.ImageObject import imageObjectLD
from schema_processor.Duration import durationLD
from schema_processor.Nutrition import nutritionLD
from schema_processor.VideoObject import videoObjectLD
from schema_processor.Author import authorLD
from schema_processor.Rating import ratingLD

class recipeLD:
    def main(self, request):
        nutrition_dict = nutritionLD().main(request)
        image_object_dict = imageObjectLD().main(request)
        video_object_dict = videoObjectLD().main(request, "simple")
        author_dict = authorLD().main(request)
        rating_dict = ratingLD().main(request, "aggregate")
        duration_dict = durationLD().main(request)

        return RecipeSchema.schema().load({
            "name": request.form['recipe_name'],
            "recipeCategory": request.form['recipe_category'],
            "cookTime": duration_dict,
            "cookingMethod": request.form['cooking_method'],
            "recipeCuisine": request.form['cuisine'],
            "recipeIngredient": request.form['ingredients'],
            "recipeInstructions": request.form['instructions'],
            "suitableForDiet": request.form['suitable_for_diet'],
            "step": request.form['step'],
            "nutrition": nutrition_dict,
            "image": image_object_dict,
            "video": video_object_dict,
            "aggregateRating": rating_dict,
            "keywords": request.form['recipe_keywords'],
            "author": author_dict,
            "description": request.form['recipe_description'],
            "prepTime": duration_dict
        }, unknown = INCLUDE).dump()
