def diagonal_AC(diagonal_AC_slope, Cx, Cy, x):
    y = diagonal_AC_slope*(x-Cx)+Cy
    return y

def diagonal_BD(diagonal_BD_slope, Dx, Dy, x):
    y = diagonal_BD_slope*(x-Dx)+Dy
    return y

Ax, Ay = map(int,input().split()) #それぞれ別の変数
Bx, By = map(int,input().split()) #それぞれ別の変数
Cx, Cy = map(int,input().split()) #それぞれ別の変数
Dx, Dy = map(int,input().split()) #それぞれ別の変数

#対角線の両サイドに点があることが条件

if (Ax-Cx) == 0:
    if Bx < Ax and Dx < Ax:
        print('No')
    elif Bx > Ax and Dx > Ax:
        print('No')
    else:
        print('Yes')
    exit()
elif (Bx-Dx) == 0:
    if Ax < Bx and Cx < Bx:
        print('No')
    elif Ax > Bx and Cx > Bx:
        print('No')
    else:
        print('Yes')
    exit()
else:
    diagonal_AC_slope = (Ay-Cy)/(Ax-Cx) #傾き
    #y = diagonal_AC_slope(x-Cx)+Cy
    diagonal_BD_slope = (By-Dy)/(Bx-Dx) #傾き
    #y = diagonal_BD_slope(x-Dx)+Dy

    if diagonal_AC(diagonal_AC_slope, Cx, Cy, Bx) > By:
        if diagonal_AC(diagonal_AC_slope, Cx, Cy, Dx) > Dy:
            print('No')
            exit()
    else:
        if diagonal_AC(diagonal_AC_slope, Cx, Cy, Dx) < Dy:
            print('No')
            exit()

    if diagonal_BD(diagonal_BD_slope, Dx, Dy, Ax) > Ay:
        if diagonal_BD(diagonal_BD_slope, Dx, Dy, Cx) > Cy:
            print('No')
            exit()
    else:
        if diagonal_BD(diagonal_BD_slope, Dx, Dy, Cx) < Cy:
            print('No')
            exit()
    print('Yes')