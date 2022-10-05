n = int(input("Задайте число - "))


def fib_and_neg(n):
    norm_fib = [1, 1]
    neg_fib = [1, -1]

    for i in range(2, n):
        #norm = norm_fib[i-1]+norm_fib[i-2]
        norm_fib.append(norm_fib[-1] + norm_fib[-2])
        neg_fib.append(neg_fib[-2] - neg_fib[-1])

    neg_fib.reverse()
    neg_fib.append(0)
    print(neg_fib+norm_fib)


fib_and_neg(n)
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
