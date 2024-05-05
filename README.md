# BlueShell
Open Source TKL keyboard
![Front of the BlueShell keyboard](https://github.com/ParksDevelopment/BlueShell/blob/main/Images/front.jpeg)
## Tools Used
PCB development done in kicad
Modeling done in Shapr3D and exported as 3mf files
Firmware written in KMK

## PCB details
The pcb follows the standard tlk layout only missing the 3 keys that sometimes are present in the top right corner. I their place are a rotary encoder and a blue shell cutout which is over the micro controller. The board is hotswap and uses standard MX spacing between the keys. The port is USB C so it is necessary to include the two resistors on the board. The main brain of the board is an RP2040 on an RP2040 stamp break out board. There are mounting holes placed along the edge of the pcb but they were put too close to several of the keys so if you attempt to top mount the board you are left with very little room. The LED is optional and used to help light up the blue shell cut out. The USBC port can either be hand soldered or ordered with the board. Everything else was intended to be hand soldered.

## Model details
The model has been exported at various 3mf files for 3d printing. some of them such as the top and bottom have been split into two files as my personal printer is not large enough to print them at once. If you are able to print them together in one piece that would be recommended. The plate should not be 3d printed and should instead be made of alluminum or some other more study material. The base has holes in it to allow for several of the "tile" model to be snapped into the back. This allows for the checkered flag pattern, however it makes the board much more fragile so it is recommended to fill in this area if you do not need the design element in the back. Any remaining models are used for the shell.

## Firmware details
The firmware is written in KMK and is pretty standard. holding escape on boot will bring up the drive to make any further edits. hitting the function key will allow for the second layer to be accessed however it is pretty limited in scope at the moment. It makes use of the standard matrix configureation as well as the LED library for the blue shell on the front.

## Front Blue Shell
The blue shell used clear tiles that have been sanded down to spread out the light of the led. inside the area there is double sided alluminum tape to help reflect the light allowing for the dispersion of the light. If you wish to replicate it there is no set of instructions. Just try and get the effect as best as you can. I am fairly certain there were better ways to use the led to get a more spread out effect since, as is, it is still possible to see the source of the light by seeing where it is brightest in the shell.

## Replication
While all the necessary files and information are present here I would advice against replicating the board. It has many flaws such as the mountaing holes mentioned earlier. It was made specifically for being produced one time and not as a simple easy to build board for a low cost. That said I still want to record the information for my own, or anyone else's, reference down the road.
