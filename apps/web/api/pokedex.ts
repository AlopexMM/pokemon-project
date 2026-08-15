"use server"

import { PokemonData } from "@/types/pokemon";

export async function getAllData(): Promise<PokemonData[]> {
    const response = await fetch("http://backend:8000/api/all")
    if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`)
    return await response.json()
}