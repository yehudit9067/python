#1
def inventory_summary(dictionary):
    count = 0
    for key, value in dictionary.items():
        count += value[1]
    return count

my_dictionary = {"aaa":[1,2],"bbb":[3,4],"ccc":[5,6]}
print(inventory_summary(my_dictionary))

#2
def print_args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

print_args_kwargs(1,2,3,4,5,6, name="aaa",age="bbb",dd="ccc")