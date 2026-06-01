#define trigger1 8
#define echo1 7
int dist1 = 0;
#define ledR 4
#define trigger2 3
#define echo2 2
int dist2 = 0;
#define ledR2 11

void setup()
 {
  Serial.begin(9600);
  pinMode(trigger1, OUTPUT);
  pinMode(trigger2, OUTPUT);
  pinMode(echo1, INPUT);
  pinMode(echo2, INPUT);
  pinMode(ledR, OUTPUT);
  pinMode(ledR2, OUTPUT);
}

void loop() {
  digitalWrite(trigger1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger1, LOW);
  dist1 = pulseIn(echo1, HIGH); // tempo em microsegundos
  dist1 = dist1 / 58; // distância em cm

  digitalWrite(trigger2, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger2, LOW);

  dist2 = pulseIn(echo2, HIGH);
  dist2 = dist2 / 58;

 
  
 
  
  if(dist1 >= 50){
    digitalWrite(ledR, HIGH);
    Serial.println("Prateleira 1 Vazio");
    delay(2000);
  }else if(dist1 >= 30){
    digitalWrite(ledR, LOW);
    Serial.println("Prateleira 1 médio");
    delay(2000);
    }else{
      digitalWrite(ledR, LOW);
    Serial.println("Prateleira 1 Cheio");
    delay(2000);
  }



  if(dist2 >= 50){
    digitalWrite(ledR2, HIGH);
    Serial.println("Prateleira 2 Vazio");
    delay(2000);
  }else if(dist2 >= 30){
    digitalWrite(ledR2, LOW);
    Serial.println("Prateleira 2 médio");
    delay(2000);
    }else{
      digitalWrite(ledR2, LOW);
    Serial.println("Prateleira 2 Cheio");
    delay(2000);
  }
}