def is_multiple_of_three(value):
    return (value % 3) == 0

def is_multiple_of_five(value):
    return (value % 5) == 0

def sum_occorrences(target_list, predicate_a, predicate_b):
    return sum([n for n in target_list if predicate_a(n) 
        or predicate_b(n)])

predicate_a = is_multiple_of_three
predicate_b = is_multiple_of_five
my_list = range(0, 1000);
result = sum_occorrences(my_list, predicate_a, predicate_b)
print(result)
