/*
   1- Author: Kiryl Baravikou - 656339218

   2- Lab: Lab 5 - Communication 

   3- Description: the following code below is used to create an Even-Odd Game,
   which uses the servo motor to determine the user was right guessing the final sum between the number
   he or she chose and the random number generated. If the user was right -> the servo motor will point to the Green Led,
   and the user wins. Otherwise, the servo motor will point to the Red LED, meaning that the user lost.

   4-Lab Questions:
    a. What function did you use to change the servo position?
        To change the servo position, I implemented the function called "rotator" which accepts 
        a boolean variable in order to start the rotation. Inside the function, to rotate the servo,
        I used two for-loops as described in the provided references by Professor, to rotate the servo from 
        0 to 180 degrees continuosly while the random generator works, and analogRead() with map() and write() 
        to move the servo to its starting position.
        
    b. What are the angles of the servo motor for the three directions?
      The angles I chose are all in the range from 0 to 180 degrees. The RED LED is located on the 180 degrees on Bredboard.
      The GREEN LED -> I used 15 degrees to shift towards this LED, since 0 degrees make no movement by servo motor.
      The neutral position is 103 degress based on my implementation.

    c. What functions/methods did you use to take input?
      I) To accept integer as input: 
        input = Serial.parseInt(); //where input is an int variable;
      II) To accept the string from user input:
        while(Serial.available() == 0){} //waits until the user input until the time runs out
        delay(1200); //delay to stabilize the function
        choice = Serial.readStringUntil("\n"); //the input will be read until the user will press enter


   5- References: where did you find code snippets, ideas, and inspirations? failing to list the references you used can result in plagiarism. If you did not use any website say: "no references used":
    a. https://www.programmingelectronics.com/serial-read/ 
    b. http://arduino.cc/en/Reference/Serial#.UwYyzfldV8E
    c. http://arduino.cc/en/Serial/Available#.UwYy2PldV8E
    d. https://docs.arduino.cc/learn/electronics/servo-motors
    e. https://www.arduino.cc/reference/en/language/functions/communication/serial/
    f. https://forum.arduino.cc/t/serial-input-basics-updated/382007

   6- Demo: in-person demonstration 3/27/2023 , 10:42 am to Elijah.
*/


#include <Servo.h>

Servo Servo1;

int servoPin = 9;
int potPin = A0;

//Define the LEDs pins
const int RED = 10;
const int GREEN = 8;

//Variable for the input integer
int input = 0;

//Variable used to store the input string
String choice = "";

const unsigned int LENGTH = 5;
//char result[LENGTH];
//unsigned int pos = 0;

//The current position of the servo motor
int pos = 0;



void rotator(bool engine){

  if(engine == true){

    //Allows to rotate the servo from 0 to 180 degrees
    for(pos = 0; pos <= 180; pos += 1) { 
        Servo1.write(pos);              
        delay(15);                      
    }

    //Allows to rotate the servo from 180 to 0 degrees
    for(pos = 180; pos >= 0; pos -= 1){ 
      Servo1.write(pos);             
      delay(15);                       
    }
  }
  else{
      int reading = analogRead(potPin);
      int angle = map(reading, 0, 1023, 0, 180);
      Servo1.write(103);
  }
}

//The function used to restart the game
void restart(){
      
      digitalWrite(RED, LOW);
      digitalWrite(GREEN, LOW);
      input = 0;
      choice = "";
      pos = 0;
      rotator(false);
      setup();
}


void setup(){

    Servo1.attach(servoPin);
    
    Serial.begin(9600);

    //Used to generate a random number 
    randomSeed(analogRead(0));

    //Creating the output for the LEDs using the pin numbers
    pinMode(GREEN, OUTPUT);
    pinMode(RED, OUTPUT);

    //Welcome message + the prompt to enter an integer from 1-5
    Serial.println("Welcome to the Even-Odd Game!");
    Serial.println("Enter a number between 1 to 5: ");
}


void loop() {

    int reading = analogRead(potPin);
    int angle = map(reading, 0, 1023, 0, 180);
    //Servo1.write(angle);
    Servo1.write(103);

    //The flag used to allow the program to accept a string odd or even
    bool received = false;

    int flag;

    //The variable used to store the sum of the input + random number
    int sum = 0;

    //Used to store a random value between 1 and 5
    int rvalue = random(5) + 1;

    
    //Allows to accept user input for the integer
    //while(Serial.available() && input == 0){
    if(input == 0){

        input = Serial.parseInt();
     
        //Check if the bounds are OK for the integer
        if(input > 0 && input <= 5){
          Serial.print("I received: ");
          Serial.print(input);
          Serial.println();
          received = true;
          flag = 0;
          sum += input;
        }
    }

  
    //If out of bounds or the number of bytes != to the number of bytes in an integer - restart the game
    if(input < 0 || input > 5 || (sizeof(input) != 2)){

      Serial.println("Wrong input!");
      delay(500);
      restart();
    }

  
    //Check if the conditions are met to end the game proprely
    if(received == true && flag == 0){

      Serial.println("Now choose odd or even! Type even or odd.");

      //Accept the string from user input from the terminal
      while(Serial.available() == 0){}
      delay(1200);
      choice = Serial.readStringUntil("\n");

      //Using the length, I determine the size of the input word, and, therefore, the further behavior of the program
      int choiceLength = choice.length();
      //Serial.println(choiceLength);

      //Sanity check
      /*if(choiceLength != 5 || choiceLength != 6){
        Serial.println("Wrong input!");
        delay(500);
        return restart();
      }*/

      /*if(choice != "even" || choice != "odd"){
        Serial.println("Wrong input!");
        delay(500);
        return restart();
      }*/
      
      Serial.print("I received: ");
      Serial.print(choice);


      delay(300);
      
      Serial.print("Generating...");
      rotator(true);
      delay(1000);

      Serial.println();
      Serial.print("My Number is: ");
      Serial.print(rvalue);
      //Serial.println();

      delay(300);

      //Update the sum
      //sum += rvalue;
      //Serial.println(sum);
      //Serial.print(choice);
      
      int final = sum + rvalue;

      //Find the substrings inside the chosen word
      int eChoice = choice.indexOf("e");
      int oChoice = choice.indexOf("o");


      //Serial.println(eChoice);
      //Serial.println(eChoice);
      //Serial.println(final);
      //Serial.println(choiceLength);

      //Check if the sum is even (even + terminating characters)
      if((final % 2 == 0) && (choice == "even")){
      //if((final % 2 == 0) && (choiceLength == 6)){

          Serial.println();
          Serial.print("Sum is: ");
          Serial.println(final);
          delay(100);

          Servo1.write(15);
          Serial.println("Sum is even! You win!");
          digitalWrite(RED, LOW);
          digitalWrite(GREEN, HIGH);
          delay(1000);
          restart();
      }
      //Check if the sum is odd (odd + terminating characters)
      if((final % 2 != 0) && (choice == "odd")){
      //if((final % 2 != 0) && (choiceLength == 5)){

          Serial.println();
          Serial.print("Sum is: ");
          Serial.println(final);
          delay(500);
          
          Servo1.write(15);
          Serial.println("Sum is odd! You win!");
          digitalWrite(RED, LOW);
          digitalWrite(GREEN, HIGH);
          delay(1000);
          restart();
      }
      //Not even and not odd
      if((final % 2 == 0) && (choice != "even")){
      //if((final % 2 == 0) && (choiceLength != 6)){

          Serial.println();
          Serial.print("Sum is: ");
          Serial.println(final);
          delay(500);

          Servo1.write(180);
          Serial.println("You Lose... Better Luck next time!");
          digitalWrite(RED, HIGH);
          digitalWrite(GREEN, LOW);
          delay(1000);
          restart();
      }
      //Not even and not odd
      if((final % 2 != 0) && (choice != "odd")){
      //if((final % 2 != 0) && (choiceLength != 5)){

          Serial.println();
          Serial.print("Sum is: ");
          Serial.println(final);
          delay(500);

          Servo1.write(180);
          Serial.println("You Lose... Better Luck next time!");
          digitalWrite(RED, HIGH);
          digitalWrite(GREEN, LOW);
          delay(1000);
          restart();
      }
      //Added
      else{
        Serial.println("Wrong input!");
        delay(500);
        restart();
      }

      flag = 1;
    }
}