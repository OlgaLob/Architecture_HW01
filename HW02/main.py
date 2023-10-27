import random

from GemGenerator import GemGenerator
from GoldGenerator import GoldGenerator
from SilverGenerator import SilverGenerator
from CupperGenerator import CupperGenerator

if __name__ == '__main__':
    fabricList = [GemGenerator(), GoldGenerator(), SilverGenerator(), CupperGenerator()]
    for i in range(5):
        rnd = random.choice(fabricList).create_item().open()