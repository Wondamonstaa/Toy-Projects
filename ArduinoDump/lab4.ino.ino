/* 
  Hedwig's theme - Harry Potter 
  Connect a piezo buzzer or speaker to pin 11 or select a new pin.
  More songs available at https://github.com/robsoncouto/arduino-songs                                            
                                              
                                              Robson Couto, 2019
*/

/*
   1- Author: Kiryl Baravikou
   2- Lab: Lab 4 - Multiple Inputs and Outputs 
   3- Description: the following program is supposed to accept multiple inputs and provide multiple outputs, including the sound of the piezzo speaker which reacts to changes in the value of the photoresistor.
   Also, the following code allows to use joystick connected to the bredboard, and based on the joystick's movement the corresponding LEDs on the x and y-axis become bright.
   4-Lab Questions:
  What does the map() function do?
  The map() function re-maps a number from one range to another. The mapped values are stored in a new local variable for further usage, in our case to change the speed of the piezzo speaker.
  
  How did you change the speed of the melody in your code?
  I created a new variable to store the input of the photoresistor which changes based on the amount of light it gets. Then inside the for loop, I assigned the noteDuration variable with a "floating" value of the photoresistor,
  which in its turn led to the ability of the piezzo speaker to change the music play speed based on the value of the photoresistor.
  
  What was the hardest part of the lab to implement?
  Piezzo speaker in combination with the photoresistor.

   5- References: where did you find code snippets, ideas, and inspirations? failing to list the references you used can result in plagiarism. If you did not use any website say: "no references used".
   1. https://www.circuitbasics.com/how-to-use-photoresistors-to-detect-light-on-an-arduino/#:~:text=PROGRAMMING%20A%20PHOTORESISTOR%20TO%20CONTROL%20THINGS
   2. https://lastminuteengineers.com/joystick-interfacing-arduino-processing/
   3. https://www.arduino.cc/reference/en/language/functions/math/map/
   4. https://www.circuitbasics.com/how-to-use-photoresistors-to-detect-light-on-an-arduino/#:~:text=PROGRAMMING%20A%20PHOTORESISTOR%20TO%20CONTROL%20THINGS
   5. https://github.com/robsoncouto/arduino-songs

   6- Demo: in-person demonstration 3/13/2023 at 11:47 am to Dhwanit. 
*/




#define NOTE_B0  31
#define NOTE_C1  33
#define NOTE_CS1 35
#define NOTE_D1  37
#define NOTE_DS1 39
#define NOTE_E1  41
#define NOTE_F1  44
#define NOTE_FS1 46
#define NOTE_G1  49
#define NOTE_GS1 52
#define NOTE_A1  55
#define NOTE_AS1 58
#define NOTE_B1  62
#define NOTE_C2  65
#define NOTE_CS2 69
#define NOTE_D2  73
#define NOTE_DS2 78
#define NOTE_E2  82
#define NOTE_F2  87
#define NOTE_FS2 93
#define NOTE_G2  98
#define NOTE_GS2 104
#define NOTE_A2  110
#define NOTE_AS2 117
#define NOTE_B2  123
#define NOTE_C3  131
#define NOTE_CS3 139
#define NOTE_D3  147
#define NOTE_DS3 156
#define NOTE_E3  165
#define NOTE_F3  175
#define NOTE_FS3 185
#define NOTE_G3  196
#define NOTE_GS3 208
#define NOTE_A3  220
#define NOTE_AS3 233
#define NOTE_B3  247
#define NOTE_C4  262
#define NOTE_CS4 277
#define NOTE_D4  294
#define NOTE_DS4 311
#define NOTE_E4  330
#define NOTE_F4  349
#define NOTE_FS4 370
#define NOTE_G4  392
#define NOTE_GS4 415
#define NOTE_A4  440
#define NOTE_AS4 466
#define NOTE_B4  494
#define NOTE_C5  523
#define NOTE_CS5 554
#define NOTE_D5  587
#define NOTE_DS5 622
#define NOTE_E5  659
#define NOTE_F5  698
#define NOTE_FS5 740
#define NOTE_G5  784
#define NOTE_GS5 831
#define NOTE_A5  880
#define NOTE_AS5 932
#define NOTE_B5  988
#define NOTE_C6  1047
#define NOTE_CS6 1109
#define NOTE_D6  1175
#define NOTE_DS6 1245
#define NOTE_E6  1319
#define NOTE_F6  1397
#define NOTE_FS6 1480
#define NOTE_G6  1568
#define NOTE_GS6 1661
#define NOTE_A6  1760
#define NOTE_AS6 1865
#define NOTE_B6  1976
#define NOTE_C7  2093
#define NOTE_CS7 2217
#define NOTE_D7  2349
#define NOTE_DS7 2489
#define NOTE_E7  2637
#define NOTE_F7  2794
#define NOTE_FS7 2960
#define NOTE_G7  3136
#define NOTE_GS7 3322
#define NOTE_A7  3520
#define NOTE_AS7 3729
#define NOTE_B7  3951
#define NOTE_C8  4186
#define NOTE_CS8 4435
#define NOTE_D8  4699
#define NOTE_DS8 4978
#define REST 0

// change this to make the song slower or faster
int tempo = 144;

// change this to whichever pin you want to use
int buzzer = 11;

// notes of the moledy followed by the duration.
// a 4 means a quarter note, 8 an eighteenth , 16 sixteenth, so on
// !!negative numbers are used to represent dotted notes,
// so -4 means a dotted quarter note, that is, a quarter plus an eighteenth!!
int melody[] = {


  // Hedwig's theme fromn the Harry Potter Movies
  // Socre from https://musescore.com/user/3811306/scores/4906610
  
  REST, 2, NOTE_D4, 4,
  NOTE_G4, -4, NOTE_AS4, 8, NOTE_A4, 4,
  NOTE_G4, 2, NOTE_D5, 4,
  NOTE_C5, -2, 
  NOTE_A4, -2,
  NOTE_G4, -4, NOTE_AS4, 8, NOTE_A4, 4,
  NOTE_F4, 2, NOTE_GS4, 4,
  NOTE_D4, -1, 
  NOTE_D4, 4,

  NOTE_G4, -4, NOTE_AS4, 8, NOTE_A4, 4, //10
  NOTE_G4, 2, NOTE_D5, 4,
  NOTE_F5, 2, NOTE_E5, 4,
  NOTE_DS5, 2, NOTE_B4, 4,
  NOTE_DS5, -4, NOTE_D5, 8, NOTE_CS5, 4,
  NOTE_CS4, 2, NOTE_B4, 4,
  NOTE_G4, -1,
  NOTE_AS4, 4,
     
  NOTE_D5, 2, NOTE_AS4, 4,//18
  NOTE_D5, 2, NOTE_AS4, 4,
  NOTE_DS5, 2, NOTE_D5, 4,
  NOTE_CS5, 2, NOTE_A4, 4,
  NOTE_AS4, -4, NOTE_D5, 8, NOTE_CS5, 4,
  NOTE_CS4, 2, NOTE_D4, 4,
  NOTE_D5, -1, 
  REST,4, NOTE_AS4,4,  

  NOTE_D5, 2, NOTE_AS4, 4,//26
  NOTE_D5, 2, NOTE_AS4, 4,
  NOTE_F5, 2, NOTE_E5, 4,
  NOTE_DS5, 2, NOTE_B4, 4,
  NOTE_DS5, -4, NOTE_D5, 8, NOTE_CS5, 4,
  NOTE_CS4, 2, NOTE_AS4, 4,
  NOTE_G4, -1, 
  
};

// sizeof gives the number of bytes, each int value is composed of two bytes (16 bits)
// there are two values per note (pitch and duration), so for each note there are four bytes
int notes = sizeof(melody) / sizeof(melody[0]) / 2;

// this calculates the duration of a whole note in ms (60s/tempo)*4 beats
int wholenote = (60000 * 4) / tempo;
int divider = 0, noteDuration = 0;

int x_axis = A0; //X-axis pin
int y_axis = A1; //Y-axis pin

const int YELLOW = 7; //Input pin for the yellow LED on UNO R3
const int BLUE = 6; //Input pin for the blue LED on UNO R3
const int GREEN = 5; //Input pin for the green LED on UNO R3
const int RED = 4; //Input pin for the red LED on UNO R3

//PHOTORESISTOR
const int photoPin = A2; //Input pin for the photoresistor on UNO R3
int photoresistor_val; //Variable to store the photoresistor's value
int speaker_freq; //Used to change the speed of the piezzo speaker later

//SPEAKER => input pin for the speaker on UNO R3
const int speaker = 11; 

//MILLIS for the millis()
const long interval = 1000; 




void setup() {
  
    Serial.begin(9600);

    //Creating the output for the LEDs using the pin numbers
    pinMode(YELLOW, OUTPUT);
    pinMode(BLUE, OUTPUT);
    pinMode(GREEN, OUTPUT);
    pinMode(RED, OUTPUT);

    pinMode(photoPin, INPUT);
    pinMode(speaker, OUTPUT);


    //Melody
    // iterate over the notes of the melody. 
    // Remember, the array is twice the number of notes (notes + durations)
    for (int thisNote = 0; thisNote < notes * 2; thisNote = thisNote + 2) {


      //Using analogRead() allows to get the value of the photoresistor and store it inside the variable for further usage
      int light = analogRead(photoPin);

      //Outputs the value to the serial monitor
      Serial.println(light);
      delay(100);

      //Using map(), here I create a connection between photoresistor and the piezzo speaker
      photoresistor_val = analogRead(photoPin); // Read photoresistor value
      speaker_freq = map(photoresistor_val, 0, 1023, 100, 500); //Right here I mapped the photoresistor value to speaker freq

      // calculates the duration of each note
      divider = melody[thisNote + 1];



    // Increase or decrease note duration based on photoresistor value    
    if (divider > 0) {
        // regular note, just proceed
        noteDuration = (wholenote) / divider;
        //noteDuration = analogRead(photoPin);
        //noteDuration = flag;

        //If the bound is reached => transform the value into the new one => speed changes
        if (photoresistor_val > 200) {
            noteDuration = photoresistor_val / 3;
        }
        else{
           noteDuration = noteDuration;
        }
    }
    else if (divider < 0) {
        // dotted notes are represented with negative durations!!
        noteDuration = (wholenote) / abs(divider);
        noteDuration *= 1.5; // increases the duration in half for dotted note

         //If the bound is reached => transform the value into the new one => speed changes
        if (photoresistor_val > 200) {
            noteDuration = photoresistor_val / 3;
        }
        else{
           noteDuration = noteDuration;
        }
  
    }


    //Used for millis()
    static unsigned long previousMillis = 0;  // remember the last time we blinked the LED
    unsigned long currentMillis = millis();   // get the current time

    /*if (currentMillis - previousMillis >= interval) {  // if it's been a second since the last blink
        previousMillis = currentMillis;   // remember the time of the last blink
        tone(buzzer, melody[thisNote], speaker_freq); // Play tone at mapped frequency
    }*/

    
     //noTone(buzzer);
    
    // we only play the note for 90% of the duration, leaving 10% as a pause MELODY PLAY
    tone(buzzer, melody[thisNote], noteDuration*0.9);
    //tone(buzzer, melody[thisNote], speaker_freq); // Play tone at mapped frequency
    
    // Wait for the specief duration before playing the next note. => need to use millis()
    delay(noteDuration);
  
    // stop the waveform generation before the next note. MELODY PLAY
    noTone(buzzer);
  }

}




void loop() {

  //Photoresistor reading
  /*int light = analogRead(photoPin);
  Serial.println(light);
  delay(100);

  //Using map(), here I create a connection between photoresistor and the piezzo speaker
  photoresistor_val = analogRead(photoPin); // Read photoresistor value
  speaker_freq = map(photoresistor_val, 0, 1023, 100, 500); //Right here I mapped the photoresistor value to speaker freq*/
  
  //tone(speaker, speaker_freq); // Play tone at mapped frequency

  // Increase or decrease note duration based on photoresistor value
  /*if (photoresistor_va222l > 300) {
    noteDuration = 50;
  }
  else if (photoresistor_val < 200) {
    noteDuration = 150;
  }*/
  
  // Wait for the note to finish playing before playing the next one
  //delay(noteDuration);


  int x = analogRead(x_axis); 
  int y = analogRead(y_axis); 
  

  // Determine which LED should be on based on joystick position => TA
  if (x < 300) { //BOTTOM
    digitalWrite(YELLOW, LOW);
    digitalWrite(BLUE, HIGH);
    digitalWrite(GREEN, LOW);
    digitalWrite(RED, LOW);
  }
   else if (y < 300) { //LEFT
    digitalWrite(YELLOW, LOW);
    digitalWrite(BLUE, LOW);
    digitalWrite(GREEN, HIGH);
    digitalWrite(RED, LOW);
  }
  else if (x > 700) { //TOP
    digitalWrite(YELLOW, LOW);
    digitalWrite(BLUE, LOW);
    digitalWrite(GREEN, LOW);
    digitalWrite(RED, HIGH);
  }
  else if (y > 700) { //RIGHT
    digitalWrite(YELLOW, HIGH);
    digitalWrite(BLUE, LOW);
    digitalWrite(GREEN, LOW);
    digitalWrite(RED, LOW);
  }
  else { //CENTER => EVERYTHING IS OFF
    digitalWrite(YELLOW, LOW);
    digitalWrite(BLUE, LOW);
    digitalWrite(GREEN, LOW);
    digitalWrite(RED, LOW);
  }
}
