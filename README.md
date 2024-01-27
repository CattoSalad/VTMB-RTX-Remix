# Vampire: The Masquerade Bloodlines RTX Remix (WIP)

![VTMB Logo](vtmb-logo.png "VTMB Logo")

A project to add RTX Remix for Vampire: The Masquerade Bloodlines.

## Captures

Captures are located under [`/rtx-remix/captures`](https://github.com/CattoSalad/VTMB-RTX-Remix/tree/main/rtx-remix/captures) folder. Feel free to download and use those with [RTX Remix](https://www.nvidia.com/en-gb/geforce/rtx-remix/https://www.nvidia.com/en-gb/geforce/rtx-remix/).

## Setup:

Preparing the game:

1. Install [Unofficial Patch](https://www.moddb.com/mods/vtmb-unofficial-patch/downloads) (without Plus Patch)

Install RTX Remix:

Download [RTX Remix](https://www.nvidia.com/en-gb/geforce/rtx-remix/).
The installation process involves installing Nvidia's omniverse. Once it is installed the RTX Remix extension can be installed.

Enabling RTX Remix Runtime:

1. Paste Remix Runtime in the main folder next to the game's executable (**not** inside the Bin folder)
   - Copy from: `C:\Users\"Your User"\AppData\Local\ov\pkg\rtx-remix-2024.1.1\deps\remix_runtime\runtime`
2. Set launch args to `-game Unofficial_Patch -dxlevel 70 +mat_dxlevel 70 -window`
3. Drop `rtx.conf` in the main directory to import the settings.

### What's included on this rtx.conf?

- Some textures have been tagged.
- Fog has been removed.

## Known Issues:

- [x] Invisible cars - Not present with plus patch, but seems to be an issues through Unofficial Patch 11.1 - 11.5. Investigating which version would best suit using the rtx remix. [Temporary Solution](https://github.com/CattoSalad/VTMB-RTX-Remix/issues/1) - Will be fixed on the next release of Unofficial Patch 11.5+.
- [ ] Some textures can become invisible when moving around - We believe it's caused by culling settings, some engine tweaks may be required to fix this issue.
- [ ] Ghost buildings - Some buildings are transparent and a lot of roofs are also affected.
