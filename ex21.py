def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def mutiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divde(a, b):
    print "DIVDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just fuctions!"

age = add(30, 5)
height = subtract(78, 4)
weight = mutiply(90, 3)
iq = divde(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle."

what = add (age, subtract(height, mutiply(weight, divde(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"