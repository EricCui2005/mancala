import board

def main():
    playBoard = board.Board()
    for elem in playBoard.pockets:
        print(elem)
    print(len(playBoard.pockets))

if __name__ == "__main__":
    main()