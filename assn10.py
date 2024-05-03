import threading

no = [1,2,3,4,5]

def sqaure():
    for i in no:
        print(pow(i,2))


def cube():
    for i in no:
        print(pow(i,3))

t1= threading.Thread(target = sqaure)
t2= threading.Thread(target = cube)

t1.start()
t2.start()

t1.join()
t2.join()