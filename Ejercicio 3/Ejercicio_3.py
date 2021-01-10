def find_palindrome_substring(palindrome_string, i, j):
    # contador palabras palindromas dentro del string
    counter = 0
    while i >= 0 and j < len(palindrome_string):
        # Si son distintos cortar ciclo
        if palindrome_string[i] != palindrome_string[j]:
            return counter
        print(palindrome_string[i: j + 1])
        counter += 1
        i -= 1
        j += 1
    return counter


def find_all_palindromes(palindrome_string):
    counter = 0
    for i in range(0, len(palindrome_string)):
        # Se suma al contador total las palabras palindromas
        counter += find_palindrome_substring(palindrome_string, i - 1, i + 1)
        counter += find_palindrome_substring(palindrome_string, i, i + 1)
    return counter


palindrome_string = "afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesmenandphilosophersanddivineswithconsistencyagreatsoulhassimplynothingtodohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinknowinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtodayahsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocratesandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwisespiritthatevertookfleshtobegreatistobemisunderstood"
#palindrome_string = "anitalavalatina"
print("Total palabras palindromas: ", find_all_palindromes(palindrome_string))
