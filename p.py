import pickle

grid_lines = [
    [(0, 200), (600, 200)],
    [(0, 400), (600, 400)],
    [(200, 0), (200, 600)],
    [(400, 0), (400, 600)]
]


print(pickle.dumps(grid_lines))
