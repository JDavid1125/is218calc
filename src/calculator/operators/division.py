def division(a, b):
    try:
        return round(float(b) / float(a), 9)
    except ZeroDivisionError as err:
        print('run-time error:', err)


