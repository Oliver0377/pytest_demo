

# yield生成器
def provider():
    for i in range(100):
        print("开始操作")
        yield i
        print("结束操作")

p = provider()

print(next(p))
print(next(p))