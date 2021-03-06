from display import *
from matrix import *
import math

def add_circle( points, cx, cy, cz, r, step ):
    x0 = cx + r
    y0 = cy
    t = 0.0
    while(t < 1.0001):
        x = cx + r * math.cos(2 * math.pi * t)
        y = cy + r * math.sin(2 * math.pi * t)
        add_edge(points,x0,y0,cz,x,y,cz)
        x0 = x
        y0 = y
        t += step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    x_co = generate_curve_coefs(x0,x1,x2,x3,curve_type)
    y_co = generate_curve_coefs(y0,y1,y2,y3,curve_type)

    x = x0
    y = y0
    t = 0.0
    print("x_co\n")
    print_matrix(x_co)
    while (t < 1.0001):
        x = t * (t * (x_co[0][0] * t + x_co[0][1])
                 + x_co[0][2] ) + (x_co[0][3])
        y = t * (t * (y_co[0][0] * t + y_co[0][1])
                 + y_co[0][2] ) + (y_co[0][3])
        add_edge(points,x0,y0,0,x,y,0)
        x0 = x
        y0 = y
        t += step

def draw_lines( matrix, screen, color ):
    if len( matrix ) < 2:
        print "Need at least 2 points to draw a line"
        
    p = 0
    while p < len( matrix ) - 1:
        draw_line( screen, matrix[p][0], matrix[p][1],
                   matrix[p+1][0], matrix[p+1][1], color )
        p+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0 )
    add_point( matrix, x1, y1, z1 )

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )


def draw_line( screen, x0, y0, x1, y1, color ):
    dx = x1 - x0
    dy = y1 - y0
    if dx + dy < 0:
        dx = 0 - dx
        dy = 0 - dy
        tmp = x0
        x0 = x1
        x1 = tmp
        tmp = y0
        y0 = y1
        y1 = tmp
    
    if dx == 0:
        y = y0
        while y <= y1:
            plot(screen, color,  x0, y)
            y = y + 1
    elif dy == 0:
        x = x0
        while x <= x1:
            plot(screen, color, x, y0)
            x = x + 1
    elif dy < 0:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y - 1
                d = d - dx
            x = x + 1
            d = d - dy
    elif dx < 0:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x - 1
                d = d - dy
            y = y + 1
            d = d - dx
    elif dx > dy:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y + 1
                d = d - dx
            x = x + 1
            d = d + dy
    else:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x + 1
                d = d - dy
            y = y + 1
            d = d + dx

