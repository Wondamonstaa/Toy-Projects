public class Decaf extends CoffeeDecorator{

    private double cost = 3.99;

    public Decaf(Coffee specialCoffee) {
        super(specialCoffee);
    }

    public double makeCoffee() {
        return specialCoffee.makeCoffee() + addDecaf();
    }

    private double addDecaf() {

        System.out.println(" + decaf: $1.50");

        return cost;
    }
}
