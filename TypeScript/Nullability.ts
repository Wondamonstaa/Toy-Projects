const searchParams = new URLSearchParams(window.location.search);

const id: string | null = searchParams.get("id");
console.log(id?.toUpperCase())

//OR
//console.log(id!.toUpperCase())

/*
//Option 2

if ( id !== null){
    console.log(id.toUpperCase());
}
else{
    console.log("ID is null!")
}
*/

/*
// Option 3
if (!id){
    throw new Error("ID is missing!");
}
*/
