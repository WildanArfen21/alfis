#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);
int sensorPin = A3; 
int sensorValue = 0; 
 
void setup(){
lcd.clear();
lcd.init();
lcd.backlight();
Serial.begin(9600);
 
pinMode(14, INPUT);digitalWrite(14, HIGH);
pinMode(15, INPUT);digitalWrite(15, HIGH);
pinMode(16, INPUT);digitalWrite(16, HIGH);
pinMode(2, INPUT);digitalWrite(2, HIGH);
pinMode(3, INPUT);digitalWrite(3, HIGH);
pinMode(4, INPUT);digitalWrite(4, LOW);
pinMode(5, OUTPUT);digitalWrite(5, LOW);
lcd.clear();
}
double i = 0;
double j = 0;
double a = millis();
double c ;
int Sudut=0;

void loop()
{
if(digitalRead(3) == HIGH){
lcd.setCursor(0,0);
lcd.print(" Bidang  Miring ");
lcd.setCursor(0,1);
lcd.print("Sudut : ");
sensorValue = analogRead(sensorPin);
Sudut=sensorValue/3.3;
lcd.setCursor(8,1);
lcd.print(Sudut);
lcd.print((char)223);
lcd.print("       ");
digitalWrite(5,LOW);
//----------------------------------------------
//Pembacaan Timer 1 ke 2
if(digitalRead(14) == LOW)
{
 
lcd.clear();
a = millis();
while(digitalRead(15) == HIGH)
{
 
c = millis();
i = (c - a) / 1000;
lcd.setCursor(0,0);
lcd.print("T:");
lcd.setCursor(2,0);
lcd.print(i);
lcd.setCursor(0,1);
lcd.print("Sudut : ");
lcd.setCursor(8,1);
lcd.print(Sudut);
lcd.print((char)223);
lcd.setCursor(0,0);
delay(10);
}
//Pembacaan Timer 2 ke 3
//----------------------------------------------
if(digitalRead(15) == LOW)
{
a = millis();
while(digitalRead(16) == HIGH)
{
 
c = millis();
j = (c - a) / 1000  ;

lcd.setCursor(9,0);
lcd.print("T: ");
lcd.setCursor(11,0);
lcd.print(j);
lcd.setCursor(0,1); 
lcd.setCursor(0,0);
delay(10);
}
//Stop
//----------------------------------------------
if(digitalRead(16) == LOW){while(digitalRead(2) == HIGH){
}}}}}

if(digitalRead(3) == LOW){
digitalWrite(5,HIGH);
lcd.setCursor(0,0);
lcd.print("Alat Jatuh Bebas");
lcd.setCursor(0,1);
lcd.print("Solenoid On       ");
//----------------------------------------------
//Pembacaan Timer 1 ke 2
if(digitalRead(4) == LOW)
{
 
lcd.clear();
a = millis();
while(digitalRead(14) == LOW)
{
 
c = millis();
i = (c - a) / 1000;
lcd.setCursor(0,0);
lcd.print("T:");
lcd.setCursor(2,0);
lcd.print(i);
lcd.setCursor(0,1);
lcd.print("Solenoid OFF ");
digitalWrite(5,LOW);

delay(10);
}
//Pembacaan Timer 2 ke 3
//----------------------------------------------
if(digitalRead(14) == HIGH)
{
a = millis();
while(digitalRead(15) == LOW)
{
 
c = millis();
j = (c - a) / 1000  ;

lcd.setCursor(9,0);
lcd.print("T: ");
lcd.setCursor(11,0);
lcd.print(j);
lcd.setCursor(0,1); 
lcd.setCursor(0,0);
delay(10);
}
//Stop
//----------------------------------------------
if(digitalRead(15) == HIGH){while(digitalRead(2) == HIGH){
}}}}}
}
