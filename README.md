# Minecraft Command Generator

## Описание

`minecraft_commands.py` — это простая библиотека для генерации команд для командных блоков в Minecraft. Она позволяет легко создавать команды для установки блоков, телепортации игроков, выдачи предметов и выполнения других действий в мире Minecraft.

## Как использовать

1. Скачайте zip
   -![image](https://github.com/user-attachments/assets/afd72f5b-61c3-4e61-a5af-cdc3feee2928)

3. Импортируйте класс `MinecraftCommand` в свой Python проект.
4. Используйте методы класса для создания команд.

**ВАЖНО файл `minecraft_commands.py` Должен быть в тойже папке что и проект**
![image](https://github.com/user-attachments/assets/c5df4d57-978c-4d61-b4ba-0a9928084cc1)

### Пример использывания библиотеки:

**Код** :

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
```
**Результат** :

![image](https://github.com/user-attachments/assets/a5807fa4-615b-41be-b492-263525ab81c1)

