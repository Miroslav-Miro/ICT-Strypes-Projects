class Goblin:
    def __init__(self, game, attack=1, defense=1):
        self.game = game
        self._base_attack = attack
        self._base_defense = defense

    @property
    def attack(self):
        result = self._base_attack
        for creature in self.game.creatures:
            if isinstance(creature, GoblinKing) and creature != self:
                result += 1
        return result

    @property
    def defense(self):
        result = self._base_defense
        for creature in self.game.creatures:
            if isinstance(creature, Goblin) and creature != self:
                result += 1
        return result


class GoblinKing(Goblin):
    def __init__(self, game):
        super().__init__(game, attack=3, defense=3)


class Game:
    def __init__(self):
        self.creatures = []
