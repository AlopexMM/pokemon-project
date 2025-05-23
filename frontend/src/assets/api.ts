import axios from 'axios'
import { type IPokemonCard } from './types/pokemon'

const instance = axios.create({
  baseURL: 'http://127.0.0.1:8000/pokemon',
  timeout: 1000,
  headers: {
    accept: 'application/json',
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
  },
})

export const pokemonAPI = {
  list: (): Promise<IPokemonCard[]> =>
    instance.get('/').then((res) => {
      return res.data
    }),
  add: (card: IPokemonCard) => instance.post('/', card),
  update: (card: IPokemonCard) => instance.put(`/${card.id}`, card),
  delete: (id: string): Promise<IPokemonCard[]> =>
    instance.delete(`/${id}`).then((res) => {
      return res.data
    }),
}
