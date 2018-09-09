import turtle as t
import math as m

#--------------------------------------------
#--------------------------------------------
#设置画布,占屏幕的长宽比例
t.showturtle()
t.speed(10)
t.setup(width=0.6, height=0.85)
t.title('哆啦A梦')

#--------------------------------------------
'''


头


'''
t.penup()
# t.goto(0, 200)
t.goto(-75, -61.8)
t.seth(150)
t.pendown()
t.color('black', '#4187F1')
t.begin_fill()
# t.circle(-150)
for i in range(300):
    t.rt(1)
    t.forward(2 * m.pi * 150 / 360)
t.end_fill()
t.seth(0)

#------------------------------------------------------
'''


脸


'''
t.penup()
t.goto(-58, -61.8)
t.seth(150)
t.pendown()
t.color('black', 'white')
t.begin_fill()
# t.circle(-150)
for i in range(300):
    t.rt(1)
    t.forward(2 * m.pi * 118 / 360)
t.end_fill()
t.seth(0)


#--------------------------------------------------------
'''


眼睛


'''
t.penup()
t.goto(-30, 90)
t.pd()
t.color('black', 'white')
t.begin_fill()
a = 0.7
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.08
        t.speed(0)
        t.lt(3)  # 向左转3度
        t.fd(a)  # 向前走a的步长
    else:
        a = a - 0.08
        t.speed(0)
        t.lt(3)
        t.fd(a)
t.penup()
t.goto(30, 90)
t.pd()
t.end_fill()
t.color('black', 'white')
t.begin_fill()
a = 0.7
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.08
        t.speed(0)
        t.lt(3)  # 向左转3度
        t.fd(a)  # 向前走a的步长
    else:
        a = a - 0.08
        t.speed(0)
        t.lt(3)
        t.fd(a)
t.end_fill()
t.pu()
t.goto(-21, 108)
# t.dot(5, 'red')
t.color('black', 'black')
t.begin_fill()
a = 0.2
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.02
        t.speed(0)
        t.lt(3)  # 向左转3度
        t.fd(a)  # 向前走a的步长
    else:
        a = a - 0.02
        t.speed(0)
        t.lt(3)
        t.fd(a)
t.end_fill()
t.pu()
t.goto(-20, 121)
t.dot(5, 'white')

t.pu()
t.goto(21, 108)
# t.dot(5, 'red')
t.color('black', 'black')
t.begin_fill()
a = 0.2
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.02
        t.speed(0)
        t.lt(3)  # 向左转3度
        t.fd(a)  # 向前走a的步长
    else:
        a = a - 0.02
        t.speed(0)
        t.lt(3)
        t.fd(a)
t.end_fill()
t.pu()
t.goto(20, 121)
t.dot(5, 'white')
#---------------------------------------------------------
'''



上嘴唇



'''
t.pu()
t.goto(-105, 75)
t.pd()
t.circle(-20,-180)
t.setheading(0)
for i in range(18):
    t.fd(3)
    t.lt(1)
for i in range(15):
    t.fd(3)
    t.rt(1)
for i in range(20):
    t.fd(3)
    t.rt(1)
for i in range(20):
    t.fd(3)
    t.lt(1)
t.setheading(0)
t.circle(20,185)
#----------------------------------------------------
'''


鼻子


'''
t.speed(10)
t.pu()
t.home()
# t.dot(5, 'red')
t.goto(0, 51)
t.pd()
t.goto(0, 80)
t.pd()
t.color('black', 'red')
t.begin_fill()
t.circle(15)
t.end_fill()
t.pu()
t.goto(2, 98)
t.dot(10, 'white')
# t.goto(-100, -61.8)
#----------------------------------------------------------
'''


嘴


'''
t.pu()
t.goto(-87.03, 35.78)
t.pd()
t.seth(270)
t.color('black', '#BB0000')
t.begin_fill()
for i in range(180):
    t.lt(1)
    t.fd(2*m.pi*87.03/360)
t.goto(83.78, 37.90)
t.seth(174)
for i in range(9):
    t.fd(3)
    t.rt(1)
for i in range(20):
    t.fd(3)
    t.lt(0.7)
for i in range(15):
    t.fd(3)
    t.lt(1.2)
for i in range(13):
    t.fd(3)
    t.rt(0.6)
t.end_fill()

t.pu()
t.goto(-87.03, 35.78)
t.seth(270)
for i in range(60):
    t.lt(1)
    t.fd(2*m.pi*87.03/360)
t.pd()
t.seth(60)
t.begin_fill()
t.color('black', '#FF6600')
for i in range(119):
    t.rt(1)
    t.fd(2 * m.pi * 50 / 360)
t.seth(210)
for i in range(60):
    t.rt(1)
    t.fd(2 * m.pi * 87.03 / 360)
t.end_fill()
t.pu()
t.goto(-42.86,90)
t.pd()
t.seth(150)
t.fd(90)
t.pu()
t.goto(-42.86,84)
t.pd()
t.seth(170)
t.fd(90)
t.pu()
t.goto(-42.86,78)
t.pd()
t.seth(190)
t.fd(90)


t.pu()
t.goto(42.86,90)
t.pd()
t.seth(30)
t.fd(90)
t.pu()
t.goto(42.86,84)
t.pd()
t.seth(10)
t.fd(90)
t.pu()
t.goto(42.86,78)
t.pd()
t.seth(350)
t.fd(90)
t.hideturtle()



#结束
t.done()
