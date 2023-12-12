import javafx.scene.control.Button;

import java.io.Serializable;

public class GameButton extends Button implements Serializable {

    //Step 1: declare the variables for the entire game associated with the button
    int Col;
    int Row;
    boolean isValid;
    int currentPlayer;
    int roundCounter;

    //Initialize the constructor for the GameButton Class
    public GameButton(int row, int col) {
        this.Col = col;
        this.Row = row;
        this.roundCounter = 0;
        isValid = false;
        currentPlayer = 0;
    }

    public Object getRow() {
        return Row;
    }

    public Object getCol() {
        return Col;
    }

    public int getX() {
        return Row;
    }

    public int getY() {
        return Col;
    }

    public void setCol(int col) {
        Col = col;
    }

    public void setRow(int row) {
        Row = row;
    }
}