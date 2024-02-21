i=0
def Monkey_go_box(x,y):
    global i
    i=i+1
    print('step:',i,'Monkey from',x,'Go to '+y)
def Monkey_move_box(x,y):
    global i
    i = i + 1
    print('step:', i, 'Monkey take the box from', x, 'deliver to ' + y)
def Monkey_on_box():
    global i
    i+=1 
    print('step:', i, 'Monkey climbs up the box')
def Monkey_get_banana():
    global i
    i+=1
    print('step:', i, 'Monkey picked a banana')
monkey=input('Enter Position where Monkey lies:\t')
banana=input('Enter Position where Banana lies:\t')
box=input('Enter Position where Box lies:\t')
print('The steps are as follows:\n')
Monkey_go_box(monkey, box)
Monkey_move_box(box, banana)
Monkey_on_box()
Monkey_get_banana()
