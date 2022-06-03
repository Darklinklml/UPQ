import math
import plotly.graph_objects as go
#'Declaramos' e inicializamos las variables a 0
global a, b, N, y_ini, t_ini, h, f_evaluar, f_exacta, y_cal, y_exacta, t, e_rel, e_abs

a = b = N = h = t_ini = y_ini = 0.0
y_cal=[]
y_exacta=[]
t=[]
e_abs=[]
e_rel=[]
f_evaluar = "3.0*y + 2.0*t"
f_exacta= "(-0.66667*t)-(0.22222)+((0.44444)*(math.exp(3.0*t)))"
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

def solucion_euler(t_ini, y_ini, h):
    log_solucion=[]; t=[]; y_cal=[]; e_abs=[]; e_rel=[]; 
    t.append(t_ini)
    y_cal.append(y_ini)
    y_exacta.append(f_e(t=t_ini))
    e_abs.append(err_abs(y=y_cal[0], y_exacta=y_exacta[0]))
    e_rel.append(err_rel(y=y_cal[0], y_exacta=y_exacta[0]))
    script=f"""|   i   |   t   | EULER | EXACTA |ERROR ABS|ERROR REL|\n|   0   | {t[0]}   |{y_cal[0]} |{y_exacta[0]} |{e_abs[0]} |{e_rel[0]}|"""
    log_solucion.append(script)
    print(script)
    for i in range(1,int(N)+1):
        y_cal.append(euler(t=t[i-1], y=y_cal[i-1]))
        t.append(t[i-1]+h)
        y_exacta.append(f_e(t=t[i]))
        e_abs.append(err_abs(y=y_cal[i], y_exacta=y_exacta[i]))
        e_rel.append(err_rel(y=y_cal[i], y_exacta=y_exacta[i]))
        script=f"""|   {i}   |{round(t[i],5)}   |{round(y_cal[i],5)}|{round(y_exacta[i],5)}|{round(e_abs[i],5)}%|{round(e_rel[i],5)}%|"""
        log_solucion.append(script)
        print(script)
    print(f"\nError absoluto promedio:{(sum(e_abs)/len(e_abs))}% \nError relativo Promedio: {sum(e_rel)/len(e_rel)}%")
    graph("Grafica de Euler",tiempo=t,y_metodo=y_cal,y_exacta=y_exacta,error=e_rel )
  

def solucion_heun(t_ini, y_ini, h):
    log_solucion=[];t=[]; y_cal=[]; y_exacta=[]; e_abs=[]; e_rel=[]; 
    t.append(t_ini)
    y_cal.append(y_ini)
    y_exacta.append(f_e(t=t_ini))
    e_abs.append(err_abs(y=y_cal[0], y_exacta=y_exacta[0]))
    e_rel.append(err_rel(y=y_cal[0], y_exacta=y_exacta[0]))
    script=f"""\n|   i   |   t   |  HEUN  | EXACTA |ERROR ABS|ERROR REL|\n|   0   |  {round(t[0],5)}   |{round(y_cal[0],5)} |{round(y_exacta[0],5)} |{round(e_abs[0],5)}%|{round(e_rel[0],5)}%|"""
    log_solucion.append(script)
    print(script)
    for i in range(1,int(N)+1):
        y_cal.append(heun(t=t[i-1],y=y_cal[i-1]))
        t.append(t[i-1]+h)
        y_exacta.append(f_e(t=t[i]))
        e_abs.append(err_abs(y=y_cal[i],y_exacta= y_exacta[i]))
        e_rel.append(err_rel(y=y_cal[i],y_exacta= y_exacta[i]))
        script=f"""|   {i}   |{round(t[i],5)}   |{round(y_cal[i],5)}|{round(y_exacta[i],5)}|{round(e_abs[i],5)}%|{round(e_rel[i],5)}%|"""
        log_solucion.append(script)
        print(script)
    print(f"\nError absoluto promedio:{(sum(e_abs)/len(e_abs))}% \nError relativo Promedio: {sum(e_rel)/len(e_rel)}%")
    graph("Grafica de Heun",tiempo=t,y_metodo=y_cal,y_exacta=y_exacta,error=e_rel )


def inicializar_h(a,b,N):
    if not(a<b):
        h=a
        a=b
        b=h
    h= (b-a)/N
    return h

def graph(title,tiempo,y_metodo,y_exacta,error):
    fig = go.Figure()
    # Create and style traces
    fig.add_trace(
        go.Scatter(
            x=tiempo,
            y=y_metodo,
            name="Y-Calculada",
            mode="lines+markers",
            line=dict(color="firebrick", width=4),
        )
    )
    if f_evaluar != "":
        fig.add_trace(
            go.Scatter(
                x=tiempo,
                y=y_exacta,
                mode="lines",
                name="Y-Exacta",
                line=dict(color="royalblue", width=4),
            )
        )
        fig.add_trace(
            go.Scatter(
                x=t,
                y=error,
                mode="lines",
                name="Error",
                line=dict(color="green", width=4),
            )
        )
    fig.update_layout(
        annotations=[
            dict(
                xref="paper",
                yref="paper",
                x=0.0,
                y=1.05,
                xanchor="left",
                yanchor="bottom",
                text=title,
                font=dict(family="Fira Code", size=30, color="rgb(37,37,37)"),
                showarrow=False,
            ) ,
            dict(
                xref="paper",
                yref="paper",
                x=0.0,
                y=1.05,
                xanchor="left",
                yanchor="top",
                text="Error relativo total: "+str(round(sum(error)/len(error),20))+"%",
                font=dict(family="Fira Code", size=30, color="rgb(37,37,37)"),
                showarrow=False,
            )
        ]
    )
    fig.show()


def main():
    global a, b, N, y_ini, t_ini, h, f_evaluar, f_exacta, y_cal, y_exacta, t, e_rel, e_abs
    print(f"""
    ============================================================================================
                        CALCULADORA DE MÉTODOS - POR ELVIA CAROLINA Y GERSON
    ============================================================================================
* Definición del intervalo *
a=0
b=5
N=100
    """)

    a=0.0#int(input("Ingresa el inicio del intervalo: "))
    b=5.0#int(input("Ingresa el final del intervalo: "))
    N=100.0#int(input(f"""* Definición de N (iteraciones)*\nIngresa la cantidad de iteraciones: """))
    h=inicializar_h(a,b,N)

    print(f"""
* Definir h *
h= {h}
    
* Definir valores iniciales *
y(0)= 2/9    """)

    t_ini=0.00000 #int(input("Ingresa el valor inicial de t: "))
    y_ini=0.22222 #int(input("Ingresa el valor inicial de y: "))
    print("""
* Seleccionar métodos para solución *""")
    op=1
    while True:
        # Escoge un metodo 
        print("\n\nSelecciona uno de los siguientes métodos:\n1. Euler\n2. Heun\n0. finalizar programa")
         #int(input("""\n\nSelecciona uno de los siguientes métodos:\n1. Euler\n2. Heun\n0. finalizar programa"""))
        if op == 0:
            print("\n\nFin de la ejecucion")
            break
        elif op == 1:
            print("\n* Solución por método de Euler *")
            solucion_euler(t_ini=t_ini, y_ini=y_ini, h=h)
            op=2           
        elif op == 2:
            solucion_heun(t_ini=t_ini, y_ini=y_ini, h=h)
            op=0
        else:
            print("\nIngresa una opción correcta...")

if __name__ == '__main__':
    main()
