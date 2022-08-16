
N,A,B = map(int,input().split())

white = '.'
black = '#'

odd_line = ''
even_line = ''

for n in range(N):
    if n % 2 == 0:
        odd_add = white
        even_add = black
    else:
        odd_add = black
        even_add = white
    
    for b in range(B):
        odd_line += odd_add
        even_line += even_add

for n in range(N):
    if n % 2 == 0:
        line = odd_line
    else:
        line = even_line
    for a in range(A):
        print(line)
