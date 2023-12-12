
// Homework 3: various functions for practicing F#.
// Name: Kiryl Baravikou, University of Illinois, Chicago
// Course: CS 341, Fall 2023


namespace homework

module hw03 =

   // Custom helper functions that is used to check whether an element is in a List or not => Returns true if S is a subset of L, false if not => DONE
  let rec contains e L =
     // Standard pattern match approach
    match L with
     // If the list is empty => then the element is not found, thus, return false
    | [] -> false
     // Otherwise, we traverse from head to tail, and check whether a current element matched the target. If there is a match => return true. Else => false
    | head :: tail -> e = head || contains e tail

   // Function 1: the following function is used to determine whether elements of one list are a subset of elements from another list => DONE
  let rec subset S L =
    match S with
     // Base case: empty set is the subset of each set, so by default must be true
    | [] -> true
     // Other cases: only if the element is within the target set, it can be considered as a subset of a set.
    | e :: other -> contains e L && subset other L


    // Function 2: the following function is used to delete all occurences of e from L, and return a new list => must be tail-recursive => DONE
  let delete_tr e L =
     // Helper function used to achieve the tail recursion
    let rec recurseHelper e L acc =
         // Standard pattern matching
        match L with
         // Base case: if L is empty => we are at the end of the list => return the reversed acc via List.rev
        | [] -> List.rev acc
         // L is Not empty => traverse from head to tail. If head == to the element => ignore the elements of the List == 'e' and move to the next element
        | head :: tail when head = e -> recurseHelper e tail acc
        | head :: tail -> recurseHelper e tail (head :: acc)
    in
     // Initialization of the recursive call: pass element, list, and an empty accumulator 
    recurseHelper e L []


   // Function 3: the following function Deletes all occurrences of e from the list L, returning the new list. This version uses a higher-order approach
  let delete_ho e L =

     // Using the monadic fold operation, we fold elements of the list from left to right, basically reducing the collection of elements to a single element by taking an acc and obj, where obj is the current element of the list being processed.The acc stores the intermediate result => we accumulate elems in the L by either including them in the acc or simply skipping them
    List.fold (fun acc obj -> if obj = e then acc else obj::acc) [] L |> List.rev


   // Function 4: the following function computes the avg scores of students as a real number + returns a list of tuples with the results
  let examAverages LT =
    let avg scores =
        match scores with
         // If zero, then zero is returned
        | [] -> 0.0
         // map() maps the list of scores to float nums [each int becomes a float], and then computes the average via in-built List.average function as suggested.
        | _ -> scores |> List.map float |> List.average
     // Via applying map to each element of the collection LT, we calculate the outcomes for each student and produce results in the form of a tuple, where id is the netID of a student + the corresponding score to that ID is produced to the right of it.
     // Reference: https://fsharp.github.io/fsharp-core-docs/reference/fsharp-collections-listmodule.html#map
    List.map (fun (id, scores) -> (id, avg scores)) LT


   // Function 5: Given 2 lists L1 and L2, both the same length, merges the corresponding elements into pairs, returning a list of pairs
   // Constaints: solve using recursion only + no zip function.
  
  let rec pairwise L1 L2 =
    match (L1, L2) with
     // Handle the base case => if empty then return empty
    | ([], []) -> []
     // Take the head from the first tuple, the head from the second tuple, put them together. Do the same with the tales by calling the pairwise() recursively on the objects.
    | (oHead::oTail, pHead::pTail) -> (oHead, pHead) :: pairwise oTail pTail
     // Diff length => must raise an error since if L1 > L2, then there wont be enough elements to create a complete pair: https://fsharp.github.io/fsharp-core-docs/reference/fsharp-core-operators.html#failwith
    | (oHead::oTail, []) -> failwith "ERROR: THE LENGTH OF THE INPUTS MUST BE THE SAME: L1's size is greater than L2's!"
     // Same as above => diff length
    | ([], pHead::pTail) -> failwith "ERROR: THE LENGTH OF THE INPUTS MUST BE THE SAME: L2's size is greater than L1's!"
    | (_, _) -> failwith "ERROR: THE LENGTH OF THE INPUTS MUST BE THE SAME!"




// Test Cases
// open System
// open homework


// let print test result =
//     printfn "%s: %A" test result

// [<EntryPoint>]
// let main argv =
//     printfn "* Starting *"
//     printfn ""

//     //Random tests
//     let random = Random()
//     let randomInt () = random.Next(1, 101)
//     let randomString () = Guid.NewGuid().ToString()

//     let randomList n generator =
//         [ for _ in 1..n -> generator() ]

//     let pairwiseResult1 = hw03.pairwise (randomList 3 randomInt) (randomList 3 randomString)
//     printfn "pairwise Test 6: %A" pairwiseResult1

//     let pairwiseResult2 = hw03.pairwise (randomList 3 randomString) (randomList 3 randomInt)
//     printfn "pairwise Test 7: %A" pairwiseResult2

//     printfn "* Testing the subset() function *"
//     let L1 = [1; 2; 3; 5; 8; 9; 13; 17; 21]
//     let L2 = [1..21]
//     let L3 = []

//     printfn "Testing the Subset(L1, L2): %A" (hw03.subset L1 L2)
//     printfn "Testing the Subset(L2, L1): %A" (hw03.subset L2 L1)
//     printfn "Testing the Subset(L3, L1): %A" (hw03.subset L3 L1)
//     printfn "Testing the Subset(L2, L3): %A" (hw03.subset L2 L3)
//     printfn "Testing the Subset(L1, L3): %A" (hw03.subset L1 L3)
//     printfn ""


    
//     delete_tr 3  [3; 1; 2]   => [1; 2]
//     delete_tr 99 [99; 0; 99] => [0]
//     delete_tr -2 []          => []
//     delete_tr "cat" ["dog"]  => ["dog"]
//     delete_tr 99999 [1..99999] => [1..99998]
    

//     printfn "Testing the Delete() function using tail recursion"
//     let delTest1 = hw03.delete_tr 3 L2
//     print "delTest Test 1" delTest1

//     let delTest2 = hw03.delete_tr 2 L2
//     print "delTest Test 2" delTest2

//     let delTest3 = hw03.delete_tr 1 L2
//     print "delTest Test 3" delTest3

//     let delTest4 = hw03.delete_tr 99 [1..1000]
//     print "delTest Test 4" delTest4

//     let delTest5 = hw03.delete_tr 900 [1..1000]
//     print "delTest Test 5" delTest5

//     let delTest6 = hw03.delete_tr -2 []
//     print "delTest Test 6" delTest6

//     let delTest7 = hw03.delete_tr 3 [3; 1; 2]
//     print "delTest Test 7" delTest7

//     let delTest8 = hw03.delete_tr 99 [99; 0; 99]
//     print "delTest Test 8" delTest8

//     let delTest9 = hw03.delete_tr -2 []
//     print "delTest Test 9" delTest9

//     let delTest10 = hw03.delete_tr "cat" ["dog"]
//     print "delTest Test 10" delTest10

//     let delTest11 = hw03.delete_tr 99999 [1..99999]
//     print "delTest Test 11" delTest11

//     (*
//     Examples: delete_ho 3  [3; 1; 2]   => [1; 2]
//               delete_ho 99 [99; 0; 99] => [0]
//               delete_ho -2 []          => []
//               delete_ho "cat" ["dog"]  => ["dog"]
//               delete_ho 99999 [1..99999] => [1..99998]
//     *)

//     printfn "Testing the Delete_HO() function"
//     let delHo1 = hw03.delete_ho 3  [3; 1; 2]
//     print "delHo Test 1" delHo1

//     let delHo2 = hw03.delete_ho 99 [99; 0; 99]
//     print "delHo Test 2" delHo2

//     let delHo3 = hw03.delete_ho -2 [] 
//     print "delHo Test 3" delHo3

//     let delHo4 = hw03.delete_ho "cat" ["dog"]
//     print "delHo Test 4" delHo4

//     let delHo5 = hw03.delete_ho 99999 [1..99999]
//     print "delHo Test 5" delHo5

//     printfn ""
//     printfn "Testing the Exam_Avg() function"
//     printfn ""

//     let avg1 = hw03.examAverages [("abc", [85; 90; 88]); ("xyz", [78; 82; 91; 75; 88])]
//     print "examAverages Test 2" avg1

//     let avg2 = hw03.examAverages [("student1", [100]); ("student2", [0; 100; 50; 75])]
//     print "examAverages Test 3" avg2

//     let avg3 = hw03.examAverages ([
//         ("John", [90; 88; 86; 92; 94]);
//         ("Mary", [78; 82; 79; 85; 88; 92]);
//         ("David", [95; 92; 88; 90; 89]);
//         ("Anna", [88; 91; 93; 89; 87; 90]);
//     ])
//     print "examAverages Test 4" avg3

//     let avg4 = hw03.examAverages ([
//         ("UserA", []);
//         ("UserB", [70; 80; 90; 75; 85]);
//         ("UserC", [60; 65; 70]);
//     ])
//     print "examAverages Test 5" avg4

//     let avg5 = hw03.examAverages [("user1", []); ("user2", [70; 80; 90])]
//     print "examAverages Test 5" avg5

//     let avg6 = hw03.examAverages [("sdeitz2",[100;90;91]); ("psankar",[100;100;100;100;98])]
//     print "examAverages Test 6" avg6

//     printfn ""
//     printfn "Testing the pairwise() function"
//     printfn ""

//     let pwTest1 = hw03.pairwise [7; 8; 9] [1; 2; 3]
//     print "pairwise Test 1" pwTest1

//     let pwTest2 = hw03.pairwise [5; 10; 15] [5; 10; 15]
//     print "pairwise Test 2" pwTest2

//     let pwTest3 = hw03.pairwise [3; 6; 9] [2; 4; 8]
//     print "pairwise Test 3" pwTest3

//     let pwTest4 = hw03.pairwise [10; 20; 30; 40] [1; 2; 3; 4]
//     print "pairwise Test 4" pwTest4

//     let pwTest5 = hw03.pairwise ["a"; "b"; "30"; "40"] [1123; 2312; 4323; 5244]
//     print "pairwise Test 5" pwTest5

//     let pwTest6 = hw03.pairwise [] []
//     print "pairwise Test 6" pwTest6

//     printfn ""
//     printfn "* Done *"
//     0
