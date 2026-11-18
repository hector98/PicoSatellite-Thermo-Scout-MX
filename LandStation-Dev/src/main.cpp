#include <Wire.h>
#include <Arduino.h>

void setup() {
  Serial.begin(115200);
}

float temp = 10.0;

void respond_ok() {
  String r = Serial.readString();
  Serial.println(r);
 delay(1);

  if(r == ""){
    respond_ok();
  }
}

void loop() {
  while (temp < 40.0){
    Serial.println("01;"+ String(temp));
    temp += 0.2;
    delay(500);
    respond_ok();
  }

  while(temp > 10.0){
    Serial.println("01"+ String(temp));
    temp -= 0.2;
    delay(500);
  }

  delay(500);
}
