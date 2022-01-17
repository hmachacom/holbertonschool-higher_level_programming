#!/user/bin/python3
from hashlib import new
from operator import ne


def list_division(my_list_1, my_list_2, list_length):
	new_list = []
	e = 0
	num = 0
	for i in range(list_length):
		try:
			num = my_list_1[i] / my_list_2[i]
			new_list.append(num)
		except ZeroDivisionError:
			num = 0
		except IndexError:
			num = 0
		except ValueError:
			num = 0
		except TypeError:
			num = 0
		finally:
			new_list.append(num)
	return new_list
