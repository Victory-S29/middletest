from django.test import TestCase
from django.urls import reverse
from .models import Recipe

class RecipeViewsTestCase(TestCase):
    def setUp(self):
        Recipe.objects.create(
            title='Test Recipe 1',
            description='Test Recipe 1 description',
            ingredients='Ingredient 1, Ingredient 2',
            instructions='Step 1, Step 2'
        )
        Recipe.objects.create(
            title='Test Recipe 2',
            description='Test Recipe 2 description',
            ingredients='Ingredient 3, Ingredient 4',
            instructions='Step 3, Step 4'
        )
        Recipe.objects.create(
            title='Test Recipe 3',
            description='Test Recipe 3 description',
            ingredients='Ingredient 5, Ingredient 6',
            instructions='Step 5, Step 6'
        )

    def test_recipe_title_in_response(self):
        response = self.client.get(reverse('main'))
        recipes = Recipe.objects.all()
        for recipe in recipes:
            self.assertContains(response, recipe.title)

    def test_recipe_description_in_response(self):
        response = self.client.get(reverse('main'))
        recipes = Recipe.objects.all()
        for recipe in recipes:
            self.assertContains(response, recipe.description)

    def test_recipe_ingredients_in_response(self):
        response = self.client.get(reverse('main'))
        recipes = Recipe.objects.all()
        for recipe in recipes:
            self.assertContains(response, recipe.ingredients)

    def test_recipe_instructions_in_response(self):
        response = self.client.get(reverse('main'))
        recipes = Recipe.objects.all()
        for recipe in recipes:
            self.assertContains(response, recipe.instructions)
    
    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertContains(response, 'Welcome to the Recipe App')
        self.assertContains(response, 'Latest Recipes')
        
        latest_recipes = Recipe.objects.order_by('-created_at')[:5]
        for recipe in latest_recipes:
            self.assertRecipeInResponse(response, recipe)
    
        self.assertNotContains(response, 'No recipes found.')
    
    def test_category_list_view(self):
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_list.html')
        self.assertContains(response, 'Category List')
        self.assertContains(response, 'Dessert')
        self.assertNotContains(response, 'No categories found.')