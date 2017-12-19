""" Codibility Lesson 1 Examples """


def factorial(n):
    """
    We are given some positive integer n. Let’s compute the factorial of n and
    assign it to the variable factorial. The factorial of n is n! = 1 · 2 · ...
    · n. We can obtain it by starting with 1 and multiplying it by all the
    integers from 1 to n. """

    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


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

    result = ""
    for i in range(1, n + 1):
        for j in range(i):
            result += "* "
        result += "\n"
    return result.strip()


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

    result = ""
    for i in range(n, 0, -1):
        for j in range(n - i):
            result += "  "
        for j in range(2 * i - 1):
            result += "* "
        result += "\n"
    return result.strip()


def count_digits(n):
    """
    Given a positive integer n, how can we count the number of digits in its
    decimal representation? One way to do it is convert the integer into a
    string and count the characters. Here, though, we will use only arithmetical
    operations instead. We can simply keep dividing the number by ten and count
    how many steps are needed to obtain 0.
    """

    result = 0
    while n > 0:
        n //= 10
        result += 1
    return result


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


if __name__ == "__main__":

    print("\nCodibility Examples\n\n")
    print(f"factorial(10)\n{factorial(10)}\n")
    print(f"asterisks_triangle(4)\n{asterisks_triangle(4)}\n")
    print(f"asterisks_triangle_sym(4)\n{asterisks_triangle_sym(4)}\n")
    print(f"count_digits(112180444)\n{count_digits(112180444)}\n")
    print(f"fibonacci(100)\n{fibonacci(100)}\n")
