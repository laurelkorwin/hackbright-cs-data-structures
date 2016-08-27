"""DISCUSSION QUESTIONS"""

"""
1. When calculating the Big O notation for a particular algorithm, it’s necessary
to consider the length of time it takes for the algorithm to run as the algorithm’s
workload approaches infinity. You can think of the workload as the number of tasks
required to complete a job. What determines the workload of figuring out whether
your box of animal crackers contains an elephant?

A: This would be O(n) (linear) runtime / workload - in order to determine if the box contained an 
elephant, the 'worst case' would be that you would go through every single cookie in the box,
and would either find the elephant as the last cookie, or not find it at all. You would
need to "loop through" every cookie, but would only have to do it one time for each cookie.

2. Order the following runtimes in ascending order by efficiency as n approaches infinity:
O(log n),
O(n2)
O(n log n)
O(n)
O(2n)
O(1)

A: (Ranked from most efficient to least efficient):
O(1) - constant
O(log n) - divide options in half each time
O(n) - go through every option
O(n log n) - more complex divide and conquer
O(n2) - have to go through two "nested loops"
O(2n) - often runtime for recursive functions, for example password cracking

"""

def string_compare(s1, s2):
    """Given two strings, figure out if they are exactly the same (without using ==).

    Put runtime here:
    -----------------
    I think runtime for the below is O(n). Although you are technically looping
    over two items, you are only doing it once and comparing at each point (vs
    for example checking every letter of the first string against every letter
    of the second string, which would be O(n2).)


    """
    # constant runtime (O(1))
    if len(s1) != len(s2):
        return False

    # linear runtime (O(n)) - although you are looping over two things, you are only
    # doing it *once*
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True


def has_exotic_animals(animals):
    """Determine whether a list of animals contains exotic animals.

    Put runtime here:
    -----------------
    This runtime is also O(n). Even if you have to iterate over the list separately
    for hippo and platypus, each loop is n - so it is n + n = 2n. The best case (not
    sure if this is how it works under the hood) is that you would loop over the list one time,
    and look for both words as you loop.

    """

    if "hippo" in animals or "platpypus" in animals:
        return True
    else:
        return False


def sum_zero_1(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    In the average case, the below is O(n) - in the worst case, O(n^2). I researched
    to find the runtime for looking up items in a set - average cast is O(1), and worst
    case is O(n). Thus, in the worst case the loop would be n^2.

    """

    result = []

    # Hint: the following line, "s = set(numbers)", is O(n) ---
    # we'll learn exactly why later
    s = set(numbers)

    for x in s:
        if -x in s:
            result.append([-x, x])

    return result


def sum_zero_2(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    The runtime for this would be O(n^2). You are looping over every number, and comparing
    it to every other number. As stated above, appending to the list is constant.

    """

    result = []

    for x in numbers:
        for y in numbers:
            if x == -y:
                result.append((x, y))
    return result


def sum_zero_3(numbers):
    """Find pairs of integers that sum to zero.

    This version gets rid of duplicates (it won't add (1, -1) if (-1, 1) already there.

    Put runtime here:
    -----------------
    The runtime for this would also be O(n^3), as you are looping over every number and comparing
    to every other number. You are then performing the extra step of comparing every tuple to the
    items in the result for every pair of numbers.

    """

    result = []

    for x in numbers:
        for y in numbers:
            if x == -y and (y, x) not in result:
                result.append((x, y))
    return result
