class Monster : Creature
{
    public int MonsterID { get; set; }
    
    //0 = "skeleton", 1 = "goblin", 2 = "troll", 3 = "ogre", 4 = "gelatinous cube", 5 = "kobold", 6 = "vampire"
    public int MonsterHP { get; set; }
    private int _low = 2;
    private int _med = 5;
    private int _high = 8;
    private int _huge = 12;
    //can change monsterHP and damges base values

    public Monster(int monsterID) : base(monsterID)
    {
        MonsterID = monsterID;
        if (MonsterID == 0)
        {
            CreatureName = "Skeleton";
            CreatureHP = _low;
            CreatureDamage = _low;
        }
        else if (MonsterID == 1)
        {
            CreatureName = "Goblin";
            CreatureHP = _med;
            CreatureDamage = _low;
        }
        else if (MonsterID == 2)
        {
            CreatureName = "Troll";
            CreatureHP = _high;
            CreatureDamage = _med;
        }
        else if (MonsterID == 3)
        {
            CreatureName = "Ogre";
            CreatureHP = _huge;
            CreatureDamage = _high;
        }
        else if (MonsterID == 4)
        {
            CreatureName = "Gelatinous Cube";
            CreatureHP = _med;
            CreatureDamage = _high;
        }
        else if (MonsterID == 5)
        {
            CreatureName = "Kobold";
            CreatureHP = _low;
            CreatureDamage = _med;
        }
        else
        {
            CreatureName = "Vampire";
            CreatureHP = _high;
            CreatureDamage = _huge;
        }
    }
}