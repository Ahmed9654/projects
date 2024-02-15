LAT_CENTER = 26.820553
LONG_CENTER = 30.8024981
import turtle
import pandas as pd
screen = turtle.Screen()
screen.title('Egypt quiz game')
image = 'egypt_location_map_svg.gif'
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv('quiz data')

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)

questio_list = ['Capital of Egypt', 'world’s greatest open-air museum',
                "was once the most vital cultural center of the ancient world", 'Bride of Upper Egypt',
                'The Land of Gold',"well that's it for today; you can exit now"]
all_places = data.government.to_list()
i = 0
while i<len(questio_list):
    answer = screen.textinput(title='Guess the government name', prompt=f'{questio_list[i]}\n').lower()

    if answer in all_places:
        leo = turtle.Turtle()
        leo.penup()
        leo.hideturtle()
        leo.pencolor('black')
        coor = data[data.government == answer]
        leo.goto(int(coor.xcor),int(coor.ycor))
        leo.write(answer.title())
        i+=1

screen.mainloop()

# location = {'government': ['Cairo','Luxor','Alex','Minia','Aswan'],
#             'xcor':[29.0,98.0,-17.0,8.0,108.0],
#             'ycor':[191.0,-48.0,263.0,50.0,-138.0]
#             }
# data = pd.DataFrame(location)
# data.to_csv('quiz data')
