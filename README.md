# piplay-portable-overlay

How to make your own Device Tree overlay for the Raspberry Pi

Compile dtb and put it directly into it's destination:

sudo dtc -@ -I dts -O dtb -o /boot/overlays/foo.dtbo foo-overlay.dts
Load the overlay by adding this to /boot/config.txt:

dtoverlay=foo
Then reboot to load the overlay.
