# Python 2.7
# by Aaron Aikman

from random import choice

class TicTacToeBoard(object):

    def __init__(self, tiles = 3):
        self.x = 'x'
        self.o = 'o'
        self.tiles = tiles
        self.board_status = ['_']*9
        self.player_turn = True
        self.win = 0
        self.win_record = [0, 0, 0]
        self.draw_board()

    def draw_board(self):
        ''' Drawing board '''
        for nl in range(10):
            print '\n'
        print self.board_status[0] + '|' + self.board_status[1] + '|' +self.board_status[2]
        print self.board_status[3] + '|' + self.board_status[4] + '|' +self.board_status[5]
        print self.board_status[6] + '|' + self.board_status[7] + '|' +self.board_status[8]
        # Printing win record if not first game
        if sum(self.win_record) > 0:
            self.show_win_record()

    def add_x(self, pos):
        ''' Placing x is possible '''
        if self.win:
            self.reset_board()
        else:
            pos_to_change = self.board_status[pos-1]
            if pos_to_change != self.x and pos_to_change != self.o:
                self.board_status[pos-1] = self.x
                self.player_turn = False
                self.check_for_win()

    def reset_board(self):
        ''' Resetting board after game over '''
        self.board_status = ['_']*9
        self.player_turn = True
        self.win = 0
        self.draw_board()

    def get_board_options(self):
        ''' Analysing board combinations '''
        return {'012': self.board_status[0:3],
                '345': self.board_status[3:6],
                '678': self.board_status[6:9],
                '036': self.board_status[0:9:3],
                '147': self.board_status[1:9:3],
                '258': self.board_status[2:9:3],
                '048':  self.board_status[0:9:4],
                '246': self.board_status[2:8:2]}

    def play_ai(self):
        ''' Choosing where ai should play '''
        spot_to_play = None

        # Claiming center if possible
        if self.board_status[4] == '_':
            spot_to_play = 4
        else:
            # Checking for only one x
            if self.board_status.count(self.x) == 1:
                if self.board_status.count(self.o) == 1:
                    spot_to_play = choice(self.get_adj_spots(self.board_status.index(self.o)))
                else:
                    spot_to_play = choice(self.get_adj_spots(self.board_status.index(self.x)))

            # checking for near-wins and picking an o win if possible
            else:
                for k, v in self.get_board_options().iteritems():
                    if v.count(self.o) == 2 and self.x not in v:
                        for spot in [int(i) for i in list(k)]:
                            if self.board_status[spot] == '_':
                                spot_to_play = spot

                    if spot_to_play != 0 and not spot_to_play and v.count(self.x) == 2 and self.o not in v:
                        for spot in [int(i) for i in list(k)]:
                            if self.board_status[spot] == '_':
                                spot_to_play = spot

            # picking a random spot to play if nothing else found
            if spot_to_play != 0 and not spot_to_play:
                spot_to_play = choice(self.get_adj_spots(4))
            while self.board_status[spot_to_play] != '_':
                spot_to_play = choice(self.get_adj_spots(4))

        self.board_status[spot_to_play] = self.o

        self.player_turn = True
        self.check_for_win()

    def get_adj_spots(self, pos):
        ''' Returns good choices '''
        adj_spots_answer = dict([(0, (1,3)),
                                 (1, (0, 2)),
                                 (2, (1, 5)),
                                 (3, (0, 6)),
                                 (4, (0, 2, 6, 8)), # Playing only in the corners
                                 (5, (2, 8)),
                                 (6, (3, 7)),
                                 (7, (6, 8)),
                                 (8, (5, 7))
            ])
        return adj_spots_answer[pos]

    def show_win_record(self):
        ''' Prints win record '''
        print 'Player Wins: {} | Computer Wins: {} | Draws: {}'.format(self.win_record[0],
                                                                       self.win_record[1],
                                                                       self.win_record[2])

    def check_for_win(self):
        ''' Checks to see if the game is over '''
        self.win = 0
        for wc in self.get_board_options().values():
            if ''.join(wc) == "xxx":
                self.win = 1
            if ''.join(wc) == "ooo":
                self.win = 2
        if self.win == 2:
            self.draw_board()
            print 'You lose!'
            self.win_record[self.win - 1] += 1
        elif self.win == 1:
            self.draw_board()
            print 'You win!'
            self.win_record[self.win - 1] += 1
        else:
            if '_' not in self.board_status:
                # Checking for draw
                self.win = 3
                self.win_record[self.win - 1] += 1
                self.draw_board()
                print "it's a draw"
            elif not self.player_turn:
                self.play_ai()
            else:
                self.draw_board()


# Creating board
b = TicTacToeBoard()

# Asking for input
while True:
    where_to_play = raw_input("Please input a number from 1-9\n")
    # Checking if input is valid
    if where_to_play != '' and int(where_to_play) in range(1,10):
        b.add_x(int(where_to_play))
    elif b.win:
        # Resetting board if game is over
        b.reset_board()

