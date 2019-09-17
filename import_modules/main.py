import cat             # import cat module  
from bird import Bird  # Import Bird class from bird module
from ninebandedarmadillo import NineBandedArmadillo as Armadillo 

def main():

    # Create Cat.
    # This code imported the cat module, Cat class is a name in the cat module
    kitten = cat.Cat('Kitty')
    kitten.make_sound()

    # Create Bird. Can use name directly.
    penguin = Bird('Penguin')
    penguin.make_sound()

    armadillo = Armadillo('Armadillo')
    armadillo.make_sound()


if __name__ == '__main__':
    main()





    # # Create bird. Imported the Bird class from the bird module 
    # dove = Bird('Dove')
    # dove.make_sound() 
