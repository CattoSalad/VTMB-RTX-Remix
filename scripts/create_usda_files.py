def create_usda_files(file_names):
    content = '#usda 1.0\n(\n    upAxis = "Z"\n)\n'

    print("Add the following to mod.usda under subLayers:")
    for name in file_names:
        print(f"@./{name}.usda@,")
        file_path = f"{name}.usda"
        with open(file_path, 'w') as file:
            file.write(content)

all_locations = [
    "sp_endsequences_a", "sm_apartment_1", "la_abandoned_building_1", "hw_609_1", "ch_cloud_1",
    "sp_endsequences_b", "sm_asylum_1", "la_bradbury_1", "hw_ash_sewer_1", "ch_dragon_1",
    "sp_epilogue", "sm_bailbonds_1", "la_bradbury_2", "hw_asphole_1", "ch_fishmarket_1",
    "sp_genesisdevice_1", "sm_basement_1", "la_bradbury_3", "hw_cemetery_1", "ch_fulab_1",
    "sp_giovanni_1", "sm_beachhouse_1", "la_chantry_1", "hw_chateau_1", "ch_glaze_1",
    "sp_giovanni_2a", "sm_coffee_1", "la_confession_1", "hw_chinese_1", "ch_hub_1",
    "sp_giovanni_2b", "sm_diner_1", "la_crackhouse_1", "hw_hub_1", "ch_lotus_1",
    "sp_giovanni_3", "sm_gallery_1", "la_dane_1", "hw_jewelry_1", "ch_ramen_1",
    "sp_giovanni_4", "sm_hub_1", "la_empire_1", "hw_luckystar_1", "ch_shrekhub",
    "sp_giovanni_5", "sm_hub_2", "la_empire_2", "hw_metalhead_1", "ch_temple_1",
    "sp_masquerade_1", "sm_junkyard_1", "la_empire_3", "hw_netcafe_1", "ch_temple_2",
    "sp_ninesintro", "sm_medical_1", "la_expipe_1", "hw_redspot_1", "ch_temple_3",
    "sp_observatory_1", "sm_oceanhouse_1", "la_hospital_1", "hw_sinbin_1", "ch_temple_4",
    "sp_observatory_2", "sm_oceanhouse_2", "la_hub_1", "hw_tawni_1", "ch_tsengs_1",
    "sp_soc_1", "sm_pawnshop_1", "la_library_1", "hw_vesuvius_1", "ch_zhaos_1",
    "sp_soc_2", "sm_pawnshop_2", "la_malkavian_1", "hw_warrens_1",
    "sp_soc_3", "sm_pier_1", "la_malkavian_2", "hw_warrens_2",
    "sp_soc_4", "sm_shreknet_1", "la_malkavian_3", "hw_warrens_2b",
    "sp_taxiride", "sm_smoke_1", "la_malkavian_3b", "hw_warrens_3",
    "sp_theatre", "sm_tattoo", "la_malkavian_4", "hw_warrens_4",
    "sp_tutorial_1", "sm_vamparena", "la_malkavian_5", "hw_warrens_5",
    "sm_warehouse_1", "la_museum_1",
    "la_parkinggarage_1",
    "la_plaguebearer_sewer_1",
    "la_skyline_1",
    "la_ventruetower_1",
    "la_ventruetower_1b",
    "la_ventruetower_2",
    "la_ventruetower_3"
]

file_names_list = [location for location in all_locations if location.startswith("ch_")] #Change to desired map
create_usda_files(file_names_list)
