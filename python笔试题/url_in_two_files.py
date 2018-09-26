"""
问题描述：
给你A,B两个文件，各存放50亿条URL，每条URL占用64字节，内存限制是16G，让你找出A,B文件共同的URL。如果是三个乃至n个文件呢？
"""
'''
1.
常规的解决办法，也是最容易想到的，就是对于文件A，读入内存，对于文件B中的每一个元素，判断是否在A中出现过。
我们来分析一下这样做的空间和时间复杂度：第一步，读入文件到内存，需要的内存是（50 *（10 ** 8）*64）= 320
G内存，显然
我们在实际中没有那么大的内存。另外通过遍历A文件和B文件中的每一个元素，需要的时间复杂度是o(M * N)，M, N是两个
文件元素的大小，时间复杂度是（50亿 * 50亿）。。。。。。这是一个悲伤的算法

2.
使用bloom过滤器。关于bloom过滤器，介绍它的文章太多了，稍微有点数学基础，都应该可以明白它的大致意思。
用一句话总结bloom过滤器就是：在需要查找，或者查重的场合，我们使用bloom过滤器能够使我们的搜索时间维持在o(1)
的水平，
而不用去考虑文件的规模，另外它的空间复杂度也维持在一个可观的水平，但是它的缺陷是存在误报的情况，具体来说就是，
假如你要验证文件中是否存在某个元素，经过bloom过滤器，告诉你的结果是元素已经存在, 那么真实的结果可能元素在文件中并不存在，
但是如果bloom过滤器告诉你的结果是不存在，那么文件中肯定不存在这个元素。下面具体分析问题：
'''

"""
对于A中50亿个文件，我们使用一个误报率为1%的bloom过滤器，那么经过计算（可以参考bloom的分析过程，里面有结论），每个元素
需要使用9.6bits，总计需要（50*(10**8）*9.6)bits =  6G，在内存的使用上，是符合我们要求的，然后对于使用A文件建立的bloom
过滤器，我们遍历B中的每一个元素，判断是否在A中出现过。
我使用了python的 pybloom模块，帮我们实现了bloom的功能。
"""
from pybloom import BloomFilter  # pip install pybloom

bloom_A_file = BloomFilter(capacity=5000000000,
                           error_rate=0.01)  # 生成一个容量为50亿个元素，错误率为1%的bloom过滤器，capacity是布隆过滤器的容积，最多可以记录多少元素 error_rate是错判率
# 这里需要估摸一下自己电脑的可用内存，至少保持电脑的可用内存在8G以上，
# 否则死机不要找我。哈哈
with open(file_A) as f1:  # 遍历A文件中的每一个元素，加入到bloom过滤器中
	
	for sel in fl:
		bloom_A_file.add(sel)
with open(file_B) as f2:  # 遍历B文件，找出在A文件中出现的元素，并打印出来
	for sel in f2:
		if sel in bloom_A_file:
			print(sel)
