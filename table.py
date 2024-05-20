from tabulate import tabulate
from robot import Robot

class Table:
    def __init__(self):
        self.robot = Robot()
        self.FACE = ['NORTH', 'EAST', 'SOUTH', 'WEST']
    
    def execute_cmd(self, cmd, x_axis=None, y_axis=None, face='NORTH'):
        state = True
        msg = "SUCCESS"
        if str(cmd).upper() == 'PLACE':

            # Checks for axes input
            if not x_axis or not y_axis:
                msg = "Unable to place robot without cooridinates."
                
                state = False
                return (state, msg)
            else:
                try:
                    x = int(x_axis)
                    y = int(y_axis)
                except Exception:
                    msg = f"Unable to place robot, coordinates should be a number. {x_axis},{y_axis}."
                    state = False
                    return (state, msg)
                
            if 0 < int(x_axis) > 4 or 0 < int(y_axis) > 4:
                msg = f"Unable to place robot, improper coordinates. {x_axis},{y_axis}."
                state = False
                return (state, msg)
            
            # Checks for face input
            if face.upper() not in self.FACE:
                msg = f"Unrecognize direction {face}."
                state = False
                return (state, msg)
            
            self.robot.place(x_axis=x_axis, y_axis=y_axis, facing=face)
            msg = f"Robot successfully placed at {x_axis},{y_axis}; facing {face}."

        elif str(cmd).upper() == 'MOVE':
            self.robot.move()
            msg = f"Current location: {self.robot.x},{self.robot.y} facing {self.robot.facing}"

        elif str(cmd).upper() == 'LEFT':
            self.robot.left()
            msg = f"Now facing {self.robot.facing}."

        elif str(cmd).upper() == 'RIGHT':
            self.robot.right()
            msg = f"Now facing {self.robot.facing}"

        elif str(cmd).upper() == 'REPORT':
            msg = self.robot.report()

        else:
            msg = "Unknown command, please select from PLACE, MOVE, LEFT, RIGHT, REPORT."
            state = False
            return (state, msg)

        return (state, msg)

    def create_table(self):
        # Create a 5 by 5 table with empty cells.
        table = [["" for _ in range(5)] for _ in range(5)]

        # Setting left-most, bottom-most as grid 0,0.
        table[4 - int(self.robot.y)][int(self.robot.x)] = 'X'
        print(tabulate(table, tablefmt="grid"))