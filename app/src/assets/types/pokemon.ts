export interface PokemonCard
{
    id: string,
    name: string,
    hp: number,
    attack: number,
    speed: number,
    defense: number,
    image: string,
    element: string,
}

export interface PokemonOption
{
    image: string,
    selected: boolean,
    name: string,
    element: string
}
