def validConsonant(word):
    consonant = {'a','e','i','o','u'}
    if (len(word) > 2):
        sw = True
        idx = 0;
        while (sw):
            if (idx + 2 >len(word) ):
                sw = False
                return sw

            print(word[idx])
            print(word[idx+1])
            print(word[idx+2])

            inConsonant = word[idx] in consonant
            if (inConsonant):
                if (word[idx + 1] in consonant and word[idx + 2] in consonant):
                    return sw
            idx = idx + 1
    else:
        print("No hay datos suficientes")

result = validConsonant("prueba")
print(f" finaliza {result}") 