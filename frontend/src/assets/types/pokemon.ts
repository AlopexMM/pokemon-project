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

export class PokemonCard implements IPokemonCard {
  id: string
  name: string
  hp: number
  attack: number
  speed: number
  defense: number
  image: string
  element: string

  constructor(
    id: string,
    name: string,
    hp: number,
    attack: number,
    speed: number,
    defense: number,
    image: string,
    element: string,
  ) {
    this.id = id
    this.name = name
    this.hp = hp
    this.attack = attack
    this.speed = speed
    this.defense = defense
    this.image = image
    this.element = element
  }
}

export interface IPokemonOption {
  image: string
  selected: boolean
  name: TPokemonOptionNames
  element: string
}

export type TPokemonOptionNames = 'pikachu' | 'bulbasaur' | 'squirtle'
