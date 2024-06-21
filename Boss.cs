public class Boss : Creature
{
    public int BossID { get; set; }
    //7 = dragon, 8 = behodler, 9 = mindflayer
    
    public Boss(int bossID) : base(bossID)
    {
        BossID = bossID;
        if (bossID == 7)
        {
            CreatureName = "Dragon";
            CreatureHP = 30;
            CreatureDamage = 20;
        }
        else if (bossID == 8)
        {
            CreatureName = "Beholder";
            CreatureHP = 20;
            CreatureDamage = 30;
        }
        else
        {
            CreatureName = "Mind Flayer";
            CreatureHP = 25;
            CreatureDamage = 25;
        }
    }
}