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
  stepper2.setSpeed(15);
}

void loop()
{

  if (Serial.available())
  {
    String data = Serial.readString();
    int op = (data & 1536) >> 9;
    int arg = (s & 511);
    if (op == 5 ||op = 6)
    {
      digitalWrite(magnetPin, arg == 5 ? HIGH : LOW);
    }
    else
    {
      int grades = arg;
      grades = (grades / 360.0) * 2048.0;
      if (op == 1)
      {
        stepper1.step(grades * -1);
        delay(2000);
      }
      else if (op == 2)
      {
        stepper1.step(grades * 1);
        delay(2000);
      }
      else if (op == 3)
      {
        stepper2.step(grades * -1);
        delay(2000);
      }
      else if (op == 4)
      {
        stepper2.step(grades * 1);
        delay(2000);
      }
    }
  }
}
