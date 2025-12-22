from motoFP import *
def lee_carreras_test(ruta_csv):
    return lee_carreras(ruta_csv)

def maximo_dias_sin_ganar_test(carreraFP, piloto):
    return maximo_dias_sin_ganar(carreraFP, piloto)

if __name__== "__main__":
    carreras=lee_carreras_test("./data/mundial_motofp.csv")
    print(carreras)
    #lee_carreras_test("./data/mundial_motofp.csv")
    print(maximo_dias_sin_ganar_test(carreras, "Marc Marquez"))
