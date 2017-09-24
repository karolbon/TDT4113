// Initialisere 
const int buttonPin = 2;
const int whiteLed = 3; 
const int yelLed = 4; 

// Konstater for signaler som skal sendes
const int dot = 0; 
const int dash = 1; 
const int letterPauseSignal = 2; 
const int wordPauseSignal = 3; 

// Konstanter tid 
const float T = 500; 
const float dotTime = T; 
const float dashTime = 2*T; 
const float letterPause = 5*T; 
const float wordPause = 10*T; 

int buttonState; 
int previousBtnState = HIGH; 

long timeFromPush; 
long releaseTime = 0; 

void setup() { 
  Serial.begin(9600);
  
  pinMode(buttonPin, INPUT); 
  pinMode(whiteLed, OUTPUT); 
  pinMode(yelLed, OUTPUT); 
}


void loop() {

  buttonState = digitalRead(buttonPin); 
  
  if (previousBtnState == HIGH && buttonState == LOW) {
    
    timeFromPush = millis(); 
    previousBtnState = LOW; 
    long pause = millis() - releaseTime;
    
    if (releaseTime != 0) {
      if (pause < wordPause && pause > letterPause){
        Serial.print(letterPauseSignal); 
      } else if (pause > wordPause){
        Serial.print(wordPauseSignal); 
      }
    }

    
     // Button is pushed


  } else if (previousBtnState == LOW && buttonState == HIGH) {
    // Button is released 
    releaseTime = millis();


    long holdTime = millis() - timeFromPush; 

    // Dot or dash 
    if (holdTime < dashTime){
      Serial.print(dot); 
      digitalWrite(yelLed, HIGH); 
      digitalWrite(whiteLed, LOW); 
     } else if (holdTime > dashTime) {
      Serial.print(dash); 
      digitalWrite(yelLed, LOW); 
      digitalWrite(whiteLed, HIGH); 
     }

  previousBtnState = HIGH; 
  }
 
delay(20);
  

}
