from typing import NamedTuple
import csv
from datetime import datetime
Piloto=NamedTuple("Piloto", [("nombre", str),("escuderia", str)])

CarreraFP=NamedTuple("CarreraFP",[
        ("fecha_hora",datetime), 
        ("circuito",str),                    
        ("pais",str), 
        ("seco",bool), # True si el asfalto estuvo seco, False si estuvo mojado
        ("tiempo",float), 
        ("podio", list[Piloto])])

def lee_carreras(ruta_csv):
    with open(ruta_csv, encoding="utf-8") as f:
        res=[]
        lector= csv.reader(f, delimiter=",")
        next(lector)
        for fh, circuito, pais, seco, tiempo, nombre_ganador, marca_ganador, nombre_segundo_clasificado, marca_segundo_clasificado,nombre_tercer_clasificado, marca_tercero_clasificado in lector:
           podio=[nombre_ganador, marca_ganador, nombre_segundo_clasificado, marca_segundo_clasificado,nombre_tercer_clasificado, marca_tercero_clasificado]
           fecha_hora= datetime.strptime(fh, "%Y-%m-%d %H:%M")
           
           res.append(CarreraFP(fecha_hora, circuito, pais, seco, tiempo, podio))

        return res
    
def maximo_dias_sin_ganar(carrerasFP, piloto):
    fechas_ganadas=[]
    for i in carrerasFP:
        if i.podio == piloto:
            fechas_ganadas.append(i.fecha_hora)
    if len(fechas_ganadas)<2:
        return None
    else:
        sorted(fechas_ganadas)
        for f in fechas_ganadas:
            max_dias=[]
            dias= (f - (f-1)).days
            max_dias.append(dias)
        return max(max_dias)
           





            
    
    
