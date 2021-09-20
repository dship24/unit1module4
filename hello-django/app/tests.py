from django.test import SimpleTestCase
from django.http import response

# Create your tests here.
class TestNearHundred(SimpleTestCase):
    def test_100(self):
        response = self.client.get("/warmup-1/near-hundred/100/")
        self.assertContains(response, "True")

    def test_150(self):
        response = self.client.get("/warmup-1/near-hundred/150/")
        self.assertContains(response, "False")

    def test_210(self):
        response = self.client.get("/warmup-1/near-hundred/210/")
        self.assertContains(response, "True")

class TestStringSplosion(SimpleTestCase):
    def test_code(self):
        response = self.client.get("/warmup-2/string-splosion/Code/")
        self.assertContains(response, "CCoCodCode")

    def test_Randy(self):
        response = self.client.get("/warmup-2/string-splosion/Randy/")
        self.assertContains(response, "RRaRanRandRandy")

    def test_Cheese(self):
        response = self.client.get("/warmup-2/string-splosion/Cheese/")
        self.assertContains(response, "CChCheCheeCheesCheese")

class TestCatDog(SimpleTestCase):
    def test_cat_dog_1(self):
        response = self.client.get("/string-2/cat_dog/catcadog/")
        self.assertContains(response, "True")

    def test_cat_dog_2(self):
        response = self.client.get("/string-2/cat_dog/catcatdogcad/")
        self.assertContains(response, "False")

    def test_cat_dog_3(self):
        response = self.client.get("/string-2/cat_dog/catdogcatdogcatdog/")
        self.assertContains(response, "True")

class TestLoneSum(SimpleTestCase):
    def test_1_2_3(self):
        response = self.client.get("/logic-2/lone-sum/1/2/3/")
        self.assertContains(response, "6")

    def test_5_10_5(self):
        response = self.client.get("/logic-2/lone-sum/5/10/5/")
        self.assertContains(response, "10")

    def test_2_2_2(self):
        response = self.client.get("/logic-2/lone-sum/2/2/2/")
        self.assertContains(response, "0")