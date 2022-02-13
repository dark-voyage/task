from django.test import TestCase


class AnimalTestCase(TestCase):
    def setUp(self):
        self.ad = Ad.objects.create(name="Van Darkholme", description="Full Dungeon Master",  price=300)
        Image.objects.create(ad=self.ad, link="https://docs.djangoproject.com/en/4.0/topics/testing/overview/")

    def test_ad_has_an_image(self):
        test_ad = self.ad
        test_image = Image.objects.get(ad=test_ad)
        self.assertEqual(test_image.ad, test_ad)
       
# Create your tests here.
