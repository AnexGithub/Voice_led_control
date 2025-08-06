# Voice-Controlled AC LED Bulb using Arduino and Relay

This project allows you to control an AC-powered LED bulb using voice commands like "Turn on the light" or "Turn off the light". It uses an Arduino Uno, a relay module, and a voice recognition interface (via a PC or smartphone) to achieve hands-free operation.

---

## Project Summary

- **Control Method**: Voice commands
- **Microcontroller**: Arduino Uno
- **Output Device**: AC LED Bulb
- **Interface**: Relay Module
- **Voice Input**: PC or smartphone microphone (Python with SpeechRecognition & PySerial)
- **Power**: AC 220V (Relay isolates Arduino)

---

## 🛠️ Hardware Components

| Component           | Quantity | Description                           |
|--------------------|----------|---------------------------------------|
| Arduino Uno        | 1        | Main controller                       |
| Relay Module (1-CH)| 1        | To control the AC bulb                |
| AC LED Bulb        | 1        | 220V AC light source                  |
| Jumper Wires       | As needed| For connections                       |
| PC or Laptop       | 1        | To capture and interpret voice input  |
| USB Cable          | 1        | To connect Arduino to PC              |
| Power Supply       | 1        | 220V AC                               |

---

## Wiring Diagram

| Arduino Pin | Relay Pin |
|-------------|-----------|
| D10         | IN        |
| 5V          | VCC       |
| GND         | GND       |

> **Relay Output**: Connect the **COM** terminal to AC live wire, and **NO** (Normally Open) terminal to the bulb’s live input. Neutral connects directly to bulb.

---

## Arduino Code

Upload the following code using Arduino IDE:

```cpp
take from main.ino file

## Python Voice Control Script
--bash
pip install pyserial speechrecognition
