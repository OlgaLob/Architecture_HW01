from ItemFabric import ItemFabric
from SilverReward import SilverReward


class SilverGenerator(ItemFabric):

    def create_item(self):
        print("Создали сундук (серебро)")
        return SilverReward()
    