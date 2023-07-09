def sum(*args):
    count = 0
    for arg in args:
        if isinstance(arg, list):
            count += sum(*arg)
        else:
            count += arg
    return count




print(sum(1, 2, 3, 4, 5))