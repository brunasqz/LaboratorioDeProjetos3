/*
   Referência
   https://www.filipeflop.com/blog/controlando-um-motor-de-passo-5v-com-arduino/
*/

#include <Stepper.h>

const int magnetPin = 2;
const int stepsPerRevolution = 500;

Stepper stepper1(stepsPerRevolution, 3, 5, 4, 6);
Stepper stepper2(stepsPerRevolution, 8, 10, 9, 11);

void setup()
{
  pinMode(magnetPin, OUTPUT);
  Serial.begin(9600);
  stepper1.setSpeed(15);
  stepper2.setSpeed(80);
}

void loop()
{

  if (Serial.available()) {
    String data = Serial.readString();
    if (data[0] == 'm') {
      digitalWrite(magnetPin, data[1] == '1' ? HIGH : LOW);
    }
    else {
      int grades = data.substring(1).toInt();
      grades = (grades / 360.0) * 2048.0;    
      if (data[0] == 'c') {
        stepper1.step(grades * -1);
        delay(2000);
      }
      else if (data[0] == 'a') {
        stepper1.step(grades  *1);
        delay(2000);
      }
      else if (data[0] == 'b') {
        stepper2.step(grades * -1);
        delay(2000);
      }
      else if (data[0] == 'd') {
        stepper2.step(grades  *1);
        delay(2000);
      }
    }
  }

}
