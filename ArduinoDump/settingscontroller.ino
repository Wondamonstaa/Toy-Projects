#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(9, 10);
const byte address[6] = "00001";


int x_axis = A0; //X-axis pin for the joystick
int y_axis = A1; //Y-axis pin for the joystick

//The pin for the joystick button
const int JOYSTICKBUTTON = 8;

void setup() {

  Serial.begin(9600);
	uint8_t error = 0;
	//error = paj7620Init();

  //Allows to provide output for the joystick
  pinMode(JOYSTICKBUTTON, INPUT_PULLUP);

  radio.begin();
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_MIN);
  radio.stopListening();
}

void loop() {


  //Read the signals from both x and y axises
  int x = analogRead(x_axis); 
  int y = analogRead(y_axis); 

  //Send the received signal from above to the joystick
  radio.write(&x, sizeof(x));
  radio.write(&y, sizeof(y));
  delay(100);

  //Get the current state of the joystick
  int joystickState = digitalRead(JOYSTICKBUTTON);


  // Determine which LED should be on based on joystick position => TA
  if (x < 300) { //BOTTOM

    Serial.println("Bottom");
    //digitalWrite(YELLOW, LOW);
    //digitalWrite(BLUE, HIGH);
    //digitalWrite(GREEN, LOW);
    //digitalWrite(RED, LOW);
  }
   else if (y < 300) { //LEFT
    Serial.println("Left");
    /*digitalWrite(YELLOW, LOW);
    digitalWrite(BLUE, LOW);
    digitalWrite(GREEN, HIGH);
    digitalWrite(RED, LOW);*/
  }
  else if (x > 700) { //TOP
    Serial.println("Top");
    /*digitalWrite(YELLOW, LOW);
    digitalWrite(BLUE, LOW);
    digitalWrite(GREEN, LOW);
    digitalWrite(RED, HIGH);*/
  }
  else if (y > 700) { //RIGHT
    Serial.println("Right");
    /*digitalWrite(YELLOW, HIGH);
    digitalWrite(BLUE, LOW);
    digitalWrite(GREEN, LOW);
    digitalWrite(RED, LOW);*/
  }
  
  //Check if the button is pressed
  if(joystickState == LOW){

      Serial.println("Button pressed");
      //radio.write("Button pressed", sizeof("Button pressed"));
      delay(10);
  }

}