import java.util.ArrayList;
import java.util.List;

public class MoreSugar extends CoffeeDecorator{

    private double cost = 2.50;
    private String description = " + sugar: $.50";

    MoreSugar(Coffee specialCoffee){
        super(specialCoffee);
    }

    public double makeCoffee() {
        return specialCoffee.makeCoffee() + addTopping();
    }

    private double addTopping() {

        System.out.println("Feel free to add any toppings or syrups from the list!");
        List<String> toppings = new ArrayList<>();

        toppings.add(" + whipped cream: $2.50");
        toppings.add(" + vanilla syrup: $2.50");
        toppings.add(" + chocolate syrup: $2.50");
        toppings.add(" + caramel syrup: $2.50");
        toppings.add(" + peppermint candies: $2.50");
        toppings.add(" + cinnamon: $2.50");
        toppings.add(" + nutmeg: $2.50");
        toppings.add(" + pumpkin spice syrup: $2.50");
        toppings.add(" + marshmallows: $2.50");

        /*for(String topping : toppings) {
            System.out.println(topping);
        }*/

        System.out.println(" + your topping: $2.50");

        return cost;
    }

}
