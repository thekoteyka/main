from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class RatingTest(TestCase):

    def test_template(self):
        response = self.client.get(reverse('main'))
        self.assertTemplateUsed(response, 'rating/rating_list.html')