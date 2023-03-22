x = 3
 
# Traditional way
if x % 2 == 1:
result = f"{x} is odd"
else:
    result = f"{x} is even"
 
# Pythonic way
result = f"{x} " + ("is odd" if x % 2 == 1 else "is even")
 
# Result
print(result)
# Shows: 3 is odd