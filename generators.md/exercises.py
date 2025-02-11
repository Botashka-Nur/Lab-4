#Ex1
def square_generator(n):
    for i in range(n + 1):
        yield i ** 2

n = int(input())
print( list(square_generator(n)))


#Ex2
def even_generator(n):
    return (i for i in range(n + 1) if i % 2 == 0)

n = int(input())
print("Even numbers".join(map(str, even_generator(n))))


#Ex3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
print("3-ке және 4-ке бөлінетін сандар:", list(divisible_by_3_and_4(n)))


#Ex4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input())
b = int(input())

for num in squares(a, b):
    print(num)



#Ex5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())

for num in countdown(n):
    print(num)
    




