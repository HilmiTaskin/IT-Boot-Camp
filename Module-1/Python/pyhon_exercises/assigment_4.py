"""In what situation the queens eat each other in chess. The queen can move horizontally, vertically and diagonally."""

def queen(players):
    p1= players[0]
    p2=players[1]
    if p1[0]==p2[0] or p1[1]==p2[1]:
        return True
    axisx = "ABCDEFGH"
    axisy = "12345678"
    locationx = abs(axisx.index(p1[0]) - axisx.index(p2[0]))
    locationy = abs(axisy.index(p1[1]) - axisy.index(p2[1]))
    if locationx == locationy:
        return True
    else:
        return False
queen([["A","1"],["C","3"]])

