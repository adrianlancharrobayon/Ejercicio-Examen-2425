from motoFP import *
def lee_carreras_test(ruta_csv):
    return lee_carreras(ruta_csv)

def maximo_dias_sin_ganar_test(carreraFP, piloto):
    return maximo_dias_sin_ganar(carreraFP, piloto)

def piloto_mas_podios_por_circuito_test(carreras):
    return piloto_mas_podios_por_circuito(carreras)

def escuderias_con_solo_un_piloto_test(carreras):
    return escuderias_con_solo_un_piloto(carreras)
if __name__== "__main__":
    carreras=lee_carreras_test("./data/mundial_motofp.csv")
    #print(carreras)
    #lee_carreras_test("./data/mundial_motofp.csv")
    #print(f"Test maximo_dias_sin_ganar: ")
    #print(f"Para Marc Marquez:{maximo_dias_sin_ganar_test(carreras, "Marc Marquez")}")
    #print(f"Para Jorge Martin:{maximo_dias_sin_ganar_test(carreras, "Jorge Martin")}")
    #print(f"Para Para Freddy Mercuri:{maximo_dias_sin_ganar_test(carreras, "Freddy Mercuri:")}")
    #print(f"Test piloto_mas_podios_por_circuito: {piloto_mas_podios_por_circuito_test(carreras)}")
    print(f"Test escuderias_con_solo_un_piloto: {escuderias_con_solo_un_piloto_test(carreras)}")


