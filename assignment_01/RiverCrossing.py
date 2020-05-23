leftshore = ["cabbage", "goat", "wolf"]
rightshore = []
final = []


def moveobject(objects, lastdirection):
    if lastdirection == "left":
        leftshore.remove(objects)
        rightshore.append(objects)
        return "right"
    else:
        rightshore.remove(objects)
        leftshore.append(objects)
        return "left"


def isSafeToMove(objects, shore):
    forbidden_pair1 = ["goat", "wolf"]
    forbidden_pair2 = ["cabbage", "goat"]
    leftover = shore.copy()
    if objects:
        leftover.remove(objects)
    leftover.sort()
    if leftover != forbidden_pair1 and leftover != forbidden_pair2:
        return True
    else:
        return False


def changedirection(lastdirection):
    if lastdirection == "left":
        return "right"
    else:
        return "left"


def solution():
    movableObjects = []
    lastmovedObject = ""
    lastdirection = "left"
    state = ""
    while len(rightshore) != 3:
        if lastdirection == "left":
            movableObjects = leftshore
        else:
            movableObjects = rightshore
        state = "farmer"
        # condition for moving the objects from the right shore:

        if len(movableObjects) == 1 and lastdirection == "right" or len(movableObjects) != 3 and lastdirection == "right" and isSafeToMove("", movableObjects):
            lastdirection = changedirection(lastdirection)
            lastmovedObject = ""

        # condition for moving the objects from the left shore :

        else:
            for objects in movableObjects:
                if lastmovedObject != objects and isSafeToMove (objects, movableObjects):
                    lastdirection = moveobject(objects, lastdirection)
                    lastmovedObject = objects
                    break
            state += " and " + lastmovedObject

        state += " rowed to " + lastdirection + " shore "

        final.append(state)


if __name__ == "__main__":
    solution()
    if len(rightshore) == 3:
        print("Successfully crossed the river")
    count = 1
    for step in final:
        print(" step {0} : ".format(count) + step)
        count += 1



