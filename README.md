# Overview


This is a simple roguelike adventure game I wrote using C#. The player goes through a randomized dungeon with various rooms trying to destory a cursed artifact. The program has 3 options for character class (warrior, thief, and mage), points for health, stealth, and mana based on class. There is an inventory system with gold, 4 armor types, 8 different weapons, and 3 different keys dropped from bosses. The room types are treasure rooms, trap rooms, a trader room (to purchase new equipment), a monster room containing 7 different monster types, a boss room with 1 of 3 different bosses, and an artifact room. The players wins by collecting all three boss keys, either by killing the bosses or buying the keys, and then entering an artifact room with the three keys. They lose buy dying from traps, monsters, or bosses.

[Software Demo Video](https://youtu.be/wHF3yVXczL8)

# Development Environment

I developed the program using C# and .NET 8.0 with System.Collections.Generic and I used VS code for writing and bug testing.

# Useful Websites

- [Microsoft .NET guide to syntax and data structures](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic?view=net-8.0)
- [Stack Overflow Q/A's for programming](https://stackoverflow.com/questions)

# Future Work

- Fix bugs- i.e. game over delayed to next round of combat, health going over max, combat number displaying in a weird order.
- Balance game- fix health and damage levels for all creatures and player to make game possible, but difficult.
- Expand game- possibly adding graphics like room sprites, making more combat choices like fleeing or hiding, and/or misc items like potions or rope.