from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from api.models import FizzBuzz

class FizzBuzzModelTests(TestCase):

    def test_fizz_15(self):
        fb = FizzBuzz(word='fizz', max_value=15)
        self.assertEqual(fb.create_fizzbuzz_dict(), {'numbers': [3,6,9,12,15]})

    def test_fizz_30(self):
        fb = FizzBuzz(word='fizz', max_value=30)
        self.assertEqual(fb.create_fizzbuzz_dict(), {'numbers': [3,6,9,12,15,18,21,24,27,30]})

    def test_buzz_15(self):
        fb = FizzBuzz(word='buzz', max_value=15)
        self.assertEqual(fb.create_fizzbuzz_dict(), {'numbers': [5,10,15]})

    def test_wrong_15(self):
        fb = FizzBuzz(word='wrong', max_value=15)
        self.assertEqual(fb.create_fizzbuzz_dict(), {'numbers': []})

    def test_fizz_neg_90(self):
        fb = FizzBuzz(word='fizz', max_value=-90)
        self.assertEqual(fb.create_fizzbuzz_dict(), {'numbers': []})

    def test_fizz_0(self):
        fb = FizzBuzz(word='fizz', max_value=0)
        self.assertEqual(fb.create_fizzbuzz_dict(), {'numbers': []})

    def test_fizzbuzz_15(self):
        fb = FizzBuzz(word='fizzbuzz', max_value=15)
        self.assertEqual(fb.create_fizzbuzz_dict(), {'numbers': [15]})


class FizzBuzzViewTests(TestCase):
    def test_fizzbuzz_15(self):
    	client = Client()
    	response = client.get(reverse('api')+'?word=fizzbuzz&max_value=15')
    	self.assertEqual(response.status_code, 200)
    	self.assertEqual(response.content, '{"status":"ok","numbers":[15]}')

    def test_fizz_15(self):
    	client = Client()
    	response = client.get(reverse('api')+'?word=fizz&max_value=15')
    	self.assertEqual(response.status_code, 200)
    	self.assertEqual(response.content, '{"status":"ok","numbers":[3,6,9,12,15]}')

    def test_buzz_30(self):
    	client = Client()
    	response = client.get(reverse('api')+'?word=buzz&max_value=30')
    	self.assertEqual(response.status_code, 200)
    	self.assertEqual(response.content, '{"status":"ok","numbers":[5,10,15,20,25,30]}')

    def test_ouch_15(self):
    	client = Client()
    	response = client.get(reverse('api')+'?word=ouch&max_value=15')
    	self.assertEqual(response.status_code, 400)
    	self.assertEqual(response.content, '{"status":"error","numbers":[]}')

    def test_fizz_neg_15(self):
    	client = Client()
    	response = client.get(reverse('api')+'?word=fizz&max_value=-15')
    	self.assertEqual(response.status_code, 400)
    	self.assertEqual(response.content, '{"status":"error","numbers":[]}')

    def test_no_word(self):
    	client = Client()
    	response = client.get(reverse('api')+'?max_value=15')
    	self.assertEqual(response.status_code, 400)
    	self.assertEqual(response.content, '{"status":"error","numbers":[]}')

    def test_no_num(self):
    	client = Client()
    	response = client.get(reverse('api')+'?word=fizz')
    	self.assertEqual(response.status_code, 400)
    	self.assertEqual(response.content, '{"status":"error","numbers":[]}')

    def test_num_is_float(self):
    	client = Client()
    	response = client.get(reverse('api')+'?word=fizz&max_value=15.0')
    	self.assertEqual(response.status_code, 400)
    	self.assertEqual(response.content, '{"status":"error","numbers":[]}')

    def test_code_injection_attempt(self):
    	client = Client()
    	response = client.get(reverse('api')+'?eval(print("hi"))')
    	self.assertEqual(response.status_code, 400)
    	self.assertEqual(response.content, '{"status":"error","numbers":[]}')

    def test_random_chars(self):
    	client = Client()
    	response = client.get(reverse('api')+'?**#lj%1-')
    	self.assertEqual(response.status_code, 400)
    	self.assertEqual(response.content, '{"status":"error","numbers":[]}')









