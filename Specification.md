# IoT Project

## **Project Description**

This project aims to design an IoT system capable of collecting, transmitting, and visualizing data using the **CoAP**, **6LoWPAN**, and **IPv6** protocols. The system relies on Zolertia boards powered by solar panels, an energy management system (**MPPT**), and batteries managed by a (**BMS**).

---

## **Objectives**

1. **Solar Energy Management**:
   - Optimize energy production and usage using **MPPT** and **BMS** modules.
   - Store energy in a rechargeable battery to ensure autonomy for the Zolertia Server.

2. **IoT Communication**:
   - Implement **CoAP** (for lightweight communication between Zolertia boards), **6LoWPAN** (for IPv6 adaptation to low-power networks), and **IPv6** (for global connectivity).

3. **Data Visualization and Processing**:
   - Transmit data collected by the Zolertia Border Router to a computer for storage and visualization via a user interface.

---

## **System Architecture**

### **1. Hardware Components**
- **Solar Panel**: Provides energy to power the entire system.
- **MPPT/BMS Board**
   - **MPPT (Maximum Power Point Tracker)**: Optimizes the captured solar energy.
   - **BMS (Battery Management System)**: Manages battery charging and protection.
- **Battery**: Stores energy.
- **Zolertia Boards**: Received data, perform wireless communication (**6LoWPAN**, **IPv6**), and transmit data using the **CoAP** protocol.

### **2. Network Communication**
- **CoAP Protocol**: Ensures efficient and lightweight communication between Zolertia boards.
- **6LoWPAN**: Adapts IPv6 for low-power sensor networks.
- **IPv6**: Provides global connectivity for Zolertia boards.

### **3. Computer**
- Receives and stores data sent by Zolertia Border Router.
- Provides a user interface to visualize the collected data.

### **4. Architecture**
![image](unnamed.png)
---

## **Specifications of the Boards**

### **1. MPPT Board**
- **Role**:
  - Converts and regulates energy from the solar panel to maximize available power.
  - Provides stable power to the **BMS** and the Zolertia Server.
- **Main Features**:
  - Maximum power point tracking (MPPT).
- **Input**: Voltage from the solar panel.
- **Output**: Regulated voltage to the **BMS**.
- **Where we are now**:
  - Siaka 

Current Path: We have understood that the current path is as follows: Check on KiCad, but in general for the MPPT. The signal goes from the panel to the sensor and the battery also goes to the sensor. Then the information passes to the microprocessor. The microprocessor sends the information to the StepDown, which directs the current from the panel to the battery with the good voltage.

The script "pwmSTM32.c" in the folder "electronique": can later be integrated for the MPPT. The goal of the PWM is to use the high and low pins of our board to create a PWM signal. This PWM signal is used to adapt the voltage provided by the solar panel and transmit it to our battery. The duty cycle represents the duration during which our signal is high compared to the entire period. It is this signal that allows us to adjust the voltage coming from the solar panel.

This script is an example of code extracted from the documentation of the STM32 Discovery board and started to be adapted for our case. We tried to integrate it into the project provided by Guillaume Le Gall (https://gitlab2.istic.univ-rennes1.fr/gulegall/esir-miot-base/-/tree/main?ref_type=heads), but we encountered compilation errors that we didn't have time to fix.

### **2. BMS Board**
- **Role**:
  - Monitors, protects, and balances battery cells.
  - Communicates with the Zolertia Server to transmit data.
- **Main Features**:
  - Protection against overcharging, over-discharging, and overcurrent.
  - Balances battery cell charge levels.
- **Input**: Regulated voltage from the MPPT.
- **Output**: Power for the Zolertia Server.
- **Where we are now**:

The script "bms.c" in the folder "electronique": We need to try testing it within the project provided by Guillaume Le Gall (https://gitlab2.istic.univ-rennes1.fr/gulegall/esir-miot-base/-/tree/main?ref_type=heads).


### **3. Zolertia Server Board**
- **Role**:
  - The Zolertia Server, powered by the battery management system (BMS), is responsible for collecting voltage and current data from the battery. The Zolertia Server communicates the data to the Zolertia Border Router via the **CoAP** protocol over the **6LoWPAN** wireless network.
- **Main Features**:
   - Received voltage, current and time data from the battery.
   - Provides a wireless interface for communication, compatible with **6LoWPAN**.
   - Ensures lightweight and efficient data exchange using the **CoAP** protocol.


### **4. Border Router Board**
- **Role**:
  - The Border router, powered via USB from a computer, retrieves voltage, current data collected by the Zolertia Server. It communicates with the Zolertia Server using the **CoAP** protocol over the **6LoWPAN** wireless interface to request and gather this information.
- **Main Features**:
   - Communicates wirelessly with the Zolertia Server.
   - Efficiently retrieves voltage, current data using the lightweight **CoAP** protocol.
   - Transmits the retrieved data to the connected computer for further processing and visualization.

---

## **Protocols Used**

1. **CoAP (Constrained Application Protocol)**:
   - Lightweight protocol for IoT devices.
   - Operates over UDP to minimize network overhead.
   - Allows basic client-server interactions (GET, POST, PUT, DELETE).

2. **6LoWPAN (IPv6 over Low Power Wireless Personal Area Networks)**:
   - Compresses IPv6 headers to make them compatible with IoT networks.
   - Suitable for low-power environments and limited bandwidth.

3. **IPv6**:
   - Provides global connectivity and a unique address for each Zolertia boards.

---

## **Transmitted Information**
   - The client Coap server will perform a **GET** request to the Zolertia Server to retrieve data such as voltage, current in a **text** format.
   - The client Coap server will then send this information to the **Database**

UART
```json
text format example: 
voltage : 3.65; current : 1.0
```

CoAP
```json
text format example: 
voltage : 3.65; current : 1.0
```

PC
```json
text format example: 
voltage : 3.65; current : 1.0
```

---

## PC System Overview
- **Role**:
The PC serves as a central hub for data processing, storage, and visualization. It connects to the **Zolertia Border Router** via USB to collect voltage and current data measured by the Zolertia Server.


### 1. Data Storage
- The collected data, including **voltage**, **current**, is stored in a **database** with **InfluxDB**.
- InfluxDB is designed for time-series data, so it automatically timestamps each entry, eliminating the need to manually transmit timestamps.
- **Database Choice (InfluxDB)**: 

| Field      | Type                | Description          |
|:----------:|:-------------------:|:--------------------:|
| Voltage    | FLOAT               | Measured voltage     |
| Intensity  | FLOAT               | Measured current     |


### 2. Data Visualisation
- For real-time visualization and analysis of the collected data, **Grafana** is used.
- **Grafana Integration**:
   - Grafana connects to the InfluxDB database to query and display the data.
   - It provides dashboards to visualize power trends over time.

---

## **Contributors**
- Thibault Guérinel, Siaka Traoré, Tristan Gallais
- ESIR-IOT
