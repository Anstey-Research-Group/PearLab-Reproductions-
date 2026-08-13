# Hardware Bill of Materials (Draft)

This document is a working draft for the hardware Bill of Materials (BOM) referenced by `hardware-bom-docs` in the mirrored ledger. It is derived from Section 2 of `pear_lab_replication_ledger.md` and is intended to be expanded with sourcing links, estimated prices, and assembly notes.

## Core components

- Arduino Uno (or Raspberry Pi Pico) — microcontroller for switching logic
- Dual-Channel 5V Relay Module — for switching mains to each LED independently
- LEDs (2 × identical fixed LED lamps)
- Light-tight enclosure / small chamber

## Avalanche noise generator (quantum noise source)

- Zener diode (6.2V–7.5V typical) — quantum/avalanche source
- 2 × 2N3904 NPN transistors — two-stage amplifier
- Capacitors: 2 × 100nF ceramic (C1, C2)
- Resistors: 3 × 10kΩ, 3 × 1kΩ (as per ledger schematic)
- Power: 9V battery or 12V wall adapter (separate supply for noise circuit)

## Wiring & signal routing

- Breadboard or protoboard for building the amplifier
- Hook-up wire (assorted lengths)
- Ground leads and shielded cable where needed

## Safety & isolation

- Properly rated mains leads and connectors for LED lamps
- Inline fuse or current-limiting measures (as local electrical code requires)
- Insulating materials and cable strain relief

## Optional / recommended tools

- Multimeter
- Oscilloscope (optional but useful for verifying amplified noise waveform)
- Soldering iron and solder
- Small screwdriver set
- Aluminum foil or Faraday shielding materials for the noise circuit enclosure

## Assembly checklist (draft)

1. Verify all components are present and match required values.
2. Build the avalanche noise generator on a separate board; keep power supply isolated.
3. Measure output at the final amplifier stage before connecting to Arduino A0.
4. Wire relay inputs to Arduino digital pins (as in firmware: pins 2 and 3).
5. Place relays and Arduino outside the light-tight chamber; route power to lamps through relays.
6. Implement shielding: wrap the noise circuit in grounded foil and keep it physically separated from the chamber.
7. Test baseline (no plant) per protocol before adding the biological anchor.

## Next steps / notes for coach review

- Add sourcing links (vendors, part numbers) and estimated cost per item.
- Confirm resistor and capacitor exact values from the schematic or propose alternatives with rationale.
- Add any local safety requirements (fuse ratings, mains wiring notes) specific to the user's jurisdiction.


*Draft created by engineer for task `hardware-bom-docs`. Update and iterate as needed.*
