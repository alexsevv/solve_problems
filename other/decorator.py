# декоратор
def dekorator(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        print(f"Start function: {start}")
        func(*args, **kwargs)
        print(f"Finish function: {start}")
        end = time.time()
        print(f'[*] Время выполнения: {(end-start)} секунд.')
    return wrapper


@dekorator
def summa(a, b):
    print(a + b)


summa(5, 1328)
