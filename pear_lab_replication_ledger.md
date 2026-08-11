# Replicating the PEAR Lab Plant Anomaly: Experimental Ledger
**Project Framework & Assembly Manual**

---

## 1. Core Experimental Framework

This document outlines a complete framework for testing whether a living plant can act as a localized thermodynamic energy sink, subtly biasing a local probability space to "pull" photons toward itself. 

By building a solid-state system with **two fixed LED lamps** and an **Arduino microcontroller**, you eliminate the mechanical, thermal, and physical anomalies introduced by moving parts.

```text
                               +-----------------------------+

                               |     LIGHT-TIGHT CHAMBER     |
                               |                             |
                               |      [ LED 1 ]   [ LED 2 ]  |
                               |          |           |      |
                               |          v           v      |
                               |      ( PLANT )    (EMPTY)   |
                               +----------|-----------|------+

                                          |           |
                                    [LEFT RELAY] [RIGHT RELAY]
                                          \           /
                                           \         /
                                        +---------------+
    +-----------------------+           |  ARDUINO UNO  |
    |   DIY ZENER DIODE     |---------->|               |
    | QUANTUM NOISE SOURCE  | (A0 pin)  | [Code Logic]  |
    +-----------------------+           +---------------+
```

---

## 2. Hardware Bill of Materials (BOM)

### Microcontroller & Switching
*   **Arduino Uno or Raspberry Pi Pico**: Handles the code execution and switching logic.
*   **Dual-Channel 5V Relay Module**: Isolates high voltage/current away from the logic board.

### Amplified Avalanche Noise Source
*   **Zener Diode (6.2V to 7.5V)**: The source of quantum subatomic noise.
*   **2N3904 NPN Transistors (x2)**: Two-stage amplifier array to boost microvolt signals.
*   **Capacitors**: 100nF Ceramic Capacitors (x2) to block DC offset.
*   **Resistors**: 10k\u03a9 (x3), 1k\u03a9 (x3) for signal attenuation and routing.
*   **9V Battery or 12V Wall Adapter**: Independent power supply for the Zener circuit.

---

## 3. DIY Avalanche Noise Generator Circuit

The voltage forces its way backward through the Zener diode, provoking **avalanche breakdown**. This outputs microscopic, completely unpredictable quantum voltage spikes.

```text
    +12V Power (or 9V)
         |
         +------+---------------+

         |      |               |
        [10k]  [10k]           [1k]

         |      |               |
         |      +--------+      |
         |      |        |      |
         |     --- C1    |     --- C2
      [Zener]  --- 100nF |     --- 100nF
     (12V max,  |        |      |
      6.2V-7.5V)|        |      |

         |      |      |/       |      |/
         +------+------|  Q1    +------|  Q2 (2N3904)

         |             |>\             |>\
         |                |               |
       [10k]            [1k]            [1k]     To Arduino 
         |                |               | ----> Analog A0 Pin
        GND              GND             GND
```

### Circuit Execution Stages:
1.  **Quantum Source**: Reverse-biased Zener breaks down randomly at subatomic scales.
2.  **Stage 1 Boost (Q1)**: Capacitor C1 strips away baseline DC voltage. Q1 amplifies the tiny AC static wave.
3.  **Stage 2 Boost (Q2)**: Capacitor C2 blocks secondary DC shifts. Q2 pushes the final noise wave into a chaotic, readable 0V–5V swing.

---

## 4. Wiring Layout

1.  **Noise Input**: Wire the amplified analog output of your Zener circuit straight to **Analog Input Pin A0** on the Arduino.
2.  **Relay Logic**: Connect your dual-channel 5V relay module input pins to **Digital Output Pins 2 and 3**.
3.  **Mains Delivery**: Wire the power lines for the Left LED through Relay 1 (Pin 2) and the Right LED through Relay 2 (Pin 3).

---

## 5. Complete Replication Code

This firmware runs a mandatory **Von Neumann debiasing engine** to completely filter out physical circuit shifts, ensuring that any deviation discovered is mathematically real.

```cpp
// PIN CONFIGURATION
const int zenerPin = A0;      // Analog pin reading Zener quantum noise
const int leftLight = 2;      // Digital pin controlling Left LED (Plant)
const int rightLight = 3;     // Digital pin controlling Right LED (Empty)

// EXPERIMENTAL PARAMETERS
const unsigned long interval = 60000; // 1 minute per cycle (in milliseconds)
unsigned long previousMillis = 0;

void setup() {
  pinMode(leftLight, OUTPUT);
  pinMode(rightLight, OUTPUT);
  Serial.begin(9600);
  
  // Start with both lights off to prevent initial power-on bias
  digitalWrite(leftLight, LOW);
  digitalWrite(rightLight, LOW);
}

void loop() {
  unsigned long currentMillis = millis();
  
  // Trigger a new quantum choice precisely every interval
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    
    int quantumDecision = getDebiasedBit();
    
    if (quantumDecision == 0) {
      // 0 = Turn on Left Light (Plant side), turn off Right Light
      digitalWrite(leftLight, HIGH);
      digitalWrite(rightLight, LOW);
      Serial.println("Decision: LEFT (Plant)");
    } 
    else if (quantumDecision == 1) {
      // 1 = Turn on Right Light (Empty side), turn off Left Light
      digitalWrite(leftLight, LOW);
      digitalWrite(rightLight, HIGH);
      Serial.println("Decision: RIGHT (Empty)");
    }
  }
}

// VON NEUMANN DEBIASING ENGINE
int getDebiasedBit() {
  while (true) {
    int bit1 = getRawBit();
    delay(10); // Small pause between readings to prevent ghost charge correlation
    int bit2 = getRawBit();
    
    // Von Neumann Logic:
    // 0 followed by 1 = Valid 0
    if (bit1 == 0 && bit2 == 1) return 0;
    // 1 followed by 0 = Valid 1
    if (bit1 == 1 && bit2 == 0) return 1;
    
    // If 0,0 or 1,1 occur, they are discarded and the loop runs again.
    // This removes any physical bias from the circuit completely.
  }
}

// RAW BIT GENERATOR (Reads Least Significant Bit of Analog Noise)
int getRawBit() {
  int rawVoltage = analogRead(zenerPin);
  // Extract only the lowest bit (even numbers = 0, odd numbers = 1)
  // This isolates the fastest-changing, most random part of the signal
  return rawVoltage & 1; 
}
```

---

## 6. Strict Testing Protocol

### Phase 1: The Baseline Control (7 to 14 Days)
Hang both lamps inside the light-tight box with **no plant inside**. Let the script cycle the lamps back and forth uninterrupted. 
*   **Verification**: Pull the logged serial lines. The total count must sit at a **50/50 split** (within acceptable short-term random bounds). If a massive bias shows up here, check for noise leakage in your breadboard.

### Phase 2: The Biological Anchor (14 Days)
Place a rapid-growth, light-hungry plant (like a young **Common Sunflower** or **Radish Greens**) directly on the **Left side** of the chamber under LED 1. Leave the right side empty. Do not alter a single line of code. Let the system run automatically.
*   **The Evaluation**: Compare the statistical distribution of Phase 2 against Phase 1. Any consistent, statistically significant elevation of the Left LED states reveals a successful replication of the PEAR anomaly.

---

## 7. Critical Safeguards Against Interference

*   **Electromagnetic Shielding**: Relays output a micro-electromagnetic pulse when clicking. Wrap your Zener board in aluminum foil (**Grounded Faraday Shielding**) and keep it outside the primary light-tight box to prevent feedback.
*   **Thermal Deflection**: Plant respiration alters local chamber heat. Keep the Arduino and the noise circuit board **completely outside the box** to ensure that environmental temperature shifts cannot drift the transistor thresholds.