year, month, day = map(int, input().split())
print(f"{year} {month} {day}")

m = [31,28,31,30,31,30,31,31,30,31,30,31]

print(m[0,month])