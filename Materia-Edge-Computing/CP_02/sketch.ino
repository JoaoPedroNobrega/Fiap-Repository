#include<Servo.h>
#define servoPin 9
#define servoPin2 3
#define trigger 12
#define echo 11
#define led 13
#define led2 2
int dist = 0;
//Criando o objeto myservo do tipo Servo
Servo myServo;
Servo myServo2;

void setup() {
  Serial.begin(9600);
  myServo.attach(servoPin);
  myServo2.attach(servoPin2);
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(led, OUTPUT);
  pinMode(led2, OUTPUT);
}
void loop() {
  digitalWrite(trigger, HIGH);
  delayMicroseconds(20);
  digitalWrite(trigger, LOW);

  dist = pulseIn(echo, HIGH);
  dist = dist/58;

  if(dist < 5) {
    myServo.write(90);
    myServo2.write(0);
    digitalWrite(led, HIGH);
    digitalWrite(led2, LOW);
  }else if (dist >= 5 && dist <= 40){
    digitalWrite(led2, HIGH);
    digitalWrite(led, LOW);
    myServo.write(0);
    myServo2.write(90);
  }else{
    digitalWrite(led, HIGH);
    digitalWrite(led2, HIGH);
    myServo.write(90);
    myServo2.write(90);
  }

}

