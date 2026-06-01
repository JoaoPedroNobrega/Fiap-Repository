#define ldrPin A0
int ldrValor = 0;
#define ledR 8
#define ledY 7
#define ledG 6

// usamos int pq o valor variar de acordo com a luz do ambiente
// se usar define o valor não mudaria


void setup() {
  // se não startar o serial.begin o serialprint não funciona
  Serial.begin(9600);
  pinMode(ldrPin, INPUT);
  pinMode(ledR, OUTPUT);
  pinMode(ledY, OUTPUT);
  pinMode(ledG, OUTPUT);
  

}

void loop() {
  ldrValor = analogRead(ldrPin);
  Serial.println(ldrValor);
  delay(2000);

if (ldrValor > 600) {
    digitalWrite(ledG, HIGH);
    digitalWrite(ledY, LOW);
    digitalWrite(ledR, LOW);
} else if (ldrValor > 300) {
    digitalWrite(ledG, LOW);
    digitalWrite(ledY, HIGH);
    digitalWrite(ledR, LOW);
} else {
    digitalWrite(ledG, LOW);
    digitalWrite(ledY, LOW);
    digitalWrite(ledR, HIGH);
}

//estrutura basica

}
