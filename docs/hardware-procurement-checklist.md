# Hardware Procurement Checklist (Draft)

This draft contains vendor part numbers and suggested sources for the core components referenced in the hardware BOM.

> NOTE: Links are examples; replace with region-appropriate vendors and exact part numbers before purchasing.

## Suggested parts and sample vendors

- Arduino Uno R3 (or equivalent)
  - Part: Arduino UNO R3
  - Vendor examples: Adafruit (https://www.adafruit.com), SparkFun (https://www.sparkfun.com), Amazon
  - Approx price: $20–30

- Dual-Channel 5V Relay Module
  - Part: 2-channel 5V relay module (optocoupled recommended)
  - Vendor examples: Amazon, eBay, AliExpress, SparkFun
  - Approx price: $5–15

- Zener diode (6.2V–7.5V)
  - Part example: BZX55C6V2 or similar
  - Vendor: Digi-Key, Mouser, Newark

- 2 × 2N3904 NPN transistors
  - Vendor: Digi-Key, Mouser, Amazon

- Capacitors
  - 2 × 100nF ceramic (0.1uF)
  - Vendor: Digi-Key, Mouser

- Resistors
  - 10kΩ and 1kΩ values — assorted 1/4W

- LEDs and lamp fixtures
  - Fixed LED lamps (low heat) — ensure identical models for both sides

## Procurement checklist

- [ ] Confirm exact part numbers and tolerances for Zener and resistors from circuit-docs
- [ ] Select primary vendor and second-source vendor for each critical item
- [ ] Verify shipping times and MOQ requirements
- [ ] Confirm any certifications required for mains-connected components
- [ ] Prepare estimated total cost and order list

## Notes for coach

- Please review part selections and confirm final procurement list.
- After approval, coach can mark `hardware-bom-checklist` as in_progress and complete procurement verification steps.

*Draft created by engineer for task `hardware-procurement-draft`.*
