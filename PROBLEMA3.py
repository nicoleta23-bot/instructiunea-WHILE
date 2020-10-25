"""
Se citesc numere de la tastatură până la introducerea unui număr impar divizibil cu 3. Să se afişeze suma tuturor numerelor pare introduse.  Exemplu: 
Date de intrare  7  4   6   2   1   9   Date de ieşire 12.  
"""
nr=0
suma_p=0
while ((nr%3!=0)or(nr%2==0)):
    nr=eval(input("dati numarul: "))
    if nr%2==0:
        suma_p+=nr
print("Suma numerelor pare este egala cu ",suma_p)
