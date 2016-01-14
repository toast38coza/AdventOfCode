import unittest

class Present:

	def __set_lwh(self, str):		
		self.l, self.w, self.h = map(int, str.strip().split("x"))

	def __init__(self, str):
		self.str = str 

		self.__set_lwh(str)

	def __show_working(self):

		smallest_side = self.get_smallest_side()
		return "Input = {}\n. Size: {}\n Smallest side area: {}x{} = {}" \
			. format (self.str, 
					  self.get_size(), 
					  smallest_side[0],
					  smallest_side[1], 
					  self.get_area(smallest_side))

	def get_size(self):
		
		return 2*self.l*self.w + 2*self.w*self.h + 2*self.h*self.l

	def get_smallest_side(self):
		
		l = [self.l, self.w, self.h]
		l.sort()
		return l[0:2]

	def get_area(self, dimensions):
		
		return dimensions[0]*dimensions[1]

	def get_volume(self):
		return self.l*self.w*self.h

	def get_wrapping_paper_area(self):
		
		return self.get_size() + self.get_area(self.get_smallest_side())

	def get_ribbon_length(self):
		side = self.get_smallest_side()

		to_tie = side[0]+side[0]+side[1]+side[1]
		vol = self.get_volume()
		return to_tie + vol
	

def main():
	total_area = 0
	total_ribbon = 0
	f = open('../input.txt', 'r')
	present_dimensions = f.read().splitlines()
	
	for present_dimension in present_dimensions:
		present = Present(present_dimension)
		present_area = present.get_wrapping_paper_area()
		#print "{}. Area: {}". format(present_dimension, present_area)
		total_area += present_area 

		present_ribbon = present.get_ribbon_length()
		total_ribbon += present_ribbon
		
	print "Total area: {}" . format(total_area)
	print "Ribbon required: {}" . format(total_ribbon)


if __name__ == '__main__':
    main()	

