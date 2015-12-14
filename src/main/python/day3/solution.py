#!/usr/bin/python

from sets import Set

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return (isinstance(other, self.__class__) and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.x) + hash(self.y)

inputFile = "input.txt";

def next_point(char, point):
    if char == "<":
        return Point(point.x - 1, point.y)
    elif char == ">":
        return Point(point.x + 1, point.y)
    elif char == "^":
        return Point(point.x, point.y + 1)
    elif char == "v":
        return Point(point.x, point.y - 1)
    else:
        return point

def solve_part_one():
    current_point = Point(0, 0)
    all_visited = set()
    all_visited.add(current_point)

    with open(inputFile) as input_file:
      while True:
        char = input_file.read(1)
        if char:
          current_point = next_point(char, current_point)
          all_visited.add(current_point)
        else:
          break

    print "Total visited houses for a single Santa: %d." % len(all_visited)

def solve_part_two():
    # Santa's starting point.
    santa_point = Point(0, 0)
    # Robo Santa's starting point.
    robo_santa_point = Point(0, 0)

    # First is Santa
    next_robo_santa = False

    # A set of all visited points.
    all_visited = set()
    all_visited.add(santa_point)

    with open(inputFile) as input_file:
      while True:
        char = input_file.read(1)
        if char:
            if next_robo_santa:
                # Robo Santa is out there, giving presents.
                robo_santa_point = point = next_point(char, robo_santa_point)
            else:
                # Santa's turn to spread joy.
                santa_point = point = next_point(char, santa_point)

            all_visited.add(point)
            next_robo_santa = not next_robo_santa
        else:
            break

    print "Total visited houses for Santa and robo Santa: %d." % len(all_visited)

def main():
    solve_part_one()
    solve_part_two()

if __name__ == "__main__":
    main()
