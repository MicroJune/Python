"""Compare with memory size between List and Generator
"""
from sys import getsizeof
from icecream import ic

list_comprehension = [x for x in range(100)]
bigger_list_comprehension = [x for x in range(10000)]
generator_expression = (x for x in range(100))
bigger_generator_expression = (x for x in range(10000))

ic(getsizeof(list_comprehension))
ic(getsizeof(bigger_list_comprehension))

ic(getsizeof(generator_expression))
ic(getsizeof(bigger_generator_expression))