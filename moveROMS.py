
import os
import shutil

roms = {
        'amstradcpc',
        'fba',
        'gbc',
        'megadrive',
        'ngpc',
        'sg-1000',
        'arcade',
        'fds',
        'n64',
        'pcengine',
        'snes',
        'atari2600',
        'gamegear',
        'mame-libretro',
        'neogeo',
        'psx',
        'vectrex',
        'atari7800',
        'gb',
        'mame-mame4all',
        'nes',
        'sega32x',
        'zxspectrum',
        'atarilynx',
        'gba',
        'mastersystem',
        'ngp',
        'segacd',
}

src_dir = '/boot/ROMS/'
dest_dir = '/home/pi/RetroPie/roms/'

print "Moving ROMS"

for r in roms:
        src = src_dir + r
        dest = dest_dir + r
        src_files = os.listdir(src)
        for file_name in src_files:
            full_file_name = os.path.join(src, file_name)
            if (os.path.isfile(full_file_name)):
                shutil.move(full_file_name, dest)

print "Finished Moving ROMS"
