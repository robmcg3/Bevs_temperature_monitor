# Bevs_temperature_monitor
A pi pico project built in wokwi to display temperature and humidity on an oled display. 

https://wokwi.com/projects/434426211786373121

written in Micropython
Libraries used
- machine (core library)
- ssd1306 (not core library)


## precusor actions
- [ ] link pico to computer
- [ ] comfirm files on pico
- [ ] find git files on speedymclappy
- [ ] break out parts of code by section
    - [ ] oled
    - [ ] temperature sensor
    - [ ] printing on console
- [ ] install micropython on pi
    - [ ] download uf2
    - [ ] press bootselect on pico
    - [ ] find rpi-rp1 folder
    - [ ] drag uf2 to rpi-rp1 folder
- [ ] install ssd1306. [ssd1306 library](https://github.com/robmcg3/ArduinoIDEProjects)

## git add warning
git add .
warning: adding embedded git repository: tftDisplay/libraries/PicoMPDisplay
hint: You've added another git repository inside your current repository.
hint: Clones of the outer repository will not contain the contents of
hint: the embedded repository and will not know how to obtain it.
hint: If you meant to add a submodule, use:
hint: 
hint: 	git submodule add <url> tftDisplay/libraries/PicoMPDisplay
hint: 
hint: If you added this path by mistake, you can remove it from the
hint: index with:
hint: 
hint: 	git rm --cached tftDisplay/libraries/PicoMPDisplayhint: 
hint: See "git help submodule" for more information.
warning: adding embedded git repository: tftDisplay/libraries/TFT_SPI_cpp
warning: adding embedded git repository: tftDisplay/libraries/micropython-st7735
warning: adding embedded git repository: tftDisplay/libraries/st7789-library-for-pico-cpp
