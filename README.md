# Minecraft Command Generator

## Описание

`minecraft_commands.py` — это простая библиотека для генерации команд для командных блоков в Minecraft. Она позволяет легко создавать команды для установки блоков, телепортации игроков, выдачи предметов и выполнения других действий в мире Minecraft.

## Как использовать

1. Скачайте файл `minecraft_commands.py`.
2. Импортируйте класс `MinecraftCommand` в свой Python проект.
3. Используйте методы класса для создания команд.

### Пример:

```python
from minecraft_commands import MinecraftCommand

mc_cmd = MinecraftCommand()
mc_cmd.set_block(10, 64, 10, "minecraft:diamond_block")
mc_cmd.teleport("Steve", 100, 64, 100)
mc_cmd.give_item("Alex", "minecraft:diamond_sword", 1)
mc_cmd.summon_entity("minecraft:zombie", 105, 64, 105)
mc_cmd.effect("Steve", "speed", 30, 2)
mc_cmd.clear_effect("Steve")

print(mc_cmd.execute())
