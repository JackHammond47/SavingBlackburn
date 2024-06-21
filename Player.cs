class Player
{
    public string Name { get; set; }
    public CharacterClass CharacterClass{ get; set; }
    public Inventory Inventory { get; set; }
    public bool Hidden { get; set; } = false;
    public Player(string name, CharacterClass characterClass)
    {
        Name = name;
        CharacterClass = characterClass;
        Inventory = new();
    }
}