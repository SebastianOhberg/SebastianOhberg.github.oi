
cont_externo = 0
cont_interno = 0

while cont_externo < 5:
    while cont_interno < 6:
        print(cont_externo, cont_interno)
        cont_interno += 1  
        if cont_interno == 3:
            print('Has llegado al 3')

    cont_externo += 1
    cont_interno = 0
