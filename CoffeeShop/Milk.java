public class Milk extends CoffeeDecorator {


    Milk(Coffee specialCoffee){
        super(specialCoffee);
    }

    public double makeCoffee() {

        if(specialCoffee instanceof CoffeeDecorator) {
            System.out.println(" + milk: $1.0");
        }

        return specialCoffee.makeCoffee() + milkAdded();
    }

    double milkAdded() {

        //Possible milk choices
        String[] milk = {"whole", "skim", "almond", "soy"};

        System.out.println(" + add a splash of milk: $1.0");

        return 1.0;
    }
}
