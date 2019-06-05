#include <Servo.h>

Servo servo;

void setup() {
  servo.attach(9);
  servo.write(0);
  pinMode(8, INPUT);
  digitalWrite(8, LOW);
}

void loop() {
 if (digitalRead(8)==HIGH){
    servo.write(90);
    delay(1000);
    servo.write(0);  
 }
 delay(100); 
}
