import time
import os
##############################################################################
##############################################################################

c_name=_________                     #设置名片姓名

c_school="温州第二外国语学校"                   #设置学校名字

c_QQ=_________                       #设置QQ号码

c_sex="男生"                         #根据自己实际情况对该项进行修改

c_dis=_________                      #设置七选三科目

c_age=_________                      #设置你的年龄

w=_________                          #体重

h=_________                          #身高

c_bmi=_________                      #利用身高体重的变量计算你的bmi,请用整除法

dic1={"姓名":_________,              #去掉划线，保留逗号，补充表示姓名的变量即可
      "学校":c_school,
      "QQ":c_QQ,
      "性别":c_sex,
      "学科":c_dis,
      "年龄":c_age,
      " bmi":c_bmi}

##############代码补充的任务结束了######################


























































s=""
s="个人电子名片\n"
for key,value in dic1.items():
    values="".join(s1 for s1 in str(value))
    s=s+key+"： "+values+"\n"
qrdata=s
print("正在生成你的名片信息....姓名")
time.sleep(1)
print("正在生成你的名片信息....学校")
time.sleep(1)
print("正在生成你的名片信息....学科")
time.sleep(1)
print("正在生成你的名片信息....其他")
time.sleep(1)
print("成功...................")
time.sleep(1)
print("姓名：",c_name)
print("学校：",c_school)
print("QQ号：",c_QQ)
print("学科：",c_dis)
print("年龄：",c_age)
print(" bmi：",c_bmi)
input()
#############################################