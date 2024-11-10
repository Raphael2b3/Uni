# game of life
import random
import matplotlib.pyplot as plt

class GameOfLife:

    def __init__(self, x, y, initial_state=None):
        self.X = x
        self.Y = y

        if initial_state is not None:
            self.board = initial_state
        else:
            self.board = [[0 for _ in range(self.X)] for _ in range(self.Y)]
            n_of_p = random.randint(0,x*y)
            for _ in range(n_of_p):
                x = random.randint(0, self.X - 1)
                y = random.randint(0, self.Y - 1)
                self.board[y][x] = 1
        print("Initial Board")
        self.visualize()

    def visualize(self):
        plt.imshow(self.board, cmap='gray')
        plt.show()

    def print_board(self):
        for i in range(self.Y):
            for j in range(self.X):
                print(self.board[i][j], end=" ")
            print()
        print()

    def count_neighbours(self, x, y):

        return sum([self.board[i][j] for i in range(max(x - 1,0), min(x + 2,self.X)) for j in range(min(y - 1,0), y + 2)])


    def next_generation(self):
        new_board = [[0 for _ in range(self.X)] for _ in range(self.Y)]
        for i in range(self.Y):
            for j in range(self.X):
                count = self.count_neighbours(i, j)
                if self.board[i][j] == 1:
                    if count < 2 or count > 3:
                        new_board[i][j] = 0
                    else:
                        new_board[i][j] = 1
                else:
                    if count == 3:
                        new_board[i][j] = 1
        self.board = new_board
        self.visualize()

    def run(self, n):
        for i in range(n):
            print("Generation", i + 1)
            self.next_generation()
            print()


if __name__ == '__main__':
    game = GameOfLife(4, 4)


