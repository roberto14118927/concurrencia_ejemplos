import time
import threading

def method1():
    time.sleep(5)
    print("Method1")

def method2():
    time.sleep(2)
    print("Method2")

def method3():
    time.sleep(2)
    print("Method3")

def method4():
    time.sleep(2)
    print("Method4")

method1()
method2()
method3()
method4()