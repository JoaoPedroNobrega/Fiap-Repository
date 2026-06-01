#include<DHT.h>
#define dhtpin 7
#define dhttype DHT22
// tem que mudar 22 e 11 dependendo do DHT

int temp = 0;
int umi = 0;

// tipo do objeto, depois vem o nome do objeto, junta os dois
DHT dht(dhtpin, dhttype);

void setup() {
Serial.begin(9600);
dht.begin();

}

void loop() {

  //leitura da temperatura
  temp = dht.readTemperature();
  //leitura da umidade
  umi = dht.readHumidity();


  Serial.println("Temperatura atual: " + String(temp));
  delay(2000);
  Serial.println("Umidade atual: " + String(umi));
  delay(2000);

}
