/*
Name: Kiryl Baravikou
Course: CS 342
Project: 4
Professor: Mark Hallenbeck

Dear TAs,

    This is not the secretmessage function you expected to see, but it is what it is :)
    This semester has been incredible difficult for me since I am taking 8 classes.
    Nevertheless, CS 342 was a "bit" challenging, I can assume, for every CS student, and I am not an exception.
    Only thanks to yours and Professor Hallenbeck's incredible hard work and patience,
    many of us step by step were growing as CS students, developing new skills and growing as future professionals.

    Thank you so much for helping us throughout this semester: I know it is a TON of work.
    You did incredible job and must be proud of yourself.

    I wish you all the best guys: set huge goals, chase your dreams, and I am sure that each of you will succeed in this life.

    Thank you again and take care!
*/

import javafx.animation.FadeTransition;
import javafx.animation.PauseTransition;
import javafx.animation.RotateTransition;
import javafx.animation.SequentialTransition;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.effect.DropShadow;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;
import javafx.util.Duration;

import java.util.Objects;

public class CoffeeShop extends Application {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		launch(args);
	}

	//feel free to remove the starter code from this method
	@Override
	public void start(Stage primaryStage) throws Exception {



		primaryStage.setTitle("Welcome to Cozmo's Coffee Shop!");

		Rectangle rect = new Rectangle (300, 40, 100, 100);
		rect.setArcHeight(50);
		rect.setArcWidth(50);
		rect.setEffect(new DropShadow(4, Color.MISTYROSE));
		rect.setFill(Color.VIOLET);

		RotateTransition rt = new RotateTransition(Duration.millis(2300), rect);
		rt.setByAngle(270);
		rt.setCycleCount(11);
		rt.setAutoReverse(true);
		SequentialTransition seqTransition = new SequentialTransition (
				new PauseTransition(Duration.millis(500)),
				rt
		);
		seqTransition.play();

		FadeTransition ft = new FadeTransition(Duration.millis(5000), rect);
		ft.setFromValue(1.0);
		ft.setToValue(0.3);
		ft.setCycleCount(4);
		ft.setAutoReverse(true);

		ft.play();
		BorderPane root1 = new BorderPane();
		root1.setCenter(rect);

		Scene scene = new Scene(root1, 500, 350);

		primaryStage = new Stage();
		primaryStage.setScene(scene);
		primaryStage.show();
		
		Coffee order = new Sugar(new Cream( new ExtraShot(new BasicCoffee())));
		
		double cost = order.makeCoffee();
		System.out.println("Total: " + cost);

		Parent root = FXMLLoader.load(Objects.requireNonNull(getClass().getResource("sceneLayout.fxml")));

		Scene scene1 = new Scene(root,600,600);
		scene1.getStylesheets().add(Objects.requireNonNull(getClass().getResource("style.css")).toExternalForm());
		primaryStage.setScene(scene1);
		primaryStage.show();

		PauseTransition delay = new PauseTransition(Duration.seconds(3));
		Stage finalStage = primaryStage;

		delay.setOnFinished(event -> finalStage.setScene(scene1) );
		delay.play();

	}

}
