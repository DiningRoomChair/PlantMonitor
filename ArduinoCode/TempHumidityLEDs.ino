//get DHT sensor ready
#include <dht11.h>
dht11 DHT;
//set pin numbers
const int dht11_data = 6;
int lightpin = 0;
int templed = 13;
int humled = 12;
int lightled = 11;
//initialize variables
int light = 0;     
int temp=0;
int hum=0;

void setup()                                                                                     
{
  Serial.begin(9600);
  pinMode(templed, OUTPUT);
  pinMode(humled, OUTPUT);
  pinMode(lightled, OUTPUT);
}
void loop()
{
  DHT.read(dht11_data);
  //read and set sensor outputs
  light = analogRead(lightpin);
  temp=DHT.temperature;
  hum=DHT.humidity;
  //print light sensor output and adjust LED
  Serial.print("Light=");
  Serial.println(light);
  if(light < 700){
    digitalWrite(lightled, HIGH);
  }
  else{
    digitalWrite(lightled, LOW);
  }
  //print temp sensor output and adjust LED
  Serial.print("Temp=");
  Serial.println(temp,DEC);
  if(temp > 22){
    digitalWrite(templed, HIGH);
  }
  else{
    digitalWrite(templed, LOW);
  }
  //print humidity sensor output and adjust LED
  Serial.print("Humidity=");
  Serial.println(hum,DEC);
  if(hum > 40){
    digitalWrite(humled, HIGH);
  }
  else{
    digitalWrite(humled, LOW);
  }
  //rerun the loop every 1s
  delay(1000);
}
