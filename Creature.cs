using System.Runtime.CompilerServices;

public abstract class Creature
{
    public int CreatureID { get; set; }
    public string? CreatureName { get; set; }
    public int CreatureHP { get; set; }
    public int CreatureDamage { get; set; }

    public Creature(int creatureID)
    {
        CreatureID = creatureID;
    }
}