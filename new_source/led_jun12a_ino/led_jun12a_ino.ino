// char incomingByte = 0; // for incoming serial data
int pin1 = 10;
int pin2 = 11;
void setup() {
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  pinMode(pin1,OUTPUT);
  pinMode(pin2,OUTPUT);
  digitalWrite(pin1,LOW);
}

void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    String incomingByte = Serial.readString();
    Serial.print("I received: ");
    Serial.println(incomingByte);
    if (incomingByte == "on") {
      Serial.print("  10!)");
      digitalWrite(pin1,HIGH);
      //digitalWrite(pin2,LOW);
      //tone(9, 700);
    }if (incomingByte == "off") {
       digitalWrite(pin1,LOW);
       //tone(9,0);
       //digitalWrite(pin2,HIGH);
       Serial.print("  2!)");
    }
  }
}
