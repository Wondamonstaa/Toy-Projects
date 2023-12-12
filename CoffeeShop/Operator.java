import javafx.animation.FadeTransition;
import javafx.fxml.Initializable;

import java.awt.*;
import java.io.IOException;
import java.net.URL;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.*;

import java.util.ResourceBundle;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Menu;
import javafx.scene.control.MenuBar;
import javafx.scene.control.MenuItem;
import javafx.scene.control.TextArea;
import javafx.scene.layout.*;
import javafx.stage.Stage;
import javafx.util.Duration;


public class Operator implements Initializable {

    public Menu file;
    private BackgroundImage image;

    public MenuItem exit;
    public Menu help;
    public MenuItem about;
    public MenuBar menuBar;
    @FXML
    private VBox root;
    @FXML
    private VBox root1;

    @FXML
    private Button addToppings;

    @FXML
    private BorderPane root2;

    @FXML
    private Button milk;
    @FXML
    private Button almond;

    @FXML
    private Button sugar;

    @FXML
    private Button CreamButton;

    @FXML
    private Button extraShot;

    @FXML
    private Button reset;

    @FXML
    private Button placeOrder;

    @FXML
    private Button exit1;

    @FXML
    private TextArea customerCopy;
    static String userInput = "";




    @Override
    public void initialize(URL location, ResourceBundle resources) {
        // TODO Auto-generated method stub
    }


    public void about(ActionEvent actionEvent) {

        String instructions = "Welcome to the Coffee Shop! \n\n"
                + "To place an order, select the type of coffee you would like to order. \n"
                + "Then, select the options you would like to add to your coffee. \n"
                + "Finally, click the 'Place Order' button to complete your order. \n\n"
                + "To cancel your order, click the 'Cancel' button. \n\n"
                + "Thank you for choosing the Cozmo's Coffee Shop!";

        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("About");
        alert.setHeaderText("About");
        alert.setContentText(instructions);
        alert.showAndWait();


    }

    public void exit(ActionEvent actionEvent) {

        System.out.println("Thank you for choosing the Cozmo's Coffee Shop!");

        System.exit(0);
    }

    public void milkAdded(ActionEvent e) throws IOException {

        //userInput = userInput + "Milk";

        if(milk.getText().equals("Milk")) {
            milk.setText("Milk Added");
            userInput = userInput + "Milk";
        }
        else {
            milk.setText("Milk");
            userInput = userInput.replace("Milk", "");
        }

        userInput = customerCopy.getText();
        customerCopy.setText(userInput + "\nMilk: $1.00");
        milk.setDisable(true);
        milk.setStyle("-fx-background-color: #b852fa");
        milk.setOpacity(1);
        FadeTransition ft = new FadeTransition(Duration.millis(1000), milk);
        ft.setFromValue(0.0);
        ft.setToValue(1.0);
        ft.play();
    }

    public void almondAdded(ActionEvent e) throws IOException {
        userInput = customerCopy.getText();
        customerCopy.setText(userInput + "\nAlmond Milk: $1.00");
        almond.setDisable(true);
        almond.setStyle("-fx-background-color: #b852fa");
        almond.setOpacity(1);
        FadeTransition ft = new FadeTransition(Duration.millis(1000), milk);
        ft.setFromValue(0.0);
        ft.setToValue(1.0);
        ft.play();
    }

    public void addCreamButton(ActionEvent e) throws IOException {

        userInput = customerCopy.getText();
        customerCopy.setText(userInput + "\nCreamButton: $0.50");
        CreamButton.setDisable(true);
        CreamButton.setStyle("-fx-background-color: #b852fa");
        CreamButton.setOpacity(1);

        FadeTransition ft = new FadeTransition(Duration.millis(1000), CreamButton);
        ft.setFromValue(0.0);
        ft.setToValue(1.0);
        ft.play();

    }

    public void addSugar(ActionEvent e) throws IOException{

        userInput = customerCopy.getText();
        customerCopy.setText(userInput + "\nSugar: $0.50");
        sugar.setDisable(true);
        sugar.setStyle("-fx-background-color: #b852fa");
        sugar.setOpacity(1);
        FadeTransition ft = new FadeTransition(Duration.millis(1000), sugar);
        ft.setFromValue(0.0);
        ft.setToValue(1.0);
        ft.play();
    }

    public void addExtraShot(ActionEvent e) throws IOException {

        userInput = customerCopy.getText();
        customerCopy.setText(userInput + "\nExtra Shot: $1.20");
        extraShot.setDisable(true);
        extraShot.setStyle("-fx-background-color: #b852fa");
        extraShot.setOpacity(1);
        FadeTransition ft = new FadeTransition(Duration.millis(1000), extraShot);
        ft.setFromValue(0.0);
        ft.setToValue(1.0);
        ft.play();
    }

    public void addMoreSugar(ActionEvent e) throws IOException {

        userInput = customerCopy.getText();
        customerCopy.setText(userInput + "\nAdditional toppings included: $2.50");
        addToppings.setDisable(true);
        addToppings.setStyle("-fx-background-color: #b852fa");
        addToppings.setOpacity(1);
        FadeTransition ft = new FadeTransition(Duration.millis(1000), addToppings);
        ft.setFromValue(0.0);
        ft.setToValue(1.0);
        ft.play();
    }

    public void cancel() {

        System.out.println("Thank you for choosing the Cozmo's Coffee Shop!");
        Button[] buttons = {milk, almond, sugar, CreamButton, extraShot, reset, placeOrder, exit1, addToppings};

        for (Button button : buttons) {
            button.setDisable(false);
        }


        reset.setStyle("-fx-background-color: #eed424");
        reset.setStyle("-fx-background-color: #161b22");
        customerCopy.setText("");
        customerCopy.setText("Your order includes: \nCozmo's Black Coffee $3.99");

        FadeTransition ft = new FadeTransition(Duration.millis(1000), reset);
        ft.setFromValue(0.0);
        ft.setToValue(1.0);
        ft.play();
    }

    public void coffeeBuilder(ActionEvent e) throws IOException {

        userInput = customerCopy.getText();
        Coffee clientCoffee = new BasicCoffee();
        int count;
        double total;

        Button[] buttons = new Button[6];
        buttons[0] = extraShot;
        buttons[1] = sugar;
        buttons[2] = CreamButton;
        buttons[3] = milk;
        buttons[4] = addToppings;
        buttons[5] = almond;

        for (count = 0; count < buttons.length; count++) {
            if (buttons[count].isDisabled()) {
                switch (count) {
                    case 0:
                        clientCoffee = new ExtraShot(clientCoffee);
                        break;
                    case 1:
                        clientCoffee = new Sugar(clientCoffee);
                        break;
                    case 2:
                        clientCoffee = new Cream(clientCoffee);
                        break;
                    case 3:
                        clientCoffee = new Milk(clientCoffee);
                        break;
                    case 4:
                        clientCoffee = new MoreSugar(clientCoffee);
                        break;
                    case 5:
                        clientCoffee = new AlmondMilk(clientCoffee);
                        break;
                }
            }
        }


        total = clientCoffee.makeCoffee();
        total += Math.round(total * 11.75) / 100.0;
        total = Math.round(total * 100.0) / 100.0;

        System.out.println("Total cost is: $" + total);

        FXMLLoader scene = new FXMLLoader(getClass().getResource("sceneLayout.fxml"));
        Parent child = scene.load();
        Operator driver = scene.getController();
        driver.orderCoffee(total);
        child.getStylesheets().add("style.css");

        root.getScene().setRoot(child);
    }

    public void orderCoffee(double price) {

        Button[] buttons = new Button[6];
        buttons[0] = extraShot;
        buttons[1] = sugar;
        buttons[2] = CreamButton;
        buttons[3] = milk;
        buttons[4] = addToppings;
        buttons[5] = almond;

        //disable all buttons
        for (Button button : buttons) {
            button.setDisable(true);
        }

        placeOrder.setDisable(true);
        placeOrder.setStyle("-fx-background-color: #5bf57f");
        reset.setDisable(false);

        //Calculates the tax in Illinois
        price += Math.round(price * 11.75) / 100.0;
        price = Math.round(price * 100.0) / 100.0;

        customerCopy.setText(userInput + "\n\nTotal: $" + price);
        FadeTransition ft = new FadeTransition(Duration.millis(1000), placeOrder);
        ft.setFromValue(0.0);
        ft.setToValue(1.0);
        ft.play();
    }

}
