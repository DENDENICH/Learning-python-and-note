from functools import singledispatchmethod

class MyClass:
	@singledispatchmethod
	def base_implement(self, arg):
		print("Базовый метод")

	@base_implement.register(int)
	def int_implement(self, arg):
		print(int)
