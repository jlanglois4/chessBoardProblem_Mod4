class Chessboard:

    def __init__(self, squares):
        self.squares = squares

    def calculate_grains(self):
        count = 0
        rice = .5
        for x in range(self.squares):
            rice *= 2
            count += 1
            print(f"Square {count}: {int(rice)} grains")
