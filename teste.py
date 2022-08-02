

from __future__ import print_function

n = 10;

vet = []; # define um vetor vazio
for i in range(0, n, 1) : 
  vet.append(n+i); #Percorre de um em um

with open("list.txt", "w") as writer:
    for vetor in vet:
        writer.write(vetor+ "\n")

# Imprime o vetor na mesma linha
print("\nO vetor: ", end=""); # informe o que vira impresso a seguir (na mesma linha devido ao parametro end=""
print(vet);




# Imprimir vet em linha unica na forma "( 0,  0) ( 1,   1)..."
print("\nNovamente o vetor impresso de 2 modos: "); # informe o que vira impresso a seguir (e "quebre" a linha)
i = 0;
for item in vet : # "item in vet" e' um iterador, item comeca em vet[0], depois vet[1] e assim por diante
  print("(%2d, %2d) " % (item, vet[i]), end="");
  i += 1;
print(); # quebre a linha