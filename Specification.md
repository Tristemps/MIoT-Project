# IoT Project

## **Project Description**

This project aims to design an IoT system capable of collecting, transmitting, and visualizing data using the **CoAP**, **6LoWPAN**, and **IPv6** protocols. The system relies on IoT nodes powered by solar panels, an energy management system (**MPPT**), and batteries managed by a **BMS**.

---

## **Objectives**

1. **Solar Energy Management**:
   - Optimize energy production and usage using **MPPT** and **BMS** modules.
   - Store energy in a rechargeable battery to ensure autonomy for IoT nodes.

2. **IoT Communication**:
   - Implement **CoAP** (for lightweight communication between IoT nodes), **6LoWPAN** (for IPv6 adaptation to low-power networks), and **IPv6** (for global connectivity).

3. **Data Visualization and Processing**:
   - Transmit data collected by IoT nodes to a cloud server for storage and visualization via a user interface.

---

## **System Architecture**

### **1. Hardware Components**
- **Solar Panel**: Provides energy to power the entire system.
- **MPPT (Maximum Power Point Tracker)**: Optimizes the captured solar energy.
- **BMS (Battery Management System)**: Manages battery charging and protection.
- **Battery**: Stores energy for IoT nodes.
- **IoT Nodes**: Collect data (sensors), perform wireless communication (**6LoWPAN**, **IPv6**), and transmit data using the **CoAP** protocol.

### **2. Network Communication**
- **CoAP Protocol**: Ensures efficient and lightweight communication between IoT nodes and the cloud server.
- **6LoWPAN**: Adapts IPv6 for low-power sensor networks.
- **IPv6**: Provides global connectivity for IoT nodes.

### **3. Cloud Server**
- Receives and stores data sent by IoT nodes.
- Provides a user interface to visualize the collected data.

---

## **Specifications of the Boards**

### **1. MPPT Board**
- **Role**:
  - Converts and regulates energy from the solar panel to maximize available power.
  - Provides stable power to the **BMS** and IoT nodes.
- **Main Features**:
  - Maximum power point tracking (MPPT).
  - Efficient DC-DC conversion.
- **Input**: Voltage from the solar panel.
- **Output**: Regulated voltage to the **BMS**.

---

### **2. BMS Board**
- **Role**:
  - Monitors, protects, and balances battery cells.
  - Communicates with IoT nodes to transmit battery data.
- **Main Features**:
  - Protection against overcharging, over-discharging, and overcurrent.
  - Balances battery cell charge levels.
- **Input**: Regulated voltage from the MPPT.
- **Output**: Power for IoT nodes.

---

### **3. IoT Node**
- **Role**:
  - Collect environmental or energy data using sensors.
  - Communicate via **CoAP** and **6LoWPAN** protocols to transmit data to the cloud server.
- **Main Features**:
  - Wireless interface for communication (radio compatible with 6LoWPAN).
  - Sensor management for data collection (temperature, light intensity, etc.).
  - Lightweight and efficient communication using **CoAP**.
- **Input**: Power provided by the **BMS**.
- **Output**: Collected data transmitted to the cloud.

---

## **Overall Functionality**

1. **Energy Production and Management**:
   - The solar panel powers the system through the **MPPT** module, which optimizes the captured energy.
   - Energy is stored in the battery under the supervision of the **BMS**.

2. **Data Collection and Transmission**:
   - IoT nodes collect data from connected sensors.
   - Data is transmitted wirelessly via **6LoWPAN** and **IPv6**, using **CoAP** as the application protocol.

3. **Data Visualization**:
   - Data is sent to a cloud server via the Internet.
   - Users can visualize the information on a graphical interface (computer or application).

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
   - Provides global connectivity and a unique address for each IoT node.

---

## **Installation and Deployment**

1. **Hardware Setup**:
   - Connect the solar panel, MPPT module, BMS, and battery.
   - Ensure that IoT nodes are properly powered and sensors are connected.

2. **Software Setup**:
   - Configure IoT nodes with a network stack supporting **6LoWPAN**, **IPv6**, and **CoAP**.
   - Deploy a cloud server compatible with **CoAP** to receive the data.

3. **Testing and Validation**:
   - Verify that IoT nodes collect data and communicate correctly with the server.
   - Ensure data is accurately visualized on the user interface.

---

## **Contributors**
- Thibault Guérinel, Siaka Traoré, Tristan Gallais
- ESIR-IOT
