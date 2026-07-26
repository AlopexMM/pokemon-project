import DataTable from "@/components/ui/data-table"
import { columns } from "@/components/ui/columns";
import { PokemonType } from "@/lib/types/pokemon";

export default function Home() {
  const data = [
    {
      uid: "0001",
      name: "Pikachu",
      pokemonElement: [PokemonType.Electric] 
    }
  ]
  return (
    <div className="flex flex-col flex-1 items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <main className="flex flex-1 w-full max-w-3xl flex-col items-center justify-between py-32 px-16 bg-white dark:bg-black sm:items-start">
        <DataTable columns={columns} data={data} />
      </main>
    </div>
  );
}
