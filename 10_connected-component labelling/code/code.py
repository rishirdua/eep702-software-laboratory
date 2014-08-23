#!/usr/bin/python

#
# Implements 8-connectivity connected component labeling
# 
# Algorithm obtained from "Optimizing Two-Pass Connected-Component Labeling 
# by Kesheng Wu, Ekow Otoo, and Kenji Suzuki
#



import sys
import math, random
from itertools import product
from ufarray import *
import numpy as np
def eightconnected(img):
	data = 1-img
	(width, height) = img.shape
	# Union find data structure
	uf = UFarray()
 
	#
	# First pass
	#
 
	# Dictionary of point:label pairs
	labels = {}
 
	for y, x in product(range(height), range(width)):
		
		#
 
		# If the current pixel is white, it's obviously not a component...
		if data[x, y] == 1:
			pass
 
		# If pixel b is in the image and black:
		#    a, d, and c are its neighbors, so they are all part of the same component
		#    Therefore, there is no reason to check their labels
		#    so simply assign b's label to e
		elif y > 0 and data[x, y-1] == 0:
			labels[x, y] = labels[(x, y-1)]
 
		# If pixel c is in the image and black:
		#    b is its neighbor, but a and d are not
		#    Therefore, we must check a and d's labels
		elif x+1 < width and y > 0 and data[x+1, y-1] == 0:
 
			c = labels[(x+1, y-1)]
			labels[x, y] = c
 
			# If pixel a is in the image and black:
			#    Then a and c are connected through e
			#    Therefore, we must union their sets
			if x > 0 and data[x-1, y-1] == 0:
				a = labels[(x-1, y-1)]
				uf.union(c, a)
 
			# If pixel d is in the image and black:
			#    Then d and c are connected through e
			#    Therefore we must union their sets
			elif x > 0 and data[x-1, y] == 0:
				d = labels[(x-1, y)]
				uf.union(c, d)
 
		# If pixel a is in the image and black:
		#    We already know b and c are white
		#    d is a's neighbor, so they already have the same label
		#    So simply assign a's label to e
		elif x > 0 and y > 0 and data[x-1, y-1] == 0:
			labels[x, y] = labels[(x-1, y-1)]
 
		# If pixel d is in the image and black
		#    We already know a, b, and c are white
		#    so simpy assign d's label to e
		elif x > 0 and data[x-1, y] == 0:
			labels[x, y] = labels[(x-1, y)]
 
		# All the neighboring pixels are white,
		# Therefore the current pixel is a new component
		else: 
			labels[x, y] = uf.makeLabel()
 
	#
	# Second pass
	#
 
	uf.flatten()
	
	colors = {}

	# Image to display the components in a nice, colorful way
	

	for (x, y) in labels:
 
		# Name of the component the current point belongs to
		component = uf.find(labels[(x, y)])

		# Update the labels with correct information
		labels[(x, y)] = component

		

	return labels

def fourconnected(img):
	data = 1-img
	(width, height) = img.shape
	# Union find data structure
	uf = UFarray()
 
	#
	# First pass
	#
 
	# Dictionary of point:label pairs
	labels = {}
 
	for y, x in product(range(height), range(width)):
		#
		# If the current pixel is white, it's obviously not a component...
		if data[x, y] == 1:
			pass
 
		# If pixel b is in the image and black:
		#    a, d, and c are its neighbors, so they are all part of the same component
		#    Therefore, there is no reason to check their labels
		#    so simply assign b's label to e
		else:
			if x>0 and y>0:
				if data[x, y-1] == 0:
					labels[x, y] = labels[(x, y-1)]
				if data[x-1, y] == 0 and data[x,y-1] == 0:
					d = labels[(x-1, y)]
					b = labels[(x, y-1)]
					if (b != d):
						uf.union(b, d)
				if data[x-1, y] == 0 and data[x,y-1] == 1:
					labels[x, y] = labels[(x-1, y)]
				if data[x-1, y] == 1 and data[x,y-1] == 1: 
					labels[x, y] = uf.makeLabel()
			if x>0 and y==0:
				if data[x-1, y] == 0:
					labels[x, y] = labels[(x-1, y)]
				else:
					labels[x, y] = uf.makeLabel()
			if x==0 and y>0:
				if data[x, y-1] == 0:
					labels[x, y] = labels[(x, y-1)]
				else:
					labels[x, y] = uf.makeLabel()
			if x==0 and y==0:
				labels[x, y] = uf.makeLabel()

 
	#
	# Second pass
	#
 
	#uf.flatten()
	
	colors = {}

	

	for (x, y) in labels:
 
		# Name of the component the current point belongs to
		component = uf.find(labels[(x, y)])

		# Update the labels with correct information
		labels[(x, y)] = component

		

	return labels    
 
def main():
	#Take input
	print "Provide pixel values"
	print "For example: 1,1,0,0,0;0,1,0,0,1;1,0,0,1,1;0,0,0,0,0;1,0,1,0,1"
	user_data = raw_input("Press Enter for default input\t")
	if (user_data==""):
		user_data = '1,1,0,0,0;0,1,0,0,1;1,0,0,1,1;0,0,0,0,0;1,0,1,0,1';
	try:
		img = np.mat(user_data)
	except:
		print "Error in taking input"
	else:
		print "You have entered:"
		print img
		print "Matrix dimensions:"
		print img.shape
		#if (img.shape==(5,5)):
			# labels is a dictionary of the connected component data in the form:
			#     (x_coordinate, y_coordinate) : component_id

		#Part A
		print "Using 4 connected labelling"
		labels = fourconnected(img)
		print labels
		print "The number of islands is:"
		print  len(set(labels.values()))

		#Part B
		print "Using 8 connected labelling"
		labels = eightconnected(img)
		print labels
		print "The number of islands is:"
		print  len(set(labels.values()))
		
		#Part c
		print "Checking water body labelling"
		user_x = int(raw_input("Enter m:\t"))
		user_y = int(raw_input("Enter n:\t"))
		try:

			if (img[user_x,user_y] == 0):
				print "water"
			else:
				print "land"
				print "Island number", labels[(user_x,0)]
		except:
			print "Error in entered values of m and n"
	
	

if __name__ == "__main__": main()
