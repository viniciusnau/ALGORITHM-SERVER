from django.http import JsonResponse, HttpResponse


unity_in_full = ('', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')

irregular_tens_in_full = ('dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
                          'dezenove')

tens_in_full = ('', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa')

hundred_in_full = ('', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos',
                   'oitocentos', 'novecentos')


def algorithm_view(request, *args, **kwargs):
    algorithm = int(str(request).replace("<WSGIRequest: GET '/", "").replace("/'>", ""))

    algorithm_list = list()
    algorithm_in_full = list()

    if algorithm < -100000 or algorithm > 100000:
        return HttpResponse("<h1>POR FAVOR ESCOLHA UM NÚMERO NO INTERVALO DE [-99999, 99999].</h1>")
    else:
        if algorithm == 0:
            algorithm_in_full.append('zero')
        if algorithm < 0:
            algorithm_in_full.append('menos')
            algorithm = algorithm * -1

        for i in range(0, 5):
            isolated = algorithm % 10
            algorithm = algorithm // 10
            algorithm_list.insert(0, isolated)

        for digit in range(0, 5):
            if digit == 0 and algorithm_list[0] > 1:
                algorithm_in_full.append(tens_in_full[algorithm_list[digit]])

            if digit == 1:
                if algorithm_list[0] == 1:
                    algorithm_in_full.append(irregular_tens_in_full[algorithm_list[digit]])
                elif algorithm_list[1] > 0:
                    if algorithm_list[0] > 1:
                        algorithm_in_full.append('e')
                    algorithm_in_full.append(unity_in_full[algorithm_list[digit]])
                if algorithm_list[0] or algorithm_list[1] > 0:
                    algorithm_in_full.append('mil')

            if digit == 2 and algorithm_list[2] > 0:
                if algorithm_list[1] > 0 or algorithm_list[0] > 0:
                    algorithm_in_full.append('e')
                if algorithm_list[3] == algorithm_list[4] == 0:
                    algorithm_in_full.append('cem')
                else:
                    algorithm_in_full.append(hundred_in_full[algorithm_list[digit]])

            if digit == 3 and algorithm_list[3] > 1:
                if algorithm_list[2] > 0 or algorithm_list[1] > 0 or algorithm_list[0] > 0:
                    algorithm_in_full.append('e')
                algorithm_in_full.append(tens_in_full[algorithm_list[digit]])

            if digit == 4:
                if algorithm_list[3] > 0 or algorithm_list[2] > 0 or algorithm_list[1] > 0 or algorithm_list[0] > 0:
                    algorithm_in_full.append('e')
                if algorithm_list[3] == 1:
                    algorithm_in_full.append(irregular_tens_in_full[algorithm_list[digit]])
                elif algorithm_list[4] > 0:
                    algorithm_in_full.append(unity_in_full[algorithm_list[digit]])

    algorithm_in_full = str(algorithm_in_full).replace("[", "").replace(",", "").replace("'", "").replace("]", "")

    return JsonResponse({"extenso": algorithm_in_full})
