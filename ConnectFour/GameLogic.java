
import javafx.scene.effect.DropShadow;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.VBox;

import java.io.FileNotFoundException;
import java.util.*;


public class GameLogic extends JavaFXTemplate {

    static VBox root = new VBox();
    static ListIterator<Integer> iterator;
    static Stack<GameButton> gameStats = new Stack<>();
    static int playerWon = 0;
    static int moves = 0;

    public void convertBoard(GridPane gb) {

    }

    //Helper function to start the new game + upload the new the board
    public static void NewGameButton(GameButton[][] matrix) {
        for (GameButton[] gameButtons : matrix) {
            for (int j = 0; j < matrix[0].length; j++) {
                gameButtons[j].currentPlayer = 0;
                gameButtons[j].isValid = false;
                gameButtons[j].setPrefSize(100, 100);
                gameButtons[j].setMinSize(100, 100);
                gameButtons[j].setMaxSize(100, 100);
                gameButtons[j].setStyle("-fx-background-color: #24ec5c;");
                gameButtons[j].setEffect(new DropShadow());

                /*gameButtons[j].setOnAction(e -> {
                    int k = 0;
                    if (gameButtons[k].isValid) {
                        gameButtons[k].setStyle("-fx-background-color: #24ec5c;");
                        gameButtons[k].isValid = false;
                    } else {
                        gameButtons[k].setStyle("-fx-background-color: #ec2424;");
                        gameButtons[k].isValid = true;
                    }
                });*/

                gameButtons[j].setDisable(false);
            }
        }

        //Reset the gameInfo
        playerWon = 0;
        gameStats.clear();
//        players.setText("Player 1 choice");
//        displayMessage.setText("");
    }

    public static void nextPlayerMove(int row, int col, GameButton[][] matrix) {

        //The flag means 5 cells => 4 must be connected to win the game, so 5th is not included
        int flag = 5;

        //If the number of rows is less than 5, then we should check if the next Player's move on the selected cell
        //is valid or not
        if (row < flag) {
            //If the move is valid, then we should check if the player won or not
            if (matrix[row + 1][col].isValid) {
                gameEnd(matrix, row, col);
            } else {
                //Invalid move => display the message
                isValidMove(row, col);
            }
        }
        if (row == flag) {
            gameEnd(matrix, row, col);
        }
    }

    //The following function must check positions of both players on the gameBoard
    //If the one of the players correctly connected the required number of cells, then this player wins.
    public static void gameEnd(GameButton[][] matrix, int row, int col) {

        //Here we check if the player connected 4 cells in a row in different diagonals + the Tie Case
        if (playerWin(matrix, matrix[row][col].currentPlayer) || TieCheck(matrix) || playerWon == 0) {
//            displayMessage.setText("[Player 1] Won The Game!");
            System.out.println("[Player 1]: Won The Game!");
            //If the player has won => stop the game and disable the buttons
            for (GameButton[] gameButtons : matrix) {
                for (int j = 0; j < matrix[0].length; j++) {
                    gameButtons[j].setDisable(true);
                }
            }
        } else if (playerWin(matrix, matrix[row][col].currentPlayer) || TieCheck(matrix) || playerWon == 1) {
            System.out.println("[Player 2]: Won The Game!");
//            displayMessage.setText("[Player 2] Won The Game!");
            //If the player has won => stop the game and disable the buttons
            for (GameButton[] gameButtons : matrix) {
                for (int j = 0; j < matrix[0].length; j++) {
                    gameButtons[j].setDisable(true);
                }
            }
        } else {
            System.out.println("[Player 2]: Won The Game!");
//            displayMessage.setText("Player 2 Won The Game!");
            //If the player has won => stop the game and disable the buttons
            for (GameButton[] gameButtons : matrix) {
                for (int j = 0; j < matrix[0].length; j++) {
                    gameButtons[j].setDisable(true);
                }
            }
        }

    }


    //Helper function to check if the game is tie
    public static boolean TieCheck(GameButton[][] matrix) {

        if (playerWon == 0) {
            return boardLoaderTieCase(matrix);
        } else if (playerWon == 1) {
            return boardLoaderTieCase(matrix);
        } else {
            return boardLoaderTieCase(matrix);
        }
    }


    //Helper function to check if a player made a valid move or not => display the appropriate message to the user
    public static void isValidMove(int row, int col) {

//        if (playerWon == 0) {
//            System.out.println("[Player 1]: Not A Valid Move!");
////            displayMessage.setText(String.format("Player 1 moved to %d,%d. NOT valid move. Player 1 choose again.", row, col));
//        } else if (playerWon == 1) {
//            System.out.println("[Player 2]: Not A Valid Move!");
////            displayMessage.setText(String.format("Player 2 moved to %d,%d. NOT valid move. Player 2 choose again.", row, col));
//        } else {
//            System.out.println("[Player 2]: Not A Valid Move!");
////            displayMessage.setText(String.format("Player 2 moved to %d,%d. NOT valid move. Player 2 choose again.", row, col));
//        }


    }


    //Helper function to check if the game is tie => used in TieCheck to reduce the time complexity
    private static boolean boardLoaderTieCase(GameButton[][] matrix) {
        for (GameButton[] gameButtons : matrix) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (gameButtons[j].currentPlayer == 0) {
                    return false;
                }
            }
        }
        System.out.println("Oops, we got a tie!");
//        displayMessage.setText("Tie!");
        return true;
    }

    //The following function checks possible directions for the Connect 4 Game using standard algorithm
    public static boolean playerWin(GameButton[][] matrix, int currentPlayer) {

        // Check for horizontal win: take every button from the gameBoard
        for (GameButton[] gameButtons : matrix) {
            for (int j = 0; j < matrix[0].length; j++) {
                //If there is a match between currentPlayer filled in the cell => proceed
                if (gameButtons[j].currentPlayer == currentPlayer) {
                    //If there is a match between currentPlayer filled in the cell => proceed
                    if (gameButtons[j + 1].currentPlayer == currentPlayer) {
                        //If there is a match between currentPlayer filled in the cell => proceed
                        if (gameButtons[j + 2].currentPlayer == currentPlayer) {
                            //If there is a match between currentPlayer filled in the cell => proceed
                            //Since there is a match 4 times in a row => we got a winner => return true
                            if (gameButtons[j + 3].currentPlayer == currentPlayer) {
                                return true;
                            }
                        }
                    }
                }
            }
        }


        // Check for vertical win
        for (int i = 0; i < matrix.length - 3; i++) {
            for (int j = 0; j < matrix[0].length - 3; j++) {
                //If there is a match between currentPlayer filled in the cell => proceed
                if (matrix[i][j].currentPlayer == currentPlayer) {
                    //If there is a match between currentPlayer filled in the cell => proceed
                    if (matrix[i + 1][j].currentPlayer == currentPlayer) {
                        //If there is a match between currentPlayer filled in the cell => proceed
                        if (matrix[i + 2][j].currentPlayer == currentPlayer) {
                            //If there is a match between currentPlayer filled in the cell => proceed
                            //Since there is a match 4 times in a row => we got a winner => return true
                            if (matrix[i + 3][j].currentPlayer == currentPlayer) {
                                return true;
                            }
                        }
                    }
                }
                //Else => the case is wrong, then return false
                else {
                    return false;
                }
            }
        }


        //Check for diagonal win
        int i = 0;
        while (i < matrix.length) {
            for (int j = 0; j < matrix[0].length - 3; j++) {
                //If there is a match between currentPlayer filled in the cell => proceed
                if (matrix[i][j].currentPlayer == currentPlayer) {
                    //If there is a match between currentPlayer filled in the cell => proceed
                    if (matrix[i][j + 1].currentPlayer == currentPlayer) {
                        //If there is a match between currentPlayer filled in the cell => proceed
                        if (matrix[i][j + 2].currentPlayer == currentPlayer) {
                            //If there is a match between currentPlayer filled in the cell => proceed
                            //Since there is a match 4 times in a row => we got a winner => return true
                            if (matrix[i][j + 3].currentPlayer == currentPlayer) {
                                return true;
                            }
                        }
                    }
                }
            }
            i++;
        }


        int k = 0;
        while (k < matrix.length - 3) {
            for (int j = 0; j < matrix[0].length; j++) {
                //If there is a match between currentPlayer filled in the cell => proceed
                if (matrix[k][j].currentPlayer == currentPlayer) {
                    //If there is a match between currentPlayer filled in the cell => proceed
                    if (matrix[k + 1][j].currentPlayer == currentPlayer) {
                        //If there is a match between currentPlayer filled in the cell => proceed
                        if (matrix[k + 2][j].currentPlayer == currentPlayer) {
                            //If there is a match between currentPlayer filled in the cell => proceed
                            //Since there is a match 4 times in a row => we got a winner => return true
                            if (matrix[k + 3][j].currentPlayer == currentPlayer) {
                                return true;
                            }
                        }
                    } else {
                        if (matrix[k][j].currentPlayer == currentPlayer) {
                            if (matrix[k - 1][j].currentPlayer == currentPlayer) {
                                if (matrix[k - 2][j].currentPlayer == currentPlayer) {
                                    if (matrix[k - 3][j].currentPlayer == currentPlayer) {
                                        return true;
                                    }
                                }
                            }
                        }
                    }
                }
                k++;
            }
            return false;
        }

        return false;
    }
}

