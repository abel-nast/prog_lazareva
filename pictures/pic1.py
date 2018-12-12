import graphics as gr

window = gr.GraphWin("Nastya's project", 500, 500)

x = 350
y = 400


def background():
    sky = gr.Line(gr.Point(0, 125), gr.Point(500, 125))
    sky.setWidth(250)
    sky.setFill('Blue')
    sky.draw(window)
    grass = gr.Line(gr.Point(0, 375), gr.Point(500, 375))
    grass.setWidth(250)
    grass.setFill('Green')
    grass.draw(window)


def draw_pig():
    leg1 = gr.Line(gr.Point(x + 50, y + 100), gr.Point(x + 50, y + 50))
    leg1.setWidth(5)
    leg1.setFill('Black')
    leg1.draw(window)
    leg2 = gr.Line(gr.Point(x + 75, y + 100), gr.Point(x + 50, y + 50))
    leg2.setWidth(5)
    leg2.setFill('Black')
    leg2.draw(window)
    leg3 = gr.Line(gr.Point(x - 50, y + 100), gr.Point(x - 50, y + 50))
    leg3.setWidth(5)
    leg3.setFill('Black')
    leg3.draw(window)
    leg4 = gr.Line(gr.Point(x - 25, y + 100), gr.Point(x - 50, y + 50))
    leg4.setWidth(5)
    leg4.setFill('Black')
    leg4.draw(window)
    ear1 = gr.Circle(gr.Point(x - 50, y - 65), 10)
    ear1.setFill('pink')
    ear1.draw(window)
    ear2 = gr.Circle(gr.Point(x + 50, y - 65), 10)
    ear2.setFill('pink')
    ear2.draw(window)
    body = gr.Circle(gr.Point(x, y), 75)
    body.setFill('pink')
    body.draw(window)
    nose = gr.Circle(gr.Point(x, y), 10)
    nose.setFill('red')
    nose.draw(window)
    nose1 = gr.Circle(gr.Point(x + 2, y), 1)
    nose1.setFill('Black')
    nose1.draw(window)
    nose2 = gr.Circle(gr.Point(x - 2, y), 1)
    nose2.setFill('Black')
    nose2.draw(window)
    eye1 = gr.Circle(gr.Point(x + 25, y - 25), 5)
    eye1.setFill('Black')
    eye1.draw(window)
    eye2 = gr.Circle(gr.Point(x - 25, y - 25), 5)
    eye2.setFill('Black')
    eye2.draw(window)


def draw_cloud():
    cloud1 = gr.Circle(gr.Point(400, 50), 25)
    cloud1.setFill('White')
    cloud1.draw(window)
    cloud2 = gr.Circle(gr.Point(412.5, 75), 25)
    cloud2.setFill('White')
    cloud2.draw(window)
    cloud3 = gr.Circle(gr.Point(425, 50), 25)
    cloud3.setFill('White')
    cloud3.draw(window)
    cloud4 = gr.Circle(gr.Point(450, 50), 25)
    cloud4.setFill('White')
    cloud4.draw(window)
    cloud5 = gr.Circle(gr.Point(437.5, 75), 25)
    cloud5.setFill('White')
    cloud5.draw(window)


def draw_sun():
    sun = gr.Circle(gr.Point(75, 75), 50)
    sun.setFill('Yellow')
    sun.draw(window)


def draw_tree():
    crown = gr.Circle(gr.Point(200, 150), 75)
    crown.setFill('Green')
    crown.draw(window)
    trunk = gr.Line(gr.Point(200, 150), gr.Point(200, 350))
    trunk.setWidth(10)
    trunk.setFill('Brown')
    trunk.draw(window)


background()
draw_cloud()
draw_sun()
draw_pig()
draw_tree()
window.getMouse()

window.close()
