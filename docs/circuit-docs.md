# Circuit Documentation (Draft)

This draft documents the DIY avalanche noise generator circuit referenced by `circuit-docs` in the mirrored ledger. It is derived from Section 3 of `pear_lab_replication_ledger.md`.
Core Experimental Framework
This document outlines a complete framework for testing whether a living plant can act as a localized thermodynamic energy sink, subtly biasing a local probability space to "pull" photons toward itself.

By building a solid-state system with two fixed LED lamps and an Arduino microcontroller, you eliminate the mechanical, thermal, and physical anomalies introduced by moving parts.

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
2. Hardware Bill of Materials (BOM)
Microcontroller & Switching
Arduino Uno or Raspberry Pi Pico: Handles the code execution and switching logic.
Dual-Channel 5V Relay Module: Isolates high voltage/current away from the logic board.
Amplified Avalanche Noise Source
Zener Diode (6.2V to 7.5V): The source of quantum subatomic noise.
2N3904 NPN Transistors (x2): Two-stage amplifier array to boost microvolt signals.
Capacitors: 100nF Ceramic Capacitors (x2) to block DC offset.
Resistors: 10k\u03a9 (x3), 1k\u03a9 (x3) for signal attenuation and routing.
9V Battery or 12V Wall Adapter: Independent power supply for the Zener circuit.
3. DIY Avalanche Noise Generator Circuit
The voltage forces its way backward through the Zener diode, provoking avalanche breakdown. This outputs microscopic, completely unpredictable quantum voltage spikes.

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
Circuit Execution Stages:
Quantum Source: Reverse-biased Zener breaks down randomly at subatomic scales.
Stage 1 Boost (Q1): Capacitor C1 strips away baseline DC voltage. Q1 amplifies the tiny AC static wave.
Stage 2 Boost (Q2): Capacitor C2 blocks secondary DC shifts. Q2 pushes the final noise wave into a chaotic, readable 0V–5V swing.
4. Wiring Layout
Noise Input: Wire the amplified analog output of your Zener circuit straight to Analog Input Pin A0 on the Arduino.
Relay Logic: Connect your dual-channel 5V relay module input pins to Digital Output Pins 2 and 3.
Mains Delivery: Wire the power lines for the Left LED through Relay 1 (Pin 2) and the Right LED through Relay 2 (Pin 3).
5. Complete Replication Code
This firmware runs a mandatory Von Neumann debiasing engine to completely filter out physical circuit shifts, ensuring that any deviation discovered is mathematically real.

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
Safeguards Against Interference
Electromagnetic Shielding: Relays output a micro-electromagnetic pulse when clicking. Wrap your Zener board in aluminum foil (Grounded Faraday Shielding) and keep it outside the primary light-tight box to prevent feedback.
Thermal Deflection: Plant respiration alters local chamber heat. Keep the Arduino and the noise circuit board completely outside the box to ensure that environmental temperature shifts cannot drift the transistor thresholds.
## Purpose

To generate an amplified, chaotic analog noise signal from a reverse-biased Zener diode avalanche event. The amplified noise is read by the Arduino analog input (A0).

## Stages

1. Quantum source (Zener diode)
   - Reverse-bias the Zener diode so it enters avalanche breakdown at a predictable voltage range; the breakdown produces high-frequency noise spikes.
2. Stage 1: Pre-amplify (Q1)
   - Use a 2N3904 configured to amplify microvolt-level spikes.
   - Capacitor C1 removes DC offsets; resistor network biases the transistor.
3. Stage 2: Secondary amplify and level-shift (Q2)
   - Second 2N3904 boosts the waveform into a 0–5V readable swing for Arduino A0.
   - Capacitor C2 blocks secondary DC and shapes transient response.
4. Optional filtering and conditioning
   - Small RC filters or comparator thresholds can be added to improve signal-to-noise for analogRead sampling.

## Wiring notes

- Keep the noise circuit physically isolated from mains and relay switching to avoid EMI coupling.
- Use short leads and shield critical traces; ground the shield to a common reference.
- Power the noise circuit from a separate supply (9V battery or isolated adapter) to prevent ground loops.

## Testing

- Validate noise presence with a multimeter and oscilloscope before connecting to the Arduino.
- Confirm that analogRead(zenerPin) yields rapidly varying values; sample the LSB for randomness as per firmware.

## Next steps

- Add a simple schematic image to the repo (assets/circuit_diagram.png or SVG).
- Add explicit resistor and capacitor part numbers and tolerances.
- Document safety notes for powering and testing the avalanche stage.

*Draft created by engineer for task `circuit-docs`.*
