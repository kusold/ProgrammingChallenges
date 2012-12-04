import math

def main():

    rt3 = math.sqrt(3)
    rt32 = rt3 / 2.0
    rt36 = rt3 / 6.0

    def distance(xa, xb, ya, yb):
        return math.hypot(xa - xb, ya - yb)

    def routeFinder(a, b):
        la = math.sqrt(a)
        lb = math.sqrt(b)
        sla = la * la
        slb = lb * lb
        xa = 0.5 * (a - sla)
        ya = ((a - sla)) * rt36
        xb = 0.5 * (la - lb + b - slb)
        yb = rt32 * (la - lb) + ((b - slb)) * rt36
        print distance(xa, xb, ya, yb)

    routeFinder(0,7)
    routeFinder(2,8)
    routeFinder(9,10)
    routeFinder(10,11)

#main()

def calc_distance(n, m):
    point_a = { 'x': 0.0, 'y': 0.0 }
    point_b = { 'x': 0.0, 'y': 0.0 }

    start = math.sqrt(n)
    point_a['x'] = (n - start * start - start) / 2.0
    
    print (start + n)

    if start:
        point_a['y'] = (start - 1) * (math.sqrt(3) / 2.0)
        point_a['y'] += ((math.sqrt(3) / 3.0))#if ((start + n) & 1.0) else (math.sqrt(3) / 2.0))
    
    end = math.sqrt(m)
    point_b['x'] = (m - end * end - end) / 2.0
    
    if end:
        point_b['y'] = (end - 1) * (math.sqrt(3) / 2.0)
        point_b['y'] += ((math.sqrt(3) / 3.0)) #if ((end + m) & 1.0) else (math.sqrt(3) / 2.0))

    return math.sqrt(math.pow(point_a['x'] - point_b['x'], 2) + math.pow(point_a['y'] - point_b['y'], 2))




calc_distance(0,7)
calc_distance(2,8)
calc_distance(9,10)
calc_distance(10,11)
raw_input()

