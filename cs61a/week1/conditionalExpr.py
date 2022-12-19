def func1(x):
    return abs(1/x if x!=0 else 0)
if __name__ == '__main__':
    print(func1(1))
    print(func1(0))
    print(func1(-1))
    