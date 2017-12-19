""" Codibility Lesson 1 Examples """


def factorial(n):
    """
    We are given some positive integer n. Let’s compute the factorial of n and
    assign it to the variable factorial. The factorial of n is n! = 1 · 2 · ...
    · n. We can obtain it by starting with 1 and multiplying it by all the
    integers from 1 to n. """

    r = 1

    for i in range(1, n + 1):
        r *= i

    return r


def asterisks_triangle(n):
    """
    Let’s print a triangle made of asterisks (‘*’) separated by spaces. The
    triangle should consist of n rows, where n is a given positive integer, and
    consecutive rows should contain 1, 2, ... , n asterisks. For example, for n
    = 4 the triangle should appear as follows:

    *
    * *
    * * *
    * * * *
    """

    r = ""

    for i in range(1, n + 1):
        for j in range(i):
            r += "* "
        r += "\n"

    return r.strip()


def asterisks_triangle_sym(n):
    """
    Let’s print a triangle made of asterisks (‘*’) separated by spaces and
    consisting of n rows again, but this time upside down, and make it
    symmetrical. Consecutive rows should contain 2n − 1, 2n − 3, ... , 3, 1
    asterisks and should be indented by 0, 2, 4, ... , 2(n − 1) spaces. For
    example, for n = 4 the triangle should appear as follows:

    * * * * * * *
      * * * * *
        * * *
          *
    """

    r = ""

    for i in range(n, 0, -1):
        for j in range(n - i):
            r += "  "
        for j in range(2 * i - 1):
            r += "* "
        r += "\n"

    return r.strip()


def count_digits(n):
    """
    Given a positive integer n, how can we count the number of digits in its
    decimal representation? One way to do it is convert the integer into a
    string and count the characters. Here, though, we will use only arithmetical
    operations instead. We can simply keep dividing the number by ten and count
    how many steps are needed to obtain 0.
    """

    r = 0

    while n > 0:
        n //= 10
        r += 1

    return r


def fibonacci(n):
    """
    The Fibonacci numbers form a sequence of integers defined recursively in the
    following way. The first two numbers in the Fibonacci sequence are 0 and 1,
    and each subsequent number is the sum of the previous two. The first few
    elements in this sequence are: 0, 1, 1, 2, 3, 5, 8, 13. Let’s write a
    program that prints all the Fibonacci numbers, not exceeding a given integer
    n.
    """

    r = []

    a = 0
    b = 1
    while a <= n:
        r.append(a)
        c = a + b
        a = b
        b = c

    return r


def binary_gap(n):
    """
    A binary gap within a positive integer N is any maximal sequence of
    consecutive zeros that is surrounded by ones at both ends in the binary
    representation of N.

    For example, number 9 has binary representation 1001 and contains a binary
    gap of length 2. The number 529 has binary representation 1000010001 and
    contains two binary gaps: one of length 4 and one of length 3. The number 20
    has binary representation 10100 and contains one binary gap of length 1. The
    number 15 has binary representation 1111 and has no binary gaps.

    Write a function:

    def solution(N)

    that, given a positive integer N, returns the length of its longest binary
    gap. The function should return 0 if N doesn't contain a binary gap.

    For example, given N = 1041 the function should return 5, because N has
    binary representation 10000010001 and so its longest binary gap is of length
    5.

    Assume that:

    N is an integer within the range [1..2,147,483,647]. Complexity:

    expected worst-case time complexity is O(log(N)); expected worst-case space
    complexity is O(1).
    """

    nbin = bin(n)[2:]

    ones = 0
    zeros = 0
    gap = 0

    for char in nbin:
        if char == "1":
            ones += 1
            gap = zeros if zeros > gap else gap
            zeros = 0
        if ones > 0 and char == "0":
            zeros += 1

    return (nbin, gap)


if __name__ == "__main__":

    print("\nCodibility Lesson 1\n\n")

    print(f"factorial(10)\n{factorial(10)}\n")
    print(f"asterisks_triangle(4)\n{asterisks_triangle(4)}\n")
    print(f"asterisks_triangle_sym(4)\n{asterisks_triangle_sym(4)}\n")
    print(f"count_digits(112180444)\n{count_digits(112180444)}\n")
    print(f"fibonacci(100)\n{fibonacci(100)}\n")

    print(f"binary_gap(1041)\n{binary_gap(1041)}\n")

    # 1 00000 1 000 1
