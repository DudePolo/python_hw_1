def hello():
    print('Hello user')

hello()

def pack(item1, item2, item3):
    print([item1, item2, item3])

pack('ham sandwich', 'chocolate milk', 'apple')

def eat_lunch(food_list):
    if food_list:
        print('First I eat', food_list[0])
        for i in food_list[1:]:
            print('Next I eat', i)
    else:
        print('My lunchbox is empty!')

food_list = ["sandwich", "apple", "chips", "chocolate milk"]
eat_lunch(food_list)
eat_lunch([])