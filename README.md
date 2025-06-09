# fly_treadmill# FicTrac-Controlled Stepper Motor on Raspberry Pi

This project uses a Raspberry Pi to control a stepper motor based on FicTrac's output from a fruit fly walking on a floating ball.

## 🧠 Overview
When a fruit fly walks on a spherical treadmill, FicTrac estimates ball movement and sends direction data via UDP. This script reads the UDP stream and moves a stepper motor accordingly:

- **Forward movement** → stepper motor rotates forward
- **Backward movement** → stepper motor rotates backward

## 🛠 Requirements
- Raspberry Pi (with GPIO header)
- Stepper motor (with driver, e.g., A4988/DRV8825)
- FicTrac running and configured to output via UDP
- Python 3

## 🧰 Wiring Example
| GPIO | Function     | Description        |
|------|--------------|--------------------|
| 19   | DIR          | Motor direction    |
| 26   | STEP         | Motor stepping     |

## ⚙️ Installation
```bash
sudo apt update
sudo apt install python3-rpi.gpio python3-pip
pip3 install sounddevice numpy  # Optional if using audio instead
```

## ▶️ Run the Script
Make sure FicTrac is running and configured to output via UDP on port `5005`.

```bash
python3 fictrac_motor_control.py
```

## 📄 License
MIT License

## 📬 Contact
For questions, reach out via [GitHub Issues](https://github.com/your-username/your-repo/issues).

---

*Inspired by the study published in iScience:*
> "The Song of the Fly: Courtship Song as a Signal for Direction Control in Virtual Environments."
> [DOI: 10.1016/j.isci.2019.09.040](https://www.cell.com/iscience/fulltext/S2589-0042(19)30333-5)
