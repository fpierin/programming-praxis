"""
Minimum And Maximum

July 4, 2014

We have today a two-part interview question:

    First, write a program that takes an array of integers and returns the minimum and maximum elements of the array. Use as few comparisons as possible.

    Second, write a program that takes an array of integers and returns the second minimum and maximum elements of the array; that is, the second-smallest element and the second-largest element. Again, use as few comparisons as possible.

Your task is to write the two programs described above, and state the number of comparisons each makes in the general case; be sure they are proof against malicious input. When you are finished, you are welcome to read or run a suggested solution, or to post your own solution or discuss the exercise in the comments below.

"""
import sys
from array import *

def maxmin(a):
	max = -sys.maxint -1
	min = sys.maxint
	for i in a:
		if i < min:
			min = i
		elif i > max:
			max = i
	print "Max value is:", max
	print "Min value is:", min

def main():
	a = array('i', [-1,12,-5,0,24])
	maxmin(a);

if __name__ == '__main__':
	main()
