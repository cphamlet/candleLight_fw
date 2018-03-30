#Make sure you plug in the canable with the BOOT pin enabled first. 
sudo dfu-util -d 0483:df11 -c 1 -i 0 -a 0 -s 0x08000000 -D ./bin/gsusb_canable.bin
