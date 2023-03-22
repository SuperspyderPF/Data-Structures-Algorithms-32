# Traditional way
a = 1
b = "ok"
 
c = a
a = b
b = c
 
# Pythonic way
a, b = 1, "ok"
a, b = b, a
 
# Result
print(a, b)
# Shows: ok 1