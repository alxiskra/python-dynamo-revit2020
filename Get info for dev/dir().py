if isinstance(IN[0], list):
	ele = UnwrapElement(IN[0])[0]
else:
	ele = UnwrapElement(IN[0])
OUT = dir(ele)
