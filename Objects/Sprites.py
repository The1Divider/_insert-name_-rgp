from InventorySystem import ThisShouldntComeUp
from dataclasses import dataclass
from typing import List, Type, Optional, Union

from .Items import WeaponType, ArmourType, UnknownWeaponType, UnknownArmourType


class MenuSprites:
    start_menu = "------------------\n" \
                 "    Epic RPG      \n" \
                 "------------------\n" \
                 "1) New Game       \n" \
                 "2) Load Game      \n" \
                 "3) Help           \n" \
                 "4) Quit             "

    main_menu = "------------------\n" \
                "    Main Menu     \n" \
                "------------------\n" \
                "1) Quest          \n" \
                "2) Inventory      \n" \
                "3) Shop           \n" \
                "4) Stats          \n" \
                "5) Load/Save      \n" \
                "6) Exit             "

    class InventoryMenus:
        @staticmethod
        def inventory_menu_spacing(menu_list: List[str], special_list: List[str]) -> str:
            """Method to align inventory display regardless of item name size"""
            max_length = len(max(menu_list, key=len))

            for menu in menu_list:

                ind = menu_list.index(menu)

                if menu in special_list:
                    while len(menu) < max_length:
                        menu = menu[:-2] + "-" + menu[-2:]
                        menu_list[ind] = menu

                while len(menu) < max_length:
                    menu = menu[:-3] + " " + menu[-3:]
                    menu_list[ind] = menu

            return "".join(menu_list)

        @staticmethod
        def stats_menu(stats_list: List[int], current_hp: Optional[int]) -> str:
            """ pass stats along with player_level + player_exp """
            hp, armour_hp, dmg, weapon_dmg, defence, armour_defence, crit, weapon_crit, crit_chance, \
                weapon_crit_chance, block, level, exp, exp_percent = stats_list
            exp_bars = "".join(["*" for _ in range(int(exp_percent) // 10) if exp != 0])

            while len(exp_bars) < 10:
                exp_bars += "-"

            menu_line1 = " ------------------------------- \n"
            menu_line2 = "| Stats |\n"
            menu_line3 = "|-------------------------------|\n"
            menu_line4 = f"| Level       | {level} |\n"
            menu_line5 = f"| Exp         | [{exp_bars}] |\n"
            menu_line6 = "|-------------------------------|\n"
            menu_line7 = f"| Hp          | {hp} + {armour_hp} |\n"
            menu_line8 = f"| Current Hp  | {current_hp} |\n"
            menu_line9 = f"| Dmg         | {dmg} + {weapon_dmg} |\n"
            menu_line10 = f"| Defence     | {defence} + {armour_defence} |\n"
            menu_line11 = f"| Crit        | {crit} + {weapon_crit} |\n"
            menu_line12 = f"| Crit Chance | {crit_chance} + {weapon_crit_chance} |\n"
            menu_line13 = f"| Block       | {block} |\n"
            menu_line14 = " ------------------------------- \n"
            menu_list = [menu_line1, menu_line2, menu_line3, menu_line4, menu_line5, menu_line6, menu_line7,
                         menu_line8, menu_line9, menu_line10, menu_line11, menu_line12, menu_line13, menu_line14]

            if current_hp is None:
                menu_list.remove(menu_line8)

            return MenuSprites.InventoryMenus.inventory_menu_spacing(menu_list,
                                                                     [menu_line1, menu_line3, menu_line6, menu_line14])

        @staticmethod
        def inventory_armour_menu(armour_list: List[Union[ArmourType, UnknownArmourType]]) -> str:
            helmet, chest, leg, boots, ring1, ring2 = armour_list
            menu_line1 = " ------------------------------- \n"
            menu_line2 = "| Armour |\n"
            menu_line3 = "|-------------------------------|\n"
            menu_line4 = f"| Helmet     | {helmet.name} |\n"
            menu_line5 = f"| Chestplate | {chest.name} |\n"
            menu_line6 = f"| Leggings   | {leg.name} |\n"
            menu_line7 = f"| Boots      | {boots.name} |\n"
            menu_line8 = f"| Ring 1     | {ring1.name} |\n"
            menu_line9 = f"| Ring 2     | {ring2.name} |\n"
            menu_line10 = " ------------------------------- \n"
            menu_list = [menu_line1, menu_line2, menu_line3, menu_line4, menu_line5,
                         menu_line6, menu_line7, menu_line8, menu_line9, menu_line10]

            return MenuSprites.InventoryMenus.inventory_menu_spacing(menu_list, [menu_line1, menu_line3, menu_line10])

        @staticmethod
        def inventory_weapon_menu(weapon_list: List[Union[WeaponType, UnknownWeaponType]]) -> str:
            weapon1, weapon2, quiver = weapon_list
            menu_line1 = " ------------------------------- \n"
            menu_line2 = "| Weapons |\n"
            menu_line3 = "|-------------------------------|\n"
            menu_line4 = f"| Weapon 1 | {weapon1.name} |\n"
            menu_line5 = f"| Weapon 2 | {weapon2.name} |\n"
            menu_line6 = f"| Quiver   | {quiver} |\n"
            menu_line7 = " ------------------------------- \n"
            menu_list = [menu_line1, menu_line2, menu_line3, menu_line4,
                         menu_line5, menu_line6, menu_line7]

            return MenuSprites.InventoryMenus.inventory_menu_spacing(menu_list, [menu_line1, menu_line3, menu_line7])

        @staticmethod
        def inventory_bag_menu(item_list: List[Union[WeaponType, UnknownWeaponType]]) -> str:
            item1, item2, item3, item4, item5, item6, item7, item8, item9, item10 = item_list
            menu_line1 = " ------------------------------- \n"
            menu_line2 = "| Bag |\n"
            menu_line3 = "|-------------------------------|\n"
            menu_line4 = f"| 1 - {item1.name} | 2 - {item2.name} |\n"
            menu_line5 = f"| 3 - {item3.name} | 4 - {item4.name} |\n"
            menu_line6 = f"| 5 - {item5.name} | 6 - {item6.name} |\n"
            menu_line7 = f"| 7 - {item7.name} | 8 - {item8.name} |\n"
            menu_line8 = f"| 9 - {item9.name} | 10 - {item10.name} |\n"
            menu_line9 = " ------------------------------- \n"
            menu_list = [menu_line1, menu_line2, menu_line3, menu_line4, menu_line5,
                         menu_line6, menu_line7, menu_line8, menu_line9]

            return str(
                MenuSprites.InventoryMenus.inventory_menu_spacing(menu_list, [menu_line1, menu_line3, menu_line9]))

        @staticmethod
        def weapon_selection(weapon: Union[WeaponType, UnknownWeaponType]) -> str:
            weapon_values_names = ["name", "item_weight", "dmg", "crit", "crit_chance", "special", "price"]
            weapon_values = [getattr(weapon, attr) for attr in weapon_values_names]
            name, weight, dmg, crit, crit_chance, special, price = weapon_values

            if special == "":
                special = None

            menu_line1 = " ------------------------------- \n"
            menu_line2 = f"| {name} |\n"
            menu_line3 = "|-------------------------------|\n"
            menu_line4 = f"| Weight      - {weight} Handed |\n"
            menu_line5 = f"| Dmg         - {dmg} |\n"
            menu_line6 = f"| Crit        - {crit} |\n"
            menu_line7 = f"| Crit Chance - {crit_chance}% |\n"
            menu_line8 = f"| Price       - {price}$ |\n"
            menu_line9 = "|-------------------------------|\n"
            menu_line10 = f"| Special     - {special} |\n"
            menu_line11 = " ------------------------------- \n"
            menu_list = [menu_line1, menu_line2, menu_line3, menu_line4, menu_line5, menu_line6,
                         menu_line7, menu_line8, menu_line9, menu_line10, menu_line11]

            return MenuSprites.InventoryMenus.inventory_menu_spacing(menu_list,
                                                                     [menu_line1, menu_line3, menu_line9, menu_line11])

        @staticmethod
        def armour_selection(weapon: Union[ArmourType, UnknownArmourType]) -> str:
            # UnknownArmourType shouldn't never get here but the linter complains without a union
            armour_values_names = ["name", "hp", "defence", "special", "price"]
            armour_values = [getattr(weapon, attr) for attr in armour_values_names]
            name, hp, defence, special, price = armour_values

            if special == "":
                special = None

            menu_line1 = " ------------------------------- \n"
            menu_line2 = f"| {name} |\n"
            menu_line3 = f"|-------------------------------|\n"
            menu_line4 = f"| Hp         - {hp} |\n"
            menu_line5 = f"| Defence    - {defence} |\n"
            menu_line6 = f"| Special    - {special} |\n"
            menu_line7 = f"| Price      - {price}$ |\n"
            menu_line8 = " ------------------------------- \n"
            menu_list = [menu_line1, menu_line2, menu_line3, menu_line4, menu_line5,
                         menu_line6, menu_line7, menu_line8]

            return MenuSprites.InventoryMenus.inventory_menu_spacing(menu_list, [menu_line1, menu_line3, menu_line8])

    class ShopMenus:
        @staticmethod
        def shop_menu_spacing(menu_list: List[str], special_list: List[int]) -> str:
            """Method to align inventory display regardless of item name size"""
            max_length = len(max(menu_list, key=len))

            for menu in menu_list:

                ind = menu_list.index(menu)

                if menu_list.index(menu) + 1 in special_list:
                    while len(menu) < max_length:
                        menu = menu[:-2] + "-" + menu[-2:]
                        menu_list[ind] = menu

                else:
                    while len(menu) < max_length:
                        menu = menu[:-3] + " " + menu[-3:]
                        menu_list[ind] = menu

            return "".join(menu_list)

        @staticmethod
        def shop_menu(balance: int):
            menu_line1 = " ------------------------------- \n"
            menu_line2 = "| Shop Menu |\n"
            menu_line3 = "|-------------------------------|\n"
            menu_line4 = "| 1) Buy |\n"
            menu_line5 = "| 2) Sell | \n"
            menu_line6 = "| 3) Inventory | \n"
            menu_line7 = "|-------------------------------|\n"
            menu_line8 = f"| Balance - {balance} |\n"
            menu_line9 = " ------------------------------- "

            menu_list = [menu_line1, menu_line2, menu_line3, menu_line4, menu_line5,
                         menu_line6, menu_line7, menu_line8, menu_line9]
            return MenuSprites.ShopMenus.shop_menu_spacing(menu_list, [1, 3, 7, 9])

        shop_menu_buy = None

        @staticmethod
        def shop_menu_sell(item_type: str, item_list: List[Union[WeaponType, ArmourType,
         UnknownWeaponType, UnknownArmourType]]):

            if item_type in ("armour", "weapons"):
                key = item_type.capitalize()

            else:
                raise ThisShouldntComeUp

            menu_list = []
            menu_list.append(" ------------------------------- \n")
            menu_list.append(f"| {key} |\n")
            menu_list.append("|-------------------------------|\n")

            for item in item_list:
                name, value = item.name, item.price
                if name is None and value == 0:
                    continue
                else:
                    menu_list.append(f"| {name} - ${value} |\n")
                    
            menu_list.append(" ------------------------------- \n")
            return MenuSprites.ShopMenus.shop_menu_spacing(menu_list, [1, 3, len(menu_list)])

    load_save_menu = None


class LandscapeSprites:
    main_village = "    888              \n" \
                   "    8888               ____[]\n" \
                   "    888               /    []\\\n" \
                   "   _| |              /     [] \\\n" \
                   " /  | |    ____     /          \\\n" \
                   "/______\\  /    \\     |   __   |\n" \
                   "|  _   |  |    |     |  |  |  | \n" \
                   "| | |  |  | [] |     |  |  |  |  \n" \
                   "You start your adventure in the village"

    mountain = "       /\\         \n" \
               "      /AA\\        \n" \
               "     /-\\/-\\      \n" \
               "    /      \\      \n" \
               "   /        \\     \n" \
               "  /    __    \\    \n" \
               " /    {  }    \\   \n" \
               "/____/    \\____\\ \n"

    mountain_range = "           /\\              \n" \
                     "          /  \\             \n" \
                     "   /\\    /    \\  /\\      \n" \
                     "  /  \\  /      \\/  \\     \n" \
                     " / /\\ \\/       /    \\   \n" \
                     "/ /  \\ \\      /      \\  \n" \
                     " /    \\ \\    /        \\ \n" \
                     "/      \\ \\  /          \\\n"

    mountain_blocked = "       /\\         \n" \
                       "      /AA\\        \n" \
                       "     /-\\/-\\      \n" \
                       "    /      \\      \n" \
                       "   /        \\     \n" \
                       "  /    __    \\    \n" \
                       " /    {OO}    \\   \n" \
                       "/____/OOOO\\____\\ \n"

    forest = "     //\\   8989898      /\\             \n" \
             "  /\\////\\989898989898  //\\\\          \n" \
             "/\\//////\\8989898989898///\\\\\\        \n" \
             "/\\\\///\\/\\\\8989898989 ////\\\\\\\\   \n" \
             "||////\\\\\\\\\\98{ 9}89 /////\\\\\\\\\\ \n" \
             "||  || ||    {  }       ||               \n"
    tree1 = "        \n" \
            "        \n" \
            "        \n" \
            "  ****  \n" \
            " ****** \n" \
            "  ****  \n" \
            "   ||   \n" \
            "___||___\n"

    tree2 = "             \n" \
            "             \n" \
            "   /\\       \n" \
            "  //\\\\     \n" \
            " ///\\\\\\   \n" \
            "////\\\\\\\\ \n" \
            "   ||        \n" \
            "___||___     \n"

    tree2_close = "  /////////\\\\\\\\\\\\\\\\\\     \n" \
                  " //////////\\\\\\\\\\\\\\\\\\\\   \n" \
                  "///////////\\\\\\\\\\\\\\\\\\\\\\ \n" \
                  "        |\\||}|                    \n" \
                  "        ||||||                    \n" \
                  "        {|{|||                    \n" \
                  "        |||||{                    \n" \
                  "________||||]|____________________\n"


class EnemySprites:
    rat_passive = " (\\,/)                   \n" \
                  "  oo   '''//,        _    \n" \
                  ",/_;~,        \\,    / '  \n" \
                  "\"'   \\    (    \\    !  \n" \
                  "      ',|  \\    |__.'    \n" \
                  "      '~  '~----''\"      \n"

    rat_aggressive = "  ,     .             \n" \
                     "  (\\,;,/)            \n" \
                     "!  (o o)\\//,         \n" \
                     "    \\ /     \\,      \n" \
                     "    `+'(  (   \\    ) \n" \
                     "       //  \\   |_./  \n" \
                     "     '~' '~----'      \n"


MenuType = Type[MenuSprites]
InventoryDisplayType = Type[MenuSprites.InventoryMenus]
LandscapeSpriteType = Type[LandscapeSprites]
