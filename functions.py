from operator import itemgetter

item = itemgetter('name')
student = [1,2,3,4,5]
daryl = {
    "name": "zhangsan",
    "age": 18
}
print(item(daryl))
