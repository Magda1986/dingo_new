from django.test import TestCase, Client
from .models import Math, Result
from .forms import ResultForm
#from unittest import TestCase (powielenie 1 linii)
from django.urls import resolve
from django.urls.exceptions import Resolver404
from .views import add, sub

class MathModelTest(TestCase):

    def setUp(self):
        Math.objects.create(operation="add", a=1, b=2)
        Math.objects.create(operation="sub", a=20, b=30)

    def test_math_str(self):
        m1 = Math.objects.get(operation="add")
        m2 = Math.objects.get(operation="sub")

        self.assertEqual(str(m1), "id:1, a=1, b=2, op=add")
        self.assertEqual(str(m2), "id:2, a=20, b=30, op=sub")


class ResultModelTest(TestCase):

    def setUp(self):
        Result.objects.create(value=10)
        Result.objects.create(error="0 division error!")

    def test_result_str(self):
        r1 = Result.objects.get(value=10)
        r2 = Result.objects.get(error="0 division error!")

        self.assertEqual(str(r1), 'value: 10.0 | error: None')
        self.assertEqual(str(r2), 'value: None | error: 0 division error!')

class MathViewsTest(TestCase):

    def setUp(self):
        Math.objects.create(operation="sub", a=20, b=30)
        self.client = Client()

    def test_maths_list(self):
        response = self.client.get("/maths/histories")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["maths"]), 1)
        self.assertIn('<li><a href="/maths/histories/1">id:1, a=20, b=30, op=sub</a></li>',
                      response.content.decode())


class ResultFormTest(TestCase):
    def test_result_save_correct_data(self):
        data = {"value": 200}
        self.assertEqual(len(Result.objects.all()), 0)
        form = ResultForm(data=data)
        self.assertTrue(form.is_valid())
        r = form.save()
        self.assertIsInstance(r, Result)
        self.assertEqual(r.value, 200)
        self.assertIsNotNone(r.id)
        self.assertIsNone(r.error)


class TestUrls(TestCase):
   def test_resolution_for_add(self):
       resolver = resolve('/maths/add/1/2')
       self.assertEqual(resolver.func, add)

   def test_resolution_for_sub(self):
       resolver = resolve('/maths/sub/1/2')
       self.assertEqual(resolver.func, sub)

   def test_arguments_should_be_integers_or_404(self):
       with self.assertRaises(Resolver404):
           resolve('maths/sub/a/b')
