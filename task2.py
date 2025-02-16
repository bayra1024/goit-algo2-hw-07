from splaytree import SplayTree

# import splaytree
from functools import lru_cache
import timeit
import matplotlib.pyplot as plt


@lru_cache
def fibonacci_lru(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)


lru_test = []
for n in range(50, 951, 50):
    start = timeit.default_timer()
    # print(str(n) + ":" + str(fibonacci_lru(n)))
    value = fibonacci_lru(n)
    res_time = timeit.default_timer() - start
    lru_test.append({"n": n, "value": value, "time": res_time})


def fibonacci_splay(n, tree):
    max_n = tree.max_n
    if n <= max_n:
        return tree.find(n).value
    for i in range(max_n + 1, n + 1):
        i1 = tree.find(i - 1).value
        i2 = tree.find(i - 2).value
        tree.insert(i, i1 + i2)
    return tree.find(n).value


sp_tree = SplayTree()
sp_tree.insert(1, 1)
sp_tree.insert(2, 1)

splay_test = []
for n in range(50, 951, 50):
    start = timeit.default_timer()
    value = fibonacci_splay(n, sp_tree)
    res_time = timeit.default_timer() - start
    splay_test.append({"n": n, "value": value, "time": res_time})

# print(lru_test)
# print(splay_test)


print("n          LRU Cache Time (s) |  Splay   Tree Time (s)")
for i, j in zip(lru_test, splay_test):
    print(f'{i["n"]:<10} {i["time"]:15.8f}    |  {j["time"]:15.8f}')
    # print(f'{i["n"]:<10} {i["time"]} | {j["time"]}')


# create data
x = [i["n"] for i in lru_test]
lru = [i["time"] for i in lru_test]
spl = [i["time"] for i in splay_test]

# plot lines
plt.plot(x, lru, label="LRU Cache", color="purple")
plt.plot(x, spl, label="Splay Tree", color="green")
plt.legend()
plt.title(
    "Порівняння часу виконання LRU Cache та Splay Tree", fontsize=14, color="blue"
)
plt.xlabel("Число Фвбоначчі (n)", fontsize=12, color="red")
plt.ylabel("Середній час виконання (сек)", fontsize=12, color="red")
plt.xticks(rotation=45, fontsize=10, color="red")
plt.yticks(fontsize=10, color="red")
plt.show()
print("DONE")
