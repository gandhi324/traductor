traduccion={
    "JUICIOSO":"es una persona responsable",
    "AGUACATE":"es una fruta que tambien se conoce como palta",
    "ESFERO":"un istrumento usado para escribir con tinta tambien conocido como boligrafo o lapicero", 
    "EH AVE MARIA PUES":"se lo utiliza para expresar sorpresa"
}

word=input("Escribe una palabra la cual no sepas el significado(en mayúsculas)")

if word in traduccion.keys():
    print("el significado de la palabra es",traduccion[word])
else:
    print("la palabra no se encuentra en el diccionario")
