import unittest
from wrapping_paper import Present 

class TestPresent(unittest.TestCase):	

	def test_create_present(self):
		p = Present("1x2x3")

		assert p.l == 1
		assert p.w == 2
		assert p.h == 3

	def test_get_size(self):

		assert Present("2x3x4").get_size() == 52

	def test_get_smallest_size(self):

		test_inputs = [
			("2x3x4", [2,3]),
			("1x1x10", [1,1]),
			("1x10x2", [1,2]),
		]
		for input, expected_output in test_inputs:
			assert Present(input).get_smallest_side() == expected_output

	def test_get_wrapping_paper_area(self):

		test_inputs = [
			("2x3x4", 58),
			("1x1x10", 43)
		]
		for input, expected_output in test_inputs:
			area = Present(input).get_wrapping_paper_area()
			assert area == expected_output, "Expected {} to be {}" . format (area, expected_output)

if __name__ == '__main__':
    unittest.main()		
		