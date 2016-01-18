from time import perf_counter as pc

class NiceString:

	def __init__(self, str):
		self.str = str 

	def has_recurring_pair(self):
		"""
		Store each pair as an index in a hash 
		Value = its location in the string. 
		If hash exists and location is further than 1 away, True
		"""
		pairs = {}
		last_char = None
		for index, char in enumerate(self.str):
			if last_char is not None:
				pair = "{}{}" . format (last_char, char)
				pair_location = pairs.get(pair, False)

				if pair_location: 
					## if a pair already exists, then we 
					# don't need to add this to the hash 
					# (we know it exists, and the other location is more reliable)
					if (pair_location+1) < index:
						return True 
				else:
					pairs[pair] = index 
			
			last_char = char
		return False

	def is_pair(self, index, collection):
		if index == 0: return False 
		return collection[index] == collection[index-1]

	def has_pair(self, arr):
		for index, char in enumerate(arr):
			if self.is_pair(index, arr):
				return True

		return False


	def has_repeating_interrupted_pair(self):
		"""
		It contains at least one letter which repeats 
		with exactly one letter between them, 
		like xyx, abcdefeghi (efe), or even aaa.
		"""
		odd_pairs = self.str[::2]
		even_pairs = self.str[1:][::2]

		if self.has_pair(odd_pairs):
			return True 
		if self.has_pair(even_pairs):
			return True 
		return False
			

	def is_nice_new(self):
		
		if self.has_recurring_pair() and self.has_repeating_interrupted_pair():
			return True 
		else:
			return False


	def is_nice(self):
		
		vowel_count = 0
		has_consecutive = False
		last_letter = None
		
		if self.contains_disallowed_chars(): return False
		
		for char in self.str:

			last_two = "{}{}" . format (last_letter, char)
			if vowel_count < 3:
				if char in ['a','e','i','o','u']:
					vowel_count += 1

			if last_letter == char:
				has_consecutive = True

			if vowel_count >= 3 and has_consecutive:
				return True
			last_letter = char
		return False

	def contains_disallowed_chars(self):

		disallowed_strings = ['ab', 'cd', 'pq', 'xy']
		for str in disallowed_strings:
			if str in self.str:
				return True 

		return False

def main():
	start_time = pc()
	nice_strings = 0
	f = open('../input.txt', 'r')
	strings = f.read().splitlines()
	for string in strings: 
		if NiceString(string).is_nice():
			nice_strings += 1

	stop_time = pc()-start_time

	print ("There are {} nice strings" . format (nice_strings))

	print ("-----")
	print ("Time: {}" . format (stop_time - start_time))
	print ("*****")

	start_time = pc()

	nice_strings = 0
	for string in strings: 
		if NiceString(string).is_nice_new():
			nice_strings += 1

	stop_time = pc()-start_time
	print ("Now there are {} nice strings" . format (nice_strings))
	print ("Time: {}" . format (stop_time - start_time))
	print ("*****")

if __name__ == '__main__':
	main()		