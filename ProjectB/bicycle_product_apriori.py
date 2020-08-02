import pandas as pd
import numpy as np
import time
data = pd.read_csv('E:/python/svw数据分析实战/exam/ProjectB/订单表.csv',encoding='gbk')
data.sort_values(by=["客户ID","订单日期"],ascending=True,inplace=True)
print(data.shape)
print(data.head())
data.to_csv('E:/python/svw数据分析实战/exam/ProjectB/sort_values.csv',encoding='gbk')

from efficient_apriori import apriori
start = time.time() #执行程序的内置计时开始
orders_series1 = data.set_index('客户ID')['产品名称'] # 得到一维数组orders_series，将transaction客户ID作为index、value值为'产品名称'
# print(type(orders_series1))
# orders_series1.sort_index(ascending=True,inplace=True)
print (orders_series1)

# 由于transaction id有重复，因此把重复的放到同一个transaction id里：
transactions = [] #创建一个空列表
temp_index = 1 #创建一个临时index
for i, v in orders_series1.items(): #items函数，将一个字典以列表的形式返回
	if i != temp_index:  #i不等于temp_index时：
		temp_set = set() #创建一个临时集合
		temp_index = i 
		#print (temp_index)
		transactions.append(temp_set) #为什么放在这里就只出现一遍transactions？
		temp_set.add(v)
		
	else:
		temp_set.add(v)
		#print (temp_set)
	#transactions.append(temp_set) 

		
print (transactions)
#orders_series1.to_csv('E:/python/svw数据分析实战/exam/ProjectB/orders_series1.csv',encoding='gbk')
# temp_set.to_csv('E:/python/svw数据分析实战/exam/ProjectB/temp_set.csv',encoding='gbk')
#print ('temp_set:',temp_set)
#print (orders_series1)
#print (transactions)

# 挖掘频繁项集和关联规则
itemsets, rules = apriori(transactions, min_support=0.1,  min_confidence=0.3) #注意：这里transactions已经变成了每一笔订单的列
print('频繁项集：', itemsets)
print('关联规则：', rules)
end = time.time()
print("用时：", end-start)


