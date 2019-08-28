/*
   Referência
   https://www.filipeflop.com/blog/controlando-um-motor-de-passo-5v-com-arduino/
*/

#include <Stepper.h>

const int stepsPerRevolution = 500;
Stepper stepper(stepsPerRevolution, 8, 10, 9, 11);

void setup()
{
  Serial.begin(9600);
  stepper.setSpeed(60);
}

void loop()
{

  if (Serial.available()) {
    String data = Serial.readString();
    int grades = data.substring(1).toInt();
    grades = (grades / 360.0) * 2048.0;    
    if (data[0] == 'c') {
      stepper.step(grades * -1);
      delay(2000);
    }
    else if (data[0] == 'a') {
      stepper.step(grades  *1);
      delay(2000);
    }
  }

}
