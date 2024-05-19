from robot import Robot

class Table:
    def __init__(self):
        self.robot = Robot()
    
    def execute_cmd(self, cmd, x_axis=None, y_axis=None):
        if cmd == 'PLACE'.lower():
            pass
        elif cmd == 'MOVE'.lower():
            pass
        elif cmd == 'LEFT'.lower():
            pass
        elif cmd == 'RIGHT'.lower():
            pass
        elif cmd == 'REPORT'.lower():
            Robot.report()
        else:
            print("Unknown command, please select from PLACE, MOVE, LEFT, RIGHT, REPORT.")

