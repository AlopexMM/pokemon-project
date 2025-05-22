export interface IPokemonCard {
  id: string
  name: string
  hp: number
  attack: number
  speed: number
  defense: number
  image: string
  element: string
}

export interface IPokemonOption {
  image: string
  selected: boolean
  name: TPokemonOptionNames
  element: string
}

export type TPokemonOptionNames = 'pikachu' | 'bulbasaur' | 'squirtle'
