# Write a function that accepts an array of 10 integers (between 0 and 9),
# that returns a string of those numbers in the form of a phone number.
def create_phone_number(n):
    s = "(" + str(n[0]) + str(n[1])+ str(n[2]) + ") " + str(n[3]) + str(n[4]) + \
    str(n[5]) + "-"  + str(n[6]) + str(n[7])+ str(n[8]) + str(n[9])
    return s

def create_phone_number_01(n):
    return '({}{}{}) {}{}{}-{}{}{}{}'.format(*n)

print (create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print (create_phone_number_01([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
