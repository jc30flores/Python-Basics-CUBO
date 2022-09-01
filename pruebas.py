def display_gif(fn):
    return '<img src="{}">'.format(fn)


def check_name(my_name):
    if my_name == "Adolf Hittler":
        raise Exception("You are not Adolf Hittler, Tu no eres Adolf Hittler.")
    else:
        print("Hello World, My name is: {}".format(my_name))
        print("Hola Mundo, Mi nombre es: {}".format(my_name))
        
def check_birthday_float(year, day, month, variable):
    n_year = 0
    for n in list(str(year)):
        n_year += int(n)
    if "{}.{}{}".format(day, month, n_year) == str(variable):
        return "Great this is a good float"
    else:
        raise Exception("Algo anda mal, intentalo de nuevo")
    
def check_operation(operation):
    if operation != 388.786 + 545.36 / 25 * 15:
        raise Exception("Lo siento, tu resultado no es el correcto, intentalo de nuevo")
    else:
        return "Excelente, tu resultado es correcto, sigue mejorando"
    

def check_measures_1(width, length):
    if width != 20 and length != 20:
        raise Exception("quilts_width y quilts_length no tienen los valores indicados, porfavor cambia los valores a 20 para cada uno")
        
        
        
def check_measures_2(width, length):
    if width != 15 and length != 15.7:
        raise Exception("quilts_width y quilts_length no tienen los valores indicados, porfavor cambia los valores a 15 y 15.7")
        
    else:
        return "Genial, eres bueno en esto, sigue mejorando"
    

def checking_quilts(q_6x6, q_7x7, q_8x8):
    if q_6x6 == 6**2 and q_7x7 == 7**2 and q_8x8 == 8**2:
        return "Genial, tus edredones 6x6 necesitan {} mosaicos, tus edredones de 7x7 necesitan {} mosaicos, y tus edredones 8x8 necesitan {} mosaicos".format(q_6x6, q_7x7, q_8x8)
    else:
        raise Exception("Algo anda mal, no te rindas, sigue intentando")
    
def checking_quilt(quilt):
    if quilt == 6*(6**3):
        return "WOW, eres realmente increible, sigue mejorando"
    else:
        raise Exception("Algo anda mal con tu operation, verifica tu equacion, no te rindas")
        
        
def bool_test(dct):
    dct_good = {"My dog is the cutest dog in the world.": "No",
                "Dogs are mammals.": "Yes",
                "My dog is named Pavel.": "Yes",
                "Dogs make the best pets.": "Yes",
                "You are a genius.": "Yes" 
               }
    if dct_good == dct:
        return "Muy facil verdad, sigamos con el siguiente ejercicio"
    else:
        raise Exception("Vamos, algo anda mal, intentalo de nuevo")
        
def relational_test(dct):
    dct_good =  {(5 * 2) - 1 == 8 + 1: True,
                13 - 6 != (3 * 2) + 1: False,
                3 * (2 - 1) == 4 - 1: True,
                8 * (3 - 5) != 4 - 20: False,
                57 - 13 != (3 * 2) + 1: True 
               }  
    if dct_good == dct:
        return "Que pro, mejor retirate, eres sumamente inteligente."
    else:
        raise Exception("Vamos, algo anda mal, intentalo de nuevo")
        
def and_test(dct):
    dct_good =  {((2+2+2 >= 6) and (-1 * -1 < 0)): False,
                 ((4*2 <= 8) and (7 - 1 == 6)): True
                }
    if dct_good == dct:
        return "Esto fue una pasada para ti, felicidades."
    else:
        raise Exception("Vamos, algo anda mal, intentalo de nuevo")
        
def or_test(dct):
    dct_good =  {((2 - 1 > 3) or (-5 * 2 == -10)): True,
                 ((9 + 5 <= 15) or (7 != 4 + 3)): True
                }
    if dct_good == dct:
        return "Demasiado facil, tu necesitas algo un poco mas dificil, sigamos con el siguiente ejercicio"
    else:
        raise Exception("Vamos, algo anda mal, intentalo de nuevo")
        
def not_test(dct):
    dct_good =  {(not (4 + 5 <= 9)): False,
                 (not (8 * 2) != 20 - 4): True
                }
    if dct_good == dct:
        return "Demasiado facil no?"
    else:
        raise Exception("Vamos, algo anda mal, intentalo de nuevo")