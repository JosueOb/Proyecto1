def perimetro(num_lad,long_lad):
    perimetro = num_lad*long_lad
    return perimetro
##esta funcion solo contendra la longitud del tamaño
def area(long_lad):
    lado_c = long_lad
    lado_b = long_lad/2
    expo_c = lado_c**2
    expo_b = lado_b**2
    resta  =  expo_c - expo_b
    altura = resta**(1/2)
    area = long_lad*altura
    return area

def menu():
    try:
        num_lad = int(input("Número de lados: "))
        if num_lad >= 3 and num_lad <=10:
            long_lad = float(input("Longitud de un lado: "))
            if num_lad == 3:
                area_fig = area(long_lad)
                perimetro_fig = perimetro(num_lad,long_lad)
            elif num_lad == 4:
                area_fig = long_lad**2
                perimetro_fig = perimetro(num_lad,long_lad)
            elif num_lad == 5:
                area_fig = num_lad*area(long_lad)
                perimetro_fig = perimetro(num_lad,long_lad)
            elif num_lad == 6:
                area_fig = num_lad*area(long_lad)
                perimetro_fig = perimetro(num_lad,long_lad)
            elif num_lad == 7:
                area_fig = num_lad*area(long_lad)
                perimetro_fig = perimetro(num_lad,long_lad)
            elif num_lad == 8:
                area_fig = num_lad*area(long_lad)
                perimetro_fig = perimetro(num_lad,long_lad)
            elif num_lad == 9:
                area_fig = num_lad*area(long_lad)
                perimetro_fig = perimetro(num_lad,long_lad)
            elif num_lad == 10:
                area_fig = num_lad*area(long_lad)
                perimetro_fig = perimetro(num_lad,long_lad)
            print(area_fig,perimetro_fig)
            menu()
        else:
            print("No existe figura \n")
            menu()
    except ValueError:
        print("Dato incorrecto \n\nIngrese de nuevo")
        menu()
        
        
menu()
