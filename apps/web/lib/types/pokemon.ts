export enum PokemonType {
    Grass = "Grass",
    Poison = "Poison",
    Fire = "Fire",
    Flying = "Flying",
    Dragon = "Dragon",
    Water = "Water",
    Bug = "Bug",
    Normal = "Normal",
    Dark = "Dark",
    Electric = "Electric",
    Psychic = "Psychic",
    Ground = "Ground",
    Ice = "Ice",
    Steel = "Steel",
    Fairy = "Fairy",
    Fighting = "Fighting",
    Rock = "Rock",
    Ghost = "Ghost",
}

export type Pokemon = {
    uid: string
    name: string
    elements: PokemonType[]
    hp: number
    attack: number
    defense: number
    special_attack: number
    special_defense: number
    speed: number
    icon: string
    img: string
}