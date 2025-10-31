from motoFP import *
def lee_carreras_test(ruta_csv):
    lee_carreras(ruta_csv)

def maximo_dias_sin_ganar_test(carrerasFP, piloto):
    print(maximo_dias_sin_ganar(carrerasFP, piloto))

if __name__== "__main__":
    carreras= lee_carreras_test("./data/mundial_motofp.csv")
    maximo_dias_sin_ganar_test(carreras, "Francesco Bagnaia")
