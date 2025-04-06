
print("______CANDIDATOS______")
Caandidatos=["1. Anastacio","2. Pancracio ","3. Eustaquio ","4. Dina "];
print(Caandidatos[0]);
print(Caandidatos[1]);
print(Caandidatos[2]);
print(Caandidatos[3]);
print("0. Salir");

contar=[0,0,0,0];

while True:
    try:
        voto=int(input("Ingrese su voto de acuerdo a los candidatos: "));
    except ValueError:
        print("El formato de su voto no es correcto, solo se aceptan numeros enteros");
        continue;
    
    if voto>=1 and voto<=4:
        contar[voto-1]+=1;
    elif voto==0:
        break;
    else:
        print("Opcion no valida, solo se aceptan votos entre 1 y 4");
       
Total=sum(contar);
print("El total de votos es: ",Total);

for i in range(4):
    Porcentaje = (contar[i]/Total)*100; 
    Aproximado = round(Porcentaje,2);
    print(Caandidatos[i],": tiene ",contar[i]," votos"," con un porcentaje de: ",Aproximado,"%");

            
    
   
    

