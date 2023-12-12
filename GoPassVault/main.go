//Name: Kiryl Baravikou
//NetID: kbara5
//Date: 11/16/2023
//Course: CS 341 Fall 2023
//Homework 4: Golang Password Manager
//Project Description:
//The goal of the following assignment is to write a password manager, which manages a set of entries, each entry containing the following information:
// @param s => the domain name of the site
// @param u => username
// @param p => password of the user
//Each user must be able to add, remove, view, and update entries in the password manager using the provided commands.
//Professor: Jon Solworth
//How to run the program: open the terminal -> locate the directory that contains the main.go of the project -> type in 'go run main.go' -> press enter -> follow the instructions.
//For your convenience, I have provided a prompt for the user to select one of the required options.

package main

import (
	"bufio"
	"fmt"
	"log"
	_ "maps"
	"os"
	_ "slices"
	"sort"
	"strings"
)

// Separate object to store the S, U, P, I values needed for the program => DONE
type Entry struct {
	Site     string
	User     string
	Password string
	Info     string
}

// Defined EntrySlice => DONE
type EntrySlice []Entry

// Serves as a storage for the current entry slice and the bool to determine whether the site was found in the map => DONE
type EntryResult struct {
	EntrySlice       EntrySlice
	Found            bool
	SortedEntrySlice SortedEntrySlice
}

// SortedEntrySlice Object to implement the sort interface => DONE
type SortedEntrySlice struct {
	EntrySlice
}

// The following methods allow to implement the basic functionality for the above interface.
// The first one is used to find the length of the slice => DONE
func (s SortedEntrySlice) Len() int {
	return len(s.EntrySlice)
}

// Compares the users in the entry slices => DONE
func (s SortedEntrySlice) Less(i, j int) bool {
	return s.EntrySlice[i].User < s.EntrySlice[j].User
}

// Swap Swaps the users in the entry slices => DONE
func (s SortedEntrySlice) Swap(i, j int) {
	s.EntrySlice[i], s.EntrySlice[j] = s.EntrySlice[j], s.EntrySlice[i]
}

// The following map will store the site as a key and the entry slice as a value as requested in the HW => DONE
var passwordMap map[string]EntrySlice
var sortedPasswordMap map[string]SortedEntrySlice

// Helper function to initialize the map => DONE
func init() {
	//For unsorted values
	passwordMap = make(map[string]EntrySlice)
	//For sorted values
	sortedPasswordMap = make(map[string]SortedEntrySlice)
}

// Helper function to find the entry slice for a given site => DONE
func locate(site string) EntryResult {

	entrySlice, found := passwordMap[site]
	if !found {
		//Return an instance of the EntryResult struct with the default values
		return EntryResult{
			EntrySlice: nil,
			Found:      false,
		}
	}

	//Return an instance of the EntryResult struct
	sortedSlice, _ := sortedPasswordMap[site]
	return EntryResult{
		EntrySlice:       entrySlice,
		Found:            true,
		SortedEntrySlice: sortedSlice,
	}
}

// Helper function to set the entry slice for a given site => DONE
func setEntrySlice(site string, entrySlice EntrySlice) {
	passwordMap[site] = entrySlice
	sortedSlice := SortedEntrySlice{entrySlice}
	//sort.Sort(sortedSlice)
	sortedPasswordMap[site] = sortedSlice
}

// Helper function to find the entry slice for a given user => DONE
func findEntrySlice(user string, entrySlice EntrySlice) (int, bool) {

	//Set up the logger to keep track of the program execution
	log.Default().SetOutput(os.Stdout)
	log.SetFlags(log.LstdFlags | log.Lshortfile)

	//Allows to get the sorted slice + its length
	sortedSlice := SortedEntrySlice{entrySlice}
	length := len(sortedSlice.EntrySlice)

	//sort.Search allows to find the index of the user in the entry slice
	index := sort.Search(length, func(i int) bool {
		return sortedSlice.EntrySlice[i].User >= user
	})

	if index < length && sortedSlice.EntrySlice[index].User == user {
		return index, true
	}

	//Access the entry slice and iterate through it within the safe range
	//If the user is found, return the index and true
	for i, entry := range sortedSlice.EntrySlice {
		if index < length && entry.User == user {
			return i, true
		}
	}

	//Default return values
	return -1, false
}

// Helper function to print the current database entries => DONE
func pmList() {

	//Sample string formatting for the output with the specified width between the columns
	const formatString = "                      %-20s %-7s %s\n"
	log.Default().SetOutput(os.Stdout)
	var result strings.Builder

	//Increases the capacity of the string builder to avoid reallocation
	if result.Cap() == 0 {
		result.Grow(100)
	}

	//Accesses the values stored in the map
	for s, entries := range passwordMap {
		for _, entry := range entries {
			//In the output I store the s, u, p values using the specified format in the formatString
			result.WriteString(fmt.Sprintf(formatString, s, entry.User, entry.Password))
			log.Flags()
		}
	}

	//Displays the output
	fmt.Print(result.String())
}

// Helper function to add a new entry to the database => DONE
func pmAdd(s, u, p string) {

	log.Default().SetOutput(os.Stdout)
	result := locate(s)

	//Sanity check
	if !result.Found {
		result.EntrySlice = make(EntrySlice, 0)
		log.Flags()
	}

	//Checks if the user is already in the entry slice
	_, userFound := findEntrySlice(u, result.EntrySlice)

	//If the user is not found, add the new entry to the slice
	if !userFound {
		entry := Entry{Site: s, User: u, Password: p}
		result.EntrySlice = append(result.EntrySlice, entry)
		//Set the entry slice for the given site
		setEntrySlice(s, result.EntrySlice)
	} else {
		//No duplicates allowed according to the description
		fmt.Println("add: duplicate entry")
	}
}

// Helper function to assist in deletion of the specified user from the entry slice => DONE
// Reference: https://pkg.go.dev/maps@go1.21.4#DeleteFunc
func DeleteFunc[S []Entry, E Entry](s []E, del func(E) bool) []E {
	var result []E
	for _, v := range s {
		if !del(v) {
			result = append(result, v)
		}
	}
	return result
}

/*
* Helper function to remove the specified user from the entry slice => DONE
* @param site string
* @param user string
 */
func pmRemove(site, user string) {

	//Find the entry slice for the given site
	result := locate(site)

	//Sanity check
	if !result.Found {
		fmt.Println("remove: site not found")
		return
	}

	//Now find the user in the entry slice
	_, userFound := findEntrySlice(user, result.EntrySlice)

	//Sanity check
	if !userFound {
		fmt.Println("remove: user not found")
		return
	}

	// Check if there is only one user for the site
	if len(result.EntrySlice) == 1 {
		delete(passwordMap, site)
	} else {
		//Finally, delete the user from the entry slice using the DeleteFunc helper function
		passwordMap[site] = DeleteFunc(result.EntrySlice, func(entry Entry) bool {
			return entry.User == user
		})
	}

	// If the site has no users after removal, delete the site
	if len(passwordMap[site]) == 0 {
		delete(passwordMap, site)
	}
}

// Helper function to remove the site from the map => DONE
func pmRemoveSite(site string) {

	//Logs help to keep track of the flow of the program execution and any errors
	log.Default().SetOutput(os.Stdout)
	log.SetFlags(log.LstdFlags | log.Lshortfile)

	//Obtain the entry slice for the given site using the locate() helper function
	result := locate(site)

	//Sanity check
	if !result.Found {
		fmt.Println("remove: site not found")
		return
	}

	//Stores the length of the entry slice
	length := len(result.EntrySlice)

	//If the length is 0, there are no users for the site
	if length == 0 {
		fmt.Println("remove: no users found for the site")
		return
	} else if length == 1 {
		//Removes just the site from the map if there is only one user with the same site
		delete(passwordMap, site)
	} else {
		fmt.Println("remove: attempted to remove multiple users")
		log.Flags()
		return
	}
}

// Helper function to read the passwordVault.txt file => DONE
func pmRead() {

	log.Default().SetOutput(os.Stdout)

	//Via os module, the program will open the file for reading
	file, err := os.Open("passwordVault.txt")

	//Sanity check
	if err != nil {
		fmt.Println("pmRead: error opening file:", err)
		log.Panic(err)
	}

	//Defer the file closing
	defer file.Close()

	scanner := bufio.NewScanner(file)

	//The following loop will read the file line by line
	for scanner.Scan() {

		//Get the current line from the file
		line := scanner.Text()

		//Splits the single line entered into fields
		fields := strings.Fields(line)

		//Since 3 arguments are expected, the program will check if the number of fields is 3
		if len(fields) != 3 {
			fmt.Println("pmRead: invalid entry format:", line)
			log.Flags()
			continue
		}

		//Obtain the site, user, and password from the fields slice
		s := fields[0]
		u := fields[1]
		p := fields[2]

		//If the site is not in the map, create a new entry slice using make()
		result, exists := passwordMap[s]
		if !exists {
			result = make(EntrySlice, 0)
		}

		//Now, append the new entry to the slice
		entry := Entry{Site: s, User: u, Password: p}
		result = append(result, entry)
		passwordMap[s] = result
	}

	//Sanity check
	if err := scanner.Err(); err != nil {
		fmt.Println("pmRead: error while reading file:", err)
		log.Panic(err)
	}
}

// Helper function to write the changes to the passwordVault.txt file => DONE
func pmWrite() {

	//Using logs, I keep track of any changes within the program
	log.Default().SetOutput(os.Stdout)

	//Creates a new file to write the changes to, as requested in the assignment
	filename, undefined := os.Create("passwordVault.txt")

	//String Builder allows to build a string using write methods
	var result strings.Builder
	result.Grow(100)

	//Sanity check
	if undefined != nil {
		fmt.Println("Cannot create the file: ", undefined)
		log.Fatal(undefined)
		return
	}

	//The following loop will iterate through the map and write the changes to the file
	for s, object := range passwordMap {
		for _, entry := range object {
			_, err := fmt.Fprintf(&result, "%s %s %s\n", s, entry.User, entry.Password)

			//Sanity check for any errors
			if err != nil {
				log.Fatal(err)
				return
			}
		}
	}

	//Update the file contents
	filename.WriteString(result.String())

	//Finally, close the file for writing
	filename.Close()
}

// Helper function to accept the user input => DONE
func getUserInput() string {
	var input string
	fmt.Scan(&input)
	return input
}

/*
* Helper function to process the input and call the appropriate function based on the number of tokens in the slice => DONE
* @param s string
* @param u string
* @param tokens []string
 */
func processInput(s string, u string, tokens []string) {

	//Based on the number of tokens, the program will decide which function to call
	switch len(tokens) {
	case 1:
		pmRemoveSite(tokens[0])
	case 2:
		pmRemove(tokens[0], tokens[1])
	default:
		fmt.Println("Invalid input")
	}
}

/*
The following function will keep looping forever until the user decides to exit the program.
The user will be prompted to enter one of the following options:

	@param l: list the current database
	@param a: add new info to the database
	@param r: remove specified info from the database
	@param x: exit the program

Based on the choice, the appropriate function will be called => DONE
*/
func loop() {

	//SUP format: s = site, u = user, p = password
	var s, u, p string

	for {
		//The following prompt was added for more clarity on the options
		fmt.Print("\nPlease, select one of the following options: \n" +
			"l: list the current database \n" +
			"a: add new info to the database\n" +
			"r: remove specified info from the database\n" +
			"x: exit the program\n\n")

		//Using the helper function, accept the user input
		e := getUserInput()

		//To make sure that the input is not case sensitive
		e = strings.ToLower(e)

		switch e {
		case "l":
			//Calls the function to list the current database
			pmList()
		case "a":
			//Allows to accept user input via fmt module
			fmt.Scan(&s, &u, &p)

			//Adds the new info to the database
			pmAdd(s, u, p)

			//And writes the changes to the file
			pmWrite()
		case "r":
			//Using the bufio module, the program will read the input until the user presses enter
			this := bufio.NewReader(os.Stdin)
			line, error := this.ReadString('\n')

			//Sanity check
			if error != nil {
				fmt.Println("Something went wrong:", error)
				//To keep track of what is going on using the log files
				log.Fatal(error)
				return
			}

			//Tokenizes the input via strings module
			tokens := strings.Fields(line)

			//The following call will process the input and call the appropriate function inside of it
			processInput(s, u, tokens)

			//Writes the changes to the file
			pmWrite()
		case "x":
			os.Exit(0)
		default:
			fmt.Println("\nInvalid command. Please enter l/a/r/x.\n")
		}
	}
}

// @main => DONE
func main() {

	//Reads the previous entries from the past session
	pmRead()

	//Main driver
	loop()

	//Writes the changes to the file to access them next time, if any
	pmWrite()
}
