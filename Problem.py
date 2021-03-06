longest = ''
s='abecedario'

for i in range(0, len(s)):
    #i para desplazarse por todo el string
    temp = s[i]
    j = i
    while j + 1 < len(s) and s[j] <= s[j+1]:
        #Nos adelantamos en la evaluación de todo el string y lo vamos almacenando en temp
        temp += s[j+1]
        j += 1
    if len(temp) > len(longest):
        #En la primera iteración se guarda y luego guarda el que sea más largo (aparece el primero de ellos)
        longest = temp

print("Longest substring in alphabetical order is:", longest)

longest = current = s[0]
while len(s) > 1:
    if s[0] <= s[1]:
        #En cada tramo alfabeticamente ordenado se va almacenando en el current
        current += s[1]
        if len(current) > len(longest):
            longest = current
    else:
        #Se reinicia el current
        current = s[1]
    #Se va acortando hasta llegar al final
    s = s[1:]
print("Longest substring in alphabetical order is: " + longest)

s='abecedario'
temp=""
alpha=""
for i in range(len(s)):
    #Empieza en 0 y acaba al final del string
    if s[i-1]<=s[i]:
        temp=temp+s[i]
        if len(temp)>len(alpha):
            alpha=temp           
    else:
        #Aquí viene en la primera iteración y siempre que se reinicia
        temp=s[i]
print('Longest substring in alphabetical order is: ' + str(alpha))

s='abecedario'
cur = lng = s[0]
for c in s[1:] + ' ':
    #Va recorriendo la c la palabra desde la posición 1 y asignando su valor a c
    #Como cuando decíamos que for letter in 'hola' iba adoptando letter cada una de ellas (h, o, l, a)
    if c < cur[-1]:
        #Se examina comparando la c con la última letra del cur
        if len(cur) > len(lng):
            #Se compara con anteriores
            lng = cur
        #Si se cumple que no está en orden, se reinicia
        cur = ''
    #Se va almacenando en el cur
    cur += c
print('Longest substring in alphabetical order is:', lng)

#Este ultimo es demasiado raro
now = ""
ans = ""
s='abecedario'
for n in range(len(s)):
    #Recorre con n todo el string
    if n+1 < len(s):
        if s[n] <= s[n+1]:
            now = now + s[n:n+1]
        else:
            now = now + s[n]
            if len(ans) < len(now):
                #Comprueba que es el más largo y reinicia
                ans = now
                now = ""
            else:
                now = ""
    elif n+1 == len(s):
        if s[n] > s[n-1]:
            now = now + s[n]
#Nos quedamos con el m
if len(now) > len(ans):
    ans = now
    print("Longest substring in alphabetical order is:",ans)
else:
    print("Longest substring in alphabetical order is:",ans)
