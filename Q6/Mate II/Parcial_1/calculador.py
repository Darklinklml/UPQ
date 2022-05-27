import math

#'Declaramos' e inicializamos las variables a 0
global a, b, N, y_ini, t_ini, h, f_evaluar, f_exacta, y_euler, y_heun, y_exacta, t, e_rel_euler, e_abs_euler, e_rel_heun, e_abs_heun

a = b = N = h = t_ini = y_ini = 0
y_euler=[]
y_heun=[]
y_exacta=[]
t=[]
e_abs_euler=[]
e_rel_euler=[]
e_abs_heun=[]
e_rel_heun=[]
f_evaluar = "10-y/t"
f_exacta= "5*t+2/t"
log_solucion=[]

def euler(t,y):
    y= y + h*f(t,y)
    return y
        
def heun(t,y):
    y_int = y + h*f(t,y)
    y = y + ((0.5*h)*(f(t,y)+f(t+h,y_int)))
    return y

def err_abs(y,y_exacta):
    err= abs(y_exacta-y)
    return err

def err_rel(y,y_exacta):
    err=100.0*err_abs(y,y_exacta)/abs(y_exacta)
    return err

def f(t,y):
    return eval(f_evaluar)

def f_e(t):
    return eval(f_exacta)

def solucion_euler(t_ini, y_ini):
    log_solucion=[]; t=[]; y_euler=[]; y_exacta=[]; e_abs_euler=[]; e_rel_euler=[]; 
    t.append(t_ini)
    y_euler.append(y_ini)
    y_exacta.append(f_e(t_ini))
    e_abs_euler.append(err_abs(y_euler[0], y_exacta[0]))
    e_rel_euler.append(err_rel(y_euler[0], y_exacta[0]))
    script=f"""
    |i: 0 | t: {t[0]} | euler: {y_euler[0]} | exacta: {y_exacta[0]} | e. abs: {e_abs_euler[0]} | e. rel: {e_rel_euler[0]}"""
    log_solucion.append(script)
    print(script)
    for i in range(1,N+1):
        y_euler.append(euler(t[i-1], y_euler[i-1]))
        t.append(t[i-1]+h)
        y_exacta.append(f_e(t[i]))
        e_abs_euler.append(err_abs(y_euler[i], y_exacta[i]))
        e_rel_euler.append(err_rel(y_euler[i], y_exacta[i]))
        script=f"""
    |i: 0 | t: {t[i]} | euler: {y_euler[i]} | exacta: {y_exacta[i]} | e. abs: {e_abs_euler[i]} | e. rel: {e_rel_euler[i]}"""
        log_solucion.append(script)
        print(script)
    print(f"\nError absoluto promedio:{(sum(e_abs_euler)/len(e_abs_euler))}% \nError relativo Promedio: {sum(e_rel_euler)/len(e_rel_euler)}%")
        

def solucion_heun(t_ini, y_ini):
    log_solucion=[];t=[]; y_heun=[]; y_exacta=[]; e_abs_heun=[]; e_rel_heun=[]; 
    t.append(t_ini)
    y_heun.append(y_ini)
    y_exacta.append(f_e(t_ini))
    e_abs_heun.append(err_abs(y_heun[0], y_exacta[0]))
    e_rel_heun.append(err_rel(y_heun[0], y_exacta[0]))
    script=f"""\n|i: 0 | t: {t[0]} | heun: {y_heun[0]} | exacta: {y_exacta[0]} | e. abs: {e_abs_heun[0]}% | e. rel: {e_rel_heun[0]}%"""
    log_solucion.append(script)
    print(script)
    for i in range(1,N+1):
        y_heun.append(heun(t[i-1], y_heun[i-1]))
        t.append(t[i-1]+h)
        y_exacta.append(f_e(t[i]))
        e_abs_heun.append(err_abs(y_heun[i], y_exacta[i]))
        e_rel_heun.append(err_rel(y_heun[i], y_exacta[i]))
        script=f"""\n|i: 0 | t: {t[i]} | heun: {y_heun[i]} | exacta: {y_exacta[i]} | e. abs: {e_abs_heun[i]}% | e. rel: {e_rel_heun[i]}%"""
        log_solucion.append(script)
        print(script)
    print(f"\nError absoluto promedio:{(sum(e_abs_heun)/len(e_abs_heun))}% \nError relativo Promedio: {sum(e_rel_heun)/len(e_rel_heun)}%")


def inicializar_h(a,b,N):
    if not(a<b):
        h=a
        a=b
        b=h
    h= (b-a)/N
    return h
def main():
    global a, b, N, y_ini, t_ini, h, f_evaluar, f_exacta, y_euler, y_heun, y_exacta, t, e_rel_euler, e_abs_euler, e_rel_heun, e_abs_heun
    print(f"""
    ============================================================================================
                        CALCULADORA DE MÉTODOS - POR ELVIA CAROLINA Y GERSON
    ============================================================================================
    
    * Definición del intervalo *
    """)

    a=int(input("Ingresa el inicio del intervalo: "))
    b=int(input("Ingresa el final del intervalo: "))
    N=int(input(f"""
* Definición de N (iteraciones)*
Ingresa la cantidad de iteraciones: """))
    h=inicializar_h(a,b,N)
    
    print(f"""
* Definir h *
h= {h}
    
* Definir valores iniciales *
    """)

    t_ini= int(input("Ingresa el valor inicial de t: "))
    y_ini= int(input("Ingresa el valor inicial de y: "))
    print("""
* Seleccionar métodos para solución *""")
    while True:
        # Escoge un metodo 
        print()
        op = int(input("""
        
Selecciona uno de los siguientes métodos:
1. Euler
2. Heun
0. finalizar programa
        """))
        if op == 0:
            print("\n\nFin de la ejecucion")
            break
        elif op == 1:
            print("\n* Solución por método de Euler *")
            solucion_euler(t_ini, y_ini)
        elif op == 2:
            solucion_heun(t_ini, y_ini)
        else:
            print("\nIngresa una opción correcta...")

if __name__ == '__main__':
    main()
