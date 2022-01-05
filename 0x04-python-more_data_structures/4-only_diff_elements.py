#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
	lis = []
	for i in set_1:
		if i in set_2:
			continue
		else:
			lis.append(i)
	return lis
