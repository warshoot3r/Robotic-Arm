import os
import time
class robot_arm:
    def __init__(self, movement_name):
        self.number_of_moves = 0
        self.movement_name = movement_name
        self.move_list = []
    
    def print_var(self):
        print("printing the properties now")
        print(
            self.number_of_moves, self.movement_name
          )
        print("printing the move list")
        
    def add_moves(self, move_goal):
        self.move_list.append([self.number_of_moves, move_goal])
        self.number_of_moves += 1
        print("added a move goal")

    def print_moves(self):
        for number_of_moves in self.move_list:
            print(self.move_list[number_of_moves[0]] )
            if(number_of_moves[0] == (self.move_list[-1][0]) ): 
             print("printed all the move list now")    

    def remove_last_move(self):
            self.move_list.pop()
            #print("removed array", self.move_list[array_number])
            print("value of",self.move_list[-1][1],"was removed")

    def write_to_file(self, saved_file_name):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        full_saved_file_name = __location__ + "/" + saved_file_name + '.txt'
        with open(full_saved_file_name, "w") as file:
         for number_of_moves in self.move_list:
            file.write( str(self.move_list[number_of_moves[0]][1]) )
            file.write('\n')
            if(number_of_moves[0] == (self.move_list[-1][0])):
                print("Exported File")

    def open_from_file(self, file_path):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        file_location =  __location__ + "/" + file_path + ".txt"
        with open(file_location, 'r') as opened_file:
            print("Imported File")
            print(opened_file.read())

    def move_arm_routine(self, number_of_times):
        print("Moving the routine name"+ ' ' + number_of_times + 'times')
        for number in range(int(number_of_times)) :
         for number_of_moves in self.move_list:
          print(self.move_list[number_of_moves[0]])
          if number_of_moves[0] == self.move_list[-1][0]:
           print('\n')

def interactive_mode():
        print("#################################")
        print("#########starting################")
        print("#################################")
        interactive_mode_robot = robot_arm("interactive_move")
        contains_moves = 0
        i = input("interactive? y or n\n")
        if i == 'y':
          print("enter interactive mode")
          while(True):
                print('1.Press 1 for Record\n2.Press 2 for play\nq to go back\n3.press R to save\n4.press L to load')
                i = input()
                if i == '1':
                    contains_moves = 1
                    print("entering record......")
                    while True:
                     i = record_mode(interactive_mode_robot)
                     if i == 1:
                       break
                elif i == '2':
                    print("entering play mode.....")
                    play_mode(interactive_mode_robot)
                    time.sleep(2)
                elif i == 'q':
                  print("going back.")
                  interactive_mode()
                elif i == 'R':
                  interactive_mode_robot.write_to_file('save.robot')
                  time.sleep(4)
                elif i == 'L':
                  interactive_mode_robot.open_from_file("save.robot")
        elif i == 'n' :
            print('Ok exiting...')



def record_mode(self):
    print('\ntype finish to end')
    i = input("\nenter a value\n")
    if i == 'finish':
        return 1
    self.add_moves(i)
    print("Ok.")


def play_mode(self):
    self.print_moves()


new = robot_arm("Move up")
new.print_var()
new.add_moves(30)
new.add_moves(40)
new.add_moves(50)
new.add_moves(60)

new.print_moves()

new.write_to_file("new")
new.open_from_file("new")
new.move_arm_routine("3")

interactive_mode()