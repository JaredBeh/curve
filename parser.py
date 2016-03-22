from display import *
from matrix import *
from draw import *

STEP = .05

def parse_file( fname, points, transform, screen, color ):
    f = open(fname,'r')
    text = f.read()
    lines = text.split('\n')
    n = 0
    while(n < len(lines)):
        if(lines[n] == "ident"):
            ident(transform)
        elif(lines[n] == "apply"):
            matrix_mult(transform,points)
        elif(lines[n] == "display"):
            clear_screen(screen)
            draw_lines(points,screen,color)
            display(screen)
        else:
            func = lines[n]
            n += 1
            argstring = lines[n].split(' ')
            args = map(float,argstring)
            argsint = map(int,args)
            if(func == "scale"):
                matrix_mult(make_scale(args[0],args[1],args[2]),transform)
            elif(func == "translate"):
                matrix_mult(make_translate(args[0],args[1],args[2]),transform)
            elif(func == "xrotate"):
                matrix_mult(make_rotX(args[0]),transform)
            elif(func == "yrotate"):
                matrix_mult(make_rotY(args[0]),transform)
            elif(func == "zrotate"):
                matrix_mult(make_rotZ(args[0]),transform)
            elif(func == "line"):
                add_edge(points,argsint[0],argsint[1],argsint[2],argsint[3],argsint[4],argsint[5])
            elif(func == "circle"):
                add_circle(points,argsint[0],argsint[1],0,argsint[2],STEP)
            elif(func == "hermite"):
                add_curve(points,argsint[0],argsint[1],argsint[2],argsint[3],
                          argsint[4],argsint[5],argsint[6],argsint[7],
                          STEP,HERMITE)
            elif(func == "bezier"):
                add_curve(points,argsint[0],argsint[1],argsint[2],argsint[3],
                          argsint[4],argsint[5],argsint[6],argsint[7],
                          STEP,BEZIER)
            elif(func == "save"):
                save_ppm(screen,argstring[0])
        n += 1
    f.close()

