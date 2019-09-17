from animals import cat 

from animals.bird import Bird

from animals.ninebandedarmadillo import NineBandedArmadillo as Armadillo 

def main():

    tabby = cat.Cat('Tabby')

    parrot = Bird('Parrot')
    armadillo = Armadillo('9-banded armadillo')

    tabby.make_sound()
    parrot.make_sound()
    armadillo.make_sound()


if __name__ == '__main__':
    main()


    