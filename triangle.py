import turtle

t = turtle.Turtle()
t.speed(1)

# t.forward(150)
# t.left(90)
# t.forward(75)

# for _ in range(4):
#     t.forward(300)
#     t.left(90)

# 메인 삼각형 그리기
def drawTriangle(points):
    t.penup()
    t.setpos(points[0][0],points[0][1])
    t.pendown()
    t.goto(points[1][0],points[1][1])
    t.goto(points[2][0],points[2][1])
    t.goto(points[0][0],points[0][1])

# 중앙위치 값
def getMid(p1, p2):
    return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2) 

#
def sierpinski(points, n):
    drawTriangle(points)
    if n > 0 : # 삼각형 그리기 n 횟수
        sierpinski([points[0],
            getMid(points[0], points[1]),
            getMid(points[0], points[2])], n-1
        )
        sierpinski([points[1],
            getMid(points[1], points[2]),
            getMid(points[1], points[0])], n-1
        )
        sierpinski([points[2],
            getMid(points[2], points[1]),
            getMid(points[2], points[0])], n-1
        )

sierpinski([[0,100],[-150,-100], [150,-100]],3)
turtle.done()