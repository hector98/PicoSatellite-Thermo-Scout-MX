// CanSat/src/main.cpp 
#include <Wire.h>
#include <Arduino.h>

void setup() {
  Serial.begin(115200);
  delay(200);

  Serial.println("Hola");
}

void loop() {
  print(serial);

  delay(500);
}
