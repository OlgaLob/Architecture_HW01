from ItemFabric import ItemFabric
from GemReward import GemReward


class GemGenerator(ItemFabric):

    def create_item(self):
        print("Создали сундук (др. камень)")
        return GemReward()