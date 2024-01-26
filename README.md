# Vampire: The Masquerade Bloodlines RTX Remix (WIP)

![VTMB Logo](vtmb-logo.png "VTMB Logo")

A project to add RTX Remix for Vampire: The Masquerade Bloodlines.

## Setup:

1. Install [Unofficial Patch](https://www.moddb.com/mods/vtmb-unofficial-patch/downloads) (without Plus Patch)
2. Install Remix Runtime in main folder with the game's executable (This can be copied over from the RTX Remix sample project.)
3. Set launch args to `-game Unofficial_Patch -dxlevel 70 +mat_dxlevel 70 -window`
4. Drop `rtx.conf` in the main directory to import settings the settings.

### What's included on this rtx.conf?

- Some textures have been tagged.
- Fog has been removed.

## Known Issues:

- [ ] Invisible cars - Not present with plus patch, but seems to be an issues through Unofficial Patch 11.1 - 11.5. Investigating which version would best suit using the rtx remix.
- [ ] Some textures can become invisible when moving around - We believe it's cause by culling settings, some engine tweaks may be required to fix this issue.
- [ ] Ghost buildings - Some buildings are transparent and a lot of roofs are also affected.
