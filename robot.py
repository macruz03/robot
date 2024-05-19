class Robot:
    FACE = ['NORTH', 'EAST', 'SOUTH', 'WEST']
    def __init__(self):
        self.x = None
        self.y = None
        self.facing = None
    
    # Place the robot within the specific coordinates and indicate where it is facing.
    def place(self, x_axis, y_axis, facing):
        self.x = x_axis
        self.y = y_axis
        self.facing = facing
            
    # Move the robot one space in the direction it is facing.
    def move(self):
        if self.facing == 'NORTH':
            # Move 1 space up
            self.y = self.y + 1
        elif self.facing == 'EAST':
            # Move 1 space left
            self.x = self.x + 1
        elif self.facing == 'SOUTH':
            # Move 1 space down
            self.y = self.y - 1
        elif self.facing == 'WEST':
            # Move 1 space right
            self.x = self.x - 1

    # Rotate the robot facing 90 degrees to the left of it's current face.
    def left(self):
        # We will try to get the index minus one (left) of the current face.
        # By using modulo 4, we can get to circular list.
        # If value of modulo is negative, the result will be module minus negative value.
        self.facing = self.FACE[(self.FACE.index(self.facing) - 1) % 4]
    
    # Rotate the robot facing 90 degrees to the right of it's current face.
    def right(self):
        # We will try to get the index plus one (right) of the current face.
        # By using modulo 4, we can get to circular list.
        self.facing = self.FACE[(self.FACE.index(self.facing) + 1) % 4]
    
    # Report the current coordinates and face of the robot.
    def report(self):
        print("Current location: x-axis: " + self.x + "y-axis: " + self.y + "Facing: " + self.facing)