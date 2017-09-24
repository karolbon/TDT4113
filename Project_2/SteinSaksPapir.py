import random
import matplotlib.pyplot


#------------------------PLAYER------------------------------

class Player:
    _actions = {0:"stein", 1:"saks", 2:"papir"}
    playersHistory = {}

    def __init__(self, name):           # Initialisering
        self.name = name
        Player.playersHistory[self] = []

    def pick_action(self, action):          # Velge trekk
        None


    def recieve_result(self, motstander, trekk):           # motta resultatet
        Player.playersHistory[motstander].append(trekk)


    def __str__(self):
        return self.name


#-------------RANDOM_PLAYER---------------------------------

class Random_Player(Player):

    def __init__(self, name):
        super().__init__(name)

    def pick_action(self, otherPlayer):
        return Action(random.randint(0,2))



#-----------------SEQUENTIAL_PLAYER--------------------------

class Sequential_Player(Player):
    def __init__(self, name):
        self.counter = 0
        super().__init__(name)

    def pick_action(self, otherPlayer):
        self.counter = (self.counter+1)%3
        return Action(self.counter)



#------------------MOST_USUAL_PLAYER--------------------------
class MostUsual_Player(Player):
    def __init__(self, name):
        super().__init__(name)


    def pick_action(self, motstander):
        history = [0,0,0]

        if (len(Player.playersHistory[motstander])>0):
            for trekk in Player.playersHistory[motstander]:
                history[trekk.getAction()] += 1

        if history != [0,0,0]:
            return Action(chooseOppositAction(history.index(max(history))))

        return Action(random.randint(0,2))


def chooseOppositAction(number):                # Hvis det blir spilt x, spill y
    beats = {0:2, 1:0, 2:1}
    return beats[number]


#---------------------HISTORIAN_PLAYER--------------------------------

class Historian_Player(Player):

    def __init__(self, name):
        super().__init__(name)
        self.remember = 2

    def pick_action(self, otherPlayer):
        history = Player.playersHistory[otherPlayer]

        subsequence = history[-self.remember:]

        next = [0,0,0]

        for i in range(len(history)-self.remember):
            if history[i:i+self.remember] == subsequence:
               next[history[i + self.remember].getAction()] += 1

        if next != [0,0,0]:
            return Action(chooseOppositAction(next.index(max(next))))

        return Action(random.randint(0,2))




#---------------------- ACTION ---------------------------------------------

class Action:

    def __init__(self, action):             # Initialisere
        self.action = action

    def __eq__(self, other):                    # Sjekke om de er like
        return self.action == other.action

    def __gt__(self, other):                    # Hva er større enn/slår hva
        a = {0: 2, 1: 0, 2: 1}
        return a[self.action] != other.action

    def __str__(self):                      # Aksjon som streng
        ordliste = ["Stein", "Saks", "Papir"]
        return ordliste[self.action]

    def getAction(self):            # Hente ut hva som spilles
        return self.action

#------------------------------------------------------------------------------


class SimpleGame:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.points = [0,0]
        self.winner = ""


    def doGame(self):
        self.action1 = self.player1.pick_action(self.player2)
        self.action2 = self.player2.pick_action(self.player1)

        if self.action1 == self.action2:
            self.points = [0.5, 0.5]
            self.winner = "Uavgjort"

        elif self.action1 > self.action2:
            self.points = [1,0]
            self.winner = str(self.player1) + " is the winner"

        elif self.action1 < self.action2:
            self.points = [0,1]
            self.winner = str(self.player2) + " is the winner"

        self.player1.recieve_result(self.player2, self.action2)
        self.player2.recieve_result(self.player1, self.action1)


    def __str__(self):
        return str(self.player1) + ": " + str(self.action1) + ". \t \t \t" + str(self.player2)+": "+str(self.action2)





class ManyGames:

    def __init__(self, player1, player2, numbGames):
        self.player1 = player1
        self.player2 = player2
        self.numbGames = numbGames
        self.result = [0,0]
        self.winningPercent = [0,0]


    def simpleGame(self):
        game = SimpleGame(self.player1, self.player2)
        game.doGame()
        print(game)
        return game.points

    def tournament(self):

        x_axis = []
        y_axis = []

        finished = 0

        for x in range(self.numbGames):
            finished += 1
            points = self.simpleGame()
            self.result[0] += points[0]
            self.result[1] += points[1]
            self.winningPercent[0] = self.result[0]/finished
            self.winningPercent[1] = self.result[1]/finished

            x_axis.append(finished)
            y_axis.append(self.winningPercent[0])

        print("Tournament done:\n" + str(self.player1)+": "+str(self.result[0])+ " points" +
                  "\n" + str(self.player2)+ ": " + str(self.result[1]) + " points.")

        matplotlib.pyplot.plot(x_axis, y_axis)
        matplotlib.pyplot.axis([0,finished,0,1])
        matplotlib.pyplot.grid(True)
        matplotlib.pyplot.axhline(y = 0.5, linewidth=0.5, color="m")
        matplotlib.pyplot.xlabel("Games")
        matplotlib.pyplot.ylabel("Winning percent for " + str(self.player1))
        matplotlib.pyplot.grid(True)
        matplotlib.pyplot.show()

def main():
    p1 = Random_Player("Tilfeldig")
    p2 = Sequential_Player("Sekvensiell")
    p3 = Historian_Player("Historiker")
    p4 = MostUsual_Player("Mest vanlig")

    game = ManyGames(p4, p3, 100)
    game.tournament()

main()















