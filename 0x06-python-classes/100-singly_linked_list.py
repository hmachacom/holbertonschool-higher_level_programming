#!/usr/bin/python3
""" class Node new """


class Node:
	"""class node an singly linked list"""

	def __init__(self, data, next_node=None):
		self.data = data
		self.next_node = next_node

	@property
	def data(self):
		"""value interger"""
		return self.__data
	
	@data.setter
	def data(self, value):
		"""check interger"""
		if type(value) != int:
			raise TypeError("data must be an integer")
		self.__data = value
	
	@property
	def next_node(self):
		"""next node"""
		return self.__next_node
	
	@next_node.setter
	def next_node(self, value):
		"""Check next node"""
		if type(value) != None or type(value) != Node:
			raise TypeError("next_node must be a Node object")
		self.__next_node = value

class SinglyLinkedList:
	"""class SinglyLinkedList"""

	def __init__(self):
		""" Inicializer SinglyLinkedList"""
		self.__head = Node
	def sorted_insert(self, value):
		if self.__head is None:
			self.__head = Node(value)
		elif value < self.__head.data:
			self.__head = Node(value, self.__head)

	



		