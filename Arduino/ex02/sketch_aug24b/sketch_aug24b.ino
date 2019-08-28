int LED_GREEN = 2;
int LED_YELLOW = 3;
int LED_RED = 4;

void setup() {
  Serial.begin(9600);
  
  pinMode(LED_GREEN, OUTPUT);
  pinMode(LED_YELLOW, OUTPUT);
  pinMode(LED_RED, OUTPUT);
  
  digitalWrite(LED_GREEN, LOW);  
  digitalWrite(LED_YELLOW, LOW);  
  digitalWrite(LED_RED, LOW);
}

void loop() {

  if (Serial.available())
  {
    String data = Serial.readString();
    if (data[0] == 'g') {
      digitalWrite (LED_GREEN, data[1] == '1' ? HIGH : LOW);
    }
    else if (data[0] == 'y') {      
      digitalWrite (LED_YELLOW, data[1] == '1' ? HIGH : LOW);
    }
    else if (data[0] == 'r') {      
      digitalWrite (LED_RED, data[1] == '1' ? HIGH : LOW);
    }    
  }
}
