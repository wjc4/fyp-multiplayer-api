#!/usr/bin/env python3
# ========================== IMPORTS ======================
import time

# ==================== CLASS SECTION ===============================

class GameRound:
    def __init__(self, verbose=False, name="Game Round"):
        """ init method
        """
        self.name = name
        self.player = {}
        self.verbose = verbose

        if self.verbose:
            print(" Round initialized named: {} ".format(self.name))


    def add_player(self, player_name, player_data):
        self.player[player_name] = player_data

    def get_player(self, player_name):
        if player_name in self.player:
            return self.player[player_name]

# class Player:
#     def __init__(self, name, verbose=False):
#         """ init method
#         """
#         self.name = name
#         self.checkpoint = 1
#         self.lap = 1
#         self.buffs = []
#         self.verbose = verbose

#         if self.verbose:
#             print(" Player initialized named: {} ".format(self.name))


#     def add_player(self, player_name, player_data):
#         pass
