from typing import List, Tuple, TypeAlias
from utils.cli import run

from itertools import pairwise

Point: TypeAlias = Tuple[int, int]
Segment: TypeAlias = Tuple[Point, Point]

def parse_inputs(inputs: List[str]):
  result = []
  for line in inputs:
    tokens = line.strip().split(',')
    assert len(tokens) == 2, f'{line} has more than two tokens'
    result.append((int(tokens[0]), int(tokens[1])))
  return result

def area(p1: Point, p2: Point):
  x1, y1 = p1
  x2, y2 = p2

  return (abs(x1-x2)+1) * (abs(y1-y2)+1)
assert area((11, 1), (7, 3)) == 15

def part1(inputs: List[str]):
  points = parse_inputs(inputs)

  result = -float('inf')
  for p1 in points:
    for p2 in points:
      result = max(result, area(p1, p2))
  return result

def visualize_points(points: List[Tuple[int, int]]):
  import turtle

  xs = [p[0] for p in points]
  ys = [p[1] for p in points]
  min_x, max_x = min(xs), max(xs)
  min_y, max_y = min(ys), max(ys)

  t = turtle.Turtle()
  
  t.screen.setworldcoordinates(min_x, min_y, max_x, max_y)
  t.penup()
  t.begin_fill()
  for x, y in points:
    t.setpos(x, y)
    t.pendown()
  t.setpos(points[0])
  t.end_fill()
  t.screen.mainloop()

# TODO this takes 1 minute
def part2(inputs: List[str]):
  points = parse_inputs(inputs)
  # uncomment below line to run a visualization
  # visualize_points(points)

  # from visualization:
  # - shape is not convex
  # - there is no enclosed holes in the shape

  # algorithm adjusted to fit
  # for each pair of points
  #   if they do not form a straight line,
  #     extrapolate the other two corners
  #     check if the extrapolated points are inside the polygon
  #       do this by finding number of lines that contain the points, the number has to be 4
  #     check if all the four lines does not intersect any other sides of the polygon

  segments = list(pairwise(points + [points[0]]))

  def segment_vertical(s: Segment):
    start, end = s
    return start[0] == end[0]
  
  def segment_horizontal(s: Segment):
    start, end = s
    return start[1] == end[1]

  def segment_above_point(s: Segment, p: Point):
    x, y = p
    start, end = s

    x1, y1 = start
    x2, y2 = end

    if x1 >= x2:
      x1, x2 = x2, x1
    return segment_horizontal(s) and y1 >= y and x1 <= x <= x2

  def segment_below_point(s: Segment, p: Point):
    x, y = p
    start, end = s

    x1, y1 = start
    x2, y2 = end

    if x1 >= x2:
      x1, x2 = x2, x1
    return segment_horizontal(s) and y1 <= y and x1 <= x <= x2
  
  def segment_left_point(s: Segment, p: Point):
    x, y = p
    start, end = s

    x1, y1 = start
    x2, y2 = end

    if y1 >= y2:
      y1, y2 = y2, y1
    return segment_vertical(s) and x1 <= x and y1 <= y <= y2
  
  def segment_right_point(s: Segment, p: Point):
    x, y = p
    start, end = s

    x1, y1 = start
    x2, y2 = end

    if y1 >= y2:
      y1, y2 = y2, y1
    return segment_vertical(s) and x1 >= x and y1 <= y <= y2

  def point_in_polygon(p: Point):    
    # up
    up = any( \
      map(lambda s: segment_above_point(s, p), segments)
    )
    # down
    down = any( \
      map(lambda s: segment_below_point(s, p), segments)
    )
    # left
    left = any( \
      map(lambda s: segment_left_point(s, p), segments)
    )
    # right
    right = any( \
      map(lambda s: segment_right_point(s, p), segments)
    )

    return up and down and left and right

  def segment_intersect(s1: Segment, s2: Segment):
    a1, b1 = s1
    a2, b2 = s2

    if segment_vertical(s1) and segment_horizontal(s2):
      y1, y2 = a1[1], b1[1]
      y = a2[1]
      x1, x2 = a2[0], b2[0]

      if y1 > y2:
        y1, y2 = y2, y1
      if x1 > x2:
        x1, x2 = x2, x1
      return y1 < y < y2 and x1 < a1[0] < x2
    elif segment_horizontal(s1) and segment_vertical(s2):
      x1, x2 = a1[0], b1[0]
      x = a2[0]
      y1, y2 = a2[1], b2[1]

      if x1 > x2:
        x1, x2 = x2, x1
      if y1 > y2:
        y1, y2 = y2, y1
      return x1 < x < x2 and y1 < a1[1] < y2
    else:
      return False

  def intersect_polygon_segment(s: Segment):
    return any(\
      map(lambda poly_segment: segment_intersect(poly_segment, s), segments)
    )

  result = -float('inf')
  for i, p1 in enumerate(points):
    for j, p2 in enumerate(points):
      if j <= i:
        continue
      
      x1, y1 = p1
      x2, y2 = p2

      if x1 == x2: # straight horizontal
        pass
      elif y1 == y2: # straight vertical
        pass
      else:
        # extrapolate
        p3 = x1, y2
        p4 = x2, y1
        rect_segments = list(pairwise([p1, p3, p2, p4, p1]))

        if point_in_polygon(p3) \
            and point_in_polygon(p4) \
            and not any(list(map(intersect_polygon_segment, rect_segments))):
            result = max(result, area(p1, p2))
  return result
if __name__ == '__main__':
  run(part1, part2)