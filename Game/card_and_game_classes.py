import time
import os


class Card:
    """
    A class representing a single card.

    Attributes:
        Suit: String
            The suit of the card

        Value: Int
            The Value of the card
    """

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"({self.value},{self.suit})"

    def __str__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    """
    A class representing a Deck of cards

    Attributes:
        deck : List
            Contains the current deck of card objects, one is generated automatically upon object creation
        Methods:
            Shuffle:
                shuffles the cards in the curent deck list
            New_Deck:
                Clears the deck of any cards and replaces it with a new complete deck
            Add_Deck:
                Adds a new complete deck ontop of and cards currently in the deck


    """

    from random import shuffle as _shuffle
    suits = ("Clubs", "Spades", "Hearts", "Diamonds")
    values = [str(i) for i in range(1, 11)] + ["J", "Q", "K", "A"]

    def __init__(self):
        """
        Generates a complete deck for the object automatically

        """

        self.deck = []
        for suit in self.suits:
            for value in self.values:
                self.deck.append(Card(suit, value))

    def __iter__(self):
        """
        Defines self.Deck as the iterable
        :return:
        """
        return self.deck.__iter__()

    def __len__(self):
        """
        Returns the length of self.deck when calling the length of a Deck object
        :return:
        """
        return len(self.deck)

    def __getitem__(self, item):
        return self.deck[item]

    def shuffle(self):
        """
        Shuffles the Deck in its current state with
        :return:
        """
        self._shuffle(self.deck)

    def new_deck(self):
        """
        Empties the deck , then generates a new deck
        """

        self.deck = []

        self.add_deck(self)

    def add_deck(self):

        """
        Adds a new deck
        :return:
        """
        for suit in self.suits:
            for value in self.values:
                self.deck.append(Card(suit, value))


class Player:
    """
    A class describing the base values for a player
        Attributes:
            self.name = The Players name
            Self.bank = The Players Bank
            self.hand = The players hand of cards

        Methods:
            change_name: lets a player change their name
            update_bank: allows a players bank to be updated
            clear_bank: clears the bank
            clear_hand: clears the hand
    """

    def __init__(self, name, bank):
        """
        Creates a Player Object with methods associated with the operations of a single player
        :param name: The name of the player
        :param bank: The current bank of the player

        """
        self.name = name
        self.bank = bank
        self.hand = []


    def change_name(self, new_name):
        """
        Allows the changing of the users name
        :param new_name: the new name
        :return:
        """
        self.name = str(new_name)

    def update_bank(self, change):
        """
        Updates the bank
        :param change: the int change to the bank
        :return:
        """
        self.bank += change

    def clear_bank(self):
        """
        Clears the bank to 0
        :return:
        """
        self.bank = 0

    def clear_hand(self):
        """
        Clears the players hand to an empty list
        :return:
        """
        self.hand = []


class PlayerManager:
    """
    Creates a player manager, handles operations around managing player objects, such as adding, removing, and changing
    all objects at the same time

        Attributes:
            Creates a dictionary for players with a unique ID assigned when they are added
    """

    def __init__(self):
        """
        Creates the empty player manager
        """
        self.player_manager = {}

    def add_player(self, name, bank):
        """

            Creates a player dictionary with a unique int key one larger than the current max value, ensures that there
            is no overwriting and player order is maintained(with the latest player to be added last in the queue

            name = the players name
            bank = the current game bank
            hand =
        """

        if self.player_manager.keys() == None:
            self.player_manager[0] = Player(name, bank)
        else:
            self.player_manager[max(self.player_manager.keys()) + 1] = Player(name, bank)
    def remove_player(self, id):
        # As this method is not meant to be called the id should exist, and an error can be suppressed here
        self.player_manager.pop("Key", None)

    '''
    def print_players(self):
        """
        returns a list of player names as strings
        :return:
        """
        # Prints the name of the players, can have duplicate values
        return [self.player_manager[player].name for player in self.player_manager]
    '''


class GameLoop:
    import sys

    def __init__(self):
        # value of the pot
        self.pot = 0
        # a dictionary denoting the players
        self.players = {}
        # the deck
        self.deck = None
        # the blind player indicator
        self.button = 0
        # the cards faceup on the table
        self.table = []
        # the blind amount
        self.blind_amount = 0

    def set_blind_amount(self, amount: int):
        """Sets a new blind amount"""
        try:
            self.blind_amount = int(amount)
        except TypeError:
            print(f"{amount} is not a valid amount of money, please enter a new value")
            self.set_blind_amount(int(input()))

    def _index_adjuster(self, value):
        """
        loops player tracker for a dynamic list
        :param value:
        :return:
        """
        return value % len(self.players.keys())

    def _set_button(self):

        """
        updates the player who is carrying the button at the end of each round
        :return:
        """
        self.button = self._index_adjuster(self.button + 1)

    def _player_order_tracker(self, index):
        """
        This returns a player based on their keys index (the last player to join will have the highest value id, orders
        by id value
        """
        return sorted(self.players.keys())[index]

    def pre_flop(self):
        # clears anything remaining from the previous round
        self.table = []
        self.pot = 0
        # run the blind
        self._blinds()
        for _ in range(2):
            for player in self.players.keys(self):
                self._deal(player)

        for _ in range(3):
            self.table.append()

    def _blinds(self):
        self.players[self._player_order_tracker(self.button)].bank -= self.blind_amount
        self._set_button()
        self.players[self._player_order_tracker(self.button)].bank -= (self.blind_amount // 2)

        self.bank += int(self.blind_amount * 1.5)

    def quit(self):
        """
        quits you out the programme
        :return:
        """
        self.sys.exit()

    def run(self):
        # used to call the setup method for the games setup
        for i in range(5):
            print("game is running")
            time.sleep(1)
        os.system("cls")

    def _setup(self):
        self.deck = Deck()

    def _deal(self, player):
        self.players[player].hand.append(self.deck.pop(-1))

    def _raise(self):
        pass

    def _pass(self):
        pass

    def add_player(self, num_players=1):
        try:
            for player in range(len(num_players)):
                self.players[(max(self.players.keys())) + 1] = Player()
        except ValueError:
            self.players[0] = Player()

            self.add_player(self, num_players=(num_players - 1))


class CardGameClass:
    def __init__(self):
        pass


def value_unpacker(func, hand, table):
    converter_dictionary = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14
    }
    #This should return 7 values
    concat_hand = [converter_dictionary[card.suit] for card in hand] + [converter_dictionary[_card.suit] for _card in table]
    print(concat_hand)


def Scorechecker(values, suit_values):


    #4 of a kind
    for i in values:
        if values.count(i) == 4:
            return 130 + i

    for i in values:
        if values.count(i) == 3:
            return

    pairs = []


    for i in values:
        if values.count(i) == 2:
            return 13 + i
    
    else:
        return max(values)


'''    
def print_with_id(self, ID=None):
        try:
            return self.player_manager[ID].self
        except KeyError:
            print("Please enter an ID")
            
class _Player_Connector(Player):
    """
    A class for handling a player connecting to a session, taking in their details and using lookups to fill
    in key details
    """
    def __init__(self, Player_Connection_Packet):
        super().__init__()
        packet = Player_Connection_Packet
'''

'''
def printer(iterable: [Deck, list]):
    """
    Generic printer
    :param card:
    :return:
    """

    for card in iterable:
        print(card)
        
        self.ranking = {"2": 2,
                        "3": 3,
                        "4": 4,
                        "5": 5,
                        "6": 6,
                        "7": 7,
                        "8": 8,
                        "9": 9,
                        "10": 10,
                        "J": 11,
                        "Q": 12,
                        "K": 13,
                        "A": 14
                        }
'''
