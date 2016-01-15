import unittest 
from delivery import Santa, get_single_santa_trip, count_houses_with_robo_santa

class SantaTestCase(unittest.TestCase):

	def test_init_santa(self):
		"""A new santa object is correctly setup"""
		santa = Santa()
		assert santa.houses_visited == set(["0:0"])
		assert santa.current_position == [0,0]

	def test_move(self):
		"""Should correctly change position according to instructions from the elf"""

		test_inputs = [
			(">", [0,1]),
			("<", [0,-1]),
			("^", [1,0]),
			("v", [-1,0]),
		]

		for input, expected_result in test_inputs:
			santa = Santa()			
			new_position = santa.move(input)
			
			assert new_position == expected_result, \
				"Expect {} to be {} for {}". format(new_position, expected_result, input)

class DeliveryTestCase(unittest.TestCase):

	def test_get_single_santa_trip(self):
		"""Should correctly count the number of houses visited by a single santa instance"""

		test_inputs = [
			(">", 2),
			("^>v<", 4),
			("^v^v^v^v^v", 2),
		]

		for input, expected_result in test_inputs:
			num_houses = get_single_santa_trip(input)
			assert num_houses == expected_result, \
			"Expected {} to be: {}" . format (num_houses, expected_result)

	def test_get_santa_and_robo_santa_trip(self):
		"""Should correctly count the number of houses visited by a santa and robo-santa collaborative effort"""

		test_inputs = [
			(">", 2),
			("^>v<", 3),
			("^v^v^v^v^v", 11),
		]

		for input, expected_result in test_inputs:
			num_houses = count_houses_with_robo_santa(input)
			assert num_houses == expected_result, \
			"Expected {} to be: {} for {}" . format (num_houses, expected_result, input)


if __name__ == '__main__':
    unittest.main()