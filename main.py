
def a():
    myString = "helLo woRld"
    myString1 = myString.lower()
    myString2 = myString.upper()
    myString3 = myString.capitalize()

    print("Original string: " + myString)
    print("Lowered string: " + myString1)
    print("Uppered string: " + myString2)
    print("Capitalized string: " + myString3)

def b():
    myStr = "Drury"
    myStr1 = myStr.replace('r', 'replaced')
    print("Original String: " + myStr)
    print("Replaced String: " + myStr1)

def c():
    myStr = "Split at every space"
    print("Original String: " + myStr)
    myStr = myStr.split(" ")
    print("String Split at Space:", myStr)

def d():
    myList = ['l','i','s','t']
    print("Original List:", myList)
    myString = "".join(myList)
    print("New String:", myString)
    myString = " ".join(myList)
    print("String with Spaces:", myString)
    print("Join daisy with M,A,Y:", "daisy".join(['M','A','Y']))

def e():
    myList = [2,3,4]
    print("myList:", myList)
    myList.append(5)
    print("myList.append(5):", myList)
    myList.append(1)
    print("myList.append(1):", myList)

def f():
    myList = [7,3,5,2]
    myString = "gfedcba"
    print("myList:", myList)
    myList = sorted(myList)
    print("myList Sorted:", myList)
    print("myString:", myString)
    myString = sorted(myString)
    print("myString Sorted:", myString)

def g():
    print("type(5):", type(5))
    print("type(5.3):", type(5.3))
    print("type('myString'):",type('myString'))
    print("type(['l','i','s','t']):", type(['l','i','s','t']))

def h():
    print("len([5,8,3,4,2,1]):", len([5,8,3,4,2,1]))
    print("len('qwertyuiop'):", len("qwertyuiop"))

def i():
    print("[1,2,3]+[4,5,6]:", [1,2,3] + [4,5,6])
    print("'abc' + 'cde':", "abc" + "cde")

def j():
    myList = ['hi', 'bye', 'hello', 'goodbye']
    print(myList)
    for i in range(0, len(myList)):
        if myList[i] == 'bye':
            myList[i] = 'replaced'
    print(myList)



j()