
def calculate_fizzes(max_value, divisor, num_list):
	'''
	Iterates from 1 to max_value (including max_value) and finds numbers that are divisible by divisor and result
	in a remainder of 0, and appends all those numbers in ascending order to the list passed into this function.

	positional arguments:

	max_value -- an integer greater than 0
	divisor -- 3, 5 or 15 to represent "fizz", "buzz" or "fizzbuzz" respectively
	num_list -- a list to append values to
	'''

	for x in xrange(1, max_value + 1): # Use xrange because we don't know how high max_num is
		if x % divisor == 0:
			num_list.append(x)


class FizzBuzz(object):
	'''
	We could have put this logic in the view, but fat models and skinny views are the way to go. This way also makes it
	easier to test smaller portions of code.

	This class enables us to call object.create_fizzbuzz_dict(), which returns a dict with the key 'numbers', and the value num_list. 

	Class is initialized with positional arguments:

	max_value -- the upper limit to iterate through (and including this value)
	word --- "fizz", "buzz" or "fizzbuzz". Other words can be used, but will return an empty dictionary
	from the class method "create_fizzbuzz_dict".

	'''

	def __init__(self, max_value, word):
		# Now we can instantiate the class with the values passed in from the request's parameters. 
		self.max_value = max_value # Must be integer
		self.word = word # Must be string

	def create_fizzbuzz_dict(self):
		'''
		This method *always* returns a single-item dictionary with a key of 'numbers', and a value of 
		num_list. num_list will only be populated if the max_value is valid and one of the following words 
		is passed to the class instantiaion: 'fizz', 'buzz', or 'fizzbuzz'.

		takes no arguments.
		'''

		num_list = []
		if self.word == 'fizzbuzz':
			calculate_fizzes(self.max_value, 15, num_list)
		elif self.word == 'fizz':
			calculate_fizzes(self.max_value, 3, num_list)
		elif self.word == 'buzz':
			calculate_fizzes(self.max_value, 5, num_list)

		return {'numbers': num_list}


