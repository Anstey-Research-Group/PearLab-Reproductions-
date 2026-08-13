# Circuit Documentation (Draft)

This draft documents the DIY avalanche noise generator circuit referenced by `circuit-docs` in the mirrored ledger. It is derived from Section 3 of `pear_lab_replication_ledger.md`.

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
