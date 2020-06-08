
if __name__ == '__main__':
    try:
        print('try...')
        r = 10 / 0
        print('result:', r)
    except ZeroDivisionError as e:
        print('except:', e)
    finally:
        print('finally...')
    print('END')

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')