import numpy as np
from rich import inspect, print

from adventofcode.helper.io import get_day, get_riddle_input, save_riddle_input


class Vertex:
    def __init__(
        self, elevation: int, start: bool, finish: bool, i: int, j: int
    ) -> None:
        self.dist_to_vertex: None | int = None
        self.elevation = elevation
        self.start = start
        self.finish = finish
        self.i = i
        self.j = j
        self.idx = (i, j)
        self.distance = 0
        self.visited = False
        self.neighbors = []

    def to_idx(self, n):
        return self.i * n + self.j

    def add_neighbor(self, vertex):
        self.neighbors.append(vertex)


def get_vertices(riddle_input: str) -> list[list[Vertex]]:
    vertices = []
    heights = []
    for i, line in enumerate(riddle_input.splitlines()):
        verticesi = []
        heightsi = []
        for j, char in enumerate(line):
            # convert a..z to 0..25
            if char == "E":
                height = 25
                start = False
                finish = True
            elif char == "S":
                height = 0
                start = True
                finish = False
            else:
                height = ord(char) - ord("a")
                start = False
                finish = False
            heightsi.append(height)

            verticesi.append(
                Vertex(height, start, finish, i, j),
            )
        heights.append(heightsi)
        vertices.append(verticesi)

    for i in range(len(vertices)):
        for j in range(len(vertices[i])):
            vertex = vertices[i][j]
            if i > 0:
                if heights[i][j] >= heights[i - 1][j] - 1:
                    vertex.add_neighbor(vertices[i - 1][j])
            if i < len(vertices) - 1:
                if heights[i][j] >= heights[i + 1][j] - 1:
                    vertex.add_neighbor(vertices[i + 1][j])
            if j > 0:
                if heights[i][j] >= heights[i][j - 1] - 1:
                    vertex.add_neighbor(vertices[i][j - 1])
            if j < len(vertices[i]) - 1:
                if heights[i][j] >= heights[i][j + 1] - 1:
                    vertex.add_neighbor(vertices[i][j + 1])
    return vertices


def get_start_finish(vertices: list[list[Vertex]]) -> tuple[Vertex, Vertex]:
    start = None
    finish = None
    for i in range(len(vertices)):
        for j in range(len(vertices[i])):
            if vertices[i][j].start:
                start = vertices[i][j]
            if vertices[i][j].finish:
                finish = vertices[i][j]
    assert start is not None
    assert finish is not None
    return start, finish


def bfs_shortest_path(start: Vertex, goal: Vertex) -> tuple[int, list[Vertex]]:
    explored = []

    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]

    # If the desired node is
    # reached
    if start == goal:
        return 0, []

    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Condition to check if the
        # current node is not visited
        if node not in explored:
            # Loop to iterate over the
            # neighbours of the node
            for neighbour in node.neighbors:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    return len(new_path) - 1, new_path
            explored.append(node)

    # Condition when the nodes
    # are not connected
    return 1000000000, []
    # raise Exception("No path found")


def riddle1(riddle_input: str) -> int | str:

    answer = 0
    vertices = get_vertices(riddle_input)
    start, finish = get_start_finish(vertices)
    answer, _ = bfs_shortest_path(start, finish)
    return answer


def riddle2(riddle_input: str) -> int | str:
    vertices = get_vertices(riddle_input)

    _, finish = get_start_finish(vertices)
    flat = [v for row in vertices for v in row]
    starting_vertices = {v.idx: v for v in flat if v.elevation == 0}
    path_lengths = {v.idx: 0 for v in flat if v.elevation == 0}

    keys = list(starting_vertices.keys())
    # randomly shuffle keys

    keys = np.random.permutation(keys)

    for i, (idx, vertex) in enumerate(starting_vertices.items()):
        # for i, idx in enumerate(keys):
        # print(i, "/", len(keys))
        # idx = tuple(idx)
        # vertex = starting_vertices[idx]
        if path_lengths[idx] == 0:
            distance, path = bfs_shortest_path(vertex, finish)
            path_lengths[idx] = distance
            for i, v in enumerate(path):
                if v.idx in path_lengths.keys() and path_lengths[v.idx] == 0:
                    path_lengths[v.idx] = distance - i
    return min(path_lengths.values())


if __name__ == "__main__":
    day = get_day(__file__)
    riddle_input = get_riddle_input(day)
    save_riddle_input(day, riddle_input)

    example = """"""
    if len(example) > 0:
        answer1 = riddle1(example)
    else:
        answer1 = riddle1(riddle_input)
    print(answer1)

    if answer1 != 0:
        print("Computation for riddle 2 is super slow and will take 5 minutes...")
        answer2 = riddle2(riddle_input)
        print(answer2)
