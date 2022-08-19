def check_list(list):
	length = len(list)
	if length==0:
		output=1
	else:
		for i in range(length-1):
			if list[i+1]-list[i]>1:
				output = list[i]+1
				return output
		output = list[length-1]+1
	return output

N=int(input())
list = []

while N != 0:
	output=check_list(list)
	list.append(output)
	list.sort()
	print(output,flush=True)
	N=int(input())
	list.append(N)
	list.sort()
