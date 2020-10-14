"""
(Parent, child)
Input format = (A, B) (B, C) (A, E) (B, D)
if you find any error report them in priortiy
E1 - Invalid input format
E2 - Duplicate pair
E3 - Parent has more than Two children
E4 - Multiple roots
E5 - Tree contains cycle

"""
from collections import Counter
class Node:
    def __int__(self, val):
        self.val = val
        self.left = None
        self.right = None

class TreeChecker:
    def __init__(self):
        self.pairs = None
        # node->(True/False, # of children)
        self.hasParent = {}
        self.E1 = False
        self.E2 = False
        self.E3 = False
        self.E4 = False
        self.E5 = False

    def isInputValid(self, input):
        if not self.isInputHasTrailingSpaces(input) or not self.isValidParanthesis(input):
            self.E1 = True

    def isDuplicatePair(self, input):
        self.pairs = input.split()
        count = Counter(self.pairs)
        for i in count.values():
            if i > 1:
                self.E2 = True

    def isMorethanTwoChild(self):
        for p, c in self.pairs.keys():
            if c not in self.hasParent:
                self.hasParent[c] = (True, 0)
            elif c in self.hasParent and self.hasParent[c][0] == True:
                self.E5 = True

            if p not in self.hasParent:
                self.hasParent[p] = (False, 1)
            elif p in self.hasParent:
                childs = self.hasParent.get(p)[1]
                if childs > 2:
                    self.E3 = True
                self.hasParent[p] = (True, childs+1)

    def isCycle(self):
        for node in self.hasParent.keys():
            if self.hasParent.get(node)[0] == True:
                continue
            else:
                break
        else:
            self.E5 = True

    def isMultipleRoots(self):
        isFound = False
        for node in self.hasParent.keys():
            if self.hasParent.get(node)[0] == False :
                isFound = True
            if self.hasParent.get(node)[0] == False and isFound:
                self.E4 = True

    def isValidParanthesis(self, str):
        ind = 0
        while ind < len(str):
            if str[ind] == "(" and str[ind+1].isUpper() and str[ind+2] == "," and str[ind+3].isUpper() and str[ind+4] == ")" and str[ind+5] == " ":
                ind += 6
            else:
                return False
        return True

    def isInputHasTrailingSpaces(self, str):
        if str[0] == " " or str[-1] == " ":
            return False
        else:
            return True

    def BTChecker(self, str):
        self.isInputValid(str)
        if self.E1:
            return "E1"
        self.isDuplicatePair(str)
        if self.E2:
            return "E2"
        self.isMorethanTwoChild()
        if self.E3:
            return "E3"
        self.isMultipleRoots()
        if self.E4:
            return "E4"
        self.isCycle()
        if self.E5:
            return "E5"
        




