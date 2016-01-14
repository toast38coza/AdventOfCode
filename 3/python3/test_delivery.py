import unittest 
from delivery import get_houses, move, save

class DeliveryTestCase(unittest.TestCase):

	def test_move(self):

		test_inputs = [
			(">", [0,1]),
			("<", [0,-1]),
			("^", [1,0]),
			("v", [-1,0]),
		]

		for input, expected_result in test_inputs:
			new_position = move(input, [0,0])
			assert new_position == expected_result, \
				"Expect {} to be {}". format(new_position, expected_result)

	def test_delivery(self):

		test_inputs = [
			(">", 2),
			("^>v<", 4),
			("^v^v^v^v^v", 2),
		]

		for input, expected_result in test_inputs:
			num_houses = get_houses(input)
			assert num_houses == expected_result, \
			"Expected {} to be: {}" . format (num_houses, expected_input)

if __name__ == '__main__':
    unittest.main()