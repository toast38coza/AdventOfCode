"""
How many houses receive at least one present?

Algorithm: 

Start at point [0:0]
Follow directions. Place each new location into a set
Find the length of the set
"""

def move(direction, current_position): 
	
	if direction == ">":
		current_position[1] += 1 
	if direction == "<":
		current_position[1] -= 1 
	if direction == "^":
		current_position[0] += 1 
	if direction == "v":
		current_position[0] -= 1 

	return current_position

def save(position, houses_visited):
	position_string = "{}:{}" . format (position[0], position[1])
	houses_visited.add(position_string)
	return houses_visited

def get_houses(input):
	
	houses_visited = set(["0:0"])
	current_position = [0,0]

	for char in input:
		new_position = move(char, current_position)
		houses_visited = save(current_position, houses_visited)

	return len(houses_visited)

def main():
	input = open('../input.txt', 'r').read()
	answer = get_houses(input)
	print answer

if __name__ == '__main__':
    main()			