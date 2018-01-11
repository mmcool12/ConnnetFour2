import random
import webbrowser
from graphics import *
def inarow_Neast( ch, r_start, c_start, A, N): 
    '''his should start from r_start and c_start and check for three-in-a-row eastward of element ch, 
    returning True or False, as appropriate '''
    if r_start > len(A) or c_start + N > len(A[0]):
        return False
    for i in range(N):                  # loop i as needed
        if A[r_start][c_start+i] != ch:   # check for mismatches
            return False                # mismatch found - return False

    return True                         # loop found no mismatches - return True  
def inarow_Nsouth( ch, r_start, c_start, A, N ): 
    '''this should start from r_start and c_start and check for three-in-a-row southward of element ch, 
    returning True or False, as appropriate '''
    if r_start + N > len(A) or c_start > len(A[0]):
        return False
    for i in range(N):                  # loop i as needed
        if A[r_start+i][c_start] != ch:   # check for mismatches
            return False                # mismatch found - return False

    return True                         # loop found no mismatches - return True  
def inarow_Nsoutheast( ch, r_start, c_start, A, N ): 
    '''    this should start from r_start and c_start and check for three-in-a-row southeastward of element ch, 
    returning True or False, as appropriate '''
    if r_start + N > len(A) or c_start + N > len(A[0]):
        return False
    for i in range(N):                  # loop i as needed
        if A[r_start+i][c_start+i] != ch:   # check for mismatches
            return False                # mismatch found - return False

    return True                         # loop found no mismatches - return True  
def inarow_Nnortheast( ch, r_start, c_start, A, N ):
    '''this should start from r_start and c_start and check for three-in-a-row northeastward of element ch, 
    returning True or False, as appropriate '''
    if r_start - N > len(A) or c_start + N > len(A[0]):
        return False
    for i in range(N):                  # loop i as needed
        if A[r_start-i][c_start+i] != ch:   # check for mismatches
            return False                # mismatch found - return False

    return True                         # loop found no mismatches - return True  



class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [ [' ']*W for row in range(H) ]
        self.gra = [ [0]*W for row in range(H) ]
        data = self.data
    def __repr__(self):
        """ this method returns a string representation
        for an object of type Board
        """
        H = self.height
        W = self.width
        s = ''   # the string to return
        for row in range(0,H):
            s += '|'   
            for col in range(0,W):
                s += self.data[row][col] + '|'
            s += '\n'
        s += (2*W+1) * '-'    # bottom of the board
        s+= '\n'
        for q in range(0, W):
            s += ' ' + str(q % 10)  # and the numbers
        return s       # the board is complete, return it
    def addMove(self, col, ox):
        H = self.height
        W = self.width
        D = self.data
        for f in range(H):
            if D[f][col] != ' ':
                D[f-1][col] = ox
                break
            if f == H-1:
                D[f][col] = ox
                break
    def clear(self):
        W = self.width
        H = self.height
        self.data = [ [' ']*W for row in range(H) ] 
    def setBoard( self, moveString ):
        """ takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'
            
            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000') to
            see them alternate in the left column.

            moveString must be a string of integers
        """
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'
    def allowsMove(self, c):
        '''This method should return True if the calling object (of type Board) 
        does allow a move into column c. It returns False if column c is 
        not a legal column number for the calling object. It also returns 
        False if column c is full. Thus, this method should check to be sure 
        that c is within the range from 0 to the last column and make sure 
        that there is still room left in the column! '''
        D = self.data
        W = self.width
        if c >= W:
            return False
        elif c < 0:
            return False
        elif D[0][c] == ' ':
            return True
        else:
            return False
    def isFull(self):
        H = self.height
        W = self.width
        D = self.data
        for row in range(0,H): 
            for col in range(0,W):
                if D[row][col] == ' ':
                    return False
        return True
    def delMove(self, c):
        H = self.height
        W = self.width
        D = self.data
        for f in range(H):
            if D[f][c] != ' ':
                D[f][c] = ' '
                break
    def winsFor(self, ox):
        W = self.width
        D = self.data
        H = self.height
        check = False
        for r in range(H):
            for c in range(W-3):
                check = inarow_Neast(ox, r, c, D, 4)
                if check == True:
                    return True
        for r in range(H-3):
            for c in range(W):
                check = inarow_Nsouth(ox, r, c, D, 4)
                if check == True:
                    return True
        for r in range(H-3):
            for c in range(W-3):
                check = inarow_Nsoutheast(ox, r, c, D, 4)
                if check == True:
                    return True
        for r in range(3, H):
            for c in range(W-3):
                check = inarow_Nnortheast(ox, r, c, D, 4)
                if check == True:
                    return True
        return False
    def hostGame(self):
        print('Welcome to Connect Four!')
        over = False
        count = 0
        print('\nX will go first')
        print(' ')
        while(over == False):
            print(self)
            if count % 2 == 0:
                users_col = -1
                while self.allowsMove( users_col ) == False:
                    users_col = int(input("X choose a column: "))
                    print(' ')
                self.addMove(users_col, 'X')
                print(self)
                count += 1
            if self.winsFor('O'):
                 print('\nO wins -- Congratulations!')
                 return 
            if self.winsFor('X'):
                print('\nX wins -- Congratulations!')
                return 
            if count % 2 == 1:
                ai = self.aiMove('O')
                print('AI chooses colum: ', ai)
                self.addMove(ai, 'O')
                print(self)
                count += 1
            if self.winsFor('O'):
                 print('\nO wins -- Congratulations!')
                 return 
            if self.winsFor('X'):
                print('\nX wins -- Congratulations!')
                return 
    def colsToWin(self, ox):
        W = self.width
        L = []
        for i in range(W):
            if(self.allowsMove(i)):
                self.addMove(i, ox)
                if (self.winsFor(ox)):
                    L = L + [i]
                self.delMove(i)
        return L
    def aiMove(self, ox):
        W = self.width
        P = []
        if (self.colsToWin(ox) != []):
            L = self.colsToWin(ox)
            return L[0]
        elif (ox == 'O'):
            if (self.colsToWin('X') != []):
                L = self.colsToWin('X')
                return L[0]
        elif (ox == 'X'):
            if (self.colsToWin('O') != []):
                L = self.colsToWin('O')
                return L[0]
        for i in range(W):
            if (self.allowsMove(i)):
                P = P + [i]
        choice = random.randint(0,len(P)-1)
        return P[choice]
    def playGame(self,px,po):
        G = self.gra
        D = self.data
        W = self.width
        H = self.height
        A = []
        B = []
        C = []
        E = []
        xspace = 94
        xspot = 115
        yspace = 110
        yspot = 80
        win = GraphWin('C4', 800, 800)
        win.setBackground(color_rgb(25, 118, 210))
        for i in range(H):
            for g in range(W):
                tempc = Circle(Point(xspot, yspot), 40)
                tempc.setFill(color_rgb(68,138,255))
                tempc.setOutline(color_rgb(68,138,255))
                tempc.draw(win)
                xspot = xspot + xspace
            yspot = yspot + yspace
            xspot = 115
        for h in range(W):
            xspot = 115
            A = A + [((xspace*h) + xspot) + 40]
            B = B + [((xspace*h) + xspot) - 40]
        for w in range(H):
            yspot = 80
            C = C + [((yspace*w) + yspot) + 40]
            E = E + [((yspace*w) + yspot) - 40]
        if px == 'human':
            print('Welcome to Connect Four!')
            over = False
            count = 0
            print('\nX will go first')
            print(' ')
            while(over == False):
                print(self)
                if count % 2 == 0:
                    users_col = -1
                    '''while self.allowsMove( users_col ) == False:
                        users_col = int(input("X choose a column: "))
                        print(' ')'''
                    num = -1
                    numm = -1
                    while self.allowsMove(num) == False:
                        click = win.getMouse()
                        clickX = click.getX()
                        for z in range(len(A)):
                            if clickX in range(B[z],A[z]):
                                num = z
                    self.addMove(num, 'O')
                    tempc = Circle(Point(A[num]-40, C[self.checkRow(num)+1]-40), 40)
                    tempc.setFill('red')
                    tempc.setOutline('red')
                    tempc.draw(win)
                    self.addMove(num, 'X')
                    print(self)
                    count += 1
                if self.winsFor('O'):
                    print('\nO wins -- Congratulations!')
                    time.sleep(5)
                    win.close()
                    return 
                if self.winsFor('X'):
                    print('\nX wins -- Congratulations!')
                    time.sleep(5)
                    win.close()
                    return
                if self.isFull():
                    print('\nTie')
                    winner = Text(Point(200,700), "It's a tie !!!")
                    winner.setSize(36)
                    winner.draw(win)
                    time.sleep(5)
                    win.close()
                    return 
                if count % 2 == 1:
                    ai = po.nextMove(self)
                    print('AI chooses colum: ', ai)
                    self.addMove(ai, 'O')
                    tempc = Circle(Point(A[num]-40, C[self.checkRow(num)+1]-40), 40)
                    tempc.setFill('black')
                    tempc.setOutline('black')
                    tempc.draw(win)
                    count += 1
                if self.winsFor('O'):
                    print('\nO wins -- Congratulations!')
                    time.sleep(5)
                    win.close()
                    return 
                if self.winsFor('X'):
                    print('\nX wins -- Congratulations!')
                    time.sleep(5)
                    win.close()
                    return
                if self.isFull():
                    print('\nTie')
                    winner = Text(Point(200,700), "It's a tie !!!")
                    winner.setSize(36)
                    winner.draw(win)
                    time.sleep(5)
                    win.close()
                    return
        elif po == 'human':
            print('Welcome to Connect Four!')
            over = False
            count = 0
            print('\nX will go first')
            print(' ')
            while(over == False):
                print(self)
                if count % 2 == 1:
                    users_col = -1
                    '''while self.allowsMove( users_col ) == False:
                        users_col = int(input("O choose a column: "))
                        print(' ')'''
                    num = -1
                    numm = -1
                    while self.allowsMove(num) == False:
                        click = win.getMouse()
                        clickX = click.getX()
                        for z in range(len(A)):
                            if clickX <= A[z] and clickX >= B[z]:
                                num = z
                    print(clickX, ' and', num)
                    self.addMove(num, 'O')
                    tempc = Circle(Point(A[num]-40, C[self.checkRow(num)+1]-40), 40)
                    print(A[num]-40, ' and', self.checkRow(num))
                    tempc.setFill('black')
                    tempc.setOutline('black')
                    tempc.draw(win)
                    count += 1
                if self.winsFor('O'):
                    print('\nO wins -- Congratulations!')
                    winner = Text(Point(200,700), 'O wins!!!')
                    winner.setSize(36)
                    winner.draw(win)
                    time.sleep(5)
                    win.close()
                    return 
                if self.winsFor('X'):
                    print('\nX wins -- Congratulations!')
                    winner = Text(Point(200,700), 'X wins!!!')
                    winner.setSize(36)
                    winner.draw(win)
                    time.sleep(5)
                    win.close()
                    return 
                if self.isFull():
                    print('\nTie')
                    winner = Text(Point(200,700), "It's a tie !!!")
                    winner.setSize(36)
                    winner.draw(win)
                    time.sleep(5)
                    win.close()
                    return
                if count % 2 == 0:
                    ai = px.nextMove(self)
                    print('AI chooses colum: ', ai)
                    self.addMove(ai, 'X')
                    tempc = Circle(Point(A[ai]-40, C[self.checkRow(ai)+1]-40), 40)
                    tempc.setFill('red')
                    tempc.setOutline('red')
                    tempc.draw(win)
                    print(self)
                    count += 1
                if self.winsFor('O'):
                    print('\nO wins -- Congratulations!')
                    winner = Text(Point(200,700), 'O wins!!!')
                    winner.setSize(36)
                    winner.draw(win)
                    time.sleep(5)
                    win.close()
                    return 
                if self.winsFor('X'):
                    print('\nX wins -- Congratulations!')
                    winner = Text(Point(200,700), 'X wins!!!')
                    winner.setSize(36)
                    winner.draw(win)
                    time.sleep(5)
                    win.close()
                    return
                if self.isFull():
                    print('\nTie')
                    winner = Text(Point(200,700), "It's a tie !!!")
                    winner.setSize(36)
                    winner.draw(win)
                    time.sleep(5)
                    win.close()
                    return
        else:
            print('Welcome to Connect Four!')
            over = False
            count = 0
            print('\nX will go first')
            print(' ')
            while(over == False):
                print(self)
                if count % 2 == 0:
                    ai = px.nextMove(self)
                    print('AI chooses colum: ', ai)
                    self.addMove(ai, 'X')
                    tempc = Circle(Point(A[ai]-40, C[self.checkRow(ai)+1]-40), 40)
                    tempc.setFill('red')
                    tempc.setOutline('red')
                    tempc.draw(win)
                    print(self)
                    count += 1
                if self.winsFor('O'):
                    print('\nO wins -- Congratulations!')
                    winner = Text(Point(200,700), 'O wins!!!')
                    winner.setSize(36)
                    winner.draw(win)
                    time.sleep(5)
                    win.close()
                    return 
                if self.winsFor('X'):
                    print('\nX wins -- Congratulations!')
                    winner = Text(Point(200,700), 'X wins!!!')
                    winner.setSize(36)
                    winner.draw(win)
                    time.sleep(5)
                    win.close()
                    return
                if self.isFull():
                    print('\nTie')
                    winner = Text(Point(200,700), "It's a tie !!!")
                    winner.setSize(36)
                    winner.draw(win)
                    time.sleep(5)
                    win.close()
                    return 
                if count % 2 == 1:
                    ai = po.nextMove(self)
                    print('AI chooses colum: ', ai)
                    self.addMove(ai, 'O')
                    tempc = Circle(Point(A[ai]-40, C[self.checkRow(ai)+1]-40), 40)
                    tempc.setFill('black')
                    tempc.setOutline('black')
                    tempc.draw(win)
                    print(self)
                    count += 1
                if self.winsFor('O'):
                    print('\nO wins -- Congratulations!')
                    winner = Text(Point(200,700), 'O wins!!!')
                    winner.setSize(36)
                    winner.draw(win)
                    time.sleep(5)
                    win.close()
                    return 
                if self.winsFor('X'):
                    print('\nX wins -- Congratulations!')
                    winner = Text(Point(200,700), 'X wins!!!')
                    winner.setSize(36)
                    winner.draw(win)
                    time.sleep(5)
                    win.close()
                    return
                if self.isFull():
                    print('\nTie')
                    winner = Text(Point(200,700), "It's a tie !!!")
                    winner.setSize(36)
                    winner.draw(win)
                    time.sleep(5)
                    win.close()
                    return
    def drawBoard(self):
        '''
        W = self.width
        H = self.height
        D = self.data
        A = []
        B = []
        C = []
        D = []
        xspace = 94
        xspot = 115
        yspace = 110
        yspot = 80
        win = GraphWin('C4', 800, 800)
        win.setBackground(color_rgb(25, 118, 210))
        for i in range(H):
            for g in range(W):
                tempc = Circle(Point(xspot, yspot), 40)
                tempc.setFill(color_rgb(68,138,255))
                tempc.setOutline(color_rgb(68,138,255))
                tempc.draw(win)
                xspot = xspot + xspace
            yspot = yspot + yspace
            xspot = 115
        for h in range(W):
            xspot = 115
            A = A + [(xspot*h) + xspace) + 40]
            B = B + [(xspot*h) + xspace) - 40]
        for w in range(H):
            xspot = 115
            C = C + [(yspot*w) + yspace) + 40]
            D = D + [(yspot*w) + yspace) - 40]
        

        Now lets focus on getting the click

        
        click = win.getMouse()
        clickY = click.getY()
        for z in range(A)
            if clickY in range(B[z],A[z])
                num = z
                break'''
        return hi
    def findP(y,x):
            xspace = 94
            xspot = 115
            yspace = 110
            yspot = 80
            realy = (yspace*y) + yspot
            realx = (xspace*x) + xspot
            '''if D[i][g] == 'X':
                tempc.setFill('red')
                tempc.setOutline('red')
            elif D[i][g] == 'O':
                tempc.setFill('black')
                tempc.setOutline('black')
            else:'''
    def checkRow(self, c):
        D = self.data
        W = self.width
        H = self.height
        for i in range(H):
            if D[i][c] != ' ':
                return i-1
    def final(self):
        '''This is the function you want to call the to play the game. By default the ai is RED and will move FIRST. You the player is BLACK and will move
        SECOND. This can be changed by simply switching the 0 and 1 in the count if statements. Any board size will work but the window does not resize therefore
        a board of 7,7 or less is recommended.'''
        G = self.gra
        D = self.data
        W = self.width
        H = self.height
        A = []
        B = []
        C = []
        E = []
        #Intro Screen
        win = GraphWin('C4', 800, 800)
        menu = Image(Point(400,400), 'hva.gif')     #Either human vs ai or ai vs ai
        menu.draw(win)
        click = win.getMouse()
        clickX = click.getX()
        hva = -1
        if clickX <= 400:
            hva = 0
        elif clickX > 400:
            hva = 1
        hcol = -1
        menu.undraw()
        if hva == 0:                               #If human choose red or black (x is red)
            menu = Image(Point(400,400), 'xo.gif')
            menu.draw(win)
            click = win.getMouse()
            clickX = click.getX()
            if clickX <= 400:
                hcol = 'O'
            elif clickX > 400:
                hcol = 'X'
            menu.undraw()
        if hcol == 'O':                            #Open ad for getting to go first
            menu = Image(Point(400,400), 'ad.gif')
            menu.draw(win)
            click = win.getMouse()
            clickX = click.getX()
            if clickX <= 400:
                webbrowser.open('https://youtu.be/izzcxSL3SMk', new=2)
                time.sleep(5)
            elif clickX > 400:
                hcol = 'X'
            menu.undraw()
        if hva == 0:
            menu = Image(Point(400,400), 'check.gif')
        elif hva == 1:
            menu = Image(Point(400,400), 'checkb.gif')
        menu.draw(win)
        click = win.getMouse()
        clickX = click.getX()
        mode = 0
        mode2 = 0
        if clickX <= 200:                         #Ply of AI person
            mode = 1
        elif clickX > 200 and clickX <= 400:
            mode = 2
        elif clickX > 400 and clickX <= 600:
            mode = 3
        else:
            mode = 4
        print(mode)
        if hva == 0:                              # If it is h vs Ai
            if hcol == 'O':
                px = Player('X', 'RANDOM', mode)
                po = 'human'
            elif hcol == 'X':
                px = Player('O', 'RANDOM', mode)
                po = 'human'
        if hva == 1:                              # Ai vs Ai
            menu.undraw()
            menu = Image(Point(400,400), 'checkr.gif')
            menu.draw(win)
            click = win.getMouse()
            clickX = click.getX()
            if clickX <= 200:
                mode2 = 1
            elif clickX > 200 and clickX <= 400:
                mode2 = 2
            elif clickX > 400 and clickX <= 600:
                mode2 = 3
            else:
                mode2 = 4
            px = Player('X', 'RANDOM', mode2)
            po = Player('O', 'RANDOM', mode)
        menu.undraw()
        #Actual game
        xspace = 94
        xspot = 115
        yspace = 110
        yspot = 80
        win.setBackground(color_rgb(25, 118, 210))
        for i in range(H):
            for g in range(W):
                tempc = Circle(Point(xspot, yspot), 40)
                tempc.setFill(color_rgb(68,138,255))
                tempc.setOutline(color_rgb(68,138,255))
                tempc.draw(win)
                xspot = xspot + xspace
            yspot = yspot + yspace
            xspot = 115
        for h in range(W):
            xspot = 115
            A = A + [((xspace*h) + xspot) + 40]
            B = B + [((xspace*h) + xspot) - 40]
        for w in range(H):
            yspot = 80
            C = C + [((yspace*w) + yspot) + 40]
        for w in range(H*2):
            yspot = 80
            E = E + [(((yspace/2)*w) + yspot) + 40]
        print('Welcome to Connect Four!')
        over = False
        count = 0
        print('\nX will go first')
        print(' ')
        while(over == False):
            print(self)
            if count % 2 == 0:      #Makes black go first
                if hva == 0 and hcol == 'O':
                    num = -1
                    numm = -1
                    while self.allowsMove(num) == False:
                        click = win.getMouse()
                        clickX = click.getX()
                        for z in range(len(A)):
                            if clickX <= A[z] and clickX >= B[z]:
                                num = z
                    print(clickX, ' and', num)
                    self.addMove(num, 'O')
                    for i in range((self.checkRow(num)+1)*2):
                        tempc = Circle(Point(A[num]-40, E[i]-40), 40)
                        tempc.setFill('black')
                        tempc.setOutline('black')
                        tempc.draw(win)
                        time.sleep(.1)
                        tempc.undraw()
                    tempc = Circle(Point(A[num]-40, C[self.checkRow(num)+1]-40), 40)
                    print(A[num]-40, ' and', self.checkRow(num))
                    tempc.setFill('black')
                    tempc.setOutline('black')
                    tempc.draw(win)
                    count += 1
                elif hva == 0 and hcol == 'X':  
                    ai = px.nextMove(self)
                    print('AI chooses colum: ', ai)
                    self.addMove(ai, 'O')
                    for i in range((self.checkRow(ai)+1)*2):
                        tempc = Circle(Point(A[ai]-40, E[i]-40), 40)
                        tempc.setFill('black')
                        tempc.setOutline('black')
                        tempc.draw(win)
                        time.sleep(.1)
                        tempc.undraw()
                    tempc = Circle(Point(A[ai]-40, C[self.checkRow(ai)+1]-40), 40)
                    tempc.setFill('black')
                    tempc.setOutline('black')
                    tempc.draw(win)
                    print(self)
                    count += 1
                elif hva == 1:  
                    ai = po.nextMove(self)
                    print('AI chooses colum: ', ai)
                    self.addMove(ai, 'O')
                    for i in range((self.checkRow(ai)+1)*2):
                        tempc = Circle(Point(A[ai]-40, E[i]-40), 40)
                        tempc.setFill('black')
                        tempc.setOutline('black')
                        tempc.draw(win)
                        time.sleep(.1)
                        tempc.undraw()
                    tempc = Circle(Point(A[ai]-40, C[self.checkRow(ai)+1]-40), 40)
                    tempc.setFill('black')
                    tempc.setOutline('black')
                    tempc.draw(win)
                    print(self)
                    count += 1
            if self.winsFor('O'):
                if hva == 1:
                    time.sleep(2)
                    print('\nO wins -- Congratulations!')
                    menu = Image(Point(400,400), 'bw.gif')
                    menu.draw(win)
                    time.sleep(5)
                    win.close()
                    return
                elif hcol == 'O':
                    time.sleep(2)
                    print('\nO wins -- Congratulations!')
                    menu = Image(Point(400,400), 'won.gif')
                    menu.draw(win)
                    time.sleep(5)
                    webbrowser.open('https://youtu.be/PxGCs_jxKfc?t=29s', new=2)
                    time.sleep(5)
                    win.close()
                    return
                elif hcol == 'X':
                    time.sleep(2)
                    print('\nO wins -- Congratulations!')
                    menu = Image(Point(400,400), 'los.gif')
                    menu.draw(win)
                    time.sleep(5)
                    webbrowser.open("https://youtu.be/fqmlffA9U9s?t=10s", new=2)
                    win.close()
                    return
            if self.winsFor('X'):
                if hva == 1:
                    time.sleep(2)
                    print('\nX wins -- Congratulations!')
                    menu = Image(Point(400,400), 'rw.gif')
                    menu.draw(win)
                    time.sleep(5)
                    win.close()
                    return
                elif hcol == 'X':
                    time.sleep(2)
                    print('\nX wins -- Congratulations!')
                    menu = Image(Point(400,400), 'won.gif')
                    menu.draw(win)
                    time.sleep(5)
                    webbrowser.open('https://youtu.be/PxGCs_jxKfc?t=29s', new=2)
                    time.sleep(5)
                    win.close()
                    return
                elif hcol == 'O':
                    time.sleep(2)
                    print('\nX wins -- Congratulations!')
                    menu = Image(Point(400,400), 'los.gif')
                    menu.draw(win)
                    time.sleep(5)
                    webbrowser.open("https://youtu.be/fqmlffA9U9s?t=10s", new=2)
                    win.close()
                    return 
            if self.isFull():
                time.sleep(2)
                print('\nTie')
                menu = Image(Point(400,400), 'ti.gif')
                menu.draw(win)
                time.sleep(5)
                webbrowser.open("https://youtu.be/HCXEV-O0kQk?t=2m35s",new=2)
                time.sleep(5)
                win.close()
                return
            if count % 2 == 1:              # makes red go secong
                if hva == 0 and hcol  == 'O':    
                    ai = px.nextMove(self)
                    print('AI chooses colum: ', ai)
                    self.addMove(ai, 'X')
                    for i in range((self.checkRow(ai)+1)*2):
                        tempc = Circle(Point(A[ai]-40, E[i]-40), 40)
                        tempc.setFill('red')
                        tempc.setOutline('red')
                        tempc.draw(win)
                        time.sleep(.1)
                        tempc.undraw()
                    tempc = Circle(Point(A[ai]-40, C[self.checkRow(ai)+1]-40), 40)
                    tempc.setFill('red')
                    tempc.setOutline('red')
                    tempc.draw(win)
                    print(self)
                    count += 1
                elif hva == 0 and hcol == 'X':
                    num = -1
                    numm = -1
                    while self.allowsMove(num) == False:
                        click = win.getMouse()
                        clickX = click.getX()
                        for z in range(len(A)):
                            if clickX <= A[z] and clickX >= B[z]:
                                num = z
                    print(clickX, ' and', num)
                    self.addMove(num, 'X')
                    for i in range((self.checkRow(num)+1)*2):
                        tempc = Circle(Point(A[num]-40, E[i]-40), 40)
                        tempc.setFill('red')
                        tempc.setOutline('red')
                        tempc.draw(win)
                        time.sleep(.1)
                        tempc.undraw()
                    tempc = Circle(Point(A[num]-40, C[self.checkRow(num)+1]-40), 40)
                    print(A[num]-40, ' and', self.checkRow(num))
                    tempc.setFill('red')
                    tempc.setOutline('red')
                    tempc.draw(win)
                    count += 1
                elif hva == 1:
                    ai = px.nextMove(self)
                    print('AI chooses colum: ', ai)
                    self.addMove(ai, 'X')
                    for i in range((self.checkRow(ai)+1)*2):
                        tempc = Circle(Point(A[ai]-40, E[i]-40), 40)
                        tempc.setFill('red')
                        tempc.setOutline('red')
                        tempc.draw(win)
                        time.sleep(.1)
                        tempc.undraw()
                    tempc = Circle(Point(A[ai]-40, C[self.checkRow(ai)+1]-40), 40)
                    tempc.setFill('red')
                    tempc.setOutline('red')
                    tempc.draw(win)
                    print(self)
                    count += 1
            if self.winsFor('O'):
                if hva == 1:
                    time.sleep(2)
                    print('\nO wins -- Congratulations!')
                    menu = Image(Point(400,400), 'bw.gif')
                    menu.draw(win)
                    time.sleep(5)
                    win.close()
                    return
                elif hcol == 'O':
                    time.sleep(2)
                    print('\nO wins -- Congratulations!')
                    menu = Image(Point(400,400), 'won.gif')
                    menu.draw(win)
                    time.sleep(5)
                    webbrowser.open('https://youtu.be/PxGCs_jxKfc?t=29s', new=2)
                    time.sleep(5)
                    win.close()
                    return
                elif hcol == 'X':
                    time.sleep(2)
                    print('\nO wins -- Congratulations!')
                    menu = Image(Point(400,400), 'los.gif')
                    menu.draw(win)
                    time.sleep(5)
                    webbrowser.open("https://youtu.be/fqmlffA9U9s?t=10s", new=2)
                    win.close()
                    return
            if self.winsFor('X'):
                if hva == 1:
                    time.sleep(2)
                    print('\nO wins -- Congratulations!')
                    menu = Image(Point(400,400), 'rw.gif')
                    menu.draw(win)
                    time.sleep(5)
                    win.close()
                    return
                elif hcol == 'X':
                    time.sleep(2)
                    print('\nO wins -- Congratulations!')
                    menu = Image(Point(400,400), 'won.gif')
                    menu.draw(win)
                    time.sleep(5)
                    webbrowser.open('https://youtu.be/PxGCs_jxKfc?t=29s', new=2)
                    time.sleep(5)
                    win.close()
                    return
                elif hcol == 'O':
                    time.sleep(2)
                    print('\nX wins -- Congratulations!')
                    menu = Image(Point(400,400), 'los.gif')
                    menu.draw(win)
                    time.sleep(5)
                    webbrowser.open("https://youtu.be/fqmlffA9U9s?t=10s", new=2)
                    win.close()
                    return
            if self.isFull():
                time.sleep(2)
                print('\nTie')
                menu = Image(Point(400,400), 'ti.gif')
                menu.draw(win)
                time.sleep(5)
                webbrowser.open("https://youtu.be/HCXEV-O0kQk?t=2m35s",new=2)
                time.sleep(5)
                win.close()
                return

            
class Player:
    """ an AI player for Connect Four """

    def __init__( self, ox, tbt, ply ):
        """ the constructor """
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__( self ):
        """ creates an appropriate string """
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s
    def oppCh(self):
        ox = self.ox
        if ox == 'O':
            return 'X'
        else:
            return 'O'
    def scoreBoard(self, b):
        ox = self.ox
        t = 50.0
        if (b.winsFor(ox)):
            t = 100.0
        elif (b.winsFor(self.oppCh())):
            t = 0.0
        return t
    def tiebreakMove(self, scores):
        tbt = self.tbt
        T = []
        m = max(scores)
        for i in range(len(scores)):
            if scores[i] == m:
                T = T + [i]
        if tbt == 'LEFT':
            return T[0]
        elif tbt == 'RIGHT':
            return T[-1]
        else:
            return random.choice(T)
    def scoresFor(self, b):
        ox = self.ox
        ply = self.ply
        tbt = self.tbt
        scores = [0.0]*b.width
        for t in range(b.width):
            if b.allowsMove(t):
                scores[t] = self.scoreBoard(b)
            else:
                scores[t] = -1.0
        if ply == 0:
            return scores
        else:
            for i in range(b.width):
                if (b.allowsMove(i)):
                    b.addMove(i, ox)
                    P = Player(self.oppCh(), tbt, ply-1)
                    scores2 = P.scoresFor(b)
                    r = max(scores2)
                    r = 100 - r
                    if (b.winsFor(ox)):
                        r = 100.0
                    elif (b.winsFor(self.oppCh())):
                        r = 0.0
                    b.delMove(i)
                    scores[i] = r
                else:
                    scores[i] = -1
            return scores
    def nextMove(self, b):
        scores = self.scoresFor(b)
        t = self.tiebreakMove(scores)
        return t
       


        

