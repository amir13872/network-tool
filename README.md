# Network Tool

A Python-based tool designed to simplify the execution of advanced network commands such as ARP, Ping, Netsh, and NetBIOS. This tool features a user-friendly graphical interface, making it accessible for users who may not be comfortable with command-line operations.

## Features

- **ARP Operations**:
  - View the ARP table to display all network entries.
  - Send ARP requests to specific IP addresses.

- **Ping Functionality**:
  - Ping a domain or IP address with configurable request counts.
  - Display ping results in both textual and graphical formats.

- **Network Configuration**:
  - Display system network configurations.
  - Configure static IP addresses, Subnet Masks, and Gateways for advanced users.

- **NetBIOS Scanning**:
  - Scan for NetBIOS names on the local network.
  - Display the NetBIOS names of the system.

## User Interface

The application uses Tkinter to provide a simple and intuitive GUI. Users can easily execute network operations through buttons and straightforward options, with results displayed in a clear format.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/network-tool.git
   ```
2. Navigate to the project directory:
   ```
   cd network-tool
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the application by executing the following command:
```
python src/main.py
```

Follow the on-screen instructions to perform network operations.

## Project Structure

- `src/`: Contains the main application code.
- `src/gui/`: Contains the GUI implementation.
- `src/core/`: Contains core functionalities for ARP, Ping, Netsh, and NetBIOS.
- `src/utils/`: Contains utility functions for command execution and result formatting.
- `requirements.txt`: Lists the dependencies required for the project.
- `setup.py`: Used for packaging the application.

## Security

The tool is designed with security in mind, preventing the execution of harmful commands and ensuring that all operations are performed within a safe scope.

## Extensibility

The project structure allows for easy addition of new features and functionalities. Future enhancements may include support for graphical results, PDF reports, and multi-language support.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
