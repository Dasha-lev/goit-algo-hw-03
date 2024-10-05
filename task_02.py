import turtle 

#Функція для малювання кривої Коха
def koch_curve(t, length, level):
    if level == 0: 
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)

#Функція для створення сніжинки
def koch_snowflake(t, length, level):
    for _ in range(3):  
        koch_curve(t, length, level)
        t.right(120)

#Основна функція
def main():
    screen = turtle.Screen()
    screen.bgcolor("white")  

    level = int(input("Введіть рівень рекурсії для сніжинки Коха (рекомендується від 0 до 4): "))

    t = turtle.Turtle()
    t.speed(0)  
    length = 300  
    t.penup() 
    t.goto(-150, 50)  
    t.pendown()  

    koch_snowflake(t, length, level) 
  
    t.hideturtle()  
    screen.exitonclick()  

if __name__ == "__main__":
    main()
