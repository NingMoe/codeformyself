# 问题主要集中在页面解析和 Selenium+Phantom JS 解析复杂页面，ajax 页面请求等，图片识别，机器学习。

# 定义 A=("a", "b", "c", "d"),执行 delA[2]后的结果为：
# A = ("a", "b", "c", "d")
# del (A[2])
# print(A)
# del用于list列表操作,删除一个或者连续几个元素,上面是元组


# String = "{1},{0}"; string = string.format("Hello", "Python"),请问将 string 打印出来为
'''
String = "{1}, {2}"
print(String)
print(type(String))
string = String.format("Hello", "Python", "Python1")
print(string)
'''

# 请对 Python 数据结构 Tuple,List,Dict 进行操作
# 1.  如何让元祖内部可变（叙述或简单定义）?
# 元组里面元素改为列表呗,列表是可变数据类型,变了
# 2.如何将 L1 = [1,2,3,4,5],L2 = [6,7,8,9];使用列表内置函数变成 L1=[1,2,3,4,5,6,7,8,9]?
# L1 = [1, 2, 3, 4, 5]
# L2 = [6, 7, 8, 9]
#
# L1.extend(L2)
#
# print(L1)
# print(L1 + L2)
# print(L1, L2)
# print(L1.extend(L2))  # +号生成的是一个新的对象，而extend则是在原地的修改a对象。

str = "#tea#"
b = str.strip("#")
print(b)

# 请使用 map 函数将[1,2,3,4]处理成[1,0,1,0]
