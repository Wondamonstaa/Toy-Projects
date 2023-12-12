/* ---------------------------------------------
Program 2: Hunt The Wumpus with Dynamic Array
System: Mac using Xcode
Author: Kiryl Baravikou
---------------------------------------------
*/


#include <stdio.h>
#include <stdlib.h>        // for srand
#include <string.h>
#include <ctype.h>
#include <getopt.h>
#include <unistd.h>
#include <time.h>
#include <stdbool.h>

#define rooms 20
#define pit1
#define pit2
#define player
#define wumpus
#define wumpusMazez


int currentPlayerLocation;
int currentWumpusLocation;
int currentPit1Location;
int currentPit2Location;
int currentBat1Location;
int currentBat2Location;
int currentArrowLocation;
int incrementor;
int arrows = 0;
bool playerAlive, wumpusAlive;


//Done => manually initialized array in ascending order
/*const static int wumpusMaze[20][4] = {
    {1, 2, 5, 8}, {2, 1, 3, 10}, {3, 2, 4, 12}, {4, 3, 5, 14}, {5, 1, 4, 6},
    {6, 5, 7, 15}, {7, 6, 8, 17}, {8, 1, 7, 9}, {9, 8, 10, 18}, {10, 2, 9, 11},
    {11, 10, 12, 19}, {12, 3, 11, 13}, {13, 12, 14, 20}, {14, 4, 13, 15},
    {15, 6, 14, 16}, {16, 15, 17, 20}, {17, 7, 16, 18}, {18, 9, 17, 19},
    {19, 11, 18, 20}, {20, 13, 16, 19}
};*/


//Done => Fills the Wumpus Maze with the contents using malloc() => HARDCODE the instructions (Assignment's description)
void loader(int** wumpusMaze){
    
    //{1, 2, 5, 8}======|=====================|=====================|================================|
    wumpusMaze[0][0] = 1; wumpusMaze[0][1] = 2; wumpusMaze[0][2] = 5; wumpusMaze[0][3] = 8;
    
    //{2, 1, 3, 10}======|=====================|=====================|===============================|
    wumpusMaze[1][0] = 2; wumpusMaze[1][1] = 1; wumpusMaze[1][2] = 3; wumpusMaze[1][3] = 10;
    
    //{3, 2, 4, 12}======|=====================|=====================|===============================|
    wumpusMaze[2][0] = 3; wumpusMaze[2][1] = 2; wumpusMaze[2][2] = 4; wumpusMaze[2][3] = 12;
    
    //{4, 3, 5, 14}======|=====================|=====================|================================|
    wumpusMaze[3][0] = 4; wumpusMaze[3][1] = 3; wumpusMaze[3][2] = 5; wumpusMaze[3][3] = 14;
    
    //{5, 1, 4, 6}======|=====================|=====================|=================================|
    wumpusMaze[4][0] = 5; wumpusMaze[4][1] = 1; wumpusMaze[4][2] = 4; wumpusMaze[4][3] = 6;
    
    //{6, 5, 7, 15}======|====================|=====================|=================================|
    wumpusMaze[5][0] = 6; wumpusMaze[5][1] = 5; wumpusMaze[5][2] = 7; wumpusMaze[5][3] = 15;
    
    //{7, 6, 8, 17}======|====================|=====================|=================================|
    wumpusMaze[6][0] = 7; wumpusMaze[6][1] = 6; wumpusMaze[6][2] = 8; wumpusMaze[6][3] = 17;
    
    //{8, 1, 7, 9}======|=====================|=====================|=================================|
    wumpusMaze[7][0] = 8; wumpusMaze[7][1] = 1; wumpusMaze[7][2] = 7; wumpusMaze[7][3] = 9;
    
    //{9, 8, 10, 18}======|===================|=====================|=================================|
    wumpusMaze[8][0] = 9; wumpusMaze[8][1] = 8; wumpusMaze[8][2] = 10; wumpusMaze[8][3] = 18;
    
    //{10, 2, 9, 11}======|====================|=====================|================================|
    wumpusMaze[9][0] = 10; wumpusMaze[9][1] = 2; wumpusMaze[9][2] = 9; wumpusMaze[9][3] = 11;
    
    //{11, 10, 12, 19}======|=====================|=====================|=============================|
    wumpusMaze[10][0] = 11; wumpusMaze[10][1] = 10; wumpusMaze[10][2] = 12; wumpusMaze[10][3] = 19;
    
    //{12, 3, 11, 13======|======================|=====================|==============================|
    wumpusMaze[11][0] = 12; wumpusMaze[11][1] = 3; wumpusMaze[11][2] = 11; wumpusMaze[11][3] = 13;
    
    //{13, 12, 14, 20}======|=====================|=====================|=============================|
    wumpusMaze[12][0] = 13; wumpusMaze[12][1] = 12; wumpusMaze[12][2] = 14; wumpusMaze[12][3] = 20;
    
    //{14, 4, 13, 15}======|=====================|=====================|==============================|
    wumpusMaze[13][0] = 14; wumpusMaze[13][1] = 4; wumpusMaze[13][2] = 13; wumpusMaze[13][3] = 15;
    
    //{15, 6, 14, 16}======|=====================|=====================|==============================|
    wumpusMaze[14][0] = 15; wumpusMaze[14][1] = 6; wumpusMaze[14][2] = 14; wumpusMaze[14][3] = 16;
    
    //{16, 15, 17, 20}======|=====================|=====================|=============================|
    wumpusMaze[15][0] = 16; wumpusMaze[15][1] = 15; wumpusMaze[15][2] = 17; wumpusMaze[15][3] = 20;
    
    //{17, 7, 16, 18}======|=====================|=====================|==============================|
    wumpusMaze[16][0] = 17; wumpusMaze[16][1] = 7; wumpusMaze[16][2] = 16; wumpusMaze[16][3] = 18;
    
    //{18, 9, 17, 19}======|=====================|=====================|==============================|
    wumpusMaze[17][0] = 18; wumpusMaze[17][1] = 9; wumpusMaze[17][2] = 17; wumpusMaze[17][3] = 19;
    
    //{19, 11, 18, 20}======|=====================|=====================|=============================|
    wumpusMaze[18][0] = 19; wumpusMaze[18][1] = 11; wumpusMaze[18][2] = 18; wumpusMaze[18][3] = 20;
    
    //{20, 13, 16, 19}======|=====================|=====================|=============================|
    wumpusMaze[19][0] = 20; wumpusMaze[19][1] = 13; wumpusMaze[19][2] = 16; wumpusMaze[19][3] = 19;
}


void monsterMoves(int** wumpusMaze);

//Done => displays the Maze layout to a player
void displayCave(void){
    
    printf( "       ______18______             \n"
            "      /      |       \\           \n"
            "     /      _9__      \\          \n"
            "    /      /    \\      \\        \n"
            "   /      /      \\      \\       \n"
            "  17     8        10     19       \n"
            "  | \\   / \\      /  \\   / |    \n"
            "  |  \\ /   \\    /    \\ /  |    \n"
            "  |   7     1---2     11  |       \n"
            "  |   |    /     \\    |   |      \n"
            "  |   6----5     3---12   |       \n"
            "  |   |     \\   /     |   |      \n"
            "  |   \\       4      /    |      \n"
            "  |    \\      |     /     |      \n"
            "  \\     15---14---13     /       \n"
            "   \\   /            \\   /       \n"
            "    \\ /              \\ /        \n"
            "    16---------------20           \n"
            "\n");
    
}


//Done => displays the provided instructions to a player
void displayInstructions(int** wumpusMaze){
    
    printf( "Hunt the Wumpus:                                             \n"
            "The Wumpus lives in a completely dark cave of 20 rooms. Each \n"
            "room has 3 tunnels leading to other rooms.                   \n"
            "                                                             \n"
            "Hazards:                                                     \n"
            "1. Two rooms have bottomless pits in them.  If you go there you fall and die.   \n"
            "2. Two other rooms have super-bats.  If you go there, the bats grab you and     \n"
            "   fly you to some random room, which could be troublesome.  Then those bats go \n"
            "   to a new room different from where they came from and from the other bats.   \n"
            "3. The Wumpus is not bothered by the pits or bats, as he has sucker feet and    \n"
            "   is too heavy for bats to lift.  Usually he is asleep.  Two things wake       \n"
            "    him up: Anytime you shoot an arrow, or you entering his room.  The Wumpus   \n"
            "    will move into the lowest-numbered adjacent room anytime you shoot an arrow.\n"
            "    When you move into the Wumpus' room, then he wakes and moves if he is in an \n"
            "    odd-numbered room, but stays still otherwise.  After that, if he is in your \n"
            "    room, he snaps your neck and you die!                                       \n"
            "                                                                                \n"
            "Moves:                                                                          \n"
            "On each move you can do the following, where input can be upper or lower-case:  \n"
            "1. Move into an adjacent room.  To move enter 'M' followed by a space and       \n"
            "   then a room number.                                                          \n"
            "2. Shoot your guided arrow through a list of up to three adjacent rooms, which  \n"
            "   you specify.  Your arrow ends up in the final room.                          \n"
            "   To shoot enter 'S' followed by the number of rooms (1..3), and then the      \n"
            "   list of the desired number (up to 3) of adjacent room numbers, separated     \n"
            "   by spaces. If an arrow can't go a direction because there is no connecting   \n"
            "   tunnel, it ricochets and moves to the lowest-numbered adjacent room and      \n"
            "   continues doing this until it has traveled the designated number of rooms.   \n"
            "   If the arrow hits the Wumpus, you win! If the arrow hits you, you lose. You  \n"
            "   automatically pick up the arrow if you go through a room with the arrow in   \n"
            "   it.                                                                          \n"
            "3. Enter 'R' to reset the person and hazard locations, useful for testing.      \n"
            "4. Enter 'C' to cheat and display current board positions.                      \n"
            "5. Enter 'D' to display this set of instructions.                               \n"
            "6. Enter 'P' to print the maze room layout.                                     \n"
            "7. Enter 'X' to exit the game.                                                  \n"
            "                                                                                \n"
            "Good luck!                                                                      \n"
            " \n\n");
    
   

    //I use this code to display the appropriate message depending on user's location:
    //If a player on the Maze is close to Wumpus (1 tunnel away) => print the scary message
    //If a player is 1 tunnel away from the pit => then he/she will feel a draft;
    //Same with the bats.
    monsterMoves(wumpusMaze);
}


//Done => used to free the memory after the program termination
void memoryCleaner(int** wumpusMaze, size_t* mazeRows){
    
   int j = 0;
    
    do{
       free(wumpusMaze[j]);
       wumpusMaze[j] = 0;
       j++;
       
    }while(j < mazeRows);
    
    free(wumpusMaze);
    wumpusMaze = 0;
}


//Done => allows a user to exit a program
void quit(int** wumpusMaze, size_t* mazeRows){
    
    //memoryCleaner(wumpusMaze, mazeRows); //FIXME: memory clean!!!!
    playerAlive = false;
    printf("\n");
    printf("Exiting Program ...\n");
}


//Done => accepts a digit from a user to activate the Move() function
int getUserNumber(char* displayMessage){

    int userNumber = 0;
    printf("%s: ", displayMessage);
    
    do{
        scanf("%d", &userNumber);
        
    }while(userNumber == 0);
    
    int result = userNumber;
  
    return result;
}


//Done => accepts a letter from a user to activate the switch() statement
int getUserLetter(char* displayMessage){

    char userLetterInput = '\n';
    
    printf("%s: ", displayMessage);
    
    do{
        scanf("%c", &userLetterInput);
        
    }while(userLetterInput == '\n');
    
    char result = toupper(userLetterInput);
  
    return result;
}


//Done => accepts a letter from a user to activate the switch() statement
int getLetterToMove(void){

    char userLetterInput = '\n';
    
    do{
        scanf("%c", &userLetterInput);
        
    }while(userLetterInput == '\n');
    
    char result = toupper(userLetterInput);
  
    return result;
}


//Done => produces the output when a player falls into a pit
void pitFall(int** wumpusMaze, size_t* mazeRows){
    
    printf("Aaaaaaaaahhhhhh....   \n");
    printf("    You fall into a pit and die. \n");
    //memoryCleaner(wumpusMaze, mazeRows); //FIXME: memory clean!!!
    quit(wumpusMaze, mazeRows);
}


//Done => produces the output depending on the Wumpus' location (If Wumpus won)
void wumpusWon(int** wumpusMaze, size_t* mazeRows){
    
    printf(    "You briefly feel a slimy tentacled arm as your neck is snapped. \n"
            "It is over.\n");
    //memoryCleaner(wumpusMaze, mazeRows); //FIXME: memory clean!!!
    quit(wumpusMaze, mazeRows);
}


//Done => I use this to organize my code inside Move() => produces the output depending on the Wumpus' location
void wumpusEscaped(void){

    printf( "You hear a slithering sound, as the Wumpus slips away. \n"
            "Whew, that was close! \n");
    
}


//Done => I use this to organize my code inside Move() => produces the output depending on the Wumpus' location
void invalidMove(void){
    
    printf("Invalid move.  Please retry.\n");
    //printf("\n"); //REMOVE LATER
    //printf("You are in room %d", currentPlayerLocation);
    //printf(".");
    //printf("\n\n");
}


//Done => I use this to organize my code inside Move() => produces the output depending on the Wumpus' location
void monsterMoves(int** wumpusMaze){

    printf( "You are in room %d. ", currentPlayerLocation);
    //printf(".");
    
    unsigned int j = 0;
    
    //Since we have 3 tunnels, the total count of them MUST be equal to 3, so from 1 to 4
    for(j = 1; j < 4; j++){
        if(currentWumpusLocation == wumpusMaze[currentPlayerLocation - 1][j]){
            printf("You smell a stench. ");
        }
    }
    
    for(j = 1; j < 4; j++){
        if(currentPit1Location == wumpusMaze[currentPlayerLocation -1][j] || currentPit2Location == wumpusMaze[currentPlayerLocation - 1][j]){
            printf("You feel a draft. ");
        }
    }
    
    for(j = 0; j < 4; j++){
        if(currentBat1Location == wumpusMaze[currentPlayerLocation - 1][j] || currentBat2Location == wumpusMaze[currentPlayerLocation - 1][j]){
            printf("You hear rustling of bat wings. ");
        }
    }
    
    printf("\n\n");
}


//Done => refills arrows if one is found
void ammo(void){
    
    currentArrowLocation = -1;
    printf("Congratulations, you found the arrow and can once again shoot.\n\n");
    
}


//Done => if the player's location is the same with the bats' location, they take a player and move him to a random room.
//If a random room contains a pit or Wumpus => the player dies.
void teleport(int** wumpusMaze, size_t* mazeRows){
    
    
    if(currentPlayerLocation == currentBat2Location){
        currentPlayerLocation = rand() % 20 + 1;
        int pos = currentBat2Location;
    
        currentBat2Location = rand() % 20 + 1;
        while((currentBat1Location == pos) || (currentBat2Location == currentBat1Location)){
            currentBat1Location = rand() % 20 + 1;
        }
    
        printf("Woah... you're flying!\nYou've just been transported by bats to room %d.\n", currentPlayerLocation);
    
        monsterMoves(wumpusMaze);
    }
    

    if(currentPlayerLocation == currentBat1Location){
        currentPlayerLocation = rand() % 20 + 1;
        int pos2 = currentBat1Location;
    
        currentBat1Location = rand() % 20 + 1;
        while((currentBat1Location == currentBat2Location) || (currentBat1Location == pos2)){
            currentBat1Location = rand() % 20 + 1;
        }
    
        printf("Woah... you're flying!\nYou've just been transported by bats to room %d.\n", currentPlayerLocation);
    
        if(currentPlayerLocation == currentPit2Location || currentPlayerLocation == currentPit1Location){
            pitFall(wumpusMaze, mazeRows);
        }
        else if(currentPlayerLocation == currentWumpusLocation){
            wumpusWon(wumpusMaze, mazeRows);
        }
    
        monsterMoves(wumpusMaze);
    }
}


//Done => check the result of the ricochet and displays it => part I
void killshot(void){
    
    //currentArrowLocation = wumpusMaze[currentArrowLocation - 1][1];
    
    if(currentArrowLocation == currentPlayerLocation){
        printf("You just shot yourself, and are dying.\nIt didn't take long, you're dead.\n\nExiting Program ...");
        exit(0);
    }
    
    if(currentPlayerLocation == currentWumpusLocation){
        printf("Your arrow ricochet killed the Wumpus, you lucky dog!\nAccidental victory, but still you win!\n\nExiting Program ...");
        exit(0);
    }
    
}


//Done => check the result of the ricochet and displays it => part II
void fatality(int* x){
    
    while(true){
        if(currentArrowLocation == currentWumpusLocation){
            printf("Wumpus has just been pierced by your deadly arrow!\nCongratulations on your victory, you awesome hunter you.\n\nExiting Program ...");
            exit(0); //FIXME: must terminate the program!!!!!!
        }
        else if(currentArrowLocation == currentPlayerLocation){
            printf("You just shot yourself.\nMaybe Darwin was right. You're dead.\n\nExiting Program ...");
            exit(0); //FIXME: must terminate the program!!!!!!
        }
        else{
            break;
        }
    }
}


//Done => this function moves a player around the maze
void Move(int* moveNumber, int** wumpusMaze, size_t* mazeRows){
    
    int userTunnelChoice;
    static int round = 1; //new incrementor
    char userChoice = 'M';
    bool generator = true; //Generator = the heart of my loop. While it beats => we can move
 
   do{
        incrementor = 1; //incrementor
        
        //printf(".");
        //printf(" ");
        incrementor += 1;
        
        
        if(userChoice == 'M'){
               //printf("%d. ", *moveNumber);
               //printf(". Enter your move (or 'D' for directions): ");
               //printf("\n");
               bool engine = false; //Engine = traffic lights: 0 = red (Stop), 1 = green (Move)
               scanf(" %d", &userTunnelChoice);
            
               for(unsigned int j = 4; j > 0; j--){
                   if(userTunnelChoice == wumpusMaze[currentPlayerLocation - 1][j]){
                       engine = true;
                       currentPlayerLocation = userTunnelChoice; //Move to the new location
                       *moveNumber++; //Increment the counter at the beginning of the printf()
                       generator = false;
                       break;
                       
                   }else{
                       engine = false;
                   }
               }

           //Below: if user's move is valid, and the new location == pits'/wumpus' location (Wumpus is in the odd room number) => the function kills a player and terminates the loop. If room number is odd, then Wumpus moves to another location.
           if(engine == true){
               
               if(currentPlayerLocation == currentPit1Location || currentPlayerLocation == currentPit2Location){
                   pitFall(wumpusMaze, mazeRows);
                   generator = false;
                   break;
               }
               
               //Check if the player found a new arrow
               if(currentPlayerLocation == currentArrowLocation){
                   ammo();
               }
               
               else if(currentPlayerLocation == currentWumpusLocation){
                   
                   //Check the even numbered rooms
                   if((currentWumpusLocation % 2) == 0){
                       wumpusWon(wumpusMaze, mazeRows);
                       generator = false;
                       break;
                   }
                   
                   else{
                       wumpusEscaped();
                       currentWumpusLocation = wumpusMaze[currentWumpusLocation - 1][1];
                       monsterMoves(wumpusMaze);
                       continue;
                   }
               }
               else if(currentPlayerLocation == currentBat1Location){
                   
                   teleport(wumpusMaze, mazeRows);
                   continue;
               }
               else if(currentPlayerLocation == currentBat2Location){
                   
                   teleport(wumpusMaze, mazeRows);
                   continue;
               }
               else{
                   
                   monsterMoves(wumpusMaze);
                   continue;
               }
           }
           else{
               invalidMove();
               (*moveNumber)--;
               monsterMoves(wumpusMaze);
               break;
           }
       }
   }while(generator);
}


//Done => the shoot() function which accepts the dynamically allocated array as a parameter
//Shots an arrow in a selected direction. If the target was met => display the message
void Shoot(int* moveNumber, int** wumpusMaze){
    
    if(currentArrowLocation == -1){
        
        //Allocate space for 3 integers around the wumpusMaze
        int* battlefield = malloc(3 * sizeof(int));
        int shots;
        int targets;
        bool guess = false; //True => rooms are adjacent; false => not adjacent
        currentArrowLocation = currentPlayerLocation;
        
        printf("Enter the number of rooms (1..3) into which you want to shoot, followed by the rooms themselves: ");
        scanf("%d", &shots);
        
        int k = 0;
        
        //Accept the number of shots via input
        do{
            scanf("%d", &targets);
            battlefield[k] = targets;
            k++;
            
        }while(k < shots);
        
        
        for(int i = 0; i < shots; i++){
            for(int j = 0; j < 4; j++){
                if(battlefield[i] == wumpusMaze[currentArrowLocation - 1][j]){
                    currentArrowLocation = battlefield[i];
                    guess = true;
                    int x = currentArrowLocation;
                    fatality(&x);
                }
            }
            
            if(guess == false){
                printf("Room %d is not adjacent. Arrow ricochets...\n\n", battlefield[i]);
                currentArrowLocation = wumpusMaze[currentArrowLocation - 1][1];
                killshot();
                break;
            }
            
            guess = false;
        }
        
        currentWumpusLocation = wumpusMaze[currentWumpusLocation - 1][1];
        moveNumber++;
        free(battlefield);
        battlefield = NULL;
        
    }
    else{
        printf("Sorry, you can't shoot an arrow you don't have. Go find it.\n");
        printf("You are in room %d", currentPlayerLocation);
        printf(". \n\n");
        moveNumber++;
    }
}


//Done: randomly sets all game elements on the map
void setLocations(void){
    
    srand(1);
    //Get position of player, Wumpus, pit1, pit2, bat1, bat2, arrow respectively with no duplicates
    /*currentWumpusLocation = rand() % 20 + 1;
    currentPlayerLocation = rand() % 20 + 1;
    currentPit1Location = rand() % 20 + 1;
    currentPit2Location = rand() % 20 + 1;
    currentBat1Location = rand() % 20 + 1;
    currentBat2Location = rand() % 20 + 1;
    currentArrowLocation = rand() % 20 + 1;*/

    /*
    srand(1);

        // Variable declaration goes here
        int moveCounter = 1;
        char userInput;
        int userMove;
        int endCondition = 0;

        // Get position of player, Wumpus, pit1, pit2, bat1, bat2, arrow respectively with no duplicates
        int positionOfPlayer = rand() % 20 + 1;
        int positionOfWumpus = rand() % 20 + 1;
        while ( positionOfWumpus == positionOfPlayer ) {
            positionOfWumpus = rand() % 20 + 1;
        }
        int positionOfPit1 = rand() % 20 + 1;
        while ( (positionOfPit1 == positionOfPlayer) || (positionOfPit1 == positionOfWumpus) ) {
            positionOfPit1 = rand() % 20 + 1;
        }
        int positionOfPit2 = rand() % 20 + 1;
        while ( (positionOfPit2 == positionOfPlayer) || (positionOfPit2 == positionOfWumpus) || (positionOfPit2 == positionOfPit1) ) {
            positionOfPit2 = rand() % 20 + 1;
        }
        int positionOfBat1 = rand() % 20 + 1;
        while ( (positionOfBat1 == positionOfPlayer) ||  (positionOfBat1 == positionOfWumpus) || (positionOfBat1 == positionOfPit1) || (positionOfBat1 == positionOfPit2) ) {
            positionOfBat1 = rand() % 20 + 1;
        }
        int positionOfBat2 = rand() % 20 + 1;
        while ( (positionOfBat2 == positionOfPlayer) ||  (positionOfBat2 == positionOfWumpus) || (positionOfBat2 == positionOfPit1) || (positionOfBat2 == positionOfPit2) || (positionOfBat2 == positionOfBat1) ) {
            positionOfBat2 = rand() % 20 + 1;
        }
        int positionOfArrow = rand() % 20 + 1;
        while ( (positionOfArrow == positionOfPlayer) ||  (positionOfArrow == positionOfWumpus) || (positionOfArrow == positionOfPit1) || (positionOfArrow == positionOfPit2) || (positionOfArrow == positionOfBat1) || (positionOfArrow == positionOfBat2) ) {
            positionOfArrow = rand() % 20 + 1;
        }
        
        // Declaration of variables for dynamic array
        size_t gameTableSize = 20;
        size_t gameTableColumnSize = 4;
        int** gameTable = malloc(sizeof(int*) * gameTableSize);
        
        // Creates the dynamically allocated gameTable
        for (int i = 0; i < gameTableSize; i++) {
            gameTable[i] = malloc(gameTableColumnSize * sizeof(int));
        }
        fillInGameTable(gameTable);
    */
    
    
    currentPlayerLocation = rand() % 20 + 1;
    currentWumpusLocation = rand() % 20 + 1;
    while(currentWumpusLocation == currentPlayerLocation){
        currentWumpusLocation = rand() % 20 + 1;
    }
    
    currentPit1Location = rand() % 20 + 1;
    while((currentPit1Location == currentPlayerLocation) || (currentPit1Location == currentWumpusLocation) ) {
        currentPit1Location = rand() % 20 + 1;
    }
    
    currentPit2Location = rand() % 20 + 1;
    while((currentPit2Location == currentPlayerLocation) || (currentPit2Location == currentWumpusLocation) || (currentPit2Location == currentPit1Location)){
        currentPit2Location = rand() % 20 + 1;
    }
    
    currentBat1Location = rand() % 20 + 1;
    while((currentBat1Location == currentPlayerLocation) ||  (currentBat1Location == currentWumpusLocation) || (currentBat1Location == currentPit1Location) || (currentBat1Location == currentPit2Location) ) {
        currentBat1Location = rand() % 20 + 1;
    }
    
    currentBat2Location = rand() % 20 + 1;
    while((currentBat2Location == currentPlayerLocation) ||  (currentBat2Location == currentWumpusLocation) || (currentBat2Location == currentPit1Location) || (currentBat2Location == currentPit2Location) || (currentBat2Location == currentBat1Location) ) {
        currentBat2Location = rand() % 20 + 1;
    }
    
    currentArrowLocation = rand() % 20 + 1;
    while ((currentArrowLocation == currentPlayerLocation) ||  (currentArrowLocation == currentWumpusLocation) || (currentArrowLocation == currentPit1Location) || (currentArrowLocation == currentPit2Location) || (currentArrowLocation == currentBat1Location) || (currentArrowLocation == currentBat2Location) ) {
        currentArrowLocation = rand() % 20 + 1;
    }
    
    
    
    
/*
    while((currentPlayerLocation == currentPit1Location) || (currentPlayerLocation == currentPit2Location) || (currentPlayerLocation == currentBat1Location) || (currentPlayerLocation == currentBat2Location) || (currentPlayerLocation == currentWumpusLocation) || (currentPlayerLocation == currentArrowLocation)){
        currentPlayerLocation = rand() % 20 + 1;
        
        if(currentPlayerLocation == currentPit2Location || currentPlayerLocation == currentPit1Location){
            currentPlayerLocation = rand() % 20 + 1;
        }
    }

    //int currentPit1Location = rand() % 20 + 1;
    while((currentPit1Location == currentPlayerLocation) || (currentPit1Location == currentWumpusLocation)){
        currentPit1Location = rand() % 20 + 1;
    }

    //int positionOfPit2 = rand() % 20 + 1;
    while((currentPit2Location == currentPlayerLocation) || (currentPit2Location == currentWumpusLocation) || (currentPit2Location == currentPit1Location)){
        currentPit2Location = rand() % 20 + 1;
    }

    //int positionOfBat1 = rand() % 20 + 1;
    while((currentBat1Location == currentPlayerLocation) ||  (currentBat1Location == currentWumpusLocation) || (currentBat1Location == currentPit1Location) || (currentBat1Location == currentPit2Location)){
        currentBat1Location = rand() % 20 + 1;
    }

    //int positionOfBat2 = rand() % 20 + 1;
    while((currentBat2Location == currentPlayerLocation) ||  (currentBat2Location == currentWumpusLocation) || (currentBat2Location == currentPit1Location) || (currentBat2Location == currentPit2Location) || (currentBat2Location == currentBat1Location)){
        currentBat2Location = rand() % 20 + 1;
    }

    //int positionOfArrow = rand() % 20 + 1;
    while((currentArrowLocation == currentPlayerLocation) ||  (currentArrowLocation == currentWumpusLocation) || (currentArrowLocation == currentPit1Location) || (currentArrowLocation == currentPit2Location) || (currentArrowLocation == currentBat1Location) || (currentArrowLocation == currentBat2Location)){
        currentArrowLocation = rand() % 20 + 1;
    }*/
    
}


//Done => sets Wumpus' location
void monstaLocations(void){
    
    do{
        currentWumpusLocation = rand() % 20 + 1;
        
    }while(currentWumpusLocation == currentPit2Location || currentWumpusLocation == currentPit1Location);
    
}


//Done => sets pits' locations
void pitsLocations(void){
    
    do{
        currentPit2Location = rand() % 20 + 1;
        currentPit1Location = rand() % 20 + 1;
        
    }while(currentPit2Location == currentPit1Location || currentPit2Location == currentWumpusLocation || currentPit1Location == currentPit2Location || currentPit1Location == currentWumpusLocation);
    
}


//Done => reset the current locations of all game elements depending on the user input
void reset(int** wumpusMaze){
    
    int resetPlayerR, resetWumpusR, resetpit1R, resetpit2R, resetBat1R, resetBat2R, resetArrow;
    int newPlayerR, newWumpusR, newPit1R, newPit2R, newBat1R, newBat2R, newArrow;
   
    
    printf("Enter the room locations (1..20) for player, wumpus, pit1, pit2, bats1, bats2, and arrow: \n");
    scanf("%d %d %d %d %d %d %d", &resetPlayerR, &resetWumpusR, &resetpit1R, &resetpit2R, &resetBat1R, &resetBat2R, &resetArrow);
    
    
    currentPlayerLocation = resetPlayerR;
    currentWumpusLocation = resetWumpusR;
    currentPit1Location = resetpit1R;
    currentPit2Location = resetpit2R;
    currentBat1Location = resetBat1R;
    currentBat2Location = resetBat2R;
    currentArrowLocation = resetArrow;
    
    do{
        newPit2R = rand() % 20 + 1;
    }while(currentPit2Location == currentPit1Location);
    
    do{
        newPit2R = rand() % 20 + 1;
    }while(currentPit2Location == currentWumpusLocation);
    
    do{
        newPit2R = rand() % 20 + 1;
    }while(currentPit2Location == currentWumpusLocation);
    
    do{
        newWumpusR = rand() % 20 + 1;
    }while(currentWumpusLocation == currentPit2Location);
    
    do{
        newPlayerR = rand() % 20 + 1;
    }while(currentPlayerLocation == currentWumpusLocation);
    
    do{
        newPit1R = rand() % 20 + 1;
    }while(currentPit1Location == currentPlayerLocation);
    
    do{
        newPit1R = rand() % 20 + 1;
    }while(currentPit1Location == currentWumpusLocation);
    
    do{
        newWumpusR = rand() % 20 + 1;
    }while(currentWumpusLocation == currentPlayerLocation);
    
    do{
        newBat1R = rand() % 20 + 1;
    }while((currentBat1Location == currentPlayerLocation) || (currentBat1Location == currentWumpusLocation));
    
    do{
        newBat1R = rand() % 20 + 1;
    }while((currentBat1Location == currentPit1Location) || (currentBat1Location == currentPit2Location));
    
    do{
        newBat2R = rand() % 20 + 1;
    }while((currentBat2Location == currentPlayerLocation) || (currentBat2Location == currentWumpusLocation));
    
    do{
        newBat2R = rand() % 20 + 1;
    }while((currentBat2Location == currentPit1Location) || (currentBat2Location == currentPit2Location));
    
    do{
        newArrow = rand() % 20 + 1;
    }while((currentArrowLocation == currentPlayerLocation) || (currentArrowLocation == currentWumpusLocation));
    
    do{
        newArrow = rand() % 20 + 1;
    }while((currentArrowLocation == currentBat1Location) || (currentArrowLocation == currentBat2Location));
    
    do{
        newArrow = rand() % 20 + 1;
    }while((currentArrowLocation == currentPit1Location) || (currentArrowLocation == currentPit2Location));
    
    
    printf("\n");
    monsterMoves(wumpusMaze);
}


//Done => see the current locations of all game elements
void cheating(int** wumpusMaze){
    
    printf( "Cheating! Game elements are in the following rooms: \n"
           "Player Wumpus Pit1 Pit2 Bats1 Bats2 Arrow \n"
           "%4d %5d %6d %5d %5d %5d %5d\n\n",
            currentPlayerLocation,
            currentWumpusLocation,
            currentPit1Location,
            currentPit2Location,
            currentBat1Location,
            currentBat2Location,
            currentArrowLocation);
    
    monsterMoves(wumpusMaze);
}


//Done => guess the room where Wumpus is hiding => if you fail, you lose
void guess(int** wumpusMaze, size_t* mazeRows){
    
    int number = getUserNumber("Enter room (1..20) you think Wumpus is in");
    
    if(number == currentWumpusLocation){
        printf("You won!\n");
        quit(wumpusMaze, mazeRows);
    }
    else{
        printf("You lost.\n");
        quit(wumpusMaze, mazeRows);
    }
}


//Done => Checks if 2 rooms are adjacent to each other. If so => return true. Else => return false
//I use it to check if we are next to pit1, pit2 or wumpus + valid moves
bool checkIfAdjacent(int tunnel1, int tunnel2, int** wumpusMaze){
    
    for(unsigned int j = 0; j < 3; j++){
        if(wumpusMaze[tunnel1][j] == tunnel2){
          return true;
        }
        else{
            return false;
        }
    }
    
    return false;
}


//Done => Checks if the input room is valid => if so, move there. If not => stay where you are (Range: 0 to 20 + MUST be adjacent)
bool checkMove(int playersRoomChoice, int** wumpusMaze){
    
    if(playersRoomChoice < 1 || playersRoomChoice > rooms){
        if(checkIfAdjacent(currentPlayerLocation, playersRoomChoice, wumpusMaze) == false){
            return false;
        }
        else{
            return true;
        }
    }
   return true;
}


//Done: command controller => choose option using switch() based on the input from a player
void commands(int* moveNumber, int** wumpusMaze, size_t* mazeRows){

    //Sent as a parameter from main => catch with an asterisk
    printf("%d", *moveNumber);
    char choice = getUserLetter(". Enter your move (or 'D' for directions)");
    
    switch(choice){
        case 'X':
            quit(wumpusMaze, mazeRows);
            break;
        case 'P':
            printf("\n");
            displayCave();
            monsterMoves(wumpusMaze);
            return;
        case 'D':
            printf("\n");
            displayCave();
            displayInstructions(wumpusMaze);
            return;
        case 'C':
            cheating(wumpusMaze);
            return;
        case 'R':
            reset(wumpusMaze);
            return;
        case 'G':
            guess(wumpusMaze, mazeRows);
            break;
        case 'M':
            Move(moveNumber, wumpusMaze, mazeRows);
            (*moveNumber)++; //Use with an asterisk => increment by 1 each time player's move is valid
            break;
            
        //FIXME: UNCOMMENT!!!!!
        case 'S':
            Shoot(moveNumber, wumpusMaze); //Must be a list of numbers separated by spaces
            (*moveNumber)++; // Might use something similar
            break;
    }
}


int main(){
    
    //srand(time(0));
    int moveNumber = 1; //Increment by 1 + move switch in main()
    //In this step we create the Dynamically Allocated Array
    size_t mazeRows = 20;
    size_t mazeColumns = 4;
    
    //srand(1);
    playerAlive = false;
    wumpusAlive = false;
    setLocations();
    
    //Important: your program starts you should use malloc to allocate space for the rooms array
    int** wumpusMaze = malloc(sizeof(int*) * mazeRows);
    

    for(int i = 0; i < mazeRows; i++) {
        wumpusMaze[i] = malloc(mazeColumns * sizeof(int));
    }
    
    loader(wumpusMaze);
    monsterMoves(wumpusMaze);

    
    //FIXME: uncomment if needed
    /*printf( "You are in room %d", currentPlayerLocation);
    printf(". ");
    printf("\n");
    printf("\n");*/
    
    
    do{
        playerAlive = true;
        wumpusAlive = true;
        commands(&moveNumber, wumpusMaze, &mazeRows); //Pass with an ampersand
        
    }while (playerAlive == true);
    
    
    memoryCleaner(wumpusMaze, mazeRows);
    
    return 0;
}



