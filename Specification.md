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
   - Transmit data collected by the Zolertia Client to a computer for storage and visualization via a user interface.

---

## **System Architecture**

### **1. Hardware Components**
- **Solar Panel**: Provides energy to power the entire system.
- **MPPT/BMS Board**
   - **MPPT (Maximum Power Point Tracker)**: Optimizes the captured solar energy.
   - **BMS (Battery Management System)**: Manages battery charging and protection.
- **Battery**: Stores energy.
- **Zolertia Boards**: Collect data, perform wireless communication (**6LoWPAN**, **IPv6**), and transmit data using the **CoAP** protocol.

### **2. Network Communication**
- **CoAP Protocol**: Ensures efficient and lightweight communication between Zolertia boards.
- **6LoWPAN**: Adapts IPv6 for low-power sensor networks.
- **IPv6**: Provides global connectivity for Zolertia boards.

### **3. Computer**
- Receives and stores data sent by Zolertia Client.
- Provides a user interface to visualize the collected data.

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

---

### **2. BMS Board**
- **Role**:
  - Monitors, protects, and balances battery cells.
  - Communicates with the Zolertia Server to transmit data.
- **Main Features**:
  - Protection against overcharging, over-discharging, and overcurrent.
  - Balances battery cell charge levels.
- **Input**: Regulated voltage from the MPPT.
- **Output**: Power for the Zolertia Server.

---

### **3. Zolertia Server Board**
- **Role**:
  - The Zolertia Server, powered by the battery management system (BMS), is responsible for collecting voltage and current data from the battery but alos the time. The Zolertia Server communicates the data to the Zolertia Client via the **CoAP** protocol over the **6LoWPAN** wireless network.
- **Main Features**:
   - Collects voltage, current and time data from the battery.
   - Provides a wireless interface for communication, compatible with **6LoWPAN**.
   - Ensures lightweight and efficient data exchange using the **CoAP** protocol.
   - Formats in **json** the collected data for seamless transmission to the Zolertia Client.

---

### **4. Zolertia Client Board**
- **Role**:
  - The Zolertia Client, powered via USB from a computer, retrieves voltage, current and time data collected by the Zolertia Server. It communicates with the Zolertia Server using the **CoAP** protocol over the **6LoWPAN** wireless interface to request and gather this information.
- **Main Features**:
   - Communicates wirelessly with the Zolertia Server.
   - Efficiently retrieves voltage, current and time data using the lightweight **CoAP** protocol.
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
   - The Zolertia Client will perform a **GET** request to the Zolertia Server to retrieve data such as voltage, current, and time in a **json** format.
   - The Zolertia Client will then send this information to the **HTTP server**, which will generate a graph displaying the solar panel's power as a function of time.

## **Contributors**
- Thibault Guérinel, Siaka Traoré, Tristan Gallais
- ESIR-IOT
