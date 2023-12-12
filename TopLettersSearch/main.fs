(*
Name: Kiryl Baravikou
Project description: F# program to input a string and print out information about the # of top 10 letters in that string and substituting certain words
*)


open System

(*explode => DONE
Given a string s, explodes the string into a list of characters.
Example: explode "apple" => ['a';'p';'p';'l';'e']
*)
//The initial string of chars is set into a list of chars
let explode (s: string) = List.ofArray (s.ToCharArray())


(* implode => DONE
The opposite of explode --- given a list of characters, returns the list as a string. Example: implode ['t';'h';'e'] => "the"
*)
let implode (L: char list) = new string (List.toArray L)


(*Helper function that returns the length of the string => DONE*)
let rec length (L: char list) =
    //Pattern match the value of the lst argument
    match L with
    //Base case: if the list is empty then return 0
    | [] -> 0
    //If the list is not empty, then take the tail and recursively count the number of letters 
    | _ :: tail -> 1 + length tail


//The following function calculates the number of cooccurences of each letter from the list in the provided string => DONE
let topTen (L: char list) =

    //# of high frequency letters in the string (e, t, a, o, i, n, s, r, h, l)
    //let ABC = ['e'; 't'; 'a'; 'o'; 'i'; 'n'; 's'; 'r'; 'h'; 'l']
    let ABC = ['a'; 'e'; 'h'; 'i'; 'l'; 'o'; 'n'; 'r'; 's'; 't']

    let map (letter: char) =
        let rec reduce (ls: char list) (acc: int) =
            match ls with
            //Base case: empty list => return the initial value, i.e. 0
            | [] -> acc
            //If there is a match right in the head, then increment the counter + apply recursion
            | head :: tail when head = letter -> reduce tail (acc + 1)
            | _ :: tail -> reduce tail acc
        reduce L 0

    //Helper function to calculate letter frequencies
    let counter =
        ABC
        //Map takes a letter as input => returns a tuple
        |> List.map (fun letter -> (letter, map letter))
        //Sort the list based on the index of each element from ABC => find the corresponding index in ABC via findIndex
        |> List.sortBy (fun (letter, _) -> List.findIndex ((=) letter) ABC)
        //Map and reduce phase
        |> List.map (fun (letter, count) -> (letter, count))

    //Return
    counter


//Helper function that allows to swap the letters in a word following the provided by Professor pattern => DONE
let swap (L: char list) =
    let rec sub (L: char list) =
        match L with
        //Base case: if empty then return empty
        | [] -> []
        //Start swapping the letters as requested
        | 'b' :: 'o' :: 'y' :: tail -> 'm' :: 'a' :: 'n' :: sub tail
        | 'r' :: 'a' :: 't' :: tail -> 'h' :: 'a' :: 't' :: sub tail
        | 'c' :: 'a' :: 't' :: tail -> 'd' :: 'o' :: 'g' :: sub tail
        //| 'o' :: 'n' :: 'e' :: tail -> 't' :: 'w' :: 'o' :: sub tail
        | 'f' :: 'o' :: 'x' :: tail -> 'n' :: 'o' :: 'x' :: sub tail
        | 't' :: 'h' :: 'e' :: tail -> 'h' :: 'e' :: 'r' :: sub tail
        //Apply the recursion
        | head :: tail -> head :: sub tail

    let s = L |> sub |> implode
    printfn "swap imploded: \"%s\"" s


//@main
[<EntryPoint>]
let main argv =

    printfn "Starting"
    printfn ""

    //Allows to accept user input
    printf("input> ")
    let input = System.Console.ReadLine()

    //Invoke explode on the trimmed input
    let L = explode (input.Trim())
    printfn "exploded: %A" L

    printfn ""
    let len = length L
    printfn "length of sentence: %A" len

    (*Compute the number of top 10 ABC chars
    Reference: https://learn.microsoft.com/en-us/dotnet/api/system.string.trim?view=net-7.0
    *)
    let num = topTen L
    printfn "# of top 10 letters: %d" (List.sumBy snd num)
    //Print count of each of the top 10 letters
    num |> List.iter (fun (char, num) -> printf "'%c': %d\n" char num)
    
    //Substitute a series of letters from a given string
    printfn ""
    let S = implode L
    printfn "imploded: \"%s\"" S
    printfn ""

    //Print updated sentence => DONE
    swap L

    printfn ""
    printfn "Done"

    //return 0 => success, much like C++
    0
