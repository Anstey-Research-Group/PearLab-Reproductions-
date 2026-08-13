# Hardware Procurement Checklist (Draft)

This draft contains vendor part numbers and suggested sources for the core components referenced in the hardware BOM.

> NOTE: Links are examples; replace with region-appropriate vendors and exact part numbers before purchasing.

## Suggested parts and sample vendors

- Arduino Uno R3 (or equivalent)
  - Part: Arduino UNO R3 (SKU: A000066)
  - Vendor examples: Adafruit (https://www.adafruit.com/product/2396), SparkFun (https://www.sparkfun.com/products/13975), Digi-Key (https://www.digikey.com/short/abcd)
  - Approx price: $20–30

- Dual-Channel 5V Relay Module
  - Part: 2-channel 5V relay module (optocoupled recommended, e.g., SONGLE SRD-05VDC-SL-C on a 2-channel board)
  - Vendor examples: Amazon (search "2 channel relay module"), SparkFun, Digi-Key
  - Approx price: $5–15

- Zener diode (6.2V–7.5V)
  - Part example: BZX55C6V2 (or 1N4735A 6.2V)
  - Vendor: Digi-Key (https://www.digikey.com/short/efgh), Mouser

- 2 × 2N3904 NPN transistors
  - Vendor: Digi-Key, Mouser, Amazon

- Capacitors
  - 2 × 100nF ceramic (0.1uF, 50V)
  - Vendor: Digi-Key, Mouser

- Resistors
  - 10kΩ and 1kΩ values — 1/4W carbon-film or metal-film

- LEDs and lamp fixtures
  - Fixed LED lamps (low heat) — ensure identical models for both sides; consider small LED panels or enclosed fixtures rated for continuous use


## Proposed procurement quantities & preferred vendors (example)

- Arduino UNO R3 x1 — Adafruit (1 unit)
- Relay module 2-channel x1 — Digi-Key or Amazon
- Zener diode (BZX55C6V2) x5 — Digi-Key (keep spares)
- 2N3904 x5 — Digi-Key
- Capacitors (100nF) x10 — Digi-Key
- Resistors assortment pack — Digi-Key
- LED fixtures x2 — Amazon or local electronics supplier

*These links are placeholders; replace with final SKUs and region-appropriate vendors before ordering.*

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
