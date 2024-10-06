class MinecraftCommand:
    def __init__(self):
        self.commands = []

    def add_command(self, command: str):
        """Добавляет команду в список команд."""
        self.commands.append(command)

    def set_block(self, x: int, y: int, z: int, block_type: str):
        """Создает команду для установки блока на указанных координатах."""
        command = f"setblock {x} {y} {z} {block_type}"
        self.add_command(command)

    def teleport(self, player: str, x: int, y: int, z: int):
        """Создает команду для телепортации игрока на указанные координаты."""
        command = f"tp {player} {x} {y} {z}"
        self.add_command(command)

    def give_item(self, player: str, item: str, count: int = 1):
        """Создает команду для выдачи предмета игроку."""
        command = f"give {player} {item} {count}"
        self.add_command(command)

    def summon_entity(self, entity: str, x: int, y: int, z: int):
        """Создает команду для призыва существа на указанных координатах."""
        command = f"summon {entity} {x} {y} {z}"
        self.add_command(command)

    def effect(self, player: str, effect: str, duration: int, amplifier: int = 1):
        """Создает команду для наложения эффекта на игрока."""
        command = f"effect give {player} {effect} {duration} {amplifier}"
        self.add_command(command)

    def clear_effect(self, player: str, effect: str = None):
        """Создает команду для снятия эффекта с игрока."""
        if effect:
            command = f"effect clear {player} {effect}"
        else:
            command = f"effect clear {player}"
        self.add_command(command)

    def execute(self) -> str:
        """Возвращает все команды в виде строки, готовой для использования в командных блоках."""
        return "\n".join(self.commands)

# Пример использования:
if __name__ == "__main__":
    mc_cmd = MinecraftCommand()
    mc_cmd.set_block(10, 64, 10, "minecraft:diamond_block")
    mc_cmd.teleport("Steve", 100, 64, 100)
    mc_cmd.give_item("Alex", "minecraft:diamond_sword", 1)
    mc_cmd.summon_entity("minecraft:zombie", 105, 64, 105)
    mc_cmd.effect("Steve", "speed", 30, 2)
    mc_cmd.clear_effect("Steve")

    print(mc_cmd.execute())
