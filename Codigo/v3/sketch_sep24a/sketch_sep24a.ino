
#include <Stepper.h>

const int magnetPin = 2;
const int stepsPerRevolution = 500;
const int GirarLanca = 1;
const int Subir_DescerIMa = 2;
const int Liga_DesligaEletroIma = 3;
const int SentidoHorario = 1;
const int SentidoAntihorario = 0;

Stepper MotorLanca(stepsPerRevolution, 3, 5, 4, 6);  //Motor da Lança
Stepper MotorIca(stepsPerRevolution, 8, 10, 9, 11);  //Motor da Iça

void setup()
{
  pinMode(magnetPin, OUTPUT);
  Serial.begin(9600);
  MotorIca.setSpeed(50);
  MotorLanca.setSpeed(15);
}

void loop()
{

  if (Serial.available())
  {
    // x  x  x  x  x  x  x x x x x x x x x x
    // 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
    
    // Data[0] = 8 [8,15] bits mais significativos do protocolo
    // Data[1] = 8 [0,7] bits menos significativos do protocolo

    byte data[2];

    Serial.readBytes(data, 2);
    byte Evento = data[0] >> 1;  
    byte Sentido = data[0] & 1;
    byte arg = data[1];
    
    if (Evento == Liga_DesligaEletroIma)
    {
      digitalWrite(magnetPin, arg == 1 ? HIGH : LOW);
    }
    else
    {
      int Graus = (arg/360.0) * 2048.0;
      
      if ((Evento == GirarLanca)&&(Sentido == SentidoHorario))
      {
        MotorLanca.step(Graus * -1);
        delay(2000);
      }
      else if ((Evento == GirarLanca)&&(Sentido == SentidoAntihorario))
      {
        MotorLanca.step(Graus * 1);
        delay(2000);
      }
      else if ((Evento == Subir_DescerIMa)&&(Sentido == SentidoHorario))
      {
        MotorIca.step(Graus * -180);
        delay(2000);
      }
      else if ((Evento == Subir_DescerIMa)&&(Sentido == SentidoAntihorario))
      {
        MotorIca.step(Graus * 180);
        delay(2000);
      }
    }
  }
}
