# FRC Button box
Reliability is critical in FIRST Robotics Competition (FRC), especially during matches where a single equipment failure can affect an entire game. One component that many teams depend on is a button box, which provides drivers with quick access to robot functions that would otherwise be difficult to control through a standard controller alone. Rather than relying on a commercially available solution, I decided to design a custom button box PCB tailored to my team's needs.

The goal of this project was to create a professional, competition-ready button box featuring plug-in terminals, an OLED display for testing and diagnostics, an indicator LED, and a large logo of my FRC Team 5402, Wreckless Robotics, integrated directly into the PCB design. Throughout the project, I researched existing button boxes used by other FRC teams, selected components through DigiKey, designed the schematic in KiCad, created the PCB layout, and prepared the board for manufacturing. Along the way, I learned more about PCB design, component libraries, footprint management, routing techniques, and design-for-manufacturing considerations.

This repository documents the complete development process, including planning, schematic design, PCB layout, manufacturing files, and project documentation. The finished design will be used to support driver practice and competition preparation for Team 5402 while providing a reliable and maintainable control interface for future seasons.


# 3D View of Final PCB Design-



Front-


<img width="1081" height="647" alt="Screenshot 2026-06-06 204653" src="https://github.com/user-attachments/assets/56f1c9d2-b660-4f7f-8d73-92480023b14f" />




Back-




<img width="963" height="638" alt="Screenshot 2026-06-06 220350" src="https://github.com/user-attachments/assets/887c2cf6-bd60-4f67-9566-803be294ace6" />



# Key Features 
-Large Team Logo (very important)
-Flexibility – features 30 independent ports where buttons can be plugged in; no fixed sequence required, just plug-and-play

-Buttons can be swapped or replaced within a minute
  
-Uses a Raspberry Pi Pico (RP2040), allowing buttons to be programmed as needed for different FRC sessions

-Supports advanced logic such as button pairing and conditional inputs

-Designed for reliability – minimal excess components, reducing potential points of failure

-Includes an indicator LED for button box status

-Features a 0.91" OLED display for individual button testing and diagnostics

-Includes mounting holes to securely fasten the PCB in an enclosure or driver station setup



# Schematic & PCB DESIGN 

Schematic- 





<img width="1100" height="757" alt="Screenshot 2026-06-06 205502" src="https://github.com/user-attachments/assets/95b10fc0-b3a4-4089-a20f-e38b8360e6ac" />






PCB Front-






<img width="1022" height="571" alt="Screenshot 2026-06-06 205647" src="https://github.com/user-attachments/assets/fdfe18e5-fc13-4cf1-b641-4830d2d9e9c3" />









PCB Back-


<img width="1012" height="560" alt="Screenshot 2026-06-06 205707" src="https://github.com/user-attachments/assets/933dcf78-4e1b-4fdf-9d55-99381d422639" />





# License

MIT
