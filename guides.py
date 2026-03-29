# start up file

x = 7
y = x + 1 # y = 8
y = y + 2 # y = 10
z = x + 2 * y # z = 7 + 2 * 10 = 27 multiplication has priority?
z = z - 1 # z = 26
print("Final value of z is", z)