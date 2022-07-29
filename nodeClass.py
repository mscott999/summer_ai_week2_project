class Node:
    def __init__(this, input, parent):
        this.rawState = input
        this.cost = 1
        if (parent == None):
            this.location = input
            this.direction = None
            this.parent = None
        else:
            this.location = input[0]
            this.direction = input[1]
            this.parent = parent
    
    def hasParent(this):
        if (this.parent == None):
            return False
        else:
            return True
