nomes = ["Mayara","Amanda", "Diulli", "Erique"]


#percorre a lista escrevendo um por um
with open("nomes.txt", "w") as writer:
    for nome in nomes:
        writer.write(nome+ "\n")