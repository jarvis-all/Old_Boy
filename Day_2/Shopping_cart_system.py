#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author: Wiliilm Fu
###########################################################################################################
import sys
import re
def Createing_Market_Dict():
    '''
    从Market.txt 商场文件中读取可以购买的商品信息，将商品信息添加到Market_Dict字典中
    '''
    Market_Dict = {}
    with open('Market.txt','r') as Market_list:
        for Commodity in Market_list.readlines():
            Market_Dict[int(Commodity.strip().split(',')[0])] = [Commodity.strip().split(',')[1],int(Commodity.strip().split(',')[2])]
    return Market_Dict
###########################################################################################################
def Add_To_Shoping(salary,user_choice,Market,Price):
    '''
    接收外部参数
    :param salary:剩余工资
    :param user_choice: 商品编号
    :param Market: 商品名称
    :param Price: 商品价格
    将以上四个参数写入 Shoping_informations.txt 文件
    '''
    with open('Shoping_informations.txt', 'a+') as Shoping_list:
        all_info = "{salary},{user_choice},{Market},{Price}\n".format(salary=salary,user_choice=user_choice,Market=Market,Price=Price)
        Shoping_list.write(all_info)
        Shoping_list.close()
###########################################################################################################
def Chack_Salary():
    '''
    检查 Shoping_informations.txt 是否有内容
    有则为 return True
    无则为 return False
    '''
    with open('Shoping_informations.txt', 'r') as Salary_lists:
        if len(Salary_lists.readlines()) > 0:
            return True
        else:
            return False
###########################################################################################################
def Get_Save_Salary():
    '''
    判断 Chack_Salary () 是否为 True,如果为 True.则读取 Shoping_informations.txt 文件.
    将每一行以 ","进行分割取索引" 0" 位并赋值给 Salarys
    否则提示用户输入工资
    :param salary:剩余工资
    :return salary
    '''
    if Chack_Salary():
        with open('Shoping_informations.txt', 'r') as Salary_lists:
            for Salarys in Salary_lists.readlines():
                if Salarys.strip().split(',')[0].isdigit():
                    Salary = Salarys.strip().split(',')[0]
    else:
        Salary = input("Input your salary:")
    return Salary
###########################################################################################################
def Get_Shoping_List():
    '''
    读取 Shoping_informations.txt 文件，循环输出用户已购买的商品信息.
    '''
    with open('Shoping_informations.txt', 'r') as Shoping:
        for i in Shoping.readlines():
            print(i.strip().split(',')[1:])
###########################################################################################################
def Seller_Functions():
    Market_List = Createing_Market_Dict()  # 将 Market_Dict 字典的值赋给 Market_List
    salary = Get_Save_Salary()  # 调用 Get_Save_Salary() 函数 并将值赋给 salary
    salary = int(salary)  # 将salary的类型转换成整型并重新赋值给变量 salary
    while True:
        for item in Market_List.items():  # 以列表返回可遍历的(键, 值) 元组数组。
            print(item)
        user_choice = input("请输入要购买的商品")
        if user_choice.isdigit():  # 判断用户输入的值是否为数字
            user_choice = int(user_choice)  # 将用户输入的值转换成整型
            if user_choice >= 0 and user_choice < len(Market_List):  # 判断用户输入的商品编号是否在范围内
                if salary >= (Market_List[user_choice][1]):  # 判断工资余额是否小于等于商品价格
                    salary = salary - Market_List[user_choice][1]  # 工资余额减去商品价格的值重新赋值给变量 salary
                    Add_To_Shoping(salary, user_choice, Market_List[user_choice][0], Market_List[user_choice][1])
                    # 将工资余额，商品编号，商品名称，商品价格等信息写入 Shoping_informations.txt 文件中。
                    print("Added {Market} into shopping cart,your current balance is "
                          "\033[31;1m{salary}\033[0m".format(Market=Market_List[user_choice][0], salary=salary))
                else:
                    print("\033[41;1m你的余额只剩{salary}\033[0m".format(salary=salary))
            else:
                print("\033[41;1m商品不存在\033[0m")
        elif user_choice == "q":
            print("----------你成功购买以下产品----------")
            Get_Shoping_List()
            print("----------你的余额\033[31;1m{salary}\033[0m----------".format(salary=salary))
            sys.exit(0)
###########################################################################################################
def Add_Market(Market_Number,Market_Name,Market_Price):
    with open("Market.txt","r+") as Add_Market_List:
        all_info = "{Market_Number},{Market_Name},{Market_Price}\n"\
            .format(Market_Number=Market_Number,Market_Name=Market_Name,Market_Price=Market_Price)
        Add_Market_List.write(all_info)
        Add_Market_List.close()
###########################################################################################################
def Change_Price():#Market_Number,Market_Price
    with open("Market.txt","r") as Change_Price_List:
        for items in Change_Price_List.readlines():
            print(items.strip())
        Change_Price_List.close()
    Market_Number = input("请输入商品编号:>>")
    if Market_Number.isdigit():
        Market_Number = int(Market_Number)
        with open("Market.txt", "r+") as Change_Price_List:
            for items in Change_Price_List.readlines():
                if Market_Number == int(items.strip().split(',')[0]):
                    print(items.strip())
                    New_Price = input("请输入新价格:>>")
                    if New_Price.isdigit():
                        #items = re.sub(New_Price,items.strip().split(',')[2],items)
                        items = items.replace(items.strip().split(',')[2],New_Price)
                        Change_Price_List.writelines(items)
                else:
                    Change_Price_List.writelines(items)
            #Market_Number = items.strip().split(',')[0]
            #Market_Name = items.strip().split(',')[1]
            #Market_Price = items.strip().split(',')[2]
###########################################################################################################
def Buyers_Functions():#Market_Number,Market_Name,Market_Price
    Category = input("1:添加商品\n2:更改商品价格\n>>")
    if Category.isdigit():
        Category = int(Category)
        if Category == 1:
            Add_Market(Market_Number,Market_Name,Market_Price)
        elif Category == 2:
            Change_Price()
    else:
        pass
###########################################################################################################
def Chack_Buyers_Or_Seller():
    Category =  input("您是买家还是卖家？>>")
    if Category == "买家":
        Seller_Functions()
    elif Category == "卖家":
        Buyers_Functions()
###########################################################################################################
def main():
    Chack_Buyers_Or_Seller()
###########################################################################################################
if __name__ == "__main__":
    main()



