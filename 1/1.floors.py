import re 

def get_floor(input_string):
	up_one_regex = "\("
	down_one_regex = "\)"
	return len(re.findall(up_one_regex, input_string)) - len(re.findall(down_one_regex, input_string))
	
def main():
	"""Test example inputs"""

	print(get_floor(open('input.txt').read()))


def test_get_floor():

	inputs = [
	]

	for input, expected_result in inputs: 
		result = get_floor(input)

		assert result == expected_result


if __name__ == "__main__":
   main()		