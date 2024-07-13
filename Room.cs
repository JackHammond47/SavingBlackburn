
using System.ComponentModel;

class Room
{
    //room types: 0 = "monster", 1 = "treasure", 2 = "trap", 3 = "boss", 4 = "trader", 5 = "artifact"
    public List<Creature> Creatures;
    public bool Victory = false;
    public Inventory Inventory;
    public Player Player;
    public int RoomType {get; set;}
    public Trader? Trader {get; set;}
    public Room(Player player)
    {
        Random random= new();
        Player = player;
        Inventory = player.Inventory;
        //next(int, int) includes min, excludes max
        Creatures= new();
        RoomType = random.Next(0, 6);
        if (RoomType == 0)
        {
            //Monster Room
            int monsterType = random.Next(0,7);
            //add multiple creatures if less dangerous
            Creatures.Add(new Monster(monsterType));
        }
        else if (RoomType == 1)
        {
            //Treasure
            Console.WriteLine("The next room is peaceful and bright");
            Console.WriteLine("You find a small chest of gold and feel your wounds start to close.");
            Inventory.Gold += 20;
            Player.CharacterClass.Health += 10;
        }
        else if (RoomType == 2)
        {
            //Trap
            Console.WriteLine("You walk into a room and spikes shoot out of the walls!");
            Player.CharacterClass.Health -= 5;
        }
        else if (RoomType == 3)
        {
            //Boss
            Creatures.Add(new Boss(random.Next(7, 10)));
        }
        else if (RoomType == 4)
        {
            //Trader
            Trader = new Trader(Player);
        }
        else 
        {
            //Artifact
            //if bosses key, vicotry = true, else =false
            Key dragonKey = new Key(4);
            Key beholderKey = new Key(5);
            Key mindflayerKey = new Key(6);
            Console.WriteLine("There is a large doorway with three keyslots, one with a dragon head, one with an eye, and one with a squid.");
            if (Inventory.Items.Contains(dragonKey) && Inventory.Items.Contains(beholderKey) && Inventory.Items.Contains(mindflayerKey))
            {
                Victory = true;
                Console.WriteLine("You have won!!");
            }
            else
            {
                Victory = false;
                Console.WriteLine("Come back when you have all three keys...");
            }
        }
    }
    //monster rooms, treasure rooms, trap rooms, Boss room, trader room, artifact room (requires 3 different boss keys, wins the game by destroying the artifact)
    //bosses = beholder, mindflayer, dragon, (maybe liche)
    //traps = (treasure but mimic), spikes, spider nest
    //treasures = potions, weapons, gold, armor, (maybe scrolls or rings)
    //trader room has trader with some shop as first one
    //
    //normal monsters drop loot, bosses drop keys
}