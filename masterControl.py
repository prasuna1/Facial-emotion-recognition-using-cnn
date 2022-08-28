"""
master control

"""

import applicationInterface as app
import cnnInterface as cnn
import dataInterface as data

if __name__ == '__main__':
	"""Runs the entire application"""
	cnn.loadModel()
	print("====================Main Interface====================")
	while True:
		print("\nOptions:\n1. Run Applications.\n2. Exit")
		opt = input("Enter the option number : ")
		if opt == "1":
			app.interface()
		
		elif opt == "2":
			break
		else:
			print("Invalid option")
