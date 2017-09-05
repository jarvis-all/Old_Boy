#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author: Wiliilm Fu
import os
import sys
def Get_User_Pass():
    with open('User_Pass.txt','r') as User_pass:
        return  User_pass.readlines()
def Chack_Lock_User(User):
    with open('User_Lock.txt', 'r') as User_Locks:
        for User_Lock in User_Locks.readlines():
            if User == User_Lock.strip():
                sys.exit("用户：{}已被锁定".format(User))
def Lock_User(User):
    with open('User_Lock.txt', 'a+') as User_Locks:
        User_Locks.writelines(User+'\n')

def Chack_Exist_User(UserName):
    User_List = []
    for Users in Get_User_Pass():
        Username = Users.strip().split(',')[0]
        User_List.append(Username)
    if UserName not in User_List:
        return False

retry_limit = 3
retry_count = 0
chack_limit = 3
chack_count = 0
while  retry_count < retry_limit:

    UserName = input("请输入用户名：")
    if Chack_Exist_User(UserName) == False:
        chack_count += 1
        if chack_count < chack_limit:
            print("用户名不存在请重新输入")
        else:
            sys.exit(0)
    else:
        Chack_Lock_User(UserName)
        PassWord = input("请输入密码：")
        flag = False
        for Infos in Get_User_Pass():
            Username,Password = Infos.strip().split(',')
            if UserName == Username and PassWord == Password:
                sys.exit("用户名密码验证成功，欢迎登录！！！")
                flag = True
        if flag != True :
            retry_count += 1
            if retry_count < retry_limit:
                print("用户名密码错误请重新登录！！！")
else:
    Lock_User(UserName)
    sys.exit("用户：{}已被锁定,请联系系统管理员".format(UserName))