# create a function that prints the range() for each day of the week. 
# print even inde numbers only 

Days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday' , 'Saturday'] 

for i in range(2, len(Days_of_the_week), 2):
    print (Days_of_the_week[i])

# print (Days_of_the_week[2:4])


Days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday' , 'Saturday'] 
breakfast= ['cereal','fruit', 'yogurt', 'panckaes', 'oatmeal', 'waffles', 'donut']
lunch= ['turkey sandwich', 'pizza','lunchable', 'pbj', 'salad', 'soup', 'gyro']
dinner= ['steak', 'chicken', 'pasta', 'tacos', 'burger', 'cassarole', 'potroast']


for day,breakfast,lunch, dinner in zip (Days_of_the_week, breakfast, lunch, dinner):

    #    for lunch, in zip (Days_of_the_week, lunch):
    #     for dinner, in zip (Days_of_the_week, dinner):

            print (f'Today on {day} I am having some {breakfast} for breakfast {lunch} for lunch and {dinner} for dinner')
            # print (f'Today on {Days_of_the_week} I am having a {lunch} for lunch')
            # print (f'Today on {Days_of_the_week} I am having some {dinner} for dinner')


# lunch 
#     for Days_of_the_week, lunch in zip (Days_of_the_week, lunch):
#      print (f'Today on {Days_of_the_week} I am having a {lunch} for lunch')

#  Dinner 
#      for Days_of_the_week, dinner in zip (Days_of_the_week, dinner):
#                 print (f'Today on {Days_of_the_week} I am having some {dinner} for dinner')

#     for i in food_list: 
#     print ('For breakfast I am having') (i)
        
    


########################Task 1 While loop Write a while loop with a condition that will never be true (an infinite loop). Ask the user a series of questions until their answer triggers a break s
            
            # while True: 
            #         User= input("Name a fruit or type quit to exit ")
            #         if User== 'quit': 
            #                 print ("Stopping loop")
            #                 break
            #         else: 
            #                 print (f'{User} Thats a tasty fruit')

## Question 3 Task 1
while True: 
        looping = input("is this your first question ")
        if looping== 'yes':
                 continue
        else: print("Please enter yes or no")

        print (f'{looping} correct answer another question')
        input ("is this your second question?")
        if looping== 'yes':
            continue
        print (f'{looping} correct answer another question')
        input ("is this your third question?")
        if looping== 'yes':
            print (f'{looping} correct answer another question')
            continue
        looping= input ("is this your fourth question?")
        if looping== 'yes':
            print (f'{looping} correct answer your last question')
            continue
        looping = input("is this your first question ")
        print ("Great you answered all my questions, have a great day!")

#Task 2 


        iteration = 1
        while iteration <= 5:
            print("Iteration", iteration)
            iteration += 1

                         
