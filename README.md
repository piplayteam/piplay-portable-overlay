# piplay-portable-overlay

How to make your own Device Tree overlay for the Raspberry Pi

Compile dtb and put it directly into it's destination:
```
sudo dtc -@ -I dts -O dtb -o /boot/overlays/foo.dtbo foo-overlay.dts
```
Load the overlay by adding this to /boot/config.txt:
```
dtoverlay=foo
```
Then reboot to load the overlay.



```
dtoverlay=rpi-portable

# Additional overlays and parameters are documented /boot/overlays/README

# Enable audio (loads snd_bcm2835)
dtparam=audio=on
gpu_mem_256=128
gpu_mem_512=256
gpu_mem_1024=256
overscan_scale=1

#dtoverlay=pwm-2chan,pin=18,func=2,pin2=19,func2=4
dtoverlay=pwm-2chan,pin=18,func=2


```
