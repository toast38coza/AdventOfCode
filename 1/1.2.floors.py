"""
"""

def find_position(input, search_floor, starting_floor=0):

	current_floor = starting_floor
	current_position = 0

	for char in input: 
		
		if char == "(":
			current_floor+=1
		if char == ")":
			current_floor-=1

		current_position+=1

		if current_floor == -1:
			return current_position

	
	return False # doesnt reach basement



def main():

	input = open('input.txt').read()
	
	print find_position(input, -1)

def test():

	test_inputs = [
		(")", 1),
		("()())", 5),
		("(((()))))", 9),
	]

	for input, expected_position in test_inputs:
		position = find_position(input, -1)
		assert expected_position == position, \
			"Expected {} to be {} with input: {}". format(position, expected_position, input)


if __name__ == "__main__":
   main()
   test()