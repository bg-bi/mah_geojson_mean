import random

with open("points.json", 'w') as pts_file:
    pts_file.write('{"type": "MultiPoint", "coordinates": [\n')
    num_pts = 10000
    for i in range(num_pts):
        pts_file.write(f'[{random.uniform(20,80)}, {random.uniform(20,80)}]')
        if not i == num_pts - 1:
            pts_file.write(',\n')
    pts_file.write("\n]}")
