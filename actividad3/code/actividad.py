
def dibujarRectangulo(base,altura):
    """Dibuja un Rectangulo segun la base y la altura de

    Args:
        base (int): base del Rectangulo
        altura (int): altura del rectangulo 
    """
    for i in range(altura):
        for j in range(base):
            print('*',end=' ')
        print()

def dibujarTriangulo(base):
    """Dibuja un triangulo rectangulo segun la base 

    Args:
        base (int):Base del rectangulo
    """
    for i in range(base):
        for j in range(i):
            print('*',end=' ')
        print()



dibujarRectangulo(5,5)
dibujarTriangulo(5)
    