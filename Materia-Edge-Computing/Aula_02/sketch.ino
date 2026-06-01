#define ledR 8
#define ledY 9
#define ledG 10

void setup() {
  //Definir que o LED é uma saída
  pinMode(ledR, OUTPUT);
  pinMode(ledY, OUTPUT);
  pinMode(ledG, OUTPUT);
  //Inicializar  a Serial
  Serial.begin(9600);
  Serial.println("oi");
}

void loop() {
  //Se a serial for aberta
  if(Serial.available() > 0){
    char comando = Serial.read();
    if(comando == '1'){
      digitalWrite(ledR, HIGH);
    }else if(comando == '0'){
    digitalWrite(ledR, LOW);
  }
  }
}