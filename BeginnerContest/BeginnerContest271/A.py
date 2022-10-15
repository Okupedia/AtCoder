N = int(input()) #整数一つ

hex_num = hex(N)[2:]

print(hex_num.zfill(2).upper())
