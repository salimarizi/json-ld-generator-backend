from calamus import fields
from calamus.schema import JsonLDAnnotation

schema = fields.Namespace("http://schema.org/")

class RecipeSchema(metaclass = JsonLDAnnotation):
    name = fields.String(schema.name)
    recipeCategory = fields.String(schema.recipeCategory)
    cookTime = fields.Dict(schema.cookTime)
    cookingMethod = fields.String(schema.cookingMethod)
    recipeCuisine = fields.String(schema.recipeCuisine)
    recipeIngredient = fields.String(schema.recipeIngredient)
    recipeInstructions = fields.String(schema.recipeInstructions)
    suitableForDiet = fields.String(schema.suitableForDiet)
    step = fields.String(schema.step)
    nutrition = fields.Dict(schema.nutrition)
    image = fields.Dict(schema.image)
    video = fields.Dict(schema.video)
    aggregateRating = fields.Dict(schema.aggregateRating)
    keywords = fields.String(schema.keywords)
    author = fields.String(schema.author)
    description = fields.String(schema.description)
    prepTime = fields.Dict(schema.prepTime)

    class Meta:
        rdf_type = schema.Recipe
