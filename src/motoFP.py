from typing import List, NamedTuple
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

def lee_carreras(filename: str) -> List[CarreraFP]:
    res=[]
    with open(filename, encoding="utf-8") as f:
        res=[]
        lector= csv.reader(f, delimiter=",")
        next(lector)
        for fh, circuito, pais, seco, t, nombre_ganador, marca_ganador, nombre_segundo_clasificado, marca_segundo_clasificado,nombre_tercer_clasificado, marca_tercero_clasificado in lector:
            podio=[Piloto(nombre_ganador, marca_ganador), Piloto(nombre_segundo_clasificado, marca_segundo_clasificado), Piloto(nombre_tercer_clasificado, marca_tercero_clasificado)]
            fecha_hora= datetime.strptime(fh, "%Y-%m-%d %H:%M")
            if seco=="Seco":
               seco=True
            else:
               seco=False
            tiempo=float(t)
            res.append(CarreraFP(fecha_hora, circuito, pais, seco, tiempo, podio))
        return res
    
def maximo_dias_sin_ganar(carreras: List[CarreraFP], nombre_piloto: str) -> int:
    max_dias=[]
    fechas_ganadas=[]
    for i in carreras:
        if i.podio[0].nombre == nombre_piloto:
            fechas_ganadas.append(i.fecha_hora)
    if len(fechas_ganadas)<2:
        return None
    else:
        sorted(fechas_ganadas)
        for i in range(len(fechas_ganadas) - 1):
            dias = (fechas_ganadas[i+1] - fechas_ganadas[i]).days
            max_dias.append(dias)
        return max(max_dias)
           
def piloto_mas_podios_por_circuito(carreras: list[CarreraFP]) -> dict[str,str]:
    diccionario={}
    for c in carreras:
        if c.circuito not in diccionario:
            diccionario[c.circuito]={}

        for p in c.podio:
            if p.nombre not in diccionario[c.circuito]:
                diccionario[c.circuito][p.nombre]=1
            else:
                diccionario[c.circuito][p.nombre]+=1
    
    diccionario2={}
    for circuito, pilotos in diccionario.items():
        diccionario2[circuito]= max(pilotos, key=pilotos.get)

    return diccionario2

def escuderias_con_solo_un_piloto(carreras: list[CarreraFP]) -> list[str]:
    escuderias={}
    for c in carreras:
        for p in c.podio:
            if p.escuderia not in escuderias:
                escuderias[p.escuderia]=set()
            escuderias[p.escuderia].add(p.nombre)
    
    lista=[]
    for escuderia, pilotos in escuderias.items():
        if len(pilotos)==1:
            lista.append(escuderia)
    
    return lista

def piloto_racha_mas_larga_victorias_consecutivas(carreras: list[CarreraFP], año: int|None = None) -> tuple[str, int]:
    carreras_filtradas=carreras
    if año is not None:
        carreras_filtradas= [c for c in carreras if c.fecha_hora.year==año]
    carreras_ordenadas=sorted(carreras_filtradas, key= lambda c:c.fecha_hora)
    
    mejor_racha=0
    mejor_piloto=""
    ganador_anterior=None
    racha=0
    
    for carrera in carreras_ordenadas:
        ganador=carrera.podio[0].nombre
        if ganador==ganador_anterior:
            racha+=1
            
        else:
            if racha>mejor_racha:
                mejor_racha=racha
                mejor_piloto=ganador_anterior
            racha=1
        ganador_anterior=ganador
        
    
    return(mejor_piloto, mejor_racha)
    

def ultimos_ganadores_por_circuito(carreras:list[CarreraFP], n: int, estado: str) -> dict[str, list[str]]:
    
    seco=(estado=="Seco")
    
    carreras_ordenadas= sorted(carreras, key=lambda c:c.fecha_hora, reverse=True)
    
    diccionario={}
    
    for c in carreras_ordenadas:
        if c.seco==seco:
            if c.circuito not in diccionario:
                diccionario[c.circuito]=[]
            if len(diccionario[c.circuito])<n:
                ganador=c.podio[0].nombre
                diccionario[c.circuito].append(ganador)

    return diccionario
    


        









            
    
    
