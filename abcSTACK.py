def a(): 
    print('a IN') #first a in
    b()# move to fun b
    d()# after b out move to fun d
    print('a OUT')# after d out next a out

def b():
    print('b IN') # after a in next n in 
    c() # move to fun C
    print('b OUT')# after c out next b out move to fun a

def c():
    print('c IN') # after b in next c in 
    print('c OUT')# after c in next c out move to fun b

def d():
    print('d IN')# after b out d in
    print('d OUT')# after d in next d out move back to a

a() # calling a fun