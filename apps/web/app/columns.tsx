"use client";

import { ColumnDef } from "@tanstack/react-table";
import { ArrowUpDown } from "lucide-react";
import { PokemonData } from "@/types/pokemon";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Avatar, AvatarImage } from "@/components/ui/avatar";

const baseUrl = process.env.NEXT_PUBLIC_IMAGE_SERVER_URL

export const columns: ColumnDef<PokemonData>[] = [
    {
        header: () => <div className="text-left">UI</div>,
        cell: ({ row }) => <div className="text-left font-medidum">{row.getValue("uid")}</div>,
        accessorKey: "uid",
    },
    {
        header: () => <div className="text-left">Icon</div>,
        cell: ({ row }) => <Avatar><AvatarImage src={`${baseUrl}/${row.getValue('icon')}`} alt={row.getValue("icon_alt")}/></Avatar>,
        accessorKey: "icon",
    },
    {
        header: ({column}) => {
            return (
                <Button
                    variant="ghost"
                    onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
                >
                    Name
                    <ArrowUpDown className="ml-2 h-4 w-4"/>
                </Button>
        )},
        cell: ({ row }) => <div className="text-left font-medidum">{row.getValue("name")}</div>,
        accessorKey: "name",
    },
    {
        header: () => <div className="text-left">Elements</div>,
        cell: ({ row }) => {
            return (
                <div className="text-left font-medidum flex gap-2">
                    {row.getValue<string[]>("elements").map( 
                        (element: string, idx: number) => <Badge key={idx} variant="secondary">{element}</Badge> 
                    )}
                </div>
            )},
        accessorKey: "elements",
    }
]

