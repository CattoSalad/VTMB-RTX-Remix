### Preparing the game:

1. Install [Unofficial Patch](https://www.moddb.com/mods/vtmb-unofficial-patch/downloads) (preferably without Plus Patch)

- No Plus Patch - Vanilla experience.
- With Plus Patch - Additional restored content.

### Install RTX Remix

Download [RTX Remix](https://www.nvidia.com/en-gb/geforce/rtx-remix/).
The installation process involves installing Nvidia's omniverse. Once it is installed the RTX Remix extension can be installed.

### Enabling RTX Remix Runtime:

1. Install Remix Runtime in main folder with the game's executable. Unlike other Source engine games, this will be outside of the Bin folder.
   - Copy from: `C:\Users\"Your User"\AppData\Local\ov\pkg\rtx-remix-2024.1.1\deps\r emix_runtime\runtime` or [rtx-remix releases](https://github.com/NVIDIAGameWorks/rtx-remix/releases) (0.4.1 seems to cause some issues with captures so go for 0.4.0 for now)
2. Set launch args to `-game Unofficial_Patch -dxlevel 70 +mat_dxlevel 70 +r_frustumcullworld 0 +c_frustumcull 0 -window` [(More about args here)](https://github.com/CattoSalad/VTMB-RTX-Remix/wiki/Launch-Args)
3. Drop [`rtx.conf`](https://github.com/CattoSalad/VTMB-RTX-Remix/blob/main/rtx.conf) in the main directory to import the settings.
