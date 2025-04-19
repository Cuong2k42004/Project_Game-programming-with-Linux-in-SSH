#!/bin/bash 
 
# File to store inventory 
INVENTORY_FILE="inventory.txt" 
 
# Function to save inventory to file 
save_inventory() { 
    > $INVENTORY_FILE 
    for item in "${inventory[@]}"; do 
        echo "$item" >> $INVENTORY_FILE 
    done 
} 
 
# Function to load inventory from file 
load_inventory() { 
    if [[ -f $INVENTORY_FILE ]]; then 
        mapfile -t inventory < $INVENTORY_FILE 
    else 
        inventory=() 
    fi 
} 
# Introduction 
echo -e "\033[1;33mWelcome to the Adventure Game!\033[0m" 
echo -e "\033[1;34mPlease choose your character:\033[0m" 
# Function to display character stats in a tabular format 
display_stats() { 
echo -e "\033[1;32m---------------------------------\033[0m" 
printf "\033[1;32m| %-2s | %-10s | %-4s | %-4s | %-4s |\033[0m\n" "ID" "Character" 
"HP" "ATK" "DEF" 
echo -e "\033[1;32m---------------------------------\033[0m" 
printf "\033[1;32m| %-2d | %-10s | %-4d | %-4d | %-4d |\033[0m\n" 1 "Warrior" 100 25 
15 
12 
8 
} 
printf "\033[1;32m| %-2d | %-10s | %-4d | %-4d | %-4d |\033[0m\n" 2 "Mage" 70 25 10 
printf "\033[1;32m| %-2d | %-10s | %-4d | %-4d | %-4d |\033[0m\n" 3 "Archer" 80 30 
printf "\033[1;32m| %-2d | %-10s | %-4d | %-4d | %-4d |\033[0m\n" 4 "Assassin" 75 35 
echo -e "\033[1;32m---------------------------------\033[0m" 
# Display character stats 
display_stats 
# Character selection 
while true; do 
    echo -e "\033[1;36mEnter the ID of your character (1 for Warrior, 2 for Mage, 3 for 
Archer, 4 for Assassin):\033[0m" 
    read character_id 
 
    case $character_id in 
        1) 
            character="Warrior" 
            base_hp=100 
            base_atk=25 
            base_def=15 
            echo -e "\033[1;34mYou have chosen the Warrior.\033[0m" 
            echo -e "\033[1;34mIn the ancient times, a mighty kingdom was attacked by a 
brutal army of monsters. As a warrior trained from a young age to protect the kingdom, 
you vowed to defeat every enemy and protect your homeland. Your journey begins in 
Lucias Forest, where ancient secrets and dangerous enemies await.\033[0m" 
            break 
            ;; 
        2) 
            character="Mage" 
            base_hp=70 
            base_atk=25 
            base_def=10 
            echo -e "\033[1;34mYou have chosen the Mage.\033[0m" 
            echo -e "\033[1;34mYou are a talented mage, who has learned the ancient secrets 
from old tomes. Using your magical powers, you can summon fire, ice, and lightning to 
defeat your enemies. However, the devastation caused by monsters has spread across the 
land, and you decide to use your power to end this chaos. Your journey begins in the 
forest 'The Rising Sun', where you will face magical and dangerous creatures.\033[0m" 
            break 
            ;; 
        3) 
            character="Archer" 
            base_hp=80 
            base_atk=30 
            base_def=12 
            echo -e "\033[1;34mYou have chosen the Archer.\033[0m" 
            echo -e "\033[1;34mAs an exceptional archer, you were once a guard for the 
kingdom. You can hit your targets from a great distance, leaving enemies with no time to 
react. When the monster army attacked, you vowed to use your skills to protect the 
people and defeat the enemies. Your journey begins in the Fortain Forest, where 
tranquility has been disturbed by the appearance of dangerous creatures.\033[0m" 
            break 
            ;; 
        4) 
            character="Assassin" 
            base_hp=75 
            base_atk=35 
            base_def=8 
            echo -e "\033[1;34mYou have chosen the Assassin.\033[0m" 
            echo -e "\033[1;34mAs a master of stealth and precision, you strike from the 
shadows. When the kingdom was attacked, you took it upon yourself to eliminate the 
leaders of the enemy forces. Your journey begins in the Whispering Woods, where 
shadows and silence reign.\033[0m" 
            break 
            ;; 
        *) 
            echo -e "\033[1;31mInvalid ID. Please choose again.\033[0m" 
            ;; 
    esac 
done 
 
echo -e "\033[1;34mYou have chosen the $character.\033[0m" 
 
# Function to set character name 
set_character_name() { 
    while true; do 
        echo -e "\033[1;36mEnter your character's name:\033[0m" 
        read character_name 
 
        if [ -n "$character_name" ]; then 
            break 
        else 
            echo -e "\033[1;31mYou cannot remember your name.\033[0m" 
        fi 
    done 
} 
 
# Set character's name 
set_character_name 
 
# Initialize level and experience 
level=1 
exp=0 
max_level=60 
exp_to_level_up=100 
# Initialize character stats based on level 
hp=$base_hp 
atk=$base_atk 
def=$base_def 
# Backup character stats 
orig_hp=$hp 
orig_atk=$atk 
orig_def=$def 
# Initialize map  
declare -A map  
map["start"]="Starting Room"  
map["north_room"]="Lucias Rainforest"  
map["east_room"]="The Rising Sun Forest"  
map["south_room"]="Misio Cold Forest"  
map["west_room"]="Fortain Forest"  
map["boss_room"]="Boss Lair"  
# Function to display the map  
 
display_map() {  
    local loc  
    echo -e "\033[1;32mMap of the Adventure Game:\033[0m"  
    for loc in "${!map[@]}"; do  
        if [ "$loc" == "$current_location" ]; then  
            echo -e "\033[1;34m* ${map[$loc]} - You are here\033[0m"  
        else  
            echo -e "\033[1;34m- ${map[$loc]}\033[0m"  
        fi  
    done  
    echo  
 
}  
 
# Display character stats in tabular format 
echo -e "\033[1;32m---------------------------------\033[0m" 
printf "\033[1;32m| %-10s | %-4s | %-4s | %-4s |\033[0m\n" "Your stats:" "HP" "ATK" 
"DEF" 
echo -e "\033[1;32m---------------------------------\033[0m" 
printf "\033[1;32m| %-10s | %-4d | %-4d | %-4d |\033[0m\n" "$character_name" "$hp" 
"$atk" "$def" 
echo -e "\033[1;32m---------------------------------\033[0m" 
 
echo -e "\033[1;34mYou find yourself in a mysterious room. And you know you should 
get out of here.\033[0m" 
echo -e "\033[1;34mYou are currently at level $level.\033[0m" 
 
# Load inventory from file 
load_inventory 
 
# Initialize gold 
gold=0 
defeated_monsters=0 
boss_unlocked=false 
boss_attempts=0 
 
# Function to display inventory 
display_inventory() { 
    echo -e "\033[1;32m---------------------------------\033[0m" 
    echo -e "\033[1;34mYour inventory:\033[0m" 
    echo -e "\033[1;32m---------------------------------\033[0m" 
    for item in "${inventory[@]}"; do 
        echo -e "\033[1;34m- $item\033[0m" 
    done 
    echo -e "\033[1;32m---------------------------------\033[0m" 
 
    echo -e "\033[1;36mChoose an action:\033[0m" 
    actions=() 
    for item in "${inventory[@]}"; do 
        case $item in 
            "long sword") 
                actions+=("Equip Long Sword (increase ATK by 15)") 
                ;; 
            "shield") 
                actions+=("Equip Shield (increase DEF by 20)") 
                ;; 
            "dagger") 
                actions+=("Equip Dagger (increase ATK by 10)") 
                ;; 
            "bow") 
                actions+=("Equip Bow (increase ATK by 12)") 
                ;; 
            "magic staff") 
                actions+=("Equip Magic Staff (increase ATK by 20)") 
                ;; 
            "Devil Sword") 
                actions+=("Equip Devil Sword (increase ATK by 50)") 
                ;; 
            "Archangel's Staff") 
                actions+=("Equip Archangel's Staff (increase ATK by 60)") 
                ;; 
            "Light Bow") 
                actions+=("Equip Light Bow (increase ATK by 40)") 
                ;; 
            "Infected Dagger") 
                actions+=("Equip Infected Dagger (increase ATK by 45)") 
                ;; 
            "Persian Sword") 
                actions+=("Equip Persian Sword (increase ATK by 90)") 
                ;; 
            "Supreme Staff") 
                actions+=("Equip Supreme Staff (increase ATK by 90)") 
                ;; 
            "Neos's Bow of Light") 
                actions+=("Equip Neos's Bow of Light (increase ATK by 90)") 
                ;; 
            "Soul Stealing Blade") 
                actions+=("Equip Soul Stealing Blade (increase ATK by 90)") 
                ;; 
            "Health Potion") 
                actions+=("Use Health Potion (restore 5 HP)") 
                ;; 
            "Outstanding Health Potion") 
                actions+=("Use Outstanding Health Potion (restore 60 HP)") 
                ;; 
            "ATK Potion") 
                actions+=("Use ATK Potion (increase ATK by 10 for next battle)") 
                ;; 
            "Supernatural Energy Drink") 
                actions+=("Use Supernatural Energy Drink (increase ATK by 40 for next 
battle)") 
                ;; 
            "Revival Potion") 
                actions+=("Use Revival Potion (revive if HP reaches 0 in next battle)") 
                ;; 
            "Body Armor") 
                actions+=("Equip Body Armor (increase DEF by 25)") 
                ;; 
        esac 
    done 
 
    actions+=("Back to main menu") 
    action_counter=1 
 
    for action in "${actions[@]}"; do 
        echo -e "\033[1;36m$action_counter. $action\033[0m" 
        ((action_counter++)) 
    done 
 
    read choice 
    selected_action=${actions[$((choice-1))]} 
 
    case $selected_action in 
        "Equip Long Sword (increase ATK by 15)") 
            if [[ " ${inventory[@]} " =~ " long sword " ]]; then 
                if [ "$character" == "Warrior" ]; then 
                    echo -e "\033[1;34mYou equipped the long sword.\033[0m" 
                    atk=$((atk + 15)) 
                    inventory=("${inventory[@]/long sword}") 
                    save_inventory 
                else 
                    echo -e "\033[1;31mOnly Warriors can equip the long sword.\033[0m" 
                fi 
            else 
                echo -e "\033[1;31mYou don't have a long sword in your inventory.\033[0m" 
            fi 
            ;; 
        "Equip Shield (increase DEF by 20)") 
            if [[ " ${inventory[@]} " =~ " shield " ]]; then 
                if [ "$character" == "Warrior" ]; then 
                    echo -e "\033[1;34mYou equipped the shield.\033[0m" 
                    def=$((def + 20)) 
                    inventory=("${inventory[@]/shield}") 
                    save_inventory 
                else 
                    echo -e "\033[1;31mOnly Warriors can equip the shield.\033[0m" 
                fi 
            else 
                echo -e "\033[1;31mYou don't have a shield in your inventory.\033[0m" 
            fi 
            ;; 
        "Equip Dagger (increase ATK by 10)") 
            if [[ " ${inventory[@]} " =~ " dagger " ]]; then 
                if [ "$character" == "Assassin" ]; then 
                    echo -e "\033[1;34mYou equipped the dagger.\033[0m" 
                    atk=$((atk + 10)) 
                    inventory=("${inventory[@]/dagger}") 
                    save_inventory 
                else 
                    echo -e "\033[1;31mOnly Assassins can equip the dagger.\033[0m" 
                fi 
            else 
                echo -e "\033[1;31mYou don't have a dagger in your inventory.\033[0m" 
            fi 
            ;; 
        "Equip Bow (increase ATK by 12)") 
            if [[ " ${inventory[@]} " =~ " bow " ]]; then 
                if [ "$character" == "Archer" ]; then 
                    echo -e "\033[1;34mYou equipped the bow.\033[0m" 
                    atk=$((atk + 12)) 
                    inventory=("${inventory[@]/bow}") 
                    save_inventory 
                else 
                    echo -e "\033[1;31mOnly Archers can equip the bow.\033[0m" 
                fi 
            else 
                echo -e "\033[1;31mYou don't have a bow in your inventory.\033[0m" 
            fi 
            ;; 
        "Equip Magic Staff (increase ATK by 20)") 
            if [[ " ${inventory[@]} " =~ " magic staff " ]]; then 
                if [ "$character" == "Mage" ]; then 
                    echo -e "\033[1;34mYou equipped the magic staff.\033[0m" 
                    atk=$((atk + 20)) 
                    inventory=("${inventory[@]/magic staff}") 
                    save_inventory 
                else 
                    echo -e "\033[1;31mOnly Mages can equip the magic staff.\033[0m" 
                fi 
            else 
                echo -e "\033[1;31mYou don't have a magic staff in your inventory.\033[0m" 
            fi 
            ;; 
        "Equip Devil Sword (increase ATK by 50)") 
            if [[ " ${inventory[@]} " =~ " Devil Sword " ]]; then 
                if [ "$character" == "Warrior" ]; then 
                    echo -e "\033[1;34mYou equipped the Devil Sword.\033[0m" 
                    atk=$((atk + 50)) 
                    inventory=("${inventory[@]/Devil Sword}") 
                    save_inventory 
                else 
                    echo -e "\033[1;31mOnly Warriors can equip the Devil Sword.\033[0m" 
                fi 
            else 
                echo -e "\033[1;31mYou don't have a Devil Sword in your inventory.\033[0m" 
            fi 
            ;; 
        "Equip Archangel's Staff (increase ATK by 60)") 
            if [[ " ${inventory[@]} " =~ " Archangel's Staff " ]]; then 
                if [ "$character" == "Mage" ]; then 
                    echo -e "\033[1;34mYou equipped the Archangel's Staff.\033[0m" 
                    atk=$((atk + 60)) 
                    inventory=("${inventory[@]/Archangel's Staff}") 
                    save_inventory 
                else 
                    echo -e "\033[1;31mOnly Mages can equip the Archangel's Staff.\033[0m" 
                fi 
            else 
                echo -e "\033[1;31mYou don't have an Archangel's Staff in your 
inventory.\033[0m" 
            fi 
            ;; 
        "Equip Light Bow (increase ATK by 40)") 
            if [[ " ${inventory[@]} " =~ " Light Bow " ]]; then 
                if [ "$character" == "Archer" ]; then 
                    echo -e "\033[1;34mYou equipped the Light Bow.\033[0m" 
                    atk=$((atk + 40)) 
                    inventory=("${inventory[@]/Light Bow}") 
                    save_inventory 
                else 
                    echo -e "\033[1;31mOnly Archers can equip the Light Bow.\033[0m" 
                fi 
            else 
                echo -e "\033[1;31mYou don't have a Light Bow in your inventory.\033[0m" 
            fi 
            ;; 
        "Equip Infected Dagger (increase ATK by 45)") 
            if [[ " ${inventory[@]} " =~ " Infected Dagger " ]]; then 
                if [ "$character" == "Assassin" ]; then 
                    echo -e "\033[1;34mYou equipped the Infected Dagger.\033[0m" 
                    atk=$((atk + 45)) 
                    inventory=("${inventory[@]/Infected Dagger}") 
                    save_inventory 
                else 
                    echo -e "\033[1;31mOnly Assassins can equip the Infected Dagger.\033[0m" 
                fi 
            else 
                echo -e "\033[1;31mYou don't have an Infected Dagger in your 
inventory.\033[0m" 
            fi 
            ;; 
        "Equip Persian Sword (increase ATK by 90)") 
            if [[ " ${inventory[@]} " =~ " Persian Sword " ]]; then 
                if [ "$character" == "Warrior" ]; then 
                    echo -e "\033[1;34mYou equipped the Persian Sword.\033[0m" 
                    atk=$((atk + 90)) 
                    inventory=("${inventory[@]/Persian Sword}") 
                    save_inventory 
                else 
                    echo -e "\033[1;31mOnly Warriors can equip the Persian Sword.\033[0m" 
                fi 
            else 
                echo -e "\033[1;31mYou don't have a Persian Sword in your 
inventory.\033[0m" 
            fi 
            ;; 
        "Equip Supreme Staff (increase ATK by 90)") 
            if [[ " ${inventory[@]} " =~ " Supreme Staff " ]]; then 
                if [ "$character" == "Mage" ]; then 
                    echo -e "\033[1;34mYou equipped the Supreme Staff.\033[0m" 
                    atk=$((atk + 90)) 
                    inventory=("${inventory[@]/Supreme Staff}") 
                    save_inventory 
                else 
                    echo -e "\033[1;31mOnly Mages can equip the Supreme Staff.\033[0m" 
                fi 
            else 
                echo -e "\033[1;31mYou don't have a Supreme Staff in your 
inventory.\033[0m" 
            fi 
            ;; 
        "Equip Neos's Bow of Light (increase ATK by 90)") 
            if [[ " ${inventory[@]} " =~ " Neos's Bow of Light " ]]; then 
                if [ "$character" == "Archer" ]; then 
                    echo -e "\033[1;34mYou equipped Neos's Bow of Light.\033[0m" 
                    atk=$((atk + 90)) 
                    inventory=("${inventory[@]/Neos's Bow of Light}") 
                    save_inventory 
                else 
                    echo -e "\033[1;31mOnly Archers can equip the Neos's Bow of 
Light.\033[0m" 
                fi 
            else 
                echo -e "\033[1;31mYou don't have a Neos's Bow of Light in your 
inventory.\033[0m" 
            fi 
            ;; 
        "Equip Soul Stealing Blade (increase ATK by 90)") 
            if [[ " ${inventory[@]} " =~ " Soul Stealing Blade " ]]; then 
                if [ "$character" == "Assassin" ]; then 
                    echo -e "\033[1;34mYou equipped the Soul Stealing Blade.\033[0m" 
                    atk=$((atk + 90)) 
                    inventory=("${inventory[@]/Soul Stealing Blade}") 
                    save_inventory 
                else 
                    echo -e "\033[1;31mOnly Assassins can equip the Soul Stealing 
Blade.\033[0m" 
                fi 
            else 
                echo -e "\033[1;31mYou don't have a Soul Stealing Blade in your 
inventory.\033[0m" 
            fi 
            ;; 
        "Use Health Potion (restore 5 HP)") 
            if [[ " ${inventory[@]} " =~ " Health Potion " ]]; then 
                echo -e "\033[1;34mYou used a Health Potion.\033[0m" 
                hp=$((hp + 5)) 
                inventory=("${inventory[@]/Health Potion}") 
                save_inventory 
            else 
                echo -e "\033[1;31mYou don't have a Health Potion in your inventory.\033[0m" 
            fi 
            ;; 
        "Use Outstanding Health Potion (restore 60 HP)") 
            if [[ " ${inventory[@]} " =~ " Outstanding Health Potion " ]]; then 
                echo -e "\033[1;34mYou used an Outstanding Health Potion.\033[0m" 
                hp=$((hp + 60)) 
                inventory=("${inventory[@]/Outstanding Health Potion}") 
                save_inventory 
            else 
                echo -e "\033[1;31mYou don't have an Outstanding Health Potion in your 
inventory.\033[0m" 
            fi 
            ;; 
        "Use ATK Potion (increase ATK by 10 for next battle)") 
            if [[ " ${inventory[@]} " =~ " ATK Potion " ]]; then 
                echo -e "\033[1;34mYou used an ATK Potion.\033[0m" 
                atk=$((atk + 10)) 
                inventory=("${inventory[@]/ATK Potion}") 
                save_inventory 
            else 
                echo -e "\033[1;31mYou don't have an ATK Potion in your inventory.\033[0m" 
            fi 
            ;; 
        "Use Supernatural Energy Drink (increase ATK by 40 for next battle)") 
            if [[ " ${inventory[@]} " =~ " Supernatural Energy Drink " ]]; then 
                echo -e "\033[1;34mYou used a Supernatural Energy Drink.\033[0m" 
                atk=$((atk + 40)) 
                inventory=("${inventory[@]/Supernatural Energy Drink}") 
                save_inventory 
            else 
                echo -e "\033[1;31mYou don't have a Supernatural Energy Drink in your 
inventory.\033[0m" 
            fi 
            ;; 
        "Use Revival Potion (revive if HP reaches 0 in next battle)") 
            if [[ " ${inventory[@]} " =~ " Revival Potion " ]]; then 
                echo -e "\033[1;34mYou used a Revival Potion.\033[0m" 
                revival_potion=true 
                inventory=("${inventory[@]/Revival Potion}") 
                save_inventory 
            else 
                echo -e "\033[1;31mYou don't have a Revival Potion in your 
inventory.\033[0m" 
            fi 
            ;; 
        "Equip Body Armor (increase DEF by 25)") 
            if [[ " ${inventory[@]} " =~ " Body Armor " ]]; then 
                echo -e "\033[1;34mYou equipped the Body Armor.\033[0m" 
                def=$((def + 25)) 
                inventory=("${inventory[@]/Body Armor}") 
                save_inventory 
            else 
                echo -e "\033[1;31mYou don't have a Body Armor in your inventory.\033[0m" 
            fi 
            ;; 
        "Back to main menu") 
            return 
            ;; 
        *) 
            echo -e "\033[1;31mInvalid choice.\033[0m" 
            ;; 
    esac 
} 
 
# Function to pick up items 
pick_up_item() { 
    item=$1 
    echo -e "\033[1;36mYou found a $item! Do you want to pick it up? (yes/no)\033[0m" 
    read pick_up 
    if [ "$pick_up" == "yes" ]; then 
        inventory+=("$item") 
        save_inventory 
        echo -e "\033[1;34mYou picked up the $item.\033[0m" 
    else 
        echo -e "\033[1;34mYou left the $item behind.\033[0m" 
    fi 
} 
 
# Function to describe the current location 
describe_location() { 
    case $1 in 
        "start") 
            echo -e "\033[1;34mYou are in the starting room. There are doors to the north, 
south, east, and west.\033[0m" 
            ;; 
        "north_room") 
            echo -e "\033[1;34mWelcome to Lucias Rainforest. In this area you will feel the 
hot, harsh atmosphere along with dangerous monsters.\033[0m" 
            ;; 
        "east_room") 
            echo -e "\033[1;34mWelcome to the eastern forest called 'The Rising Sun'. In this 
area you will experience magical and amazing creatures.\033[0m" 
            ;; 
        "south_room") 
            echo -e "\033[1;34mWelcome to the cold forest of Misio. Here you will feel the 
cold snow surrounding the forest.\033[0m" 
            ;; 
        "west_room") 
            echo -e "\033[1;34mWelcome to the western forest called Fortain. Here, you will 
feel the cool, peaceful feeling but no less dangerous creatures.\033[0m" 
            ;; 
        "boss_room") 
            echo -e "\033[1;34mYou have entered the boss's lair. Prepare for the final 
battle!\033[0m" 
            ;; 
        "shop") 
            echo -e "\033[1;34mYou have entered Furina's shop.\033[0m" 
            shop 
            ;; 
        *) 
            echo -e "\033[1;31mYou are lost.\033[0m" 
            ;; 
    esac 
} 
 
# Initialize list of defeated monsters with count 
declare -A defeated_monsters_list 
 
# Function to display defeated monsters 
display_defeated_monsters() { 
    echo -e "\033[1;32m---------------------------------\033[0m" 
    echo -e "\033[1;34mDefeated Monsters:\033[0m" 
    echo -e "\033[1;32m---------------------------------\033[0m" 
    for monster in "${!defeated_monsters_list[@]}"; do 
        echo -e "\033[1;34m- $monster (x${defeated_monsters_list[$monster]})\033[0m" 
    done 
    echo -e "\033[1;32m---------------------------------\033[0m" 
} 
 
# Function to handle monster encounters 
encounter_monster() { 
    monsters=("goblin" "slime" "ghost" "dragon" "lightcrusher" "spearback") 
    monster=${monsters[$((RANDOM % ${#monsters[@]}))]} 
    case $monster in 
        "goblin") 
            figlet "Goblin" | lolcat 
            echo -e "\033[1;31mA wild Goblin appears!\033[0m" 
            echo -e "\033[1;32m---------------------------------\033[0m" 
            printf "\033[1;32m| %-10s | %-4s | %-4s | %-4s |\033[0m\n" "Goblin" "HP" 
"ATK" "DEF" 
            echo -e "\033[1;32m---------------------------------\033[0m" 
            printf "\033[1;32m| %-10s | %-4d | %-4d | %-4d |\033[0m\n" "Goblin" 30 15 5 
            echo -e "\033[1;32m---------------------------------\033[0m" 
            monster_hp=30 
            monster_atk=15 
            monster_def=5 
            exp_gain=20 
            ;; 
        "slime") 
            figlet "Slime" | lolcat 
            echo -e "\033[1;31mA slimy Slime appears!\033[0m" 
            echo -e "\033[1;32m---------------------------------\033[0m" 
            printf "\033[1;32m| %-10s | %-4s | %-4s | %-4s |\033[0m\n" "Slime" "HP" "ATK" 
"DEF" 
            echo -e "\033[1;32m---------------------------------\033[0m" 
            printf "\033[1;32m| %-10s | %-4d | %-4d | %-4d |\033[0m\n" "Slime" 20 10 3 
            echo -e "\033[1;32m---------------------------------\033[0m" 
            monster_hp=20 
            monster_atk=10 
            monster_def=3 
            exp_gain=20 
            ;; 
        "ghost") 
            figlet "Ghost" | lolcat 
            echo -e "\033[1;31mA spooky Ghost appears!\033[0m" 
            echo -e "\033[1;32m---------------------------------\033[0m" 
            printf "\033[1;32m| %-10s | %-4s | %-4s | %-4s |\033[0m\n" "Ghost" "HP" "ATK" 
"DEF" 
            echo -e "\033[1;32m---------------------------------\033[0m"  
            printf "\033[1;32m| %-10s | %-4s | %-4s | %-4s |\033[0m\n" "Ghost" 40 20 10 
            echo -e "\033[1;32m---------------------------------\033[0m" 
            monster_hp=40 
            monster_atk=20 
            monster_def=10 
            exp_gain=30 
            ;; 
        "dragon") 
            figlet "Dragon" | lolcat 
            echo -e "\033[1;31mA fierce Dragon appears!\033[0m" 
            echo -e "\033[1;32m---------------------------------\033[0m" 
            printf "\033[1;32m| %-10s | %-4s | %-4s | %-4s |\033[0m\n" "Dragon" "HP" 
"ATK" "DEF" 
            echo -e "\033[1;32m---------------------------------\033[0m" 
            printf "\033[1;32m| %-10s | %-4d | %-4d | %-4d |\033[0m\n" "Dragon" 80 30 27 
            echo -e "\033[1;32m---------------------------------\033[0m" 
            monster_hp=80 
            monster_atk=30 
            monster_def=27 
            exp_gain=60 
            ;; 
        "lightcrusher") 
            figlet "Lightcrusher" | lolcat 
            echo -e "\033[1;31mA wild Lightcrusher appears!\033[0m" 
            echo -e "\033[1;32m---------------------------------\033[0m" 
            printf "\033[1;32m| %-10s | %-4s | %-4s | %-4s |\033[0m\n" "Lightcrusher" "HP" 
"ATK" "DEF" 
            echo -e "\033[1;32m---------------------------------\033[0m" 
            printf "\033[1;32m| %-10s | %-4s | %-4s | %-4s |\033[0m\n" "Lightcrusher" 40 20 
15 
            echo -e "\033[1;32m---------------------------------\033[0m"  
            monster_hp=40  
            monster_atk=20 
            monster_def=15 
            exp_gain=30 
            ;; 
        "spearback") 
            figlet "Spearback" | lolcat 
            echo -e "\033[1;31mA wild Spearback appears!\033[0m" 
            echo -e "\033[1;32m---------------------------------\033[0m" 
            printf "\033[1;32m| %-10s | %-4s | %-4s | %-4s |\033[0m\n" "Spearback" "HP" 
"ATK" "DEF" 
            echo -e "\033[1;32m---------------------------------\033[0m" 
            printf "\033[1;32m| %-10s | %-4d | %-4d | %-4d |\033[0m\n" "Spearback" 35 15 
20 
            echo -e "\033[1;32m---------------------------------\033[0m" 
            monster_hp=35 
            monster_atk=15 
            monster_def=20 
            exp_gain=30 
            ;; 
        *) 
            echo -e "\033[1;31mNothing here.\033[0m" 
            ;; 
    esac 
    battle 
} 
 
# Function to handle the boss encounter 
encounter_boss() { 
    figlet "Jué" | lolcat 
    echo -e "\033[1;31mA mighty Jué appears!\033[0m" 
    echo -e "\033[1;32m---------------------------------\033[0m" 
    printf "\033[1;32m| %-10s | %-4s | %-4s | %-4s |\033[0m\n" "Jué" "HP" "ATK" "DEF" 
    echo -e "\033[1;32m---------------------------------\033[0m" 
    printf "\033[1;32m| %-10s | %-4d | %-4d | %-4d |\033[0m\n" "Jué" 120 80 50 
    echo -e "\033[1;32m---------------------------------\033[0m" 
    monster_hp=120 
    monster_atk=80 
    monster_def=50 
    exp_gain=100 
    battle 
    if [ $monster_hp -le 0 ]; then 
        echo -e "\033[1;32mCongratulation. You are completing all the challenges. Thanks 
for playing our game \033[0m" 
        exit 0 
    fi 
} 
 
# Function to handle battle 
battle() { 
    while [ $hp -gt 0 ] && [ $monster_hp -gt 0 ]; do 
        while true; do 
            echo -e "\033[1;36mChoose your action: (1. Attack, 2. Defend, 3. Open Inventory, 
4. Dodge, 5. Escape)\033[0m" 
            read action 
            case $action in 
                1) 
                    damage=$((atk - monster_def)) 
                    if [ $damage -lt 0 ]; then 
                        damage=0 
                    fi 
                    monster_hp=$((monster_hp - damage)) 
                    if [ $monster_hp -lt 0 ]; then 
                        monster_hp=0 
                    fi 
                    echo -e "\033[1;34mYou dealt $damage damage to the monster. Monster HP: 
$monster_hp\033[0m" 
 
                    if [ $monster_hp -gt 0 ]; then 
                        damage=$((monster_atk - def)) 
                        if [ $damage -lt 0 ]; then 
                            damage=0 
                        fi 
                        hp=$((hp - damage)) 
                        if [ $hp -lt 0 ]; then 
                            hp=0 
                        fi 
                        echo -e "\033[1;31mThe monster dealt $damage damage to you. Your HP: 
$hp\033[0m" 
                    fi 
                    break 
                    ;; 
                2) 
                    if [ $monster_hp -gt 0 ]; then 
                        reduced_damage=$((monster_atk - (def * 2))) 
                        if [ $reduced_damage -lt 0 ]; then 
                            reduced_damage=0 
                        fi 
                        hp=$((hp - reduced_damage)) 
                        if [ $hp -lt 0 ]; then 
                            hp=0 
                        fi 
                        echo -e "\033[1;34mYou defended and reduced the damage. The monster 
dealt $reduced_damage damage to you. Your HP: $hp\033[0m" 
                    else 
                        echo -e "\033[1;34mThe monster is already defeated!\033[0m" 
                    fi 
                    break 
                    ;; 
                3) 
                    display_inventory 
                    ;; 
                4) 
                    if [ $monster_hp -gt 0 ]; then 
                        echo -e "\033[1;34mYou chose to dodge, the monster misses its 
attack.\033[0m" 
                    else 
                        echo -e "\033[1;34mThe monster is already defeated!\033[0m" 
                    fi 
                    break 
                    ;; 
                5) 
                    echo -e "\033[1;34mYou chose to escape from the battle.\033[0m" 
                    return 
                    ;; 
                *) 
                    echo -e "\033[1;31mInvalid action. Please re-enter.\033[0m" 
                    ;; 
            esac 
        done 
 
        if [ $monster_hp -le 0 ]; then 
            echo -e "\033[1;32mYou defeated the monster!\033[0m" 
            defeated_monsters_list["$monster"]=$((defeated_monsters_list["$monster"] + 1)) 
            display_defeated_monsters 
            drop_items=("Health Potion" "long sword" "shield" "dagger" "bow" "magic 
staff") 
            drop_item=${drop_items[$((RANDOM % ${#drop_items[@]}))]} 
            pick_up_item "$drop_item" 
 
            # Add gold based on monster type 
            case $monster in 
                "goblin") 
                    gold_earned=$((RANDOM % 3 + 5)) 
                    ;; 
                "slime") 
                    gold_earned=$((RANDOM % 3 + 3)) 
                    ;; 
                "ghost") 
                    gold_earned=$((RANDOM % 3 + 7)) 
                    ;; 
                "dragon") 
                    gold_earned=$((RANDOM % 21 + 20)) 
                    ;; 
                "lightcrusher") 
                    gold_earned=$((RANDOM % 6 + 7)) 
                    ;; 
                "spearback") 
                    gold_earned=$((RANDOM % 6 + 7)) 
                    ;; 
                "Jué") 
                    gold_earned=0 
                    ;; 
            esac 
            gold=$((gold + gold_earned)) 
            echo -e "\033[1;32mYou earned $gold_earned gold! You now have $gold 
gold.\033[0m" 
             
            # Gain experience 
            if [ $level -lt $max_level ]; then 
                exp=$((exp + exp_gain)) 
                echo -e "\033[1;32mYou gained $exp_gain EXP! You now have $exp 
EXP.\033[0m" 
                while [ $exp -ge $exp_to_level_up ] && [ $level -lt $max_level ]; do 
                    exp=$((exp - $exp_to_level_up)) 
                    level=$((level + 1)) 
                    exp_to_level_up=$((exp_to_level_up + 100)) 
                    echo -e "\033[1;32mCongratulations! You leveled up to level 
$level!\033[0m" 
                    hp=$((hp + 10)) 
                    atk=$((atk + 10)) 
                    def=$((def + 5)) 
 
                    # Update original stats to include new level 
                    orig_hp=$hp 
                    orig_atk=$atk 
                    orig_def=$def 
                done 
                echo -e "\033[1;34mYou are currently at level $level.\033[0m" 
                echo -e "\033[1;34mCurrent stats: HP=$hp, ATK=$atk, DEF=$def\033[0m" 
            else 
                echo -e "\033[1;34mYou have max level already.\033[0m" 
            fi 
 
            # Check if 6 types of monsters have been defeated 
            monster_types_defeated=0 
            for monster in "${!defeated_monsters_list[@]}"; do 
                if [ ${defeated_monsters_list[$monster]} -ge 1 ]; then 
                    ((monster_types_defeated++)) 
                fi 
            done 
 
            if [ $monster_types_defeated -ge 6 ] && [ "$boss_unlocked" = false ]; then 
                echo -e "\033[1;34mYou have unlocked the boss area!\033[0m" 
                boss_unlocked=true 
            fi 
 
            # Random chance to open Clorinde's shop 
            if [ $level -ge 2 ] && [ $((RANDOM % 100)) -le 45 ]; then 
                echo -e "\033[1;36mDo you want to visit Furina's shop or Clorinde's shop? (1. 
Furina's shop, 2. Clorinde's shop)\033[0m" 
                read shop_choice 
                case $shop_choice in 
                    1) 
                        shop 
                        ;; 
                    2) 
                        clorinde_shop 
                        ;; 
                    *) 
                        echo -e "\033[1;31mInvalid choice. Visiting Furina's shop by 
default.\033[0m" 
                        shop 
                        ;; 
                esac 
            else 
                # Ask if player wants to visit the shop after each battle 
                echo -e "\033[1;36mDo you want to visit the shop? (yes/no)\033[0m" 
                read visit_shop 
                if [ "$visit_shop" == "yes" ]; then 
                    shop 
                fi 
            fi 
 
            # Increase player stats randomly 
            hp_gain=$((RANDOM % 6 + 5)) 
            hp=$((hp + hp_gain)) 
            echo -e "\033[1;32mYou gained $hp_gain HP, after defeating the 
monster!\033[0m" 
            echo -e "\033[1;34mCurrent stats: HP=$hp, ATK=$atk, DEF=$def\033[0m" 
 
            break 
        elif [ $hp -le 0 ]; then 
            if [[ " ${inventory[@]} " =~ " Revival Potion " ]]; then 
                echo -e "\033[1;34mYou have been revived by the Revival Potion!\033[0m" 
                hp=100 
                inventory=("${inventory[@]/Revival Potion}") 
                save_inventory 
                echo -e "\033[1;31mNow you have 100 HP.\033[0m" 
            else 
                echo -e "\033[1;31mYou have been defeated by the monster. Game 
Over.\033[0m" 
                exit 0 
            fi 
        fi 
    done 
} 
 
# Function to handle player movement 
move() {  
    local direction=$1  
    if [ "$direction" = "boss" ]; then  
 
        if [ "$boss_unlocked" = true ]; then  
            current_location="boss_room"  
        else  
            echo -e "\033[1;31mYou need to farm at least 6 types of monsters in 4 areas to be 
able to open this BOSS area.\033[0m"  
            return  
        fi  
    else  
        case $direction in  
            "north")  
                current_location="north_room"  
                ;;  
            "south")  
                current_location="south_room"  
                ;;  
            "east")  
                current_location="east_room"  
                ;;  
            "west")  
                current_location="west_room"  
                ;;  
            *)  
                echo -e "\033[1;31mInvalid direction. Please choose again.\033[0m"  
                return  
                ;;  
        esac  
    fi  
 
    describe_location "$current_location"  
    display_map # Call the display_map function to show current location  
    if [ "$current_location" = "boss_room" ]; then  
        encounter_boss  
    else  
        encounter_monster  
    fi  
}  
 
# Function for Furina's shop 
shop() { 
    echo -e "\033[1;34mWelcome to Furina's shop! What would you like to buy?\033[0m" 
    while true; do 
        echo -e "\033[1;32m---------------------------------\033[0m" 
        echo -e "\033[1;34m1. Health Potion (+5 HP) - 7 gold\033[0m" 
        echo -e "\033[1;34m2. ATK Potion (+10 ATK) - 20 gold\033[0m" 
        echo -e "\033[1;34m3. Revival Potion - 200 gold\033[0m" 
        echo -e "\033[1;34m4. Devil Sword (increase ATK by 50, Warrior only) - 65 
gold\033[0m" 
        echo -e "\033[1;34m5. Archangel's Staff (increase ATK by 60, Mage only) - 75 
gold\033[0m" 
        echo -e "\033[1;34m6. Light Bow (increase ATK by 40, Archer only) - 60 
gold\033[0m" 
        echo -e "\033[1;34m7. Infected Dagger (increase ATK by 45, Assassin only) - 63 
gold\033[0m" 
        echo -e "\033[1;34m8. Exit shop\033[0m" 
        echo -e "\033[1;32m---------------------------------\033[0m" 
        read choice 
        case $choice in 
            1) 
                if (("$gold" >= 7)); then 
                    gold=$((gold - 7)) 
                    inventory+=("Health Potion") 
                    save_inventory 
                    echo -e "\033[1;34mYou bought a Health Potion. You have $gold gold 
left.\033[0m" 
                else 
                    echo -e "\033[1;31mNot enough gold.\033[0m" 
                fi 
                ;; 
            2) 
                if (("$gold" >= 20)); then 
                    gold=$((gold - 20)) 
                    inventory+=("ATK Potion") 
                    save_inventory 
                    echo -e "\033[1;34mYou bought an ATK Potion. You have $gold gold 
left.\033[0m" 
                else 
                    echo -e "\033[1;31mNot enough gold.\033[0m" 
                fi 
                ;; 
            3) 
                if (("$gold" >= 200)); then 
                    gold=$((gold - 200)) 
                    inventory+=("Revival Potion") 
                    save_inventory 
                    echo -e "\033[1;34mYou bought a Revival Potion. You have $gold gold 
left.\033[0m" 
                else 
                    echo -e "\033[1;31mNot enough gold.\033[0m" 
                fi 
                ;; 
            4) 
                if (("$gold" >= 65)); then 
                    if [ "$character" == "Warrior" ]; then 
                        gold=$((gold - 65)) 
                        inventory+=("Devil Sword") 
                        save_inventory 
                        echo -e "\033[1;34mYou bought a Devil Sword. You have $gold gold 
left.\033[0m" 
                    else 
                        echo -e "\033[1;31mOnly Warriors can buy the Devil Sword.\033[0m" 
                    fi 
                else 
                    echo -e "\033[1;31mNot enough gold.\033[0m" 
                fi 
                ;; 
            5) 
                if (("$gold" >= 75)); then 
                    if [ "$character" == "Mage" ]; then 
                        gold=$((gold - 75)) 
                        inventory+=("Archangel's Staff") 
                        save_inventory 
                        echo -e "\033[1;34mYou bought an Archangel's Staff. You have $gold gold 
left.\033[0m" 
                    else 
                        echo -e "\033[1;31mOnly Mages can buy the Archangel's Staff.\033[0m" 
                    fi 
                else 
                    echo -e "\033[1;31mNot enough gold.\033[0m" 
                fi 
                ;; 
            6) 
                if (("$gold" >= 60)); then 
                    if [ "$character" == "Archer" ]; then 
                        gold=$((gold - 60)) 
                        inventory+=("Light Bow") 
                        save_inventory 
                        echo -e "\033[1;34mYou bought a Light Bow. You have $gold gold 
left.\033[0m" 
                    else 
                        echo -e "\033[1;31mOnly Archers can buy the Light Bow.\033[0m" 
                    fi 
                else 
                    echo -e "\033[1;31mNot enough gold.\033[0m" 
                fi 
                ;; 
            7) 
                if (("$gold" >= 63)); then 
                    if [ "$character" == "Assassin" ]; then 
                        gold=$((gold - 63)) 
                        inventory+=("Infected Dagger") 
                        save_inventory 
                        echo -e "\033[1;34mYou bought an Infected Dagger. You have $gold gold 
left.\033[0m" 
                    else 
                        echo -e "\033[1;31mOnly Assassins can buy the Infected Dagger.\033[0m" 
                    fi 
                else 
                    echo -e "\033[1;31mNot enough gold.\033[0m" 
                fi 
                ;; 
            8) 
                echo -e "\033[1;34mThanks for visiting Furina's shop!\033[0m" 
                break 
                ;; 
            *) 
                echo -e "\033[1;31mInvalid choice. Please choose again.\033[0m" 
                ;; 
        esac 
    done 
} 
 
# Function for Clorinde's shop 
clorinde_shop() { 
    echo -e "\033[1;34mWelcome to Clorinde's shop! What would you like to 
buy?\033[0m" 
    while true; do 
        echo -e "\033[1;32m---------------------------------\033[0m" 
        echo -e "\033[1;34m1. Outstanding Health Potion (+60 HP) - 30 gold\033[0m" 
        echo -e "\033[1;34m2. Supernatural Energy Drink (+40 ATK) - 40 gold\033[0m" 
        echo -e "\033[1;34m3. Body Armor (+25 DEF) - 40 gold\033[0m" 
        echo -e "\033[1;34m4. Persian Sword (increase ATK by 90, Warrior only) - 100 
gold\033[0m" 
        echo -e "\033[1;34m5. Supreme Staff (increase ATK by 90, Mage only) - 100 
gold\033[0m" 
        echo -e "\033[1;34m6. Neos's Bow of Light (increase ATK by 90, Archer only) - 100 
gold\033[0m" 
        echo -e "\033[1;34m7. Soul Stealing Blade (increase ATK by 90, Assassin only) - 
100 gold\033[0m" 
        echo -e "\033[1;34m8. Exit shop\033[0m" 
        echo -e "\033[1;32m---------------------------------\033[0m" 
        read choice 
        case $choice in 
            1) 
                if (("$gold" >= 30)); then 
                    gold=$((gold - 30)) 
                    inventory+=("Outstanding Health Potion") 
                    save_inventory 
                    echo -e "\033[1;34mYou bought an Outstanding Health Potion. You have 
$gold gold left.\033[0m" 
                else 
                    echo -e "\033[1;31mNot enough gold.\033[0m" 
                fi 
                ;; 
            2) 
                if (("$gold" >= 40)); then 
                    gold=$((gold - 40)) 
                    inventory+=("Supernatural Energy Drink") 
                    save_inventory 
                    echo -e "\033[1;34mYou bought a Supernatural Energy Drink. You have 
$gold gold left.\033[0m" 
                else 
                    echo -e "\033[1;31mNot enough gold.\033[0m" 
                fi 
                ;; 
            3) 
                if (("$gold" >= 40)); then 
                    gold=$((gold - 40)) 
                    inventory+=("Body Armor") 
                    save_inventory 
                    echo -e "\033[1;34mYou bought Body Armor. You have $gold gold 
left.\033[0m" 
                else 
                    echo -e "\033[1;31mNot enough gold.\033[0m" 
                fi 
                ;; 
            4) 
                if (("$gold" >= 100)); then 
                    if [ "$character" == "Warrior" ]; then 
                        gold=$((gold - 100)) 
                        inventory+=("Persian Sword") 
                        save_inventory 
                        echo -e "\033[1;34mYou bought a Persian Sword. You have $gold gold 
left.\033[0m" 
                    else 
                        echo -e "\033[1;31mOnly Warriors can buy the Persian Sword.\033[0m" 
                    fi 
                else 
                    echo -e "\033[1;31mNot enough gold.\033[0m" 
                fi 
                ;; 
            5) 
                if (("$gold" >= 100)); then 
                    if [ "$character" == "Mage" ]; then 
                        gold=$((gold - 100)) 
                        inventory+=("Supreme Staff") 
                        save_inventory 
                        echo -e "\033[1;34mYou bought a Supreme Staff. You have $gold gold 
left.\033[0m" 
                    else 
                        echo -e "\033[1;31mOnly Mages can buy the Supreme Staff.\033[0m" 
                    fi 
                else 
                    echo -e "\033[1;31mNot enough gold.\033[0m" 
                fi 
                ;; 
            6) 
                if (("$gold" >= 100)); then 
                    if [ "$character" == "Archer" ]; then 
                        gold=$((gold - 100)) 
                        inventory+=("Neos's Bow of Light") 
                        save_inventory 
                        echo -e "\033[1;34mYou bought a Neos's Bow of Light. You have $gold 
gold left.\033[0m" 
                    else 
                        echo -e "\033[1;31mOnly Archers can buy the Neos's Bow of 
Light.\033[0m" 
                    fi 
                else 
                    echo -e "\033[1;31mNot enough gold.\033[0m" 
                fi 
                ;; 
            7) 
                if (("$gold" >= 100)); then 
                    if [ "$character" == "Assassin" ]; then 
                        gold=$((gold - 100)) 
                        inventory+=("Soul Stealing Blade") 
                        save_inventory 
                        echo -e "\033[1;34mYou bought a Soul Stealing Blade. You have $gold 
gold left.\033[0m" 
                    else 
                        echo -e "\033[1;31mOnly Assassins can buy the Soul Stealing 
Blade.\033[0m" 
                    fi 
                else 
                    echo -e "\033[1;31mNot enough gold.\033[0m" 
                fi 
                ;; 
            8) 
                echo -e "\033[1;34mThanks for visiting Clorinde's shop!\033[0m" 
                break 
                ;; 
            *) 
                echo -e "\033[1;31mInvalid choice. Please choose again.\033[0m" 
                ;; 
        esac 
    done 
} 
 
# Function to receive a buff 
receive_buff() { 
    random_number=$((RANDOM % 100 + 1)) 
    if [ $random_number -le 45 ]; then 
        buff_type=$((RANDOM % 3 + 1)) 
        buff_value=$((RANDOM % 6 + 5)) 
        case $buff_type in 
            1) 
                hp=$((hp + buff_value)) 
                echo -e "\033[1;32mYou received a buff! HP increased by 
$buff_value.\033[0m" 
                ;; 
        esac 
    elif [ $random_number -le 75 ]; then 
        gold_received=$((RANDOM % 21 + 20)) 
        gold=$((gold + gold_received)) 
        echo -e "\033[1;32mYou received a gold buff! You gained $gold_received 
gold.\033[0m" 
    elif [ $random_number -le 85 ]; then 
        inventory+=("Revival Potion") 
        save_inventory 
        echo -e "\033[1;32mYou received a Revival Potion!\033[0m" 
    else 
        echo -e "\033[1;31mYou get nothing.\033[0m" 
    fi 
} 
 
# Initialize starting location 
location="start" 
describe_location "$location" 
 
# Main game loop 
while true; do 
    echo -e "\033[1;36mWhere do you want to move? (north, south, east, west, 
boss)\033[0m" 
    read direction 
 
    move "$direction" 
    while [ $? -ne 0 ]; do 
        echo -e "\033[1;36mWhere do you want to move? (north, south, east, west, 
boss)\033[0m" 
        read direction 
        move "$direction" 
    done 
 
    echo -e "\033[1;36mDo you want to continue exploring? (yes/no)\033[0m" 
    read continue_exploring 
 
    if [ "$continue_exploring" != "yes" ]; then 
        echo -e "\033[1;34mThanks for playing!\033[0m" 
break 
fi 
done