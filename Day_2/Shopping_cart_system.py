#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author: Wiliilm Fu
import sys
def Createing_Market_Dict():
    Market_Dict = {}
    with open('Market.txt','r') as Market_list:
        for Commodity in Market_list.readlines():
            Market_Dict[int(Commodity.strip().split(',')[0])] = [Commodity.strip().split(',')[1],int(Commodity.strip().split(',')[2])]
    return Market_Dict

def Add_To_Shoping(salary,user_choice,Market,Price):
    with open('Shoping_informations.txt', 'a+') as Shoping_list:
        all_info = "{salary},{user_choice},{Market},{Price}\n".format(salary=salary,user_choice=user_choice,Market=Market,Price=Price)
        Shoping_list.write(all_info)
        Shoping_list.close()

def Chack_Salary():
    with open('Shoping_informations.txt', 'r') as Salary_lists:
        if len(Salary_lists.readlines()) > 0:
            return True
        else:
            return False
def Get_Save_Salary():
    if Chack_Salary():
        with open('Shoping_informations.txt', 'r') as Salary_lists:
            for Salarys in Salary_lists.readlines():
                if Salarys.strip().split(',')[0].isdigit():
                    Salary = Salarys.strip().split(',')[0]
    else:
        Salary = input("Input your salary:")
    return Salary

def Get_Shoping_List():
    with open('Shoping_informations.txt', 'r') as Shoping:
        for i in Shoping.readlines():
            print(i.strip().split(',')[1:])


Market_List = Createing_Market_Dict()
salary = Get_Save_Salary()
salary = int(salary)
while True:
    for item in Market_List.items():
        print(item)
    user_choice = input("请输入要购买的商品")
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice >= 0 and user_choice < len(Market_List):
            if salary >= (Market_List[user_choice][1]):
                salary = salary - Market_List[user_choice][1]
                Add_To_Shoping(salary,user_choice,Market_List[user_choice][0],Market_List[user_choice][1])
                print("Added {Market} into shopping cart,your current balance is "
                      "\033[31;1m{salary}\033[0m" .format(Market=Market_List[user_choice][0],salary=salary))
            else:
                print("\033[41;1m你的余额只剩{salary}\033[0m".format(salary=salary))
    elif user_choice == "q":
        print("----------你成功购买以下产品----------")
        Get_Shoping_List()
        print("----------你的余额\033[31;1m{salary}\033[0m----------".format(salary=salary))
        sys.exit(0)
    else:
        print("商品不存在")