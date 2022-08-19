K = int(input())

h = 21
while(K >= 60):
	h += 1
	K -= 60

print(h, ":", str(K).zfill(2), sep="")