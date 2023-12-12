/*
   1- Author: Kiryl Baravikoiu - UIN 656339218

   2- Lab: Lab 7 - Interrupts 

   3- Description: the following code is supposed to support a game using the counter and the display: the counter starts
   from 1 to 9 with a speed 2 digits per second, and the player is supposed to press the button at the digit which will be equal to the randomly
   selected number at the beginning of the game. If it was done - the player wins. Otherwise the game will be running until the player will hit the correct number.

   4-Lab Questions:
  What is the purpose of a current-limiting resistor in a seven-segment display circuit?
    a. This prevents the burnout of the seven-segment display. When an Arduino outputs a voltage to a seven-segment display, it can provide more current than the display can handle => display to heats up => this can damage or destroy the LEDs inside.

  Can you display special characters? If yes, How?
    a. Yes, but not all characters (Excluding the special ones: $, #, % etc.). 
    We simply have to use a combination of segments to create the desired shape by lighting up the chosen sections on the seven-segment display, for example, H => light up 1, 4, 5, and 6

  What are some common applications of seven-segment displays?
    a. Digital clocks;
    b. Electronic meters;
    c. Calculators;
    d. Scoreboards;
    e. Military industry.

   5- References: where did you find code snippets, ideas, and inspirations? failing to list the references you used can result in plagiarism. If you did not use any website say: "no references used".
    https://www.electronics-tutorials.ws/blog/7-segment-display-tutorial.html
    https://lastminuteengineers.com/seven-segment-arduino-tutorial/
    https://www.youtube.com/watch?v=QhIm6e5AH44&ab_channel=PaulMcWhorter	
    https://www.youtube.com/watch?v=9VZUb5cMrV0&ab_channel=CoreElectronics
    https://drive.google.com/file/d/1pfPjrYY_Kjk6k0xoTilEh4Ar0oo_9xoT/view


   6- Demo: in-person demonstration 4/17/2023 10:35 am to [Elijah].
*/



#include "SevSeg.h"
SevSeg sevseg;



//BUTTON
const int BUTTON = 2;

//LED
const int LED = 12;

//BUTTON STATE
volatile int isPressed = 0;

//The random number that will be generated at the beginning of the game
int RANDOM_NUM = 0;

//The condition to check if a player won or not
bool playerWon = false;
bool playerLost = false;


void buttonPressed(){
  isPressed = 1;
}



void setup(){

  pinMode(BUTTON, INPUT_PULLUP);
  pinMode(LED, OUTPUT);

  Serial.begin(9600); // initialize the serial communication

	//Set to 1 for single digit display
	byte numDigits = 1;

	//defines common pins while using multi-digit display. Left empty as we have a single digit display
	byte digitPins[] = {};

	//Defines arduino pin connections in order: A, B, C, D, E, F, G, DP
	//byte segmentPins[] = {3, 2, 8, 7, 6, 4, 5, 9};
  byte segmentPins[] = {5, 4, 10, 9, 8, 6, 7, 11};
	bool resistorsOnSegments = true;

	//Initialize sevseg object. Uncomment second line if you use common cathode 7 segment
	sevseg.begin(COMMON_CATHODE, numDigits, digitPins, segmentPins, resistorsOnSegments);
	//sevseg.begin(COMMON_CATHODE, numDigits, digitPins, segmentPins, resistorsOnSegments);

	sevseg.setBrightness(50);
  //Timer1.initialize(10000);
  //Timer1.attachInterrupt(buttonPressed);

  //Attaches interrupt to the BUTTON
  attachInterrupt(digitalPinToInterrupt(BUTTON), buttonPressed, HIGH);

  //Allows to place the random seed to generate the random number later each time setup() is being called
  randomSeed(analogRead(A0));

  //Generate a random number between 1 and 10
  RANDOM_NUM = random(1, 10);
  
  //Print the random number to the serial monitor
  Serial.print("The selected random number is: ");
  Serial.println(RANDOM_NUM);


}


//Helper function which allows to restart the game
void restart(){

  //Reset the initial values
  digitalWrite(LED, LOW);
  RANDOM_NUM = random(1, 10);
  isPressed = 0;
  playerWon = false;
  playerLost = false;
  setup();
  //loop();
  

}


//Helper function which allows to resume the game
void resume(int current){

  //Reset the initial values
  digitalWrite(LED, LOW);
  RANDOM_NUM = current;
  isPressed = 0;
  playerWon = false;
  playerLost = false;

  //Print the random number to the serial monitor
  Serial.print("The selected random number is: ");
  Serial.println(RANDOM_NUM);

  //setup();
  //loop();

}


void loop(){ 

  //Used to store the initial value of the RANDOM_NUM to resume the game later
  int sample = RANDOM_NUM;

  //Sanity check: if the win condition was not met => keep looping
  if(playerWon == false){

    //Display numbers one by one with 2 seconds delay
    for(int i = 0; i < 10; i++){
      
      //Allows to change the digits with an interval of 2 seconds
      sevseg.setNumber(i);
      sevseg.refreshDisplay(); 
      delay(500);

      //Sanity check if the button was pressed
      if(isPressed){
        
        //Win condition => if the button was pressed + the player chose the correct digit == to the random value
        if(i == RANDOM_NUM){

          Serial.println("Congratulations! You pressed at the correct number.");
          digitalWrite(LED, HIGH);
          playerWon = true;

          //Check the terminal condition
          if(playerWon == true){
            Serial.println("Game is restarting...");
            delay(1000);
            restart();
          }

          break;
        }
        else{
          
          //If player selected the wrong number -> continue the game without stopping
          if(playerWon == false){

            Serial.println("Oops! You stopped at the wrong number. Resuming the game.");

            //Helper function which allows to resume the game from the point where it was paused
            resume(sample);
          }
        
          //break;
        }
      }
    }
  }
}