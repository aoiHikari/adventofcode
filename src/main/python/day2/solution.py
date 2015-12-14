#!/usr/bin/python

inputFile = "input.txt";

def get_wrapping_paper_for_box(width, height, length):
    top_surface = 2 * length * width
    side_surface = 2 * height * length
    front_surface = 2 * width * height
    smallest_surface = min(top_surface, side_surface, front_surface) / 2
    return top_surface + side_surface + front_surface + smallest_surface

def get_ribbon_for_box(width, height, length):
    largest_dimension = max(width, height, length)
    base_ribbon_needed = 2 * (width + height + length - largest_dimension)
    volume_ribbon = width * height * length
    return base_ribbon_needed + volume_ribbon

total_wrapping_paper = 0
total_ribbon = 0

with open(inputFile) as f:
    for line in f:
        content = line
        tokens = content.split("x")
        w = int(tokens[0])
        h = int(tokens[1])
        l = int(tokens[2])

        total_wrapping_paper += get_wrapping_paper_for_box(w, h, l)
        total_ribbon += get_ribbon_for_box(w, h, l)

print "Total paper needed: " + str(total_wrapping_paper)
print "Total ribbon needed: " + str(total_ribbon)
