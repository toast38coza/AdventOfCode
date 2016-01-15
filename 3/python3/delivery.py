"""
How many houses receive at least one present?

Algorithm: 

Start at point [0:0]
Follow directions. Place each new location into a set
Find the length of the set
"""

class Santa:

	def __init__(self):
		self.houses_visited = set(["0:0"])
		self.current_position = [0,0]

	def __save(self):
		position_string = "{}:{}" . format (self.current_position[0], self.current_position[1])
		self.houses_visited.add(position_string)

	def move(self, direction): 
		
		direction_map = {
			# direction: (co-ordinate (up/down or east/west), positive or negative) 
			">": (1,1),
			"<": (1,-1),
			"^": (0,1),
			"v": (0,-1),
		}
		co_ordinate = direction_map[direction][0]
		direction = direction_map[direction][1]
		self.current_position[co_ordinate] += direction

		"""
		# the map feels a little more elegant, 
		# but the if's are a little easier to read
		if direction == ">":
			current_position[1] += 1 
		if direction == "<":
			current_position[1] -= 1 
		if direction == "^":
			current_position[0] += 1 
		if direction == "v":
			current_position[0] -= 1 
		"""
		self.__save()
		return self.current_position

	

def get_single_santa_trip(input):
	
	santa = Santa()
	for char in input:
		santa.move(char)

	return len(santa.houses_visited)

def count_houses_with_robo_santa(input):

	santa = Santa()
	robo_santa = Santa()
	for index, char in enumerate(input):
		if index%2 == 0:
			santa.move(char)
		else:
			robo_santa.move(char)

	santa_houses = len(santa.houses_visited)
	robo_houses = len(robo_santa.houses_visited)

	# this is the simple way of doing it (handles this specific case)
	# more efficient, but less _correct_
	# return santa_houses + robo_houses -1

	# this is a little less efficient (you have to union two sets which is: O(len(s)+len(t)) )
	# but does make this method more reliable/flexible and less prone to surprising outputs
	return len(santa.houses_visited.union(robo_santa.houses_visited))


def main():
	input = open('../input.txt', 'r').read()
	part_one_answer = get_single_santa_trip(input)
	print "Houses visited by a single santa: {}" . format (part_one_answer)

	part_two_answer = count_houses_with_robo_santa(input)
	print "Houses visited by santa and robo-santa: {}" . format (part_two_answer)


if __name__ == '__main__':
    main()			