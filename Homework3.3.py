def print_bonacci(a):
    def bonacci(n):
        bonacci_list=[]
        if n>=3:
            return bonacci(n-1)+bonacci(n-2)
        elif n==1:
            return 0
        elif n==2:
            return 1
    return [bonacci(i+1) for i in range(a)]
n=int(input("请输入斐波那契数列项数："))
print(print_bonacci(n))