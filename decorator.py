import time

def task_2(a):
    print("task2")
    yield "x"
    yield "xx"

def task_3(b):
    print("task3")
    yield "yy"
    yield "yy"

def task_4(a, b):
    print("task 4")
    yield "xy"
    yield "xyxy"

def test():

    yield task_2(2)
    yield task_3(2)
    yield task_4(2, 3)

for i in test():
    time.sleep(1)
    for j in i:
        time.sleep(1)
        print(j)
