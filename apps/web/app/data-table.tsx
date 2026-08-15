"use client";

import { 
    ColumnDef, 
    ColumnFiltersState,
    flexRender, 
    getCoreRowModel,
    getFilteredRowModel,
    getPaginationRowModel, 
    getSortedRowModel, 
    useReactTable, 
    SortingState 
} from "@tanstack/react-table";

import {
    PolarAngleAxis,
    PolarGrid,
    Radar,
    RadarChart
} from "recharts";

import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardContent, CardDescription, CardTitle, CardHeader } from "@/components/ui/card";
import { ChartContainer, ChartTooltip, ChartTooltipContent, type ChartConfig } from "@/components/ui/chart";

import { PokemonData, PokemonStats } from "@/types/pokemon";

import { useState } from "react";

import Image from "next/image";
import { customImageLoader } from "@/lib/utils";

interface DataTableProps<TData, TValue> {
    columns: ColumnDef<TData, TValue>[]
    data: TData[],
    db: PokemonData[]
}

export function DataTable<TData, TValue>({ columns, data, db }: DataTableProps<TData, TValue>) {
    
    const [sorting, setSorting] = useState<SortingState>([])
    const [columnFilters, setColumnFilters] = useState<ColumnFiltersState>([])
    const [pokemonSelected, setPokemonSelected] = useState<PokemonStats | null>(null)
    const [pokemonImage, setPokemonImage] = useState<string>("")

    const showPokemon = (pokemonId: string) => {

        try {
            const pokemon = db.find((element: PokemonData) => element.uid === pokemonId) as PokemonData
            setPokemonSelected({
                name: pokemon.name,
                stats: [
                    {statName: "HP", value: pokemon.hp},
                    {statName: "Attack", value: pokemon.attack},
                    {statName: "Defense", value: pokemon.defense},
                    {statName: "SP Attack", value: pokemon.special_attack},
                    {statName: "SP Defense", value: pokemon.special_defense},
                    {statName: "Speed", value: pokemon.speed},
                ]
            })
            setPokemonImage(pokemon.img)
        } catch (Error) {
            console.error(Error)
        }
        
    }
    
    const chartConfig = {
        value: {
            label: "Value",
            color: "var(--chart-5)",
        },
    } satisfies ChartConfig
    
    const table = useReactTable({
        data,
        columns,
        getCoreRowModel: getCoreRowModel(),
        getPaginationRowModel: getPaginationRowModel(),
        onSortingChange: setSorting,
        getSortedRowModel: getSortedRowModel(),
        onColumnFiltersChange: setColumnFilters,
        getFilteredRowModel: getFilteredRowModel(),
        state: {
            sorting,
            columnFilters,
        },
    })
    return (
        <div className="mt-4">
            <div className={`${pokemonSelected ? "visible w-full flex gap-2" : "hidden"}`}>
                <Card className="w-full flex justify-center items-center">
                    <Image 
                        loader={customImageLoader}
                        src={`/${pokemonImage}`}
                        width={400}
                        height={400}
                        alt={pokemonSelected ? pokemonSelected.name : "pokemon"}
                        loading="lazy"
                    />
                </Card>
                <Card className="w-full">
                    <CardHeader className="items-center pb-4">
                        <CardTitle>{pokemonSelected?.name}</CardTitle>
                    </CardHeader>
                    <CardContent className="pb-0">
                        <ChartContainer
                            config={chartConfig}
                            className="mx-auto aspect-square max-h-112.5"
                        >
                            <RadarChart data={pokemonSelected?.stats}>
                                <ChartTooltip cursor={false} content={<ChartTooltipContent/>} />
                                <PolarAngleAxis dataKey="statName" className="w-full"/>
                                <PolarGrid />
                                <Radar
                                    dataKey="value"
                                    fill="var(--chart-2)"
                                    fillOpacity={0.8}
                                />
                            </RadarChart>
                        </ChartContainer>
                    </CardContent>
                </Card>
            </div>
            <div className="flex items-center py-4">
                <Input
                    placeholder="Filter pokemons..."
                    value={(table.getColumn("name")?.getFilterValue() as string) ?? ""}
                    onChange={(event) => table.getColumn("name")?.setFilterValue(event.target.value)}
                    className="w-full"
                />
            </div>
            <div className="overflow-hidden rounded-md border">
                <Table>
                    <TableHeader>
                        {table.getHeaderGroups().map((headerGroup) => (
                            <TableRow key={headerGroup.id}>
                                {headerGroup.headers.map((header) => {
                                    return (
                                        <TableHead key={header.id}>
                                            {header.isPlaceholder 
                                                ? null 
                                                : flexRender(
                                                    header.column.columnDef.header,
                                                    header.getContext()
                                                )}
                                        </TableHead>
                                    )
                                })}
                            </TableRow>
                        ))}
                    </TableHeader>
                    <TableBody>
                        {table.getRowModel().rows?.length ? (
                            table.getRowModel().rows.map((row) => (
                                <TableRow
                                    key={row.id}
                                    data-state={row.getIsSelected() && "selected"}
                                    onClick={() => showPokemon(row.getValue("uid"))}
                                >
                                    {row.getVisibleCells().map((cell) => (
                                        <TableCell key={cell.id}>
                                            {flexRender(cell.column.columnDef.cell, cell.getContext())}
                                        </TableCell>
                                    ))}
                                </TableRow>
                            ))
                        ) : (
                            <TableRow>
                                <TableCell colSpan={columns.length} className="h-24 text-center">
                                    No results.
                                </TableCell>
                            </TableRow>
                        )}
                    </TableBody>
                </Table>
            </div>
            <div className="flex items-center justify-end space-x-2 py-4">
                <Button
                    variant="outline"
                    size="sm"
                    onClick={() => table.previousPage()}
                    disabled={!table.getCanPreviousPage()}>
                        Previous
                    </Button>
                <Button
                    variant="outline"
                    size="sm"
                    onClick={() => table.nextPage()}
                    disabled={!table.getCanNextPage()}>
                        Next
                    </Button>
            </div>
        </div>
    )
}
