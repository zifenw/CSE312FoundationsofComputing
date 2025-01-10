import numpy as np
import matplotlib.pyplot as plt
print('helloworld')
print("""multiple
            lines""")

print(np.array([3, 2, 5, 6]))
cubes = [x ** 3 for x in range(3,10)]
print(cubes)
print(np.array(cubes))
print(np.array([x ** 3 for x in range(3,10)]))
print(np.array(range(10, 21, 3)))

# python3 [filename].py

print(np.zeros((3,4)) + 3)
print(np.zeros((3,4), dtype=int) + 3)
print(np.arange(1, 13).reshape((3, 4)))
print(np.array([7,5,3,1]*5).reshape((5,4)))


arr = np.array([[1, 3, 5, 7], [2, 4, 6, 0], [8, 4, 6, 5]])
print(arr)

print(np.mean(arr))

print(np.min(arr, axis=0))

print(np.max(arr, axis=1))

print(np.argmax(arr, axis=1))

x = np.arange(10)
y = x ** 2
z = 5*x + 7
plt.plot(x, y, color="b", label="y = x^2", linestyle="-")
plt.plot(x, z, color="r", label="z = 5x + 7", linestyle="-.")
plt.legend(loc="upper left")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("An interesting graph")
plt.show()
# plt.savefig("plot.png")

# 创建一个2x2的图形网格
plt.subplot(2, 2, 1)  # 第一子图
plt.plot([1, 2, 3], [4, 5, 6])

plt.subplot(2, 2, 2)  # 第二子图
plt.scatter([1, 2, 3], [7, 8, 9])

plt.subplot(2, 2, 3)  # 第三子图
plt.bar([1, 2, 3], [10, 20, 30])

plt.subplot(2, 2, 4)  # 第四子图
plt.hist([1, 2, 3, 4, 5, 6, 7], bins=3)
plt.show()