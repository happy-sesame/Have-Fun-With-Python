import turtle as t
import random
import time
#
# ######################################
# # Initialization - screen creation
# ######################################
#
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRAVITY = 0.001 #used later on

wn = t.Screen()
wn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
wn.bgcolor('white')
wn.title('Raining cats and dogs')
wn.tracer(0) # turns off screen update; screen update is done in the while loop
#
# ######################################
# # Initialization - cat_dog creation
# ######################################
#
CAT1_SHAPE = 'cat1.gif'
CAT2_SHAPE = 'cat2.gif'
CAT3_SHAPE = 'cat3.gif'
CAT4_SHAPE = 'cat4.gif'
CAT5_SHAPE = 'cat5.gif'
CAT6_SHAPE = 'cat6.gif'
DOG1_SHAPE = 'dog1.gif'
DOG2_SHAPE = 'dog2.gif'
DOG3_SHAPE = 'dog3.gif'
DOG4_SHAPE = 'dog4.gif'
DOG5_SHAPE = 'dog5.gif'
DOG6_SHAPE = 'dog6.gif'
t.register_shape(CAT1_SHAPE)
t.register_shape(CAT2_SHAPE)
t.register_shape(CAT3_SHAPE)
t.register_shape(CAT4_SHAPE)
t.register_shape(CAT5_SHAPE)
t.register_shape(CAT6_SHAPE)
t.register_shape(DOG1_SHAPE)
t.register_shape(DOG2_SHAPE)
t.register_shape(DOG3_SHAPE)
t.register_shape(DOG4_SHAPE)
t.register_shape(DOG5_SHAPE)
t.register_shape(DOG6_SHAPE)
shapes = [CAT1_SHAPE, CAT2_SHAPE, CAT3_SHAPE, CAT4_SHAPE, CAT5_SHAPE, CAT6_SHAPE, DOG1_SHAPE, DOG2_SHAPE, DOG3_SHAPE, DOG4_SHAPE, DOG5_SHAPE, DOG6_SHAPE]

def new_cat_dog():
    cat_dog = t.Turtle()

    # cat_dogs are of different shapes
    shape = random.choice(shapes)
    cat_dog.shape(shape)

    # go to a random location
    cat_dog.penup()
    x = random.randint(-SCREEN_WIDTH//2+40, SCREEN_WIDTH//2-40)
    y = SCREEN_HEIGHT//2
    cat_dog.goto(x,y)

    # each cat_dog moves at different speed horizontally
    cat_dog.dx = random.randint(-10,10)/20
    if(cat_dog.dx == 0):
        cat_dog.dx += 0.5
    cat_dog.dy = 0
    return cat_dog

cat_dogs = []
for i in range(12):
    if(i == 6):
        time.sleep(1)
    new = new_cat_dog()
    cat_dogs.append(new)

# ######################################
# # movement starts here
# ######################################
#
count = 0

while True:
    wn.update()
    if count <= 10:
        duplicate = 2
    else:
        duplicate = 1

    for cat_dog in cat_dogs:

        cat_dog.dy = cat_dog.dy + GRAVITY
        cat_dog.setx(cat_dog.xcor()-cat_dog.dx)
        cat_dog.sety(cat_dog.ycor()-cat_dog.dy)

        if cat_dog.xcor() > SCREEN_WIDTH//2+40 or cat_dog.xcor() < -SCREEN_WIDTH//2-40 or cat_dog.ycor() < -SCREEN_HEIGHT//2 - 80:
            cat_dogs.remove(cat_dog)
            for i in range(duplicate):
                new = new_cat_dog()
                cat_dogs.append(new)
    count +=1