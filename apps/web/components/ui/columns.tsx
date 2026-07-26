"use client"

import { ColumnDef } from "@tanstack/react-table"
import { PokemonType } from "@/lib/types/pokemon"

type PokemonColumns = {
    uid: string
    name: string
    pokemonElement: PokemonType[]
}

export const columns: ColumnDef<PokemonColumns>[] = [
    {
        accessorKey: "uid",
        header: "UID"
    },
    {
        accessorKey: "name",
        header: "Name"
    },
    {
        accessorKey: "pokemonElement",
        header: "Type"
    }
]