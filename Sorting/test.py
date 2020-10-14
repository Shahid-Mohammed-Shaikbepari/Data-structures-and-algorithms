def fun():
    s =9
    def inner():
        s = 2
        print(s)
    inner()
    print(s)
fun()