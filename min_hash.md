## main
```py
class MinHash:
    def __init__(self, seed_offset:int=0):
        """
        :param seed_offset: Allows for multiple instances of this
        class to provide different results.
        
        We only use one variable, self.val, in our entire
        implementation.
        """
        self.seed_offset = seed_offset
        self.val = float("inf")
        # self.val 初始化为无穷大
    def hash(self, x:int) -> float:
        """
        :param x: The element x to be hashed.
        :return: A Unif(0,1) continuous random variable. However,
        if the same x is passed in, we will return the same exact
        Unif(0,1) rv. We do this by taking the modulus by a large
        number, and dividing by it so that we get "approximately" a
        random float between 0 and 1.
        """
        large_num = 2 ** 31
        h = mmh3.hash(x, self.seed_offset) % large_num + 1
        # 取模 2^31 以防止溢出，并确保结果位于 [0, 2^{31}-1] 之间。
        # 再加 1，保证范围变为 [1, 2^{31}]，避免 0 影响归一化计算。
        return h / large_num


if __name__ == '__main__':
    # You can test out things here. Feel free to write anything below.
    stream = np.genfromtxt('data/stream_small.txt', dtype='int')

    # 312 actual distinct Elements in the stream
    print("True Dist Elts: {}".format(312))

    # Create a MinHash object, and update for each element in the stream.
    # Finally, print out the estimate.
    de = MinHash()
    for x in stream:
        de.update(x)
    print("Min Hash Estimate: {}".format(de.estimate()))

    # Create a MultMinHash object, and update for each element in the 
    # stream. Finally, print out the estimate.
    num_reps = 50
    mde = MultMinHash(num_reps=num_reps)
    for x in stream:
        mde.update(x)
    print("Mult Min Hash Estimate with {} copies: {}".format(num_reps, mde.estimate()))

```
## `update`
For each new element x, compute its hash using the hash method.

Update self.val to be the minimum of the current self.val and the hash value of x.

## estimate
Estimate 代表的是集合中不同元素（distinct elements）的估计数量，也就是集合的基数（cardinality）
E[X] = 1/m+1
m=1/X - 1