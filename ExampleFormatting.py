"""
ExampleFormatting.py
ProjectName
"""

from Database import CONSTANT_1, CONSTANT_2, CONSTANT_3
from OtherFile import OtherClass
import OtherLib



class Class1:
	

	def function_1():

		## Section Comment:
		some_var = None
		pass
		pass
		pass

		## Section Comment:
		pass
		pass
		pass


	### REGION COMMENT ###


	def function_2():
		
		print("") # Specific Line comment
		
		pass
		pass
		pass


	def function_3():
		
		## Debug comments:
		#### pass
		pass #### "Debug Line" annotation


	### REGION COMMENT ###


	def function_4(): pass



class Class2: pass