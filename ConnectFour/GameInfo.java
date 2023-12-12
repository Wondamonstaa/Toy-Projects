import java.io.Serializable;

public class GameInfo implements Serializable{

    //Step 1: Declare the variables
    GameButton[][] gameBoard; //game board in matrix format
    int counter; //Counter for the number of moves
    boolean isRunning; //True => game in progress, False => game over
    int gameTurn; //Count the number of turns in the game
    int curRow; //Current row the play has chosen to make a move
    int curCol; //Current column the play has chosen to make a move
    String gameInfo; //Displays information about the current status of the game
    int playerID = 1; //Tracks player number
    int playerWin; //Represents who won the game, when zero game is still in progress.


    //Step 2: Initialize the default constructor
    public GameInfo(){

//        gameBoard = new int[6][7];
        gameBoard = new GameButton[7][6];
        counter = 0;
        isRunning = false;
        gameTurn = 0;
        curRow = -1;
        curCol = -1;
        gameInfo = "";
    }

    public void printInfo() {
        System.out.println("\n" + gameBoard + "\n");
        System.out.println("Counter: " + counter);
        System.out.println("Is running: " + isRunning);
        System.out.println("Game Turn: " + gameTurn);
        System.out.println("Current Column: " + curCol);
        System.out.println("Current Row: " + curRow);
        System.out.println("GameInfo: " + gameInfo);
        System.out.println("Player ID: " + playerID);
        System.out.println("Player Win: " + playerWin);
    }
}

