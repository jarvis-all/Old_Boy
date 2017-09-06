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
    '''
    Seller_Functions 函数为 买家 功能主函数.
    循环输出 Market.txt 文件中的商品信息.
    获取salary(工资/余额).
    接收用户要购买商品的编号（商品编号为数字），判断用户输入是否为数字，是数字则将变量转换成整型.
    判断用户输入的商品编号是否在 Market.txt 文件中，同时判断工资余额是否大于等于商品价格.
    满足条件则将商品添加到购物车文件 Shoping_infomations.txt 文件中，并显示工资余额.
    否则只打印工资余额.
    如果用户输入的商品编号不在 Market.txt 文件中则提示用户商品不存在.
    如果用户输入的商品编号不是数字则判断值是否为“Q” or “q”，是则打印用户购物中的商品，同时展示余额.
    如果不是则判断是否为“B” or “b”,是则返回上级.
    :return:
    '''
    Market_List = Createing_Market_Dict()  # 将 Market_Dict 字典的值赋给 Market_List
    salary = Get_Save_Salary()  # 调用 Get_Save_Salary() 函数 并将值赋给 salary
    salary = int(salary)  # 将salary的类型转换成整型并重新赋值给变量 salary
    while True:
        for item in Market_List.items():  # 以列表返回可遍历的(键, 值) 元组数组。
            print(item)
        user_choice = input("请输入要购买的商品")
        if user_choice.isdigit():  # 判断用户输入的值是否为数字
            user_choice = int(user_choice)  # 将用户输入的值转换成整型
            #print(type(user_choice))
            #if user_choice >= 0 and user_choice < len(Market_List):  # 判断用户输入的商品编号是否在范围内
            if user_choice in Market_List:
                if salary >= (Market_List[user_choice][1]):  # 判断工资余额是否小于等于商品价格
                    salary = salary - Market_List[user_choice][1]  # 工资余额减去商品价格的值重新赋值给变量 salary
                    Add_To_Shoping(salary, user_choice, Market_List[user_choice][0], Market_List[user_choice][1])
                    # 将工资余额，商品编号，商品名称，商品价格等信息写入 Shoping_informations.txt 文件中。
                    print("商品 {Market} 已添加至购物车,你的余额为： "
                          "\033[31;1m{salary}\033[0m".format(Market=Market_List[user_choice][0], salary=salary))
                else:
                    print("\033[41;1m你的余额只剩{salary}\033[0m".format(salary=salary))
            else:
                print("\033[41;1m商品不存在\033[0m")
        elif user_choice == "B" or user_choice == "b":
            break
        elif user_choice == "q" or user_choice == "Q":
            print("----------你成功购买以下产品----------")
            Get_Shoping_List()
            print("----------你的余额\033[31;1m{salary}\033[0m----------".format(salary=salary))
            sys.exit(0)
###########################################################################################################
def Add_Market():
    '''
    Add_Market函数用于卖家向 Market.txt 文件中添加商品.
    判断用户输入的商品编号是否为数字同时是否存在与Market.txt 文件中，存在则提示用户商品编号存在，同时提示用户重新输入.
    如果商品编号不存在于Market.txt 文件中，则提示用户输入商品名和商品价格.
    将商品编号、商品名称、商品价格写入Market.txt 文件,并提示用户.
    如果用户输入的商品编号不是数字则判断值是否为“Q” or “q”，是则退出.
    如果不是则判断是否为“B” or “b”,是则返回上级.
    :return:
    '''
    while True:
        with open("Market.txt", "a+") as Add_Market_List:
            Market_Number = input("请输入商品编号：")
            if Market_Number.isdigit():
                Market_Number = int(Market_Number)
                Market_List = Createing_Market_Dict()  # 将 Market_Dict 字典的值赋给 Market_List
                if Market_Number in Market_List:
                    print("\033[41;1m商品编号已存在\033[0m")
                else:
                    Market_Name = input("请输入商品名称>>")
                    Market_Price = input("请输入商品价格>>")
                    if not Market_Price.isdigit():
                        print("\033[41;1m格式错误，请重新输入\033[0m")
                        break
                    else:
                        all_info = ("{Market_Number},{Market_Name},{Market_Price}\n"
                                    .format(Market_Number=Market_Number, Market_Name=Market_Name, Market_Price=Market_Price))
                        print(all_info)
                        Add_Market_List.writelines(all_info)
                        print("成功将{all_info}添加致Market".format(all_info=all_info))
                        Add_Market_List.close()
            elif Market_Number == "B" or Market_Number == "b":
                Add_Market_List.close()
                break
            elif Market_Number == "Q" or Market_Number == "q":
                Add_Market_List.close()
                sys.exit(0)
            else:
                print("\033[41;1m格式错误，请重新输入\033[0m")
###########################################################################################################
def Write_Market(items):
    '''
    Write_Market 函数用于将更新后商品价格写于Market.txt文件.
    :param items:
    :return:
    '''
    f_w = open("Market.txt","r+")
    for item in items:
        item = item.strip()
        item = "{item}\n".format(item=item)
        f_w.write(item)
    f_w.close()
###########################################################################################################
def Change_Price():
    '''
    Change_Price 函数为更新商品价格主体函数
    :return:
    '''
    items_list = []
    while True:
        with open("Market.txt","r") as Change_Price_List:
            for items in Change_Price_List.readlines():
                print(items.strip())
        Market_Number = input("请输入商品编号:>>")
        if Market_Number.isdigit():
            if int(Market_Number) in Createing_Market_Dict():
                with open("Market.txt", "r+") as Change_Price_List:
                    for items in Change_Price_List.readlines():
                        if Market_Number == items.strip().split(',')[0]:
                            print(items.strip())
                            New_Price = input("请输入新价格:>>")
                            if New_Price.isdigit():
                                items = items.replace(items.strip().split(',')[2],New_Price)
                                items_list.append(items.strip())
                            elif New_Price == "B" or New_Price == "b":
                                break
                            elif New_Price == "Q" or New_Price == "q":
                                sys.exit(0)
                            else:
                                print("\033[41;1m格式错误，请重新输入\033[0m")
                        else:
                            items_list.append(items.strip())
            elif Market_Number == "B" or Market_Number == "b":
                break
            elif Market_Number == "Q" or Market_Number == "q":
                sys.exit(0)
            else:
                print("\033[41;1m商品编号有误，请重新输入\033[0m")
        Write_Market(items_list)
###########################################################################################################
def Buyers_Functions():
    '''
    Buyers_Functions 函数为 买家 功能主函数.
    接收用户参数用于判断是添加商品还是更改商品价格，从而调用不同的功能函数》
    :return:
    '''
    while True:
        Category = input("1:添加商品\n2:更改商品价格\n>>")
        if Category.isdigit():
            Category = int(Category)
            if Category == 1:
                Add_Market()
            elif Category == 2:
                Change_Price()
        elif Category == "B" or Category == "b":
            break
        elif Category == "Q" or Category == "q":
            sys.exit(0)
###########################################################################################################
def Chack_Buyers_Or_Seller():
    '''
    Chack_Buyers_Or_Seller 函数用于判断用户是"买家"还是"卖家",从而调用不同的功能函数.
    :return:
    '''
    while True:
        Category =  input("您是买家还是卖家？>>")
        if Category == "买家":
            Seller_Functions()
        elif Category == "卖家":
            Buyers_Functions()
        elif Category == "Q" or Category == "q":
            sys.exit(0)
###########################################################################################################
def main():
    '''
    main 函数为总函数开关
    :return:
    '''
    Chack_Buyers_Or_Seller()
###########################################################################################################
if __name__ == "__main__":
    main()



