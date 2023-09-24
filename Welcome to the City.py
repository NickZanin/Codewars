# DESCRIPTION:

def say_hello_1(name, city, state):
    print(len(name))
    s = ""
    i = 0
    while i < len(name):
        s = s + name[i] + " "
        print(s)
        i += 1
    s =  s.strip()
    s = "Hello, " + s +"! Welcome to " + city + ", " + state + "!"
    return s

# def say_hello(name, city, state):
#   return "Hello, {}! Welcome to {}, {}!".format(" ".join(name), city, state)

def say_hello(name, city, state):
    return f"Hello, {' '.join(name)}! Welcome to {city}, {state}!"
print (say_hello(['Alex', 'Gibadov'], 'Phoenix', 'Arizona'))