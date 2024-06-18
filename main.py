from graphics import Window, Line, Point, Cell

def main():
    win = Window(1200, 800)
    coords = []
    for x in range(0, 1200, 100):
        for y in range(0, 800, 100):
            coords.append((x, y))
    print(coords)
    # wait for close starts the loop
    win.wait_for_close()

if __name__ == '__main__':
    main()

