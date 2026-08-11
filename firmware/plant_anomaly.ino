// PEAR Lab replication sketch
// This firmware implements the documented debiasing logic for the LED switching experiment.

const int zenerPin = A0;
const int leftLight = 2;
const int rightLight = 3;

const unsigned long interval = 60000; // 1 minute per cycle
unsigned long previousMillis = 0;

void setup() {
  pinMode(leftLight, OUTPUT);
  pinMode(rightLight, OUTPUT);
  Serial.begin(9600);

  digitalWrite(leftLight, LOW);
  digitalWrite(rightLight, LOW);
}

void loop() {
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

    int quantumDecision = getDebiasedBit();

    if (quantumDecision == 0) {
      digitalWrite(leftLight, HIGH);
      digitalWrite(rightLight, LOW);
      Serial.println("Decision: LEFT (Plant)");
    } else if (quantumDecision == 1) {
      digitalWrite(leftLight, LOW);
      digitalWrite(rightLight, HIGH);
      Serial.println("Decision: RIGHT (Empty)");
    }
  }
}

int getDebiasedBit() {
  while (true) {
    int bit1 = getRawBit();
    delay(10);
    int bit2 = getRawBit();

    if (bit1 == 0 && bit2 == 1) return 0;
    if (bit1 == 1 && bit2 == 0) return 1;
  }
}

int getRawBit() {
  int rawVoltage = analogRead(zenerPin);
  return rawVoltage & 1;
}
