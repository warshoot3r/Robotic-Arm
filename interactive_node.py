import time
import os
from robot_class import robot_arm
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
                  time.sleep(4)
        elif i == 'n' :
            print('Ok exiting...')
            StopIteration

def record_mode(self):
    print('\ntype finish to end')
    i = input("\nMove the arm in RVIS plan and execute. Then Press any key to remember the step\n")
    if i == 'finish':
        return 1
    self.add_moves(i)
    print("Ok.")


def play_mode(self):
    self.print_moves()