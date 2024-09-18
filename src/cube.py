from typing import Optional, Dict

class Cube:
    def __init__(self, state: Optional[dict] = None):
        if state is None:
            state = {
                "top": [
                    ["⬜", "⬜", "⬜"],
                    ["⬜", "⬜", "⬜"],
                    ["⬜", "⬜", "⬜"]
                    ],
                "bottom": [
                    ["🟨", "🟨", "🟨"],
                    ["🟨", "🟨", "🟨"],
                    ["🟨", "🟨", "🟨"]
                    ],
                "left": [
                    ["🟩", "🟩", "🟩"],
                    ["🟩", "🟩", "🟩"],
                    ["🟩", "🟩", "🟩"]
                    ],
                "right": [
                    ["🟦", "🟦", "🟦"],
                    ["🟦", "🟦", "🟦"],
                    ["🟦", "🟦", "🟦"]
                    ],
                "front": [
                    ["🟥", "🟥", "🟥"],
                    ["🟥", "🟥", "🟥"],
                    ["🟥", "🟥", "🟥"]
                    ]
                    ,
                "back": [
                    ["🟧", "🟧", "🟧"],
                    ["🟧", "🟧", "🟧"],
                    ["🟧", "🟧", "🟧"]
                    ]
            }
        self.state = state
    def print_cube(self, face):
        content = ""
        for row in self.state[face]:
            print(row)
            content += f"\n|{row[0]} | {row[1]} | {row[2]} |\n"
        return {"State": face, "Face": content, "dict": self.state["bottom"]}

    def rotate_face_clockwise(self, face_name):
        state = self.state[face_name]
        ####### Corner cublet rotation ######
        temp = state[0][0]
        state[2][0] = state[2][2]
        state[0][0] = state[2][0]
        state[2][2] = state[0][2]
        state[0][2] = temp

        ###### Edge cublet rotation ######
        temp = state[0][1]
        state[0][1] = state[1][0]
        state[1][0] = state[2][1]
        state[2][1] = state[1][2]
        state[1][2] = temp

    def turn_cube(self, turn_direction: str, times: int):
        return TurnCubeFactory.turn_cube(self, turn_direction)

class TurnCubeFactory():
    @staticmethod
    def turn_cube(cube: Cube, turn_direction):

        if turn_direction == "right":
            cube.state["left"], cube.state["front"], cube.state["right"] = cube.state["front"], cube.state["right"], cube.state["back"]
    """

    def rotate_top_clockwise(self):
        self.rotate_face_clockwise("Top")
        temp = self.face["Front"][0]
        self.face["Front"][0] = self.face["Right"][0]
        self.face["Right"][0] = self.face["Back"][0]
        self.face["Back"][0] = self.face["Left"][0]
        self.face["Left"][0] = temp

    def rotate_bottom_clockwise(self):
        self.rotate_face_clockwise("Bottom")
        temp = self.face["Front"][2]
        self.face["Front"][2] = self.face["Left"][2]
        self.face["Left"][2] = self.face["Back"][2]
        self.face["Back"][2] = self.face["Right"][2]
        self.face["Right"][2] = temp

    def rotate_left_clockwise(self):
        self.rotate_face_clockwise("Left")
        temp_col = [self.face["Top"][i][0] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][0] = self.face["Back"][2 - i][2]
            self.face["Back"][2 - i][2] = self.face["Bottom"][i][0]
            self.face["Bottom"][i][0] = self.face["Front"][i][0]
            self.face["Front"][i][0] = temp_col[i]

    def rotate_right_clockwise(self):
        self.rotate_face_clockwise("Right")
        temp_col = [self.face["Top"][i][2] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][2] = self.face["Front"][i][2]
            self.face["Front"][i][2] = self.face["Bottom"][i][2]
            self.face["Bottom"][i][2] = self.face["Back"][2 - i][0]
            self.face["Back"][2 - i][0] = temp_col[i]

    def rotate_front_clockwise(self):
        self.rotate_face_clockwise("Front")
        temp = [self.face["Top"][2][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][2][i] = self.face["Left"][i][2]
            self.face["Left"][i][2] = self.face["Bottom"][0][i]
            self.face["Bottom"][0][i] = self.face["Right"][i][0]
            self.face["Right"][i][0] = temp[i]

    def rotate_back_clockwise(self):
        self.rotate_face_clockwise("Back")
        temp = [self.face["Top"][0][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][0][i] = self.face["Right"][i][2]
            self.face["Right"][i][2] = self.face["Bottom"][2][i]
            self.face["Bottom"][2][i] = self.face["Left"][i][0]
            self.face["Left"][i][0] = temp[i]

"""
#myCube = Cube()
myCube = Cube({'top': [['1', '2', '3'], ['⬜', '⬜', '⬜'], ['⬜', '⬜', '⬜']], 'bottom': [['🟨', '🟨', '🟨'], ['🟨', '🟨', '🟨'], ['🟨', '🟨', '🟨']], 'left': [['🟩', '🟩', '🟩'], ['🟩', '🟩', '🟩'], ['🟩', '🟩', '🟩']], 'right': [['🟦', '🟦', '🟦'], ['🟦', '🟦', '🟦'], ['🟦', '🟦', '🟦']], 'front': [['🟥', '🟥', '🟥'], ['🟥', '🟥', '🟥'], ['🟥', '🟥', '🟥']], 'back': [['🟧', '🟧', '🟧'], ['🟧', '🟧', '🟧'], ['🟧', '🟧', '🟧']]})
print(myCube.state)
print(myCube.state)
print(myCube.print_cube("top"))

myCube.rotate_face_clockwise("top")

print(myCube.state)

