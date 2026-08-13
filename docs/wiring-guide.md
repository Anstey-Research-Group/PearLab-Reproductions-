# Wiring Guide (Draft)

This draft wiring guide complements `wiring-guide` task in the mirrored ledger and describes pin connections and relay wiring.

## Pin mapping (Arduino Uno)
- Zener noise input -> A0 (zenerPin)
- Left LED relay input -> D2 (leftLight)
- Right LED relay input -> D3 (rightLight)

## Relay wiring
- Use relay module VCC to 5V, GND to GND, IN1 to D2, IN2 to D3.
- Wire mains live through relay contact for each LED lamp; keep neutral constant.
- Use properly rated connectors and secure strain relief.

## Layout
- Place Arduino and noise circuit outside the light-tight chamber.
- Route shielded signal wire from noise circuit to A0 with a grounded shield.
- Keep relay coil wiring away from signal lines, and ground shields to common ground.

## Verification checklist
- [ ] Confirm analogRead on A0 shows a varying signal when noise circuit powered.
- [ ] Verify relay activation toggles the correct lamp.
- [ ] Confirm no visible sparks or overheatings on relay contact during switching.
- [ ] Validate that signal wiring is physically separated from mains wiring by at least 2 cm.

## Notes
- This guide is a draft; coach should add verification tolerances and final safety approvals.

*Draft created by engineer for task `wiring-guide`.*
