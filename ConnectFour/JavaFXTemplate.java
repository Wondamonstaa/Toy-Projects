import javafx.animation.FadeTransition;
import javafx.animation.PauseTransition;
import javafx.animation.RotateTransition;
import javafx.animation.SequentialTransition;
import javafx.application.Application;

import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.fxml.FXMLLoader;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.Button;
import javafx.scene.control.Menu;
import javafx.scene.control.MenuBar;
import javafx.scene.control.MenuItem;
import javafx.scene.effect.BlurType;
import javafx.scene.effect.DisplacementMap;
import javafx.scene.effect.DropShadow;
import javafx.scene.effect.Glow;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.*;
import javafx.scene.paint.Color;
import javafx.scene.paint.CycleMethod;
import javafx.scene.paint.LinearGradient;
import javafx.scene.paint.Stop;
import javafx.scene.shape.Rectangle;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.scene.text.Text;
import javafx.scene.text.TextBoundsType;
import javafx.stage.Modality;
import javafx.stage.Stage;
import javafx.util.Duration;

import java.awt.*;
import java.beans.EventHandler;
import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class JavaFXTemplate extends Application {

	static Text displayMessage = new Text();
	static GameButton[][] matrix = new GameButton[6][7];
	private Menu menu;
	private MenuItem EXIT;
	private Stage stage;
	private MenuBar menubar;
	private MenuItem FreshStart;
	private BorderPane core;
	private MenuItem NewLook;
	private int option;
	String buttonSize = "-fx-font-size: 30;";
	final int height = 350;
	final int width = 350;
	final int buttonWidth = 200;
	final String fontSize = "-fx-font-size: 50;";
	final String basicPane = "-fx-background-image: url(background2.jpg);-fx-background-color: rgba(0, 0, 0, 0.5);";
	final String alternativePane = "-fx-background-image: url(background2.jpg);";
	final String colorMenu = "-fx-background-color: linear-gradient(to top, rgb(36,236,92), rgb(36,236,92));";
	final String menuBarOption2 = "-fx-background-color: linear-gradient(to top, #24ec5c, #24ec5c);";
	final String buttonLook1 = "-fx-background-color: linear-gradient(#5bf57f, #24ec5c);";
	final String buttonLook3 = "-fx-background-color: linear-gradient(#e52170, #e52170);";




	public static void main(String[] args) {
		// TODO Auto-generated method stub
		launch(args);

	}


	//Allows to display the starting scene for the user => my code from the previous project
	public Scene StartScene() {

		Rectangle r = new Rectangle(100, 40, 100, 100);
		r.setArcHeight(50);
		r.setArcWidth(50);
		r.setFill(Color.VIOLET);

		RotateTransition rt = new RotateTransition(Duration.millis(5000), r);
		rt.setByAngle(270);
		rt.setCycleCount(4);
		rt.setAutoReverse(true);
		SequentialTransition seqTransition = new SequentialTransition(
				new PauseTransition(Duration.millis(500)),
				rt
		);
		seqTransition.play();

		FadeTransition ft = new FadeTransition(Duration.millis(5000), r);
		ft.setFromValue(1.0);
		ft.setToValue(0.3);
		ft.setCycleCount(4);
		ft.setAutoReverse(true);

		ft.play();

		BorderPane root = new BorderPane();
		root.setCenter(r);

		//Scene scene = new Scene(root, 700,700);
		//primaryStage.setScene(scene);
		//primaryStage.show();

		BorderPane paneCenter = new BorderPane();
		paneCenter.setStyle("-fx-background-color: #000000");

		BorderPane newPane = new BorderPane();
		newPane.setPadding(new javafx.geometry.Insets(20, 0, 20, 20));

		EXIT = new javafx.scene.control.MenuItem("EXIT");
		FreshStart = new javafx.scene.control.MenuItem("FRESH START");
		NewLook = new javafx.scene.control.MenuItem("NEW LOOK");

		menubar = new javafx.scene.control.MenuBar();
		menu = new javafx.scene.control.Menu("OPTIONS", null);
		menu.setStyle("-fx-font-weight: bold;");
		menu.setOnHidden(e -> {
			paneCenter.setStyle(basicPane);
		});

		menu.setStyle(colorMenu);
		menu.getItems().addAll(EXIT, FreshStart, NewLook);
		menubar.setEffect(new DropShadow());
		menubar.setMinSize(75, 35);
		menubar.setPadding(new javafx.geometry.Insets(10, 10, 10, 10));
		menubar.setEffect(new DropShadow());
		menubar.setBorder(new Border(new BorderStroke(Color.BLACK, BorderStrokeStyle.SOLID, CornerRadii.EMPTY, BorderWidths.DEFAULT)));
		menubar.setStyle(colorMenu);

		menubar.getMenus().add(menu);
		menu.setStyle(colorMenu);
		menubar.setStyle(colorMenu);
		menubar.setCenterShape(true);
		menubar.setPrefSize(100, 50);


		//Allows to click the menubar
		EXIT.setOnAction(e -> {
			//display root after clicking

			System.exit(0);
		});

		javafx.scene.control.MenuItem EXIT2 = new javafx.scene.control.MenuItem("EXIT");
		javafx.scene.control.MenuItem freshStart2 = new javafx.scene.control.MenuItem("FRESH START");
		javafx.scene.control.MenuItem newLook2 = new javafx.scene.control.MenuItem("NEW LOOK");

		javafx.scene.control.MenuBar menubar2 = new javafx.scene.control.MenuBar();
		javafx.scene.control.Menu menu2 = new Menu("OPTIONS");
		menu2.getItems().addAll(EXIT2, freshStart2, newLook2);
		menubar2.setMinSize(75, 50);
		menubar2.setPadding(new javafx.geometry.Insets(10, 10, 10, 10));
		menubar2.setEffect(new DropShadow());
		menubar2.setOnKeyPressed(e -> {
			System.out.println("Key Pressed");
		});
		menubar2.setBorder(new Border(new BorderStroke(Color.BLACK, BorderStrokeStyle.SOLID, CornerRadii.EMPTY, BorderWidths.DEFAULT)));

		menubar2.getMenus().add(menu2);
		menu2.setStyle(colorMenu);
		menubar2.setStyle(colorMenu);

		newPane.setTop(menubar2);
		BorderPane.setAlignment(menubar2, Pos.TOP_RIGHT);

		ToggleButton rules = new ToggleButton("RULES");
		rules.setEffect(new DropShadow());
		Text newText = new Text("NEW GAME");


		//Contact us button
		ToggleButton contactUs = new ToggleButton("CONTACT US");
		contactUs.setStyle("-fx-font-size: 25;" + "-fx-text-fill: #5bf57f;");
		contactUs.setFont(javafx.scene.text.Font.font("Verdana", FontWeight.SEMI_BOLD, 20));
		contactUs.setPadding(new javafx.geometry.Insets(0, 0, 0, 0));
		contactUs.setBackground(new Background(new BackgroundFill(Color.BLACK, CornerRadii.EMPTY, javafx.geometry.Insets.EMPTY)));
		contactUs.setOpacity(0.65);

		newText.setStyle(fontSize);
		newText.setEffect(new DropShadow());
		newText.setFill(Color.WHITE);
		newText.setStroke(Color.BLACK);
		newText.setStrokeWidth(2);
		newText.setEffect(new DropShadow());
		newText.setEffect(new DropShadow(BlurType.GAUSSIAN, Color.BLACK, 10, 0, 0, 0));

		newText.setFont(javafx.scene.text.Font.font("Verdana", FontWeight.BOLD, 50));

		Text rulesText = new Text(
				"The goal of this game is to get the highest score possible. \n" +
						"Each time you click on the screen, you will get a point. \n" +
						"However, if you click on the wrong color, you will lose a point. \n" +
						"Each time you click on the screen, the color will change. \n" +
						"Good luck and have fun! ");


		rules.setOnAction((ActionEvent) -> {

			//Open new scene
			Stage newStage = new Stage();
			BorderPane newPane2 = new BorderPane();
			newPane2.setStyle(basicPane);
			newPane2.setPadding(new javafx.geometry.Insets(20, 0, 20, 20));
			newPane2.setCenter(rules);



			rulesText.setFont(javafx.scene.text.Font.font("Verdana", FontWeight.BOLD, 25));
			rulesText.setFill(Color.WHITE);
			rulesText.setBoundsType(TextBoundsType.VISUAL);

			Rectangle rect = new Rectangle();
			rect.setX(50);
			rect.setY(50);
			rect.setWidth(500);
			rect.setHeight(500);

			LinearGradient gradient = new LinearGradient(0, 0, 0, 1, true, CycleMethod.NO_CYCLE, new Stop(0, Color.BLACK), new Stop(1, Color.BLACK));
			rect.setFill(gradient);
			rect.setStroke(Color.WHITE);
			rect.setStrokeWidth(5);
			rect.setArcWidth(20);
			rect.setArcHeight(20);
			rect.setEffect(new DropShadow());
			rect.setEffect(new DropShadow(BlurType.GAUSSIAN, Color.BLACK, 10, 0.5, 0, 0));

			//Add text to the rectangle
			TitledPane stack = new TitledPane();
			stack.setAnimated(false);

			Alert alert = new Alert(Alert.AlertType.INFORMATION);
			alert.setTitle("Game Rules");
			alert.setHeaderText("Connect Four Rules");
					alert.setContentText("The goal of the Connect Four is to connect four places in a row to win the game.");


			alert.getDialogPane().setStyle("-fx-background-color: #ffffff; -fx-text-fill: #FFFFFF; -fx-font-size: 25px; -fx-font-weight: bold; -fx-border-color: #000000; -fx-border-width: 5px; -fx-border-radius: 20px; -fx-background-radius: 20px;");
			alert.getDialogPane().setEffect(new DropShadow());
			alert.getDialogPane().setMinSize(500, 500);
			alert.getDialogPane().setMaxSize(500, 500);
			alert.getDialogPane().setPrefSize(500, 500);
			alert.getDialogPane().setPadding(new javafx.geometry.Insets(10, 10, 10, 10));
			alert.getDialogPane().setMinHeight(Region.USE_PREF_SIZE);

			Rectangle rect2 = new Rectangle(500, 500);
			rect2.setArcWidth(20);
			rect2.setArcHeight(20);
			rect2.setFill(Color.BLACK);
			alert.getDialogPane().setClip(rect2);
			alert.showAndWait();
			newPane2.setCenter(stack);
			rulesText.setEffect(new DropShadow());
			rules.setDisable(true);

			ToggleButton escape = new ToggleButton("BACK");
			escape.getBackground();
			escape.setEffect(new Glow());
			escape.setEffect(new DropShadow());
			escape.setOnAction((e) -> {
				newStage.close();
			});

			newPane2.setBottom(escape);
			newStage.show();
		});


		//FIXME: create buttons for the starting scene => DONE
		ToggleButton playBtn = new ToggleButton("NEW GAME");
		playBtn.setStyle(fontSize);
		playBtn.setEffect(new Glow());
		playBtn.setEffect(new DropShadow());
		playBtn.setFont(javafx.scene.text.Font.font("Verdana", FontWeight.BOLD, 50));
		playBtn.setBackground(new Background(new BackgroundFill(Color.GREEN, CornerRadii.EMPTY, javafx.geometry.Insets.EMPTY)));

		Button quitBtn = new Button("QUIT");
		quitBtn.setBackground(new Background(new BackgroundFill(Color.RED, CornerRadii.EMPTY, javafx.geometry.Insets.EMPTY)));
		quitBtn.setEffect(new DropShadow());
		quitBtn.setFont(javafx.scene.text.Font.font("Verdana", FontWeight.BOLD, 50));

		ToggleButton welcomeButton = new ToggleButton("CONNECT FOUR");
		welcomeButton.setEffect(new DropShadow());
		welcomeButton.setBackground(new Background(new BackgroundFill(Color.WHITE, CornerRadii.EMPTY, javafx.geometry.Insets.EMPTY)));


		welcomeButton.setEffect(new Glow());
		welcomeButton.setStyle("-fx-background-color: MediumSeaGreen");
		welcomeButton.setAlignment(Pos.TOP_CENTER);
		welcomeButton.setOnAction((ActionEvent) -> {
			System.out.println("Welcome to Connect Four Game!");
			welcomeButton.setText("WELCOME! CHOOSE AN OPTION BELOW!");
			welcomeButton.setEffect(new Glow());
			welcomeButton.setEffect(new DisplacementMap());
			welcomeButton.setDisable(true);
		});

		//Contact button
		Button contactBtn = new Button("CONTACT US");
		contactUs.setEffect(new DropShadow());
		contactUs.setBackground(new Background(new BackgroundFill(Color.WHITE, CornerRadii.EMPTY, javafx.geometry.Insets.EMPTY)));
		contactUs.setEffect(new Glow());
		contactUs.setStyle("-fx-background-color: MediumSeaGreen");
		contactUs.setAlignment(Pos.BOTTOM_CENTER);
		contactUs.setOnAction((ActionEvent) -> {
			contactUs.setText("CONTACT US: kbara5@uic.edu");
			contactUs.setDisable(false);
		});

		//use contactBtn
		contactBtn.setOnAction((ActionEvent) -> {
			contactBtn.setText("CONTACT US: kbara5@uic.edu");
			//create pop up window with contact info
			Stage newStage = new Stage();
			newStage.setTitle("Contact Us");
			newStage.setResizable(false);
			newStage.initModality(Modality.APPLICATION_MODAL);
			BorderPane np = new BorderPane();
			Scene newScene = new Scene(np, 500, 500);
			newStage.setScene(newScene);
			newStage.show();
			contactBtn.setDisable(false);
		});

		//put contactBtn on the bottom of the box
		contactBtn.setAlignment(Pos.BOTTOM_CENTER);

		//A new border pane for the contact button
		BorderPane contactPane = new BorderPane();
		contactPane.setCenter(contactBtn);

		//Contact Button
		BorderPane.setAlignment(contactPane, Pos.BOTTOM_LEFT);

		javafx.scene.image.Image pic = new javafx.scene.image.Image("background2.png");
		ImageView front1 = new ImageView(pic);
		javafx.scene.image.Image pic2 = new javafx.scene.image.Image("background2.png");
		ImageView front2 = new ImageView(pic2);
		javafx.scene.image.Image pic3 = new Image("background2.png");
		ImageView front3 = new ImageView(pic3);

		//A feedback button
		Button feedbackBtn = new Button("FEEDBACK");
		feedbackBtn.setPrefSize(100, 50);
		feedbackBtn.setStyle(buttonSize + buttonLook3);
		feedbackBtn.setOnAction((ActionEvent) -> {
			feedbackBtn.setText("FEEDBACK:");
			feedbackBtn.setDisable(false);
		});

		//pop up window after clicking feedbackBtn
		feedbackBtn.setOnAction(e -> {
			Stage feedbackStage = new Stage();
			feedbackStage.setTitle("FEEDBACK");
			feedbackStage.initModality(Modality.APPLICATION_MODAL);
			feedbackStage.initOwner(stage);
			feedbackStage.setMinWidth(250);
			feedbackStage.setMinHeight(250);
			feedbackStage.setMaxWidth(250);
			feedbackStage.setMaxHeight(250);
			feedbackStage.setResizable(false);
			feedbackStage.show();
		});

		HBox background = new HBox(front1, front2, front3);
		HBox test = new HBox(200, menubar);

		final Pane spacer = new Pane();
		HBox.setHgrow(spacer, Priority.ALWAYS);
		spacer.setMaxSize(24, 0);

		//This makes the top of the BorderPane putting menuBar at top and flush image below
		VBox topPane = new VBox(test, background);
		topPane.setSpacing(30);

		playBtn.setPrefSize(300, 100);
		HBox btnBox = new HBox(contactPane, rules, playBtn, quitBtn, feedbackBtn);
		btnBox.setSpacing(20);
		VBox labelBox = new VBox(welcomeButton, btnBox);

		EXIT.setOnAction(e -> System.exit(0));
		FreshStart.setOnAction(e -> {

		});
		NewLook.setOnAction(e -> {
			if(option == 0){
				option = 1;
				welcomeButton.setStyle(fontSize + "-fx-text-fill: #29e843;");
				menu.setStyle(menuBarOption2);
				menubar.setStyle(menuBarOption2);
				paneCenter.setStyle(alternativePane);
				playBtn.setStyle(buttonSize + buttonLook1);
				rules.setStyle(buttonSize + buttonLook3);
				quitBtn.setStyle(buttonSize + buttonLook3);
			}
			else{
				option = 0;
				welcomeButton.setStyle(fontSize + "-fx-text-fill: #24ec5c;");
				menu.setStyle(colorMenu);
				menubar.setStyle(colorMenu);
				paneCenter.setStyle(basicPane);
				playBtn.setStyle(buttonSize + buttonLook1);
				rules.setStyle(buttonSize + buttonLook3);
				quitBtn.setStyle(buttonSize + buttonLook3);
			}
		});

		//Set the front images => DONE
		front1.setFitHeight(height);
		front1.setFitWidth(width);
		front1.setPreserveRatio(true);
		front2.setFitHeight(height);
		front2.setFitWidth(width);
		front2.setPreserveRatio(true);
		front3.setFitHeight(height);
		front3.setFitWidth(width);
		front3.setPreserveRatio(true);
		background.setSpacing(40);
		background.setAlignment(Pos.TOP_CENTER);


		//Buttons to be placed at the bottom
		playBtn.setPrefSize(buttonWidth, 65);
		playBtn.setStyle(buttonSize + buttonLook1);
		playBtn.setOnAction(e -> {
			//stage.setScene(start(primaryStage)); //FIXME
		});

		rules.setPrefSize(buttonWidth, 45);
		rules.setStyle(buttonSize + buttonLook3);
		quitBtn.setPrefSize(buttonWidth, 45);
		quitBtn.setStyle(buttonSize + buttonLook3);
		quitBtn.setOnAction(e -> System.exit(0));
		btnBox.setAlignment(Pos.CENTER);
		btnBox.setSpacing(70);
		btnBox.setPadding(new javafx.geometry.Insets(70, 0, 0, 0));

		welcomeButton.setStyle(fontSize + "-fx-text-fill: #000000;");
		welcomeButton.setFont(Font.font("Times New Roman", 25));
		labelBox.setPadding(new Insets(20, 0, 0, 0));
		labelBox.setAlignment(Pos.TOP_CENTER);


		paneCenter.setCenter(labelBox);
		paneCenter.setTop(topPane);
		paneCenter.setBottom(contactUs);
		paneCenter.setStyle(basicPane);


		return new Scene(paneCenter, 1200, 750);

	}


	//feel free to remove the starter code from this method
	@Override
	public void start(Stage primaryStage) throws Exception {
		// TODO Auto-generated method stub
		primaryStage.setTitle("Project 3 Connect 4 Game client");

		Rectangle rect = new Rectangle (100, 40, 100, 100);
		rect.setArcHeight(50);
		rect.setArcWidth(50);
		rect.setFill(Color.VIOLET);

		RotateTransition rt = new RotateTransition(Duration.millis(5000), rect);
		rt.setByAngle(270);
		rt.setCycleCount(4);
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

		Parent root = FXMLLoader.load(getClass().getResource("/clientWelcome.fxml"));
		root.getStylesheets().add("/styles/style2.css");//set style

		Scene rootScene = new Scene(root, 900, 600);
		primaryStage.setScene(rootScene);

		primaryStage.setOnCloseRequest(new EventHandler<WindowEvent>() {
			@Override
			public void handle(WindowEvent t) {
				Platform.exit();
				System.exit(0);
			}
		});

		/*PauseTransition delay = new PauseTransition(Duration.seconds(1));
		delay.setOnFinished( event -> primaryStage.setScene(rootScene) );
		delay.play();*/

		primaryStage.show();
	}

}

}









