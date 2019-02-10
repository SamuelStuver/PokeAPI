# Attempt to guess the pokemon type based on known strengths and weaknesses

import numpy as np
import pandas as pd
#from enum import *
from collections import Counter

typeTable = {
    'normal': {

        'offensive': {
            2.0: set(),
            0.5: {'rock', 'steel'},
            0.0: {'ghost'}
        },
        'defensive': {
            2.0: {'fighting'},
            0.5: set(),
            0.0: {'ghost'}
        }

    },
    'fighting': {

        'offensive': {
            2.0: {'dark', 'ice', 'normal', 'rock', 'steel'},
            0.5: {'bug', 'fairy', 'flying', 'poison', 'psychic'},
            0.0: {'ghost'}
        },
        'defensive': {
            2.0: {'fairy', 'flying', 'psychic'},
            0.5: {'bug', 'dark', 'rock'},
            0.0: set()
        }

    },
    'flying': {

        'offensive': {
            2.0: {'bug', 'fighting', 'grass'},
            0.5: {'electric', 'rock', 'steel'},
            0.0: set()
        },
        'defensive': {
            2.0: {'electric', 'ice', 'rock'},
            0.5: {'bug', 'fighting', 'grass'},
            0.0: {'ground'}
        }

    },
    'poison': {

        'offensive': {
            2.0: {'grass', 'fairy'},
            0.5: {'poison', 'ground', 'rock', 'ghost'},
            0.0: {'steel'}
        },
        'defensive': {
            2.0: {'ground', 'psychic'},
            0.5: {'fighting', 'poison', 'bug', 'grass', 'fairy'},
            0.0: set()
        }

    },
    'ground': {

        'offensive': {
            2.0: {'electric', 'fire', 'poison', 'rock', 'steel'},
            0.5: {'bug', 'grass'},
            0.0: {'flying'}
        },
        'defensive': {
            2.0: {'grass', 'ice', 'water'},
            0.5: {'poison', 'rock'},
            0.0: {'electric'}
        }

    },
    'rock': {

        'offensive': {
            2.0: {'bug', 'fire', 'flying', 'ice'},
            0.5: {'fighting', 'ground'},
            0.0: set()
        },
        'defensive': {
            2.0: {'fighting', 'grass', 'ground', 'steel', 'water'},
            0.5: {'fire', 'flying', 'normal', 'poison'},
            0.0: set()
        }

    },
    'bug': {

        'offensive': {
            2.0: {'dark', 'grass', 'psychic'},
            0.5: {'fighting', 'fire', 'ghost', 'poison', 'steel'},
            0.0: set()
        },
        'defensive': {
            2.0: {'fire', 'flying', 'rock'},
            0.5: {'fighting', 'grass', 'ground'},
            0.0: set()
        }

    },
    'ghost': {

        'offensive': {
            2.0: {'ghost', 'psychic'},
            0.5: {'dark'},
            0.0: {'normal'}
        },
        'defensive': {
            2.0: {'dark', 'ghost'},
            0.5: {'bug', 'poison'},
            0.0: {'normal', 'fighting'}
        }

    },
    'steel': {

        'offensive': {
            2.0: {'fairy', 'ice', 'rock'},
            0.5: {'electric', 'fire', 'steel', 'water'},
            0.0: set()
        },
        'defensive': {
            2.0: {'fight', 'fire', 'ground'},
            0.5: {'bug', 'dragon', 'fairy', 'flying', 'grass', 'ice', 'normal', 'psychic', 'rock', 'steel'},
            0.0: {'poison'}
        }

    },
    'fire': {

        'offensive': {
            2.0: {'bug', 'grass', 'ice', 'steel'},
            0.5: {'dragon', 'fire', 'rock', 'water'},
            0.0: set()
        },
        'defensive': {
            2.0: {'ground', 'rock', 'water'},
            0.5: {'bug', 'fairy', 'fire', 'grass', 'ice', 'steel'},
            0.0: set()
        }

    },
    'water': {

        'offensive': {
            2.0: {'fire', 'ground', 'rock'},
            0.5: {'dragon', 'grass', 'water'},
            0.0: set()
        },
        'defensive': {
            2.0: {'electric', 'grass'},
            0.5: {'fire', 'ice', 'steel', 'water'},
            0.0: set()
        }

    },
    'grass': {

        'offensive': {
            2.0: {'ground', 'rock', 'water'},
            0.5: {'bug', 'dragon', 'fire', 'flying', 'grass', 'poison', 'steel'},
            0.0: set()
        },
        'defensive': {
            2.0: {'bug', 'fire', 'flying', 'ice', 'poison'},
            0.5: {'electric', 'grass', 'ground', 'water'},
            0.0: set()
        }

    },
    'electric': {

        'offensive': {
            2.0: {'flying', 'water'},
            0.5: {'dragon', 'electric', 'grass'},
            0.0: {'ground'}
        },
        'defensive': {
            2.0: {'ground'},
            0.5: {'electric', 'flying', 'steel'},
            0.0: set()
        }

    },
    'psychic': {

        'offensive': {
            2.0: {'fighting', 'poison'},
            0.5: {'psychic', 'steel'},
            0.0: {'dark'}
        },
        'defensive': {
            2.0: {'bug', 'dark', 'ghost'},
            0.5: {'fighting', 'psychic'},
            0.0: set()
        }

    },
    'ice': {

        'offensive': {
            2.0: {'dragon', 'flying', 'grass', 'ground'},
            0.5: {'fire', 'ice', 'steel', 'water'},
            0.0: set()
        },
        'defensive': {
            2.0: {'fighting', 'fire', 'rock', 'steel'},
            0.5: {'ice'},
            0.0: set()
        }

    },
    'dragon': {

        'offensive': {
            2.0: {'dragon'},
            0.5: {'steel'},
            0.0: {'fairy'}
        },
        'defensive': {
            2.0: {'dragon', 'fairy', 'ice'},
            0.5: {'electric', 'fire', 'grass', 'water'},
            0.0: set()
        }

    },
    'dark': {

        'offensive': {
            2.0: {'ghost', 'psychic'},
            0.5: {'dark', 'fairy', 'fighting'},
            0.0: set()
        },
        'defensive': {
            2.0: {'bug', 'fairy', 'fighting'},
            0.5: {'dark', 'ghost'},
            0.0: {'psychic'}
        }

    },
    'fairy': {

        'offensive': {
            2.0: {'dark', 'dragon', 'fighting'},
            0.5: {'fire', 'poison', 'steel'},
            0.0: set()
        },
        'defensive': {
            2.0: {'poison', 'steel'},
            0.5: {'bug', 'dark', 'fighting'},
            0.0: {'dragon'}
        }

    },

}

compareStringTable = {
    2.0: " is Super Effective against ",
    0.5: " is Not Very Effective against ",
    0.0: " has No Effect against ",
    1.0: " is Neutral against "
}


class Type:
    def __init__(self, typeName):
        allTypes = typeTable
        self.name = typeName
        self.offensive = allTypes[typeName]['offensive']
        self.defensive = allTypes[typeName]['defensive']

    def vs(self, opponentTypeName, verbose=False):

        opponentType = Type(opponentTypeName)

        # see if super effective against opponent
        offReturn = 1.0
        if opponentTypeName in self.offensive[2.0]:
            offReturn = 2.0
        elif opponentTypeName in self.offensive[0.5]:
            offReturn = 0.5
        elif opponentTypeName in self.offensive[0.0]:
            offReturn = 0.0

        # see if opponent is super effective against this
        defReturn = 1.0
        if opponentTypeName in self.defensive[2.0]:
            defReturn = 2.0
        elif opponentTypeName in self.defensive[0.5]:
            defReturn = 0.5
        elif opponentTypeName in self.defensive[0.0]:
            defReturn = 0.0

        if verbose:
            print(self.name + compareStringTable[offReturn] + opponentTypeName)
            print(opponentTypeName + compareStringTable[defReturn] + self.name)

        return {"offensive": offReturn, "defensive": defReturn}
    
    def vsDual(self, dualTypeName, verbose=False):
        oppType1 = dualTypeName.split('/')[0]
        oppType2 = dualTypeName.split('/')[1]
        oppDualType = DualType(oppType1, oppType2)
        
        # see if 4x effective against dual type opponent
        offReturn = 1.0
        for p in oppDualType.defensive.keys():
            if self.name in oppDualType.defensive[p]:
                offReturn = p
                break
        return {'offensive':offReturn}

def generateTypeChart():
    nTypes = len(list(typeTable.keys()))
    matrix = np.zeros((nTypes, nTypes)) + 1
    typeNames = [t for t in typeTable.keys()]
    for i, t1 in enumerate(typeNames):
        TypeSelf = Type(t1)
        for j, t2 in enumerate(typeNames):
            #TypeOpponent = Type(t2)
            print("{:25}".format(t1 + ' vs ' + t2), end=': ')
            comparison = TypeSelf.vs(t2, verbose=False)
            matrix[i][j] = comparison['offensive']
            print(TypeSelf.vs(t2, verbose=False))
    typeChart = pd.DataFrame(matrix, index=typeNames, columns=typeNames)
    return typeChart

def allDualTypes():
    allDualTypeSet = set()
    for t1 in typeTable.keys():
        for t2 in typeTable.keys():
            if t1 != t2:
                allDualTypeSet.add(frozenset([t1,t2]))
    
    allDualTypeList = ['/'.join(s) for s in allDualTypeSet]

    return allDualTypeList

class DualType:
    def __init__(self, type1, type2):
        allTypes = typeTable
        self.type1 = Type(type1)
        self.type2 = Type(type2)
        self.name = '/'.join([self.type1.name, self.type2.name])
        self.defensive = {4.0:set(), 2.0:set(), 1.0:set(allTypes.keys()), 0.5:set(), 0.25:set(), 0.0:set()}


        for p in [2.0, 0.5, 0.0]:
            self.defensive[p] = self.type1.defensive[p] | self.type2.defensive[p]
            #print(p, self.name, self.defensive[p])
            for t in self.defensive[p]:
                self.defensive[1.0].discard(t)

        for p1 in [2.0, 0.5, 0.0]:
            for p2 in [2.0, 0.5, 0.0]:
                for t in self.type1.defensive[p1]:
                    if t in self.type2.defensive[p2]:
                        self.defensive[p1*p2].add(t)
                        if p1 != 0.0:
                            self.defensive[p1].discard(t)
                        if p2 != 0.0:
                            self.defensive[p2].discard(t)

class Application:
    def __init__(self):
        self.possibleTypes = set([t for t in typeTable.keys()])
        self.possibleDualTypes = set(allDualTypes()) 
    def reduceFromAttackVsOpponent(self, attackType, powerMultiplier):
        Attack = Type(attackType)
        
        print()
        for t in self.possibleTypes.copy():
            if (Attack.vs(t)['offensive'] != powerMultiplier):
                print('{} eliminated'.format(t))
                self.possibleTypes.remove(t)
        
        print()

        for t in self.possibleDualTypes.copy():
            if powerMultiplier == 2.0:
                if Attack.vsDual(t)['offensive'] < powerMultiplier:
                    print('{} eliminated'.format(t))
                    self.possibleDualTypes.remove(t)
            elif powerMultiplier == 0.5:
                if Attack.vsDual(t)['offensive'] > powerMultiplier:
                    print('{} eliminated'.format(t))
                    self.possibleDualTypes.remove(t)
            else:
                if Attack.vsDual(t)['offensive'] != powerMultiplier:
                    print('{} eliminated'.format(t), Attack.vsDual(t)['offensive'])
                    self.possibleDualTypes.remove(t)
 

        print("\nPossible Types: ")
        for t in self.possibleTypes:
            print(t)
        
        print('\nPossible Dual Types: ')
        for t in self.possibleDualTypes:
            print(t)
        print()
    
    def run(self):
        try:
            done = False
            while not done:

                user_input = input('\nattackType powerMultiplier: ').split(' ')
                attackType, powerMultiplier = str(user_input[0]), float(user_input[1])
                self.reduceFromAttackVsOpponent(attackType, powerMultiplier)
                if sum([len(self.possibleTypes), len(self.possibleDualTypes)]) == 1: 
                    print("\nOpponent's Type Found: ")
                    print(self.possibleTypes)
                    print(self.possibleDualTypes)
                    done = True
            print('\napplication closing.')
        except KeyboardInterrupt:
            print('\napplication closed.')

if __name__ == "__main__":
    #typeChart = generateTypeChart()
    #print(typeChart)
    app = Application()
    app.run()
    
    '''
    dtTest = DualType('dark', 'psychic')
    print(dtTest.name)
    for p in dtTest.defensive.keys():
        print(p, ' - ', dtTest.defensive[p])
    '''
