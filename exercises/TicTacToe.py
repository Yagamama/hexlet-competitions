class TicTacToe():
    def __init__(self, level='easy'):
        self.field = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        if level == 'easy':
            self.level = Easy()
        else:
            self.level = Normal()

    def go(self, x=-1, y=-1):
        self.level.go(x, y, self.field)
        print('next go')
        for i in range(3):
            print(self.field[i])
        return self.is_win(x, y)

    def is_win(self, x, y):
        result = False
        for i in range(3):
            if ((self.field[i][0] == self.field[i][1] == self.field[i][2] and self.field[i][0]) or \
                (self.field[0][i] == self.field[1][i] == self.field[2][i] and self.field[0][i])):
                result = True
        if ((self.field[0][0] == self.field[1][1] == self.field[2][2] and self.field[0][0]) or \
            (self.field[2][0] == self.field[1][1] == self.field[0][2] and self.field[2][0])):
            result = True
        return result


class Easy():
    # BEGIN (write your solution here)
    def go(self, x, y, field):
        if x >= 0 and y >=0: 
            field[x][y] = 'x'
        else:
            can_go = True
            for i in range(3):
                for j in range(3):
                    if field[i][j] is None and can_go:
                        field[i][j] = 'o'
                        can_go = False
        return field
    # END


class Normal():
    def go(self, x, y, field):
        if x >= 0 and y >=0: 
            field[x][y] = 'x'
        else:
            can_go = True
            for i in range(2, -1, -1):
                for j in range(3):
                    if field[i][j] is None and can_go:
                        field[i][j] = 'o'
                        can_go = False
        return field


if __name__ == '__main__':
    game = TicTacToe()
    game.go(1, 1)
    game.go()
    game.go(1, 2)
    print(not game.go())
    print(not game.go(2, 2))
    is_winner = game.go()
    print(is_winner)
    # game = TicTacToe('normal')
    # game.go(0, 2)
    # game.go()
    # game.go(0, 1)
    # print(not game.go())
    # print(not game.go(1, 2))
    # is_winner = game.go()
    # print(is_winner)