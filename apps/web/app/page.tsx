import { DataTable } from "./data-table"
import { getAllData } from "@/api/pokedex"
import { columns } from "./columns"

export const dynamic = 'force-dynamic';

export default async function Page() {

  const data = await getAllData()
  
  return (
    <div className="min-h-svh p-6">
      <div className="flex flex-col h-screen w-full| justify-center items-center min-w-0 gap-4 text-sm leading-loose pt-50">
        <div className="container py-10">
          <DataTable columns={columns} data={data} db={data} />
        </div>
      </div>
    </div>
  )
}
