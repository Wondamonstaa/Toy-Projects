/*
   1- Author1: Kiryl Baravikou

   2- Lab: Lab 6 - Serial Communication

   3- Description: 
   a) In your own words, what is this code supposed to do? 
      The following code is suppoosed to establish connection between 2 arduinos so that the players could play a racing game: whoever comes to the finish first, wins the game => the green light 
      indicates the winner, while the red one indicates the one who lost.

   b) Explain the division of labor between the teammates.
      Since my partner bailed on me, I had to write all this code by myself and wire the circuits by myself as well. Due to the big amount of work for this project,
      I was not able to fully finish it due to credit hour overload this semester.

   4- Serial Communication: describe how serial communication works in this lab. (include in this description the pin numbers you used)
      To establish the serial communication, I connected TX to RX using the red wire, and RX to TX using the blue wire. 
      To provide a power supply, I connected both GNDs of 2 arduinos with each other, and then using the red wire I sent 
      the power from one arduino to another by connect + from one to the + of the second arduino. 
      Using serial communication, we read the incoming byte, store it inside a variable, and then send it to the second arduino.
      We repeat the procedure and store the bytes in variables, which further will be compared to start the game for both players.

   5- References: where did you find code snippets, ideas, and inspirations? failing to list the references you used can result in plagiarism. If you did not use any website say: "no references used".
    a. LiquidCrystal.h documentation
    b. Lab 2 - The LCD 
    c. Lab Submission Guidelines - Lab 6 
    d. https://docs.arduino.cc/learn/built-in-libraries/software-serial 
    e. https://reference.arduino.cc/reference/en/language/functions/communication/wire/ 
    f. https://www.youtube.com/watch?v=xqz5CDpM6HA&feature=youtu.be
    g. https://www.youtube.com/watch?v=DzBwPWsb-5A&feature=youtu.be
    h. https://robotic-controls.com/learn/arduino/arduino-arduino-serial-communication
    i. https://www.google.com/search?rlz=1C1CHBF_enUS964US964&q=arduino+i2c&tbm=vid&sa=X&ved=2ahUKEwjx2v-zv_r9AhX9lmoFHd2dBv0Q0pQJegQICRAB&biw=1707&bih=916&dpr=1.5#fpstate=ive&vld=cid:acfe01a2,vid:PnG4fO5_vU4

   6- Demo: in-person demonstration 4/10/2023 2:30 PM to Ameer.
*/



#include <LiquidCrystal.h>

//Library used for establishing connection between two arduinos
#include <SoftwareSerial.h>

//The wire library for I2C
#include <Wire.h>



// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);


//Pin used for set up the contrast value without using potentiometer (Lab 3)
#define CONTRAST_PIN 7

#define SLAVE_ADDRESS 9

//Slave answer size
#define ANSWERSIZE 5

//Step 1: define the buttons => left and right buttons must corespond to its pins => DONE
const int leftButton = 13; //Pin 6 for the second arduino
const int rightButton = 6;

//Step 2: player identifiers
const char player1 = "x";
const char player2 = "o";

//Step 3: LEDs
const int RED = 9;
const int GREEN = 8;

//Step 4: BUZZER
const int BUZZER = 10;

//Step 5: Serial Objects
SoftwareSerial player1Serial(0, 1); // RX, TX
SoftwareSerial player2Serial(0, 1); // RX, TX


//Step 6: button inputs
int buttonInputPlayer1 = 1;
int buttonInputPlayer2 = 1;

int buttonInputPlayer1_Old = 1;
int buttonInputPlayer2_Old= 1;

int stateP1 = 1;
int stateP2 = 1;


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

//Used to start the game
int starter = 0;
int p1 = 0;
int p2 = 0;
int incomingByte = 0; //I2C


//States for the input reading
int readState = 0;
int prevState = 0;

//Functions definitions
void player1Start();
void player2Start();
void restartGame();


//Checks whether two players pressed the buttons => i.e "Ready"
bool startGame(){


    if(isPressed1 == true){
      
      lcd.setCursor(0, 0);
      lcd.print("Ready");

      if(isPressed2 == true){

        lcd.setCursor(0, 0);
        lcd.print("Ready");

        return true;
      }
    }
    
    return false;
}


/*void setup() {

  lcd.clear();
  lcd.begin(16, 2); //Initializes the interface to the LCD screen, and specifies the dimensions (width and height) of the display.

  //Game inputs and outputs => buttons and LEDs
  pinMode(leftButton, INPUT_PULLUP);
  pinMode(rightButton, INPUT_PULLUP);
  
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);  


  //The engine of the game
  if((starter == 0) && (p1 == 0) && (p2 == 0)){
    
    if(p1 == 0){
      //Displays the prompt for player 1 to start the game
      player1Start();
      delay(300);

      if(digitalRead(leftButton) == LOW && !isPressed1){

        p1 = 1;
        
        if(p1 == 1){
          //Displays the prompt for player 2 to start the game
          player2Start();
          delay(300);
                
          if(digitalRead(rightButton) == LOW && !isPressed2){

              p2 = 1;
              starter = 1;
              //welcome();
          }
        }
      }
    }
  }
  
  
  if((starter == 1) && (p1 == 1) && (p2 == 1)){

    welcome();
    delay(1000);
    lcd.clear();
    lcd.setCursor(0, 0);

  }

  //welcome();
  //delay(1000);
  //lcd.clear();
  //lcd.setCursor(0, 0);
 
  //pinMode(leftButton, INPUT_PULLUP);
  //pinMode(rightButton, INPUT_PULLUP);
  
  //pinMode(RED, OUTPUT);
  //pinMode(GREEN, OUTPUT);
  
  flag = 1;
}*/


//Helper function to create a timer for the game
void timer() {

    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Ready");
    delay(200);
    lcd.clear();


    for(int i = 3; i >= 1; i--) {
      lcd.setCursor(0, 0);
      lcd.print(i);
      tone(BUZZER, 1000, 200); //Generate a sound on the buzzer
      //delay(500);
      delay(1000);

    }
    
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Go!!!");
    tone(BUZZER, 1000, 500); //Generate a sound on the buzzer
}


void setup() {

  //Serial.print(9600);
  lcd.clear();
  lcd.begin(16, 2); //Initializes the interface to the LCD screen, and specifies the dimensions (width and height) of the display.

  //Port initialization
  //player1Serial.begin(9600);  
  //player2Serial.begin(9600);


  //Initialize I2C communication as MASTER
  //Wire.begin();

  //Initialize I2C communication as SLAVE
  //Wire.begin(9);

  //Wire.onReceive(receiveEvent);

  //Setup serial monitor
  Serial.begin(9600);

  //Game inputs and outputs => buttons and LEDs
  pinMode(leftButton, INPUT_PULLUP);
  pinMode(rightButton, INPUT_PULLUP);
  pinMode(BUZZER, OUTPUT);
  pinMode(CONTRAST_PIN, OUTPUT);
  analogWrite(CONTRAST_PIN, 75);
  
  //LEDs
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);  

  int stopper = 0;
  p1 = 0;
  p2 = 0;
  starter = 0;

  //The engine of the game
  while((starter == 0 && p2 != 1)){

    //Display prompt to start the game
    if((starter == 0)){
      
      if(p1 != 1){
        player1Start();
        delay(200);
      }
      else{
        //Separate function for waiting on a second player
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Ready, waiting");
        lcd.setCursor(0, 1);
        lcd.print("for player 2");
        delay(1500);        
      }
        
      //Wait for player 1 input
      if(digitalRead(leftButton) == LOW && stopper != 1){
     
        p1 = 1;
  
        if(p1 == 1 && starter == 0 && p2 == 0){
          
          //Display prompt to start the game
          player2Start();
          //delay(200);
          
          //Wait for player 2 input
          if(digitalRead(rightButton) == LOW){
            p2 = 1;
            starter = 1;
            stopper = 1;
            delay(200);
          }
        }
      }
    }
  }
  
  if(starter == 1){

    //Display prompt to start the game
    lcd.clear();
    lcd.setCursor(0, 0);
    //lcd.print("Ready");
    timer();
    delay(500);

    lcd.clear();
    lcd.setCursor(0, 0);
  }
  
  //All variables are set, start the game
  flag = 1;
}


//Used for I2C connection
/*void receiveEvent(int bytes) {
    x = Wire.read();
}*/


//Helper function to help player1 to get started the game
void player1Start(){

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Player 1, press");

  lcd.setCursor(0, 1);
  lcd.print("button to start");
  delay(1000);
  //lcd.clear();

  if(digitalRead(leftButton) == LOW){

        p1 = 1;

        //Serial.write('1');

        //This command will send a message to the second player
        //Wire.write('1'); 
        //delay(200);
  }
}


//Helper function to help player2 to get started the game
void player2Start(){
  
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Player 2, press");

  lcd.setCursor(0, 1);
  lcd.print("button to start");
  delay(1000);
  //lcd.clear();

  if(digitalRead(rightButton) == LOW){

        p2 = 1;



        //This command will send a message to the second player
        //Wire.write('1'); 
        //delay(200);
  }
}


void loop() {

  int counter = 0;
  int row = 0;
  int col = 0;
  

  //Begin serial communication between arduinos
  if(Serial.available() > 0){

    //This is where I store the input from the buffer
    incomingByte = Serial.read();

  }


  readState = digitalRead(leftButton);

  Serial.println(readState);

  if(prevState == 0 && readState == 1){
        Serial.write(1);
  }

  prevState = readState;


  int secondButtonState = digitalRead(rightButton);

  if (secondButtonState == HIGH) {
      Serial.write(1);
  }

      if(starter == 0 && (p1 == 0 || p2 == 0)){

        if(p1 == 1 && p2 == 0){
          
          //p2 = Serial.read(incomingByte);
          player2Start();
          p2 = 1;
        }

        if((p1 == 0 && p2 == 0)){
          player1Start();
        }

      }
      else{

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
          delay(500);
          lcd.clear();
          restartGame();
        }
        else{
            player1Wins();
            delay(500);
            lcd.clear();
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
          delay(500);
          lcd.clear();
        }
        else{
            player2Wins();
            delay(500);
            lcd.clear();
        }
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
    //lcd.setCursor(16, 0);
    //lcd.print("#");
    lcd.setCursor(15, 0); 
    lcd.write("#");
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
    lcd.setCursor(15, 1); 
    lcd.write("#");
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
  
  //LIGHT THE GREEN LED UP
  digitalWrite(GREEN, HIGH);
  delay(200);

  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Player 1 Wins!");
  delay(500);
  lcd.clear();
  //lcd.setCursor(0,0);
  //lcd.print("XXX to Restart");
  delay(500);
  restartGame();
}


void player2Wins(){
  
  //LIGHT THE GREEN LED UP
  digitalWrite(GREEN, HIGH);
  delay(200);

  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Player 2 Wins!");
  delay(500);
  lcd.clear();
  //lcd.setCursor(0,0);
  //lcd.print("XXX to Restart");
  delay(500);
  //lcd.clear();
  restartGame();
}


void tie(){

  digitalWrite(RED, HIGH);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Ooops, tie!");
  delay(500);
  lcd.clear();
  //lcd.setCursor(0,0);
  //lcd.print("XXX to Restart");
  delay(500);
  restartGame();
}


void welcome(){

  //LIGHT THE GREEN LED UP
  //digitalWrite(GREEN, LOW);
  //digitalWrite(GREEN, LOW);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Player 1: x");
  lcd.setCursor(0,1);
  lcd.print("Player 2: o");
}


void restartGame(){

  lcd.clear();
  lcd.setCursor(0, 0);
 

  if((player1Won == true || player2Won == true || playerTie == true)){
    
    digitalWrite(GREEN, LOW);
    lcd.clear();

    //Resets the starter values
    p1 = 0;
    p2 = 0;
    starter = 0;

    player1NumWins = 0;
    player2NumWins = 0;

    player1Pos = 0;
    player2Pos = 0;

    player1Won = false;
    player2Won = false;
    playerTie = false;
  
    isPressed1 = false;
    isPressed2 = false;
    flag = 0;

    restart = 0;
    lcd.setCursor(0,0);
    p1 = 0;
    p2 = 0;
    starter = 0;
    setup();
    loop();
  }

}


