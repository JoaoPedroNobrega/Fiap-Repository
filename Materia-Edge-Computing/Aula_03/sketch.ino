#define trigger 7
#define echo 8
int dist = 0;
#define ledR 5
#define ledY 4
#define ledG 3

void setup() {
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(ledR, OUTPUT);
  pinMode(ledY, OUTPUT);
  pinMode(ledG, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);

  dist = pulseIn(echo, HIGH); // tempo em microsegundos
  dist = dist / 58; // distância em cm
  
  if(dist < 5){
    digitalWrite(ledR, HIGH);
    digitalWrite(ledY, LOW);
    digitalWrite(ledG, LOW);
    Serial.println(dist);
  }else if(dist < 10){
    digitalWrite(ledY, HIGH);
    digitalWrite(ledR, LOW);
    digitalWrite(ledG, LOW);
    Serial.println(dist);
  }else{
    digitalWrite(ledG, HIGH);
    digitalWrite(ledY, LOW);
    digitalWrite(ledR, LOW);
    Serial.println(dist);
  }
}
