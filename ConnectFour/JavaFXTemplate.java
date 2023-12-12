import javafx.animation.FadeTransition;
import javafx.animation.PauseTransition;
import javafx.animation.RotateTransition;
import javafx.animation.SequentialTransition;
import javafx.application.Application;

import javafx.application.Platform;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;
import javafx.stage.WindowEvent;
import javafx.util.Duration;

public class JavaFXTemplate extends Application {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		launch(args);
//		Server test = new Server(data -> {
//			System.out.println("CLI debugging for Server.");
//			System.out.println("Info from data class: ");
//			data.printInfo();
//		}, 5000);

	}


	//feel free to remove the starter code from this method
	@Override
	public void start(Stage primaryStage) throws Exception {
		// TODO Auto-generated method stub
		primaryStage.setTitle("Project 3 Connect 4 Server");

		Parent scene1 = FXMLLoader.load(getClass().getResource("/welcome.fxml"));
		Parent scene2 = FXMLLoader.load(getClass().getResource("/serverGUI.fxml"));


		Scene welcome = new Scene(scene1, 300, 400);
		primaryStage.setScene(welcome);

		primaryStage.setOnCloseRequest(new EventHandler<WindowEvent>() {
			@Override
			public void handle(WindowEvent t) {
				Platform.exit();
				System.exit(0);
			}
		});

		primaryStage.show();

	}

}