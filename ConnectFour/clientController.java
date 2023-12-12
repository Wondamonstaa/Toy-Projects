import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.geometry.Insets;
import javafx.scene.Node;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import javafx.util.Pair;

import java.io.IOException;
import java.net.URL;
import java.util.ArrayList;
import java.util.ResourceBundle;
import java.util.Timer;
import java.util.TimerTask;

public class clientController implements Initializable {

    @FXML
    private VBox root;

    @FXML
    private TextField ipText;

    @FXML
    private TextField portText;

    @FXML
    private Button startButton;

    @FXML
    private BorderPane root2;

    @FXML
    private ListView<String> eventsList;

    @FXML
    private VBox playBox;

    @FXML
    private GridPane gameBoard;

    @FXML
    private Button makeMove;


    Client player;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {

    }

    public void startGame() throws IOException {
        root2 = FXMLLoader.load(getClass().getResource("/clientPlay.fxml"));

        //FIXME: right here i used the style sheet i created. I will upload it later.
        //root2.getStylesheets().add("/styles/style2.css");//set style
        root.getScene().setRoot(root2);
        playBox = (VBox) root2.getLeft();
        gameBoard = (GridPane) root2.getCenter();
        makeMove = (Button) playBox.getChildren().get(1);
        eventsList = (ListView<String>) playBox.getChildren().get(0);
        Stage primary = (Stage) eventsList.getScene().getWindow();
        GameButton[][] logicalBoard = new GameButton[7][6];

        System.out.println("Client connecting...");

        player = new Client(data -> {
            Platform.runLater(() -> {
                eventsList.getItems().add(data.gameInfo);
            });
        }, ipText.getText(), Integer.parseInt(portText.getText()));

        for (int i = 0; i < 7; i++){
            for (int j = 0; j < 6; j++){

                //Create a button with the specified coordinates
                player.data.gameBoard[i][j] = new GameButton(i, j);
                GameButton button = player.data.gameBoard[i][j];

                //Populate the gameBoard with the buttons
                gameBoard.add(button, i, j);
                logicalBoard[i][j] = button;

                //Set each button on Action using lambda expression
                button.setOnAction(e -> {

                    //get the coordinates of the button
                    int x = button.getX();
                    int y = button.getY();
                    player.data.curCol = y;
                    player.data.curRow = x;
                    player.data.gameInfo = "Player " + player.data.playerID + " made a move at (" + x + ", " + y + ")";
                    if (player.data.playerID == 1) {
                        button.setStyle("-fx-background-color: red");
                        button.setDisable(true);
                    } else if (player.data.playerID == 2) {
                        button.setStyle("-fx-background-color: yellow");
                        button.setDisable(true);
                    }

                    // Add player input to gameboard and update board
                    player.data.curCol = button.Col;
                    player.data.curRow = button.Row;
                    player.data.gameBoard[button.Row][button.Col].isPressed();

                    //check if button is clicked
                    System.out.println("Button clicked: " + button.Row + " " + button.Col);
                    System.out.println("Player " + player.data.playerID + " made a move at (" + x + ", " + y + ")");

                });

                makeMove.setOnAction(e ->{
                    // Use game logic to determine if move is valid and if any win conditions have been met
                    // If a win condition is met, flag in game info and send info to server.
//                    gameBoard.setDisable(false);

                    GameLogic.isValidMove(player.data.curRow, player.data.curCol);
                    player.send(player.data);
                });


            }
            primary.setTitle("Player " + player.data.playerID + " client");
        }



        player.start();
    }

}