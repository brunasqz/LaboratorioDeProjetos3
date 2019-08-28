int green = 2;
int yellow = 3;
int red = 4;

void setup() {
  pinMode(green, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(red, OUTPUT);
}

void loop() {

  long rGreen = random(100);
  long rYellow = random(100);
  long rRed = random(100);
  
  digitalWrite(green, rGreen > 50 ? HIGH : LOW);
  digitalWrite(yellow, rYellow > 50 ? HIGH : LOW);
  digitalWrite(red, rRed > 50 ? HIGH : LOW);  
  delay(500); 
  
}
