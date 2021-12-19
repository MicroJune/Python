# Main usage is to record data
from collections import namedtuple
from sys import getsizeof
from icecream import ic

Student = namedtuple("Student", "name age grade gentle")
daryl = Student("daryl", 30, "class-1", "male")

# instant has the same memory size compared with tupe
ic(getsizeof(daryl))
ic(getsizeof(("daryl", 30, "class-1", "male")))

ic(daryl.name)
ic(daryl[1])
ic(daryl._fields)
ic(daryl._asdict)