from django.test import TestCase

from  .models import MyModel

class MyModel(TestCase):
    def test_my_model_creation(self):
        my_model = MyModel.objects.create(name='Test Model')

        self.asserEqual(my_model.name, 'Test Model')

    def test_my_model_str_representation(self):
        my_model = MyModel.objects.create(name='Test Model')

        self.asserEqual(str(my_model), 'Test Model')