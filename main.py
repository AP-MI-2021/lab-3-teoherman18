def is_prime(num):
    """
    Verifica daca un numar este prim
    Input:
    -num : int
    Output
    -True, daca n e palindrom, False in caz contrar : bool
    """
    if num < 2:
        return False
    elif num==2:
        return True
    else:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False

        return True


def test_is_prime():
    assert is_prime(7) == True
    assert is_prime(10) == False
    assert is_prime(1) == False
    assert is_prime(29) == True
test_is_prime()


def toate_numerele_sunt_neprime(lst):
    '''
    Verifica daca toate elementele dintr-o lista sunt neprime
    :param lst: lista de numere intregi
    :return: True, daca toate elementele din lis sunt neprime, False in caz contrar
    '''

    for num in lst:
        if is_prime(num) == True:
            return False
    return True

def test_toate_numerele_sunt_neprime():
    assert toate_numerele_sunt_neprime([16]) is True
    assert toate_numerele_sunt_neprime([10,4,8]) is True
    assert toate_numerele_sunt_neprime([2,3,5,7]) is False
    assert toate_numerele_sunt_neprime([12,2,3]) is False

#7.Toate numerele sunt neprime
def get_longest_all_not_prime(lst):
    '''
    Determina cea mai lunga subsecventa de numere neprime
    :param lst: lista de numere intregi
    :return: cea mai lunga subsecventa de numere neprime
    '''

    subsecventaMax=[]
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if toate_numerele_sunt_neprime(lst[i:j+1]) is True and len(lst[i:j+1]) > len(subsecventaMax):
                subsecventaMax = lst[i:j+1]
    return subsecventaMax

def test_get_longest_all_not_prime():
    assert get_longest_all_not_prime([]) == []
    assert get_longest_all_not_prime([2,10,20,12,4])==[10,20,12,4]
    assert get_longest_all_not_prime([2,3,5])==[]
    assert get_longest_all_not_prime([2,5,10])==[10]
    assert get_longest_all_not_prime([2,10,20,12,8,5,7])==[10,20,12,8]


def media_numerelor(lst):
    '''
    Calculeaza media valorilor din lista
    :param lst: lista de numere intregi
    :return: media : float
    '''

    suma = 0
    media = 0
    for num in lst:
        suma = suma + num

    if len(lst) != 0 :
        media = suma/len(lst)
    return media

def test_media_numerelor():
    assert media_numerelor([]) == 0
    assert media_numerelor([2,3,4]) == 3
    assert media_numerelor([18,20,5,12]) == 13.75
    assert media_numerelor([10,20,30]) == 20
test_media_numerelor()

def media_e_mai_mica(lst, valoare):
    '''
    Verifica daca media este media este mai mica decat valoarea citita
    :param lst: lista de numere intregi
    :param valoare: valoarea cu care se compara media : float
    :return: True, daca media numerelor este mai mica decat valoarea citita, False in caz contrar
    '''
    if media_numerelor(lst) > valoare:
        return False
    return True

def test_media_e_mai_mica():
    assert media_e_mai_mica([2,3,4],4.0) is True
    assert media_e_mai_mica([18,20,5,12],5.0) is False
    assert media_e_mai_mica([3,4,5],6.5) is True
    assert media_e_mai_mica([3,4,5],2.0) is False
test_media_e_mai_mica()

#17.Media numerelor nu depaseste o valoare citita
def get_longest_average_below(lst, average):
   '''
    Determina cea mai lunga subsecventa de numere a caror medie nu depaseste o valoare citita
   :param lst: lista de numere intregi
   :param average: valoarea cu care se compara media : float
   :return: cea mai lunga subsecventa de numere a caror medie nu depaseste o valoare citita
   '''
   subsecventaMax = []
   for i in range(len(lst)):
       for j in range(i, len(lst)):
           if media_e_mai_mica(lst[i:j+1],average) is True and len(lst[i:j + 1]) > len(subsecventaMax):
               subsecventaMax = lst[i:j+1]
   return subsecventaMax

def test_get_longest_average_below():
    assert get_longest_average_below([], 4.0) == []
    assert get_longest_average_below([4], 4.0) == [4]
    assert get_longest_average_below([3, 6], 4.0) == [3]
    assert get_longest_average_below([5], 4.0) == []
    assert get_longest_average_below([1, 2, 3, 5, 6, 7, 8, 9, 11, 13, 19, 23, 17], 4.0) == [1, 2, 3, 5, 6, 7]
    assert get_longest_average_below([8, 9, 11, 1, 2, 3, 5, 6, 7, 13, 19, 23, 17], 4.0) == [1, 2, 3, 5, 6, 7]
test_get_longest_average_below()

def PrintMenu():
    print('1. Citire lista')
    print('2. Determinare cea mai lunga subsecventa in care numerele sunt neprime')
    print('3. Determinare cea mai lunga subsecventa in care media numerelor este mai mica decat o valoare citita')
    print('4. Iesire')

def citireLista():
    lst = []
    givenString = input("Dati lista, cu elemente separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        lst.append(int(x))
    return lst

def main():
    test_toate_numerele_sunt_neprime()
    test_media_e_mai_mica()
    test_media_numerelor()
    test_is_prime()
    test_get_longest_average_below()
    test_get_longest_all_not_prime()
    lst=[]
    while True:
        PrintMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lst = citireLista()
        elif optiune == "2":
            print(get_longest_all_not_prime(lst))
        elif optiune == "3":
            average = float(input("Dati valoarea: "))
            print(get_longest_average_below(lst, average))
        elif optiune == "4":
            break
        else:
            print("Optiune gresita! Reincercati!")


if __name__ == '__main__':
    main()
