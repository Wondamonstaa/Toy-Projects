import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.control.TextField;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

public class serverController implements Initializable {

    @FXML
    private Button startServer;

    @FXML
    private VBox eventsVBox;

    @FXML
    private ListView<String> serverView;

    @FXML
    private TextField portText;

    @FXML
    private HBox welcomeBox;

    private Server serverConnection;
    private GameLogic logic;
    private GameInfo data;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {

    }

    public void launch() throws IOException {
        eventsVBox = FXMLLoader.load(getClass().getResource("/serverGUI.fxml"));
        serverView = (ListView<String>) eventsVBox.getChildren().get(0);
        welcomeBox.getScene().setRoot(eventsVBox);
        serverConnection = new Server(data -> {
            Platform.runLater(() -> {
                serverView.getItems().add(data.gameInfo);
            });
        }, Integer.parseInt(portText.getText()));
    }
}