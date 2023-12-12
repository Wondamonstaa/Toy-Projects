#include <Wire.h>
#include "paj7620.h"

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(9, 10);
const byte address[6] = "00001";

int buttonOneCurrState = 0, buttonTwoCurrState = 0, buttonOnePrevState = 0, buttonTwoPrevState = 0;

void setup() {
  pinMode(2, INPUT);
  pinMode(7, INPUT);

	uint8_t error = 0;
	error = paj7620Init();

  radio.begin();
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_MIN);
  radio.stopListening();
}

void loop() {
  const char button[10];
  buttonOneCurrState = digitalRead(2);
  buttonTwoCurrState = digitalRead(7);
  if (buttonOneCurrState != buttonOnePrevState) {
    if (buttonOneCurrState == HIGH && buttonOnePrevState == LOW) {
      strcpy(button, "buttonOne");
      radio.write(button, sizeof(button)); 
    }
  }

  buttonOnePrevState = buttonOneCurrState;
  
  if (buttonTwoCurrState != buttonTwoPrevState) {
    if (buttonTwoCurrState == HIGH && buttonTwoPrevState == LOW) {
      strcpy(button, "buttonTwo");
      radio.write(button, sizeof(button));
    }
  }
  buttonTwoPrevState = buttonTwoCurrState;
  const char gesture[10];
	uint8_t data = 0, error;
	error = paj7620ReadReg(0x43, 1, &data);
	if (!error) {
		switch (data) {
			case GES_RIGHT_FLAG: 
        strcpy(gesture, "Right");
        radio.write(gesture, sizeof(gesture));    
				break;
			case GES_LEFT_FLAG:
        strcpy(gesture, "Left");
        radio.write(gesture, sizeof(gesture));  
				break;
			case GES_UP_FLAG:
        strcpy(gesture, "Up");
        radio.write(gesture, sizeof(gesture));  
				break;
			case GES_DOWN_FLAG:
        strcpy(gesture, "Down");
        radio.write(gesture, sizeof(gesture));   
				break;
		}
	}
  delay(50);
}