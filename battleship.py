'''
Tiamara Craig
Csc 120- 2D
Descripition: This program works to model the game battleship, where
              two players enter a series of guesses in order to find
              the x,y coordinates of where their oppponent has placed
              a set of ships. In this program the ships and the guesses
              will be read in from the user in order to sink one or all ships
              with the help of classes.

'''




from sys import*




''' class ship: used to store information about the
    ship, such as the type, size, and its positions'''
class Ship:
    ''' init(): initializes the attributes for the ship class, &
        parameters: ship_type, size, (x1,y1) and (x2,y2)
        pre-condition: the paramteres are strings
        post-condidtion: the parameters are class obj's'''
    def __init__(self, ship_type, size, x1, y1, x2, y2):
        self._type = ship_type
        self._size = size
        self._x1 = int(x1)
        self._y1 = int(y1)
        self._x2 = int(x2)
        self._y2 = int(y2)
        # keeps track of ships left for one type
        self._surived = int(size)
        



    def get_type(self):
        return self._type




    def get_size(self):
        return self._size




    ''' ship_pos(): creates a 2d list of all the pos occupied for one ship
        returns: pos_lis, the lis of all pos's occupied by a ship
        pre-condidtion: the positions stretch vertically and horizontally
        post_condition: pos_lis is the len of the ship size'''
    def ship_pos(self):
        pos_lis = []
        # if statements to check ship direction on board
        # when x vals are the same: vertical
        # when y vals are the same: horizontal
        if self._x1 == self._x2:
            # end: the end pt for the ship 
            # start: the start pt for the ship 
            end = max(self._y1, self._y2)
            start = min(self._y1, self._y2)
            # loops from start to end pt, adds vert. pos's type(lis)
            for pos in range(start, end+1):
                pos_lis.append([self._x1, pos])
        if self._y1 == self._y2:
            end = max(self._x1, self._x2)
            start = min(self._x1, self._x2)
            # loops from start to end pt, adds horz. pos's type(lis)
            for pos in range(start, end+1):
                pos_lis.append([pos, self._y1])
        return pos_lis




    def destroy_ship(self):
        self._surived -= 1




    def ships_left(self):
        return self._surived




    def __str__(self):
        return str(self._type)




    def __repr__(self):
        return str(self._type)




''' class GridPos: stores info about a ship's x,y
    coordinates, if there is a ship occupying that
    x,y pos on the board, and if the pos has been guessed'''
class GridPos:
    ''' init(): initializies the attributes for the GridPos class
        parameters: x, y, ship
        pre-condidtion: the x, y, and ship vals are Ship obj's
        post_condition: the atrributes are Gridpos obj's being a
        collection of Ship obj's'''
    def __init__(self, x, y, ship):
        self._x = x
        self._y = y
        # shipThere indicates the type of ship or None if empty
        self._shipThere = ship
        # initializes all guessed pos's to False
        self._guessed = False


    def get_x(self):
        return self._x

    def get_y(self):
        return self._y
    
    def occupied(self):
        return self._shipThere

    def set_guess(self):
        self._guessed = True

    def guessed(self):
        return self._guessed

    def __str__(self):
        return('({},{}): {}'.format(self._x, self._y, self._shipThere))

    def __repr__(self):
        return('({},{}): {}'.format(self._x, self._y, self._shipThere))

    
''' class Board: stores info about the size of the board
    (10x10) and the number of ships on the board
    as well as their location'''
class Board:
    ''' init(): initializes the attributes for the Board class
        pre-condidtion: the board is empty
        post_condition: the board has been created'''
    def __init__(self):
        self._board = []
        # the numbers of ships that have completely sunk
        self._ships_sunk = 0
        self.make_board()

    
    ''' make_board(): creates the 10x10 board of
        GridPos obj's with ship pos set as None
        returns: the 2d list of the 10x10 board of GridPos obj's
        pre-condidtion: the board is empty
        post_condition: the board is created with no ships'''
    def make_board(self):
        # for loops: creates a 2d list each len(10)
        for x in range(10):
            inner_lis = []
            for y in range(10):
                # create a GridPos obj for each x,y val
                # with no ships at those pos's
                g_pos = GridPos(x, y, None)
                inner_lis.append(g_pos)
            self._board.append(inner_lis)
        return self._board
    



    def get_board(self): 
        return str(self._board)
        
    


    ''' add_ship(): adds all correct ship positions to the board,
        now an x,y GripPos obj holds info from the Ship class
        parameters: s, ship info from the file input
        returns: the board, with ships now occupying some x,y pos's
        pre-condidtion: the board contains 0 ships
        post_condition: the board contains 5 ships, one of each type'''
    def add_ship(self, s):
        ship_lis = []
        # a dict to store info about a ship and its correct size
        size = {'A': 5, 'B': 4, 'S': 3, 'D': 3, 'P': 2}
        # abbriv: the letter that stands for the ship type
        abbriv = s[0]
        # create a ship obj for each ship, s, passed in
        ship = Ship(s[0], size[abbriv], s[1], s[2], s[3], s[4])
        # checks if the ships are diagonal, prints error/exits
        if s[1] != s[3] and s[2] != s[4]:
            print('ERROR: ship not horizontal or vertical: ' + ' '.join(s) +'\n')
            exit(1)
        # checks if the ship is the wrong size for its type, prints error/exits
        if len(ship.ship_pos()) != size[str(ship)]:
            print('ERROR: incorrect ship size: ' + ' '.join(s) +'\n')
            exit(1)
        # loops over the ship pos from the Ship class
        for i in range(len(ship.ship_pos())):
            x = ship.ship_pos()[i][0]
            y = ship.ship_pos()[i][1]
            # create a GridPos obj for the ship at the x,y pos
            g_pos = GridPos(x, y, ship)
            # checks if the GridPos obj on the board[x][y] is already a ship,
            # then prints error/exits
            if self._board[x][y].occupied() != None:
                print('ERROR: overlapping ship: ' + ' '.join(s) + '\n')
                exit(1)
            # adds the GridPos obj as a Ship obj on the board
            self._board[x][y] = g_pos
        return self._board


        

    ''' process_guess(): reads in the file for player 2's guesses,
        then feeds each guess, one at a time into the method
        check_guess to see if its a hit or miss
        pre-condidtion: the file is not empty
        post_condition: the file can be read'''
    def process_guess(self):
        guess = []
        fname = input()
        # catches/raises an error message if the file can not be read
        # exits the program
        try:
            file = open(fname).readlines()
        except:
            print('ERROR: Could not open file: ' + fname)
            exit(1)
        # loops over the line in the file
        for line in file:
            parts = line.split()
            # guess: adds the list or x,y pos from parts
            guess.append(parts)
        # loops through each elem, a lis, in guess
        for elem in guess:
            if elem != []:
                # calls the method check_guess to evaluate elem
                self.check_guess(elem)





        ''' check_guess(): compares the pos read in from the method process_guess()
            to check if the guess is a valid Ship pos on the Board, evaluates
            each guess to be a hit, miss, or illegal guess
            parameters: guess, lis of one x,y pair from process_guess()
            returns: None
            pre-condidtion: board has 5 valid ships 
            post_condition: the board has less than 5 or 0 ships'''
    def check_guess(self, guess):
        i = 0
        # checks if the guess value is out of bounds
        if int(guess[0]) > 10 or int(guess[1]) > 10:
            print('illegal guess')
            return
        # while loop: loops over the 2d grid/ board
        while i < len(self._board):
            j  = 0
            while j < len(self._board[i]):
                # x, y the str representation of the x, y GridPos on the board
                x = self._board[i][j].get_x()
                y = self._board[i][j].get_y()
                # ship_type: calls to GridPos method to detemine if a pos holds a ship
                # grid_pos: the GridPos obj at the pos i,j
                ship_type = self._board[i][j].occupied()
                grid_pos = self._board[i][j]
                # checks if the guessed x,y matches the the pos on the board
                # and if there is a ship there, prints hit
                if guess[0] == str(x) and guess[1] == str(y) and ship_type != None:
                    # checks if the guess has already been called
                    # calls the GridPos methods to set guessed to True
                    if grid_pos.guessed() == False:
                        grid_pos.set_guess()
                        # subtracts from the num ships on the board for one type
                        ship_type.destroy_ship()
                        # calls to the GridPos  method to see if a type of ship has 0
                        # surving ships on the board
                        if int(ship_type.ships_left()) == 0:
                            # updates the num of total ships sunk
                            self._ships_sunk += 1
                            print('{} sunk'.format(ship_type))
                            # if the tot num of ships sunk is 5, game is over
                            if int(self._ships_sunk) == 5:
                                print('all ships sunk: game over')                           
                        else:
                            print('hit')
                    else:
                        # if the guess has been previously guessed
                        print('hit (again)')
                    return
                    i, j= 0, 0
                else:
                    j += 1
                # if the pos's for a guess is on the board but does not hold a ship
                # print miss, updates guessed to True
                if guess[0] == str(x) and guess[1] == str(y) and ship_type == None:
                    if grid_pos.guessed() == False: 
                        print('miss')
                        grid_pos.set_guess()
                    else:
                        # if the guess has been previously guessed
                        print('miss (again)')
                    return
            i += 1
                      


                                  
    def __str__(self):
        return str(self._board)




    def __repr__(self):
        return str(self._board)




''' main() calls to the algorithm and fxns below in order written'''
def main():
    # holds info on how many ships for one type
    ships = {}
    fname = input()
    # catches/raises an error message if file can not be read, exits
    try:
        place_file = open(fname).readlines()
    except:
        print('ERROR: Could not open file: ' + fname)
        exit(1)
    # create a Board obj
    board = Board()
    # loops through the placement file
    for line in place_file:
        ship_info = line.split()
        # loops over the lis of x,y pos's in ship_info
        for pos in ship_info[1:]:
            # checks if the ship pos is out-of-bounds
            # prints error/ exits
            if int(pos) > 10:
                print('ERROR: ship out-of-bounds: ' + line)
                exit(1)
        # adds the ship info from file to the Board method add_ship()
        board.add_ship(ship_info)
        s_type = ship_info[0]
        # maps the ship type to how many there are in the file
        if s_type not in ships:
            ships[s_type] = 0
        ships[s_type] += 1
    # loops over the num of ships in the dict, ships
    # checks if there are only 5 ships, one of each type
    for num_of in ships.values():
        if len(ships) != 5 or num_of != 1:
            print('ERROR: fleet composition incorrect')
            exit(1)
    # calls the the Board method process_guess() to print out
    # what each guess evaluated to 
    board.process_guess()
main()

