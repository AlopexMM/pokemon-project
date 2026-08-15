export type PokemonData = {
    uid: string;
    name: string;
    elements: string[];
    hp: number;
    attack: number;
    defense: number;
    special_attack: number;
    special_defense: number;
    speed: number;
    icon: string;
    icon_alt: string;
    img: string;
}

type Stat = {
    statName: string,
    value: number
}

export type PokemonStats = {
    name: string;
    stats: Stat[]
}