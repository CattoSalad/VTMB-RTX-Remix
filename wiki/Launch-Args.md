# Launch Options

This page is a Work in Progress.

## Other source games
### CS Source uses:

`-dxlevel 80 +mat_dxlevel 80 +r_worldlights 16 +r_novis 1 +r_frustumcullworld 0 +c_frustumcull 0 +r_occlusion 0 +r_shadows 0 +mat_queue_mode 0 +r_unloadlightmaps 1 +mat_drawwater 0 -novid` so I am investigating how each one of these helps us get the most out of the source engine for RTX Remix to work optimally.

#### What do these options do?
`-dxlevel <level>`: Forces the game to start using specified DirectX API (aka feature level) version.
`+mat_dxlevel [DirectX version]`: changes the DirectX (feature level) mode used within a Source game.
`-dxlevel <level>` specifies extra presets while `+mat_dxlevel [DirectX version]` just changes the feature level.
`+r_worldlights`: number of world lights to use per vertex.
`+r_novis`: Enabling this disables the PVS system, causing the whole world to be rendered at once.
`+r_frustumcullworld`: ?
`+c_frustumcull`: ?
`+r_occlusion`: Activate/deactivate the occlusion system.
`+r_shadows`: Determines whether shadows are drawn.
`+mat_queue_mode [-1,0,1,2]`: This setting determines the threading mode the material system uses. A value of -1 uses the default for your system, a value of 0 uses synchronous single thread, 1 uses queued single threaded mode, and value of 2 uses multi-threaded mode.
`+r_unloadlightmaps`: Controls whether lightmap data is unloaded from memory after being updated. When set to 1, the engine unloads lightmap data to save memory. Useful for debugging or when frequent changes to lighting occur.
`+mat_drawwater`: enable/disable the water textures.
`-novid`: Disable the intro video.

#### How do these affect VTMB?
For `-dxlevel 80` and `+mat_dxlevel 80` we know we can safely get down to 70 as that was previously done.

`+r_frustumcullworld 0` and `+c_frustumcull 0` helps with some culling (but some culling issues still occur such as the car park in Santa Monica).
Seems to be better with than without.

`+r_occlusion 0` and `+r_shadows 0` seem to not have a big effect, disabling occlusion and shadows helps us so we want that too.

`+r_novis 1` seems to help quite a lot with invisible walls. Almost ruling out that problem entirely however I experience some strange stutters in places where I used to be able to see these invisible textures.

##### unknown
I am unsure what `-novid` does. I didn't notice any differences.

##### what breaks it?
`+r_worldlights 16` results in a black screen after loading.

## Known fixes:
### Culling issues

Adding `+r_frustumcullworld 0 +c_frustumcull 0` fixes some of the invisible floors as well as some walls.

Such as the floors on the blood bank (back entrance of the medical clinic in Santa Monica) and the tunnel that leads to the Pier.

<img src="https://github.com/CattoSalad/VTMB-RTX-Remix/assets/71943884/a702abee-9068-4013-9c61-83e6b3b95276" width="450" height="330">

Some walls for the car park in Santa Monica aren't affected by this change:
<img src="https://github.com/CattoSalad/VTMB-RTX-Remix/assets/71943884/5733b191-fccb-46d4-88ca-83d2c0ec0ead" width="800" height="342">

Combining: `+r_novis 1 +r_frustumcullworld 0 +c_frustumcull 0` nearly fixes all the issues. But some stutters are still present at some places. 
<img src="https://github.com/CattoSalad/VTMB-RTX-Remix/assets/71943884/ba37e32c-5b91-4ade-9bb3-76c0785f98c4" width="800" height="342">

Additionally the sky changes when using `+r_novis 1` (unsure if for better or worse in terms of RTX Remix compatibility)

<img src="https://github.com/CattoSalad/VTMB-RTX-Remix/assets/71943884/33a8dc0b-16c0-48d1-aa52-7d712371bc1e" width="800" height="342">
