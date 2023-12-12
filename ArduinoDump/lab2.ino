/*
   1- Author: Kiryl Baravikou  - UIN: 656339218

   2- Lab: Lab 2 - The LCD 

   3- Description: the following code is supposed to run a 2-player game on the lcd using arduino. The goal of each player is to run its own row 2 times to win. Whoever does it first - wins.

   4- LCD Pins: List what each of the following LCD pins are for, i.e. “D4: Data pin 4”. (Read the prelab):
   
     VSS(GND): ground or power supply pins (Grounded to the negative side on the position 44 on the board using the black wire);
     VDD(+5V): power supply pins => voltage provider (Connected to the position 42 (Positive side) on the board using the red wire);
     V0: contrast control on the LCD => changes in voltage adjust the contrast of the LCD, therefore, the display will be producing optimal image (Connect to 49H position on the board using the blue wire); 
     RS: register select => for selecting the type of data that we sent to the LCD (Connected to the pin 12 on UNO R3 using the yellow wire): 
         a) LOW => data = a command; 
         b) HIGH => data = data for the display => send to the LCD;

     RW (Read/Write): This pin is used to determine the type of operation being performed (Grounded from R3 to the position 37 (Negative side) on the board);
     E(Enable): controls the dataflow between the LCD and microcontroller => allows to send/receive the data from the LCD (Connected to the pin 11 on UNO R3 using the yellow wire);
     D4: Data pin 4 => supplies the LCD with power and activates it (I connected D4 with the pin 5 on UNO R3 using the white wire);
     D5: Data pin 5 => supplies the LCD with power and activates it (I connected D5 with the pin 4 on UNO R3 using the white wire);
     D6: Data pin 6 => supplies the LCD with power and activates it (I connected D6 with the pin 3 on UNO R3 using the white wire);
     D7: Data pin 7 => supplies the LCD with power and activates it (I connected D7 with the pin 2 on UNO R3 using the white wire);
     A(BKlt+): LCD's backlight control => turn on/off by adjusting the voltage;
     K(BKlt-): the following pin is used for grounding for the backlight control circuit (Connected to the negative side at the position 37 using the black wire on the board);

   5- References: where did you find code snippets, ideas, and inspirations? failing to list the references you used can result in plagiarism. If you did not use any website say: "no references used".

   6- Demo: "in-person demonstration" on the 2/13/2023, 10:30 am, checked by Elijah;
*/


#include <LiquidCrystal.h>


// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);


//Step 1: define the buttons => left and right buttons must corespond to its pins => DONE
const int leftButton = 8;
const int rightButton = 9;

//Step 2: player identifiers
const char player1 = "x";
const char player2 = "o";

const int cols = 16;
const int rows = 2;

bool player1Won = false;
bool player2Won = false;
bool playerTie = false;

int player1NumWins = 0;
int player2NumWins = 0;
int playerNumTie = 0;

int player1Pos = 0;
int player2Pos = 0;

bool isPressed1 = false;
bool isPressed2 = false;

int flag = 0;
int restart = 0;


void setup() {

  lcd.clear();
  lcd.begin(16, 2); //Initializes the interface to the LCD screen, and specifies the dimensions (width and height) of the display.
  welcome();
  delay(2000);
  lcd.clear();
  lcd.setCursor(0, 0);
 
  pinMode(leftButton, INPUT_PULLUP);
  pinMode(rightButton, INPUT_PULLUP);
  flag = 1;
  //lcd.setCursor(0,0);
  //lcd.print("Player 1: x");
  //lcd.setCursor(0,1);
  //lcd.print("Player 2: o");
  
}


void loop() {

  int counter = 0;
  int row = 0;
  int col = 0;


  if((!player1Won)){

    if(digitalRead(leftButton) == LOW && !isPressed1){

      moveCursorRight1();
      isPressed1 = true;

    }
    else if(digitalRead(leftButton) == HIGH){
      isPressed1 = false;
    }

  } 
  else if(player1Pos == 16 && player2Pos == 16 && player1Pos == player2Pos){
    tie();
    playerTie = true;
    delay(2000);
    lcd.clear();
    //player1Won = false;
    //player2Won = false;
    //playerTie = false;
    //lcd.print("Press xxx to start");
    restartGame();
  }
  else{
      player1Wins();
      delay(2000);
      lcd.clear();
      //player1Won = false;
      //player2Won = false;
      //playerTie = false;
      //lcd.print("Press xxx to start");
      restartGame();
  }


  if((!player2Won)){

    if(digitalRead(rightButton) == LOW && !isPressed2){

      moveCursorRight2();
      isPressed2 = true;

    }
    else if(digitalRead(rightButton) == HIGH){
      isPressed2 = false;
    }

  }
  else if(player1Pos == 16 && player2Pos == 16 && player1Pos == player2Pos){
    tie();
    playerTie = true;
    delay(2000);
    lcd.clear();
    //player1Won = false;
    //player2Won = false;
    //playerTie = false;
    //lcd.print("Press xxx to start");
    restartGame();
  }
  else{
      player2Wins();
      delay(2000);
      lcd.clear();
      //player1Won = false;
      //player2Won = false;
      //playerTie = false;
      //lcd.print("Press xxx to start");
      restartGame();
  }

}


//Moves player1 one step to the right
void moveCursorRight1() {

  //int counter = 0;
  lcd.setCursor(player1Pos, 0);
  lcd.print(" ");
  player1Pos++;

  /*if(player1Pos >= cols){
    player1Won = true;
  }*/

  if(player1Pos == 16 && player1NumWins < 2){
    player1NumWins++;
    lcd.setCursor(16, 0);
    lcd.print("#");
    player1Pos = 0;    
  }
  
  //lcd.print("#");

  if(player1NumWins == 2){
    player1Won = true;
  }

  lcd.setCursor(player1Pos, 0);
  lcd.print("x");
}


//Moves player2 one step to the right
void moveCursorRight2() {

  //int counter = 0;
  lcd.setCursor(player2Pos, 1);
  lcd.print(" ");
  player2Pos++;

  /*if(player2Pos >= cols){
    player2Won = true;
  }*/

  if(player2Pos == 16 && player2NumWins < 2){
    player2NumWins++;
    //lcd.setCursor(16, 1);
    lcd.print("#");
    player2Pos = 0;
  }

  //lcd.print("#");
  
  if(player2NumWins == 2){
    player2Won = true;
  }

  lcd.setCursor(player2Pos, 1);
  lcd.print("o");
}


void player1Wins(){
  
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Player 1 Wins!");
  delay(2000);
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("XXX to Restart");
  delay(2000);
  restartGame();
}


void player2Wins(){
  
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Player 2 Wins!");
  delay(2000);
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("XXX to Restart");
  delay(2000);
  //lcd.clear();
  restartGame();
}


void tie(){

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Ooops, tie!");
  delay(2000);
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("XXX to Restart");
  delay(2000);
  restartGame();
}


void welcome(){
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Player 1: x");
  lcd.setCursor(0,1);
  lcd.print("Player 2: o");
}


void restartGame(){

  lcd.clear();
  lcd.setCursor(0, 0);
  //lcd.print("XXX to Restart");

  if((player1Won == true || player2Won == true || playerTie == true) && digitalRead(rightButton) == LOW){
    restart++;
  }

  //lcd.clear();

  if((player1Won == true || player2Won == true || playerTie == true) && restart >= 3){

    lcd.clear();
    player1Won = false;
    player2Won = false;
    playerTie = false;
    player1Pos = 0;
    player2Pos = 0;
    isPressed1 = false;
    isPressed2 = false;
    flag = 0;
    lcd.clear();
    restart = 0;
    lcd.setCursor(0,0);
    setup();
    loop();
  }

}


