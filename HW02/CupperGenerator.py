from ItemFabric import ItemFabric
from CupperReward import CupperReward


class CupperGenerator(ItemFabric):

    def create_item(self):
        print("Создали сундук (медь)")
        return CupperReward()