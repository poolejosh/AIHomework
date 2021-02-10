from constraint import *
base = 10


def a():
    print("Problem a.\n")

    # init problem
    problem = Problem()
    # add var for each unique letter
    # each var will be a number in a range 0-9
    # vars for first letter of word will be range 1-9 to avoid leading zeros
    problem.addVariable('s', range(1, base))
    problem.addVariable('i', range(base))
    problem.addVariable('n', range(base))
    problem.addVariable('c', range(1, base))
    problem.addVariable('e', range(base))
    problem.addVariable('j', range(1, base))
    problem.addVariable('u', range(base))
    problem.addVariable('l', range(base))
    problem.addVariable('a', range(base))
    problem.addVariable('r', range(base))
    # enforce different number for each var
    problem.addConstraint(AllDifferentConstraint())

    # create function describing the cryptarithmetic
    def func(s, i, n, c, e, j, u, l, a, r):
        word_1 = s * (base ** 4) + i * (base ** 3) + n * (base ** 2) + c * base + e
        word_2 = j * (base ** 5) + u * (base ** 4) + l * (base ** 3) + i * (base ** 2) + u * base + s
        solution = c * (base ** 5) + a * (base ** 4) + e * (base ** 3) + s * (base ** 2) + a * base + r

        return word_1 + word_2 == solution

    # add constraint for function above passing in letter vars
    problem.addConstraint(FunctionConstraint(func), ['s', 'i', 'n', 'c', 'e', 'j', 'u', 'l', 'a', 'r'])

    # print a solution
    print("\t since")
    print("+\tjulius")
    print("----------")
    print("=\tcaesar")

    print("\nSolution(s):")
    solutions = problem.getSolutions()
    for solution in solutions:
        print(f"\n\t {solution['s']}{solution['i']}{solution['n']}{solution['c']}{solution['e']}")
        print(f"+\t{solution['j']}{solution['u']}{solution['l']}{solution['i']}{solution['u']}{solution['s']}")
        print("----------")
        print(f"=\t{solution['c']}{solution['a']}{solution['e']}{solution['s']}{solution['a']}{solution['r']}")

    print()


def b():
    print("Problem b.\n")

    # init problem
    problem = Problem()
    # add var for each unique letter
    # each var will be a number in a range 0-9
    # vars for first letter of word will be range 1-9 to avoid leading zeros
    problem.addVariable('c', range(1, base))
    problem.addVariable('h', range(base))
    problem.addVariable('e', range(base))
    problem.addVariable('k', range(base))
    problem.addVariable('t', range(1, base))
    problem.addVariable('i', range(base))
    problem.addVariable('r', range(base))
    problem.addVariable('s', range(base))
    # enforce different number for each var
    problem.addConstraint(AllDifferentConstraint())

    # create function describing the cryptarithmetic
    def func(c, h, e, k, t, i, r, s):
        word_1 = c * (base ** 4) + h * (base ** 3) + e * (base ** 2) + c * base + k
        word_2 = t * (base ** 2) + h * base + e
        solution = t * (base ** 4) + i * (base ** 3) + r * (base ** 2) + e * base + s

        return word_1 + word_2 == solution

    # add constraint for function above passing in letter vars
    problem.addConstraint(FunctionConstraint(func), ['c', 'h', 'e', 'k', 't', 'i', 'r', 's'])

    # print a solution
    print("\tcheck")
    print("+\t  the")
    print("---------")
    print("=\ttires")

    print("\nSolution(s):")
    solutions = problem.getSolutions()
    for solution in solutions:
        print(f"\n\t{solution['c']}{solution['h']}{solution['e']}{solution['c']}{solution['k']}")
        print(f"+\t  {solution['t']}{solution['h']}{solution['e']}")
        print("---------")
        print(f"=\t{solution['t']}{solution['i']}{solution['r']}{solution['e']}{solution['s']}")

    print()


def c():
    print("Problem c.\n")

    # init problem
    problem = Problem()
    # add var for each unique letter
    # each var will be a number in a range 0-9
    # vars for first letter of word will be range 1-9 to avoid leading zeros
    problem.addVariable('d', range(1, base))
    problem.addVariable('o', range(base))
    problem.addVariable('y', range(1, base))
    problem.addVariable('u', range(base))
    problem.addVariable('f', range(1, base))
    problem.addVariable('e', range(base))
    problem.addVariable('l', range(1, base))
    problem.addVariable('c', range(base))
    problem.addVariable('k', range(base))
    # enforce different number for each var
    problem.addConstraint(AllDifferentConstraint())

    # create function describing the cryptarithmetic
    def func(d, o, y, u, f, e, l, c, k):
        word_1 = d * base + o
        word_2 = y * (base ** 2) + o * base + u
        word_3 = f * (base ** 3) + e * (base ** 2) + e * base + l
        solution = l * (base ** 4) + u * (base ** 3) + c * (base ** 2) + k * base + y

        return word_1 + word_2 + word_3 == solution

    # add constraint for function above passing in letter vars
    problem.addConstraint(FunctionConstraint(func), ['d', 'o', 'y', 'u', 'f', 'e', 'l', 'c', 'k'])

    # print a solution
    print("\t   do")
    print("+\t  you")
    print("+\t feel")
    print("---------")
    print("=\tlucky")

    print("\nSolution(s):")
    solutions = problem.getSolutions()
    for solution in solutions:
        print(f"\n\t   {solution['d']}{solution['o']}")
        print(f"+\t  {solution['y']}{solution['o']}{solution['u']}")
        print(f"+\t {solution['f']}{solution['e']}{solution['e']}{solution['l']}")
        print("---------")
        print(f"=\t{solution['l']}{solution['u']}{solution['c']}{solution['k']}{solution['y']}")

    print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a()
    b()
    c()
