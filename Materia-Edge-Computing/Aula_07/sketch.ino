#include<LiquidCrystal_I2C.h>

//Tipo do objeto => nome do objeto
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  //inicializando a tela
  lcd.init();

  //liga a luz de fundo da tela
  lcd.backlight();
  //posição Inicial
  lcd.setCursor(0,0);
  lcd.print("Bem vindo");
  delay(1000);
  lcd.setCursor(9,0);
  lcd.print(".");
  delay(1000);
  lcd.setCursor(10,0);
  lcd.print(".");
  delay(1000);
  lcd.setCursor(11,0);
  lcd.print(".");
  delay(1000);
  lcd.setCursor(12,0);
  lcd.print(".");
  delay(1000);
  lcd.clear();
}

void loop() {
  lcd.setCursor(0,1);
  lcd.print("Joao Pedro");

}