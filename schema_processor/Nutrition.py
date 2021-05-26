from schema.Nutrition import NutritionSchema
from calamus.schema import INCLUDE

class nutritionLD:
    def main(self, request):
        return NutritionSchema.schema().load({
            "name": request.form['nutrition_name'],
            "calories": request.form['nutrition_calories']
        }, unknown = INCLUDE).dump()
