import unittest 
from strings import NiceString
class NiceStringTestCase(unittest.TestCase):

	def test_contains_disallowed_chars(self):

		test_inputs = [
			("ab", True),
			("adhgjb", False),
			("xsyabcxyxy", True)
		]
		for input, expectation in test_inputs:
			
			has_disallowed_chars = NiceString(input).contains_disallowed_chars()

			assert has_disallowed_chars == expectation, \
				"Expect s{} to be {} for {}" . format (has_disallowed_chars, expectation, input)

	def test_has_recurring_pair(self):

		test_inputs = [
			('xyxy', True),
			('aabcdefgaa', True),
			('aaa', False),
			('aaaa', True),
			('aaabaa',True),
			('abcde', False)
		]
		for input, expectation in test_inputs:
			result = NiceString(input).has_recurring_pair()
			assert result == expectation, \
				'Expect {} to be {} in {}' . format (result, expectation, input)

	def test_is_pair(self):

		assert NiceString("aa").is_pair(0, "aa") == False
		assert NiceString("aa").is_pair(1, "aa") == True
		assert NiceString("ab").is_pair(1, "ab") == False

	def test_has_pair(self):
		assert NiceString("").has_pair("ababa") == False
		assert NiceString("").has_pair("aaaba") == True

	def test_is_nice(self):
		test_inputs = [
			("ab", False),
			("xsyabcxyxy", False),
			("aaa", True),
			("jchzalrnumimnmhp", False),
			("haegwjzuvuyypxyu", False),
			("dvszwmarrgswjxmb", False)
		]

		for input, expectation in test_inputs:
			result = NiceString(input).is_nice()
			assert result == expectation, \
				"Expect {} to be {} for {}" . format (result, expectation, input)

	def test_has_repeating_interrupted_pair(self):

		test_inputs = [
			("xyx", True),
			("abcdefeghi", True),
			("aaa", True),
			("abcd", False)
		]
		for input, expectation in test_inputs:
			result = NiceString(input).has_repeating_interrupted_pair()
			assert result == expectation, \
				"Expect {} to be {} for {}" . format (result, expectation, input)

	def test_is_nice_new(self):
		test_inputs = [
			("qjhvhtzxzqqjkmpb", True),
			("xxyxx", True),
			("uurcxstgmygtbstg", False),
			("ieodomkazucvgmuy", False),
			("a", False)
		]
		
		for input, expectation in test_inputs:
			result = NiceString(input).is_nice_new()
			assert result == expectation, \
				"Expect {} to be {} for {}" . format (result, expectation, input)


if __name__ == '__main__':
    unittest.main()