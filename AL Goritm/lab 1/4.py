with open('input.txt') as fp:
    lines = fp.readlines()
    segments = lines[1:]

def optimal_points(segment):
    points = []
    segment = [[int(i) for i in segment.split()] for segment in segment]
    segment.sort(key = lambda x: x[1])
    while segment:
        point = segment[0][1]
        points.append(point)
        segment = [segment for segment in segment if segment[1] < point or segment[0] > point]
    return points

f = open('output.txt', 'w')
f.write(str(len(optimal_points(segments))) + '\n' + ' '.join([str(i) for i in optimal_points(segments)]))
