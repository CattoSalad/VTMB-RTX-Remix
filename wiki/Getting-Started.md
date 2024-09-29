### Preparing the game:

1. Install [Unofficial Patch](https://www.moddb.com/mods/vtmb-unofficial-patch/downloads) (preferably without Plus Patch)

- No Plus Patch - Vanilla experience.
- With Plus Patch - Additional restored content.

### Install RTX Remix

Download [RTX Remix](https://www.nvidia.com/en-gb/geforce/rtx-remix/).
The installation process involves installing Nvidia's omniverse. Once it is installed the RTX Remix extension can be installed.

### Enabling RTX Remix Runtime:

1. Install Remix Runtime in main folder with the game's executable. Unlike other Source engine games, this will be outside of the Bin folder.
   - **RECOMMENDED** [rtx-remix releases](https://github.com/NVIDIAGameWorks/rtx-remix/releases).
   - **OR** Use the [RTX Remix Downloader script](https://github.com/Kim2091/RTX-Remix-Downloader) more info about it [here](https://discord.com/channels/1028444667789967381/1098785289838796850/1202002632672280578).
2. Set launch args to `-game Unofficial_Patch -dxlevel 70 +mat_dxlevel 70  +r_novis 1 +r_frustumcullworld 0 +c_frustumcull 0 +r_occlusion 0 +r_shadows 0 +mat_queue_mode 0 +r_unloadlightmaps 1 +mat_drawwater 0 -novid -window` [(More about args here)]
3. Drop [`rtx.conf`](https://github.com/CattoSalad/VTMB-RTX-Remix/blob/main/rtx.conf) in the main directory to import the settings.

## Contributing

### Setting up the enviornment

#### Requirements:

- RTX GPU
- Windows 10/11
- [Git](https://git-scm.com/download/win)

#### Setup:

- Clone the repo with Git desktop or [`from here`](https://github.com/CattoSalad/VTMB-RTX-Remix)
- As mentioned above install RTX Remix through omniverse - an Nvidia account is required.

##### Add symlinks

Replace **PATH TO GAME** with the path to your game and replace **PATH TO REPO** with the path where you copied your repo. Keep the double quotes.

RECOMMENDED if you intend to work on the repo

- Rename or Delete your `rtx-remix` folder inside of your game folder (to something like `rtx-remix-backup`)
- Open CMD as Admin

* run `mklink /J "PATH TO GAME\rtx-remix" "PATH TO REPO\rtx-remix"` (if you have issues with this feel free to reach out on the threat on the Nvidia RTX Remix discord channel)

Note: Your game's `rtx-remix` folder will need to be emtpy.

This will link your game's rtx-remix folder to the rtx-remix folder on the repo which will allow you to take captures directly to the repo. Update and make changes to the mod, while facilitating colaboration.

Aditionally link your rtx.conf file so changes go through to the repo and your game loads the latest changes.
* run `mklink /J "PATH TO GAME\rtx.conf" "PATH TO REPO\rtx.conf"`

##### Adding the mod to RTX Remix

- Go to Setup Project
- Select Open
- Make your way to the repo and select `VTMB-RTX-Remix/rtx-remix/mods/mod/vtmb_rtx_remix.usda`
- Add the captures folder `VTMB-RTX-Remix/rtx-remix`

It should complain about ot finding one of the captures.
So you will need to reselect your captures folder and this time it'll be `VTMB-RTX-Remix/rtx-remix/captures/`

### DOs and DON'Ts:

#### When contributing:

- Create a new branch, name it appropriately by describing what you are adding and separated by dashes such as `captures-for-last-round`.
- When you have made and commited your changes to your new branch create a Pull Request.

#### DON'T:

- Commit AI upscaled textures - We are hand authoring all materials and meshes.

#### Naming convensions:

We are naming every caputure with the map name and prefixed with some detail, separated by underscores such as `sm_hub_1`. A list to all maps can be found [here](https://github.com/CattoSalad/VTMB-RTX-Remix/wiki/Useful-Console-Commands#map-names).

When in doubt teleport to a map with `map *map_name*` from the ingame console. That way you can ensure you are on the correct map and your captures are named accordingly.
