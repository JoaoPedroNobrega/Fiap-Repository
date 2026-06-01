#include <Servo.h>
#define servoPin 10
#define trigger 7
#define echo 8
int dist = 0;
#define ledR 5

// Criando o objeto myservo do tipo servo
Servo myServo;



void setup() {
  Serial.begin(9600);
  myServo.attach(servoPin);
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(ledR, OUTPUT);

}

void loop() {
  
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);

  dist = pulseIn(echo, HIGH);
  dist = dist / 58;

  if(dist < 20){

  digitalWrite(ledR, HIGH);
  myServo.write(180);
 
  }else{
    digitalWrite(ledR, LOW);
  myServo.write(0);
  }
}
