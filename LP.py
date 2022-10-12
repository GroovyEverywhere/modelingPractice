#1 scipy求解函数
# res = optimize.linprog(c,A,b,Aeq,beq,LB,UB,X0,options)
   
#目标最小函数
# print(res.fun)

#目标最优解
#print(res.x)

'''样例1: 求解下列线性规划问题
    max z = 2x1+3x2-5x3
        { x1+x2+x3 = 7
    s.t.{ 2x1-5x2+x3 >= 10
        { x1+3x2+x3 <= 12
        { x1, x2, x3 >= 0
'''
from scipy import optimize
import numpy as np

#确定c,A,b,Aeq,beq
c = np.array([2,3,-5])
A = np.array([[-2,5,-1],[1,3,1]])   #添加负号为了变成小于等于
B = np.array([-10,12])
Aeq = np.array([[1,1,1]])
Beq = np.array([7])

res = optimize.linprog(-c,A,B,Aeq,Beq)  #求最小化 所以c加负号
print(res)
print(res.fun)
print(res.x)

#---------------------------------------------------------------------

#2 pulp求解函数
'''样例2: 求解下列线性规划问题
    max z = 2x1+3x2+x3
        { x1+2x2+4x3 = 101
    s.t.{ x1+4x2+2x3 >= 8
        { 3x1+2x2 >= 6
        { x1, x2, x3 >= 0
'''
import pulp    #调用里面专门的LP函数

#目标函数系数
z = [2,3,1]
#约束
a = [[1,4,2],[3,2,0]]
b = [8,6]
#确定最大化最小化问题，最大化max最小化min
m = pulp.LpProblem(sense = pulp.LpMinimize)
#定义三个变量放到列表中
x = [pulp.LpVariable(f'x{i}', lowBound = 0) for i in [1,2,3]]
#定义目标函数，lpDot可以将两个列表的对应为相乘再相加
#e.g x1*y1 + x2*y2 + x3*y3 ...
m += pulp.lpDot(z,x)

#设置约束条件
for i in range(len(a)):
    m += (pulp.lpDot(a[i],x) >= b[i])  #通过for loop 把表达式输入到m里面 然后进行Lpminimize

#求解
m.solve()
print(f'优化结果：{pulp.value(m.objective)}')
print(f'参数取值：{[pulp.value(var) for var in x]}')

#--------------------------------------------------------------------