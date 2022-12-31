from ft_map import ft_map
from ft_filter import ft_filter
# from ft_reduce import ft_reduce

def double(n):
    return n + n

def present(n, lst):
    if (n in lst):
        return True
    else:
        return False

#### Example 1:

print("map")
x = [1, 2, 3, 4, 5]
print(ft_map(lambda dum: dum + 1, x))

result = ft_map(double, [1, 2, 3, 4])
print(list(result))

print(list(ft_map(lambda t: t + 1, x)))

#### Example 2:
print("\nfilter")
ft_filter(lambda dum: not (dum % 2), x)

list(ft_filter(lambda dum: not (dum % 2), x))

result = ft_filter(present, [1, 2, 3, 4])
print(list(result))

# #### Example 3:
# print("\nreduce")

# lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
# ft_reduce(lambda u, v: u + v, lst)
