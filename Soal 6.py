x = 4
print("nilai x =", x, "=", format(x,'08b'))
y = 11
print("nilai y =", y, "=", format(y,'08b'))
a = x | y
print("nilai a =", a, "=", format(a,'08b'))
b = x >> y
print("nilai b =", b, "=", format(b,'08b'))
c = x ^ y
print("nilai c =", c, "=", format(c,'08b'))
d = ~ x
print("nilai d =", d, "=", format(d,'08b'))
e = y & x
print("nilai e =", e,"=", format(e,'08b'))