# Vampire: The Masquerade Bloodlines RTX Remix
A project to RTX Remix Vampire: The Masquerade Bloodlines.

## Setup: 
1) Install Unofficial Patch (without Plus Patch)
2) Install Remix Runtime in main folder with exe ( This can be copied over from the RTX Remix sample project.  )
3) Set launch args to `-game Unofficial_Patch -dxlevel 70 +mat_dxlevel 70 -window`
4) Drop `rtx.conf` in the main directory to import settings the settings.


## Known Issues:
- [ ] Invisible cars - Not present with plus patch, but seems to be an issues through Unofficial Patch 11.1 - 11.5. Investigating which version would best suit using the rtx remix.
- [ ] Some textures can become invisible when moving around - We believe it's cause by culling settings, we will need to tweak things to hopefully resolve this issue.
