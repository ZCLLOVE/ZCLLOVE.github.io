import re

def extract_mod_numbers(input_string):
    # 使用正则表达式提取模组编号
    pattern = r"workshop-(\d+)"
    mod_numbers = re.findall(pattern, input_string)

    return mod_numbers

def format_output(mod_numbers):
    # 格式化输出
    output_lines = []
    for mod_number in mod_numbers:
        output_lines.append(f'ServerModSetup("{mod_number}")')
        output_lines.append(f'ServerModCollectionSetup("{mod_number}")\n')

    return '\n'.join(output_lines)

# 传入字符串示例
input_string = '''
return {
  ["workshop-1079538195"]={
    configuration_options={
      beebox=true,
      birdcage=true,
      cartographydesk=true,
      cookpot=true,
      dragonflychest=true,
      dragonflyfurnace=true,
      endtable=true,
      firesuppressor=true,
      icebox=true,
      lightning_rod=true,
      meatrack=true,
      modsupport=false,
      moondial=true,
      mushroom_farm=true,
      mushroom_light=true,
      nightlight=true,
      perdshrine=true,
      pottedfern=true,
      rainometer=true,
      researchlab=true,
      researchlab2=true,
      researchlab3=true,
      researchlab4=true,
      resurrectionstatue=true,
      saltlick=true,
      scarecrow=true,
      sculptingtable=true,
      succulent_potted=true,
      townportal=true,
      treasurechest=true,
      wardrobe=true,
      winterometer=true 
    },
    enabled=true 
  },
  ["workshop-1185229307"]={
    configuration_options={
      CAMERA=true,
      CAPTURE=false,
      DAMAGE_NUMBERS=true,
      DAMAGE_RESISTANCE=true,
      FRAME_PHASES=true,
      GLOBAL=false,
      GLOBAL_NUMBERS=false,
      HEADER_CLIENT=false,
      HEADER_SERVER=false,
      HORIZONTAL_OFFSET=0,
      TAG="EPIC",
      TRANSLATOR=false,
      WETNESS_METER=false 
    },
    enabled=true 
  },
  ["workshop-1216718131"]={ configuration_options={ clean=true, lang=true, stack=true }, enabled=true },
  ["workshop-1265737101"]={ configuration_options={  }, enabled=true },
  ["workshop-1595631294"]={
    configuration_options={
      BundleItems=false,
      ChangeSkin=true,
      Digornot=false,
      DragonflyChest=false,
      Icebox=false,
      SaltBox=false 
    },
    enabled=true 
  },
  ["workshop-1595934840"]={
    configuration_options={
      base_hp=0.3,
      ghost_button=true,
      ghost_delay=60,
      hunger_kills=true,
      language="auto",
      no_death_announcement=false,
      rip_cmd=true,
      wes_mult=0.5,
      wilson_extra_hp=0.3,
      wilson_speed_mult=0.5 
    },
    enabled=true 
  },
  ["workshop-2189004162"]={
    configuration_options={
      DEBUG_ENABLED=false,
      DEBUG_SHOW_DISABLED=false,
      DEBUG_SHOW_NOTIMPLEMENTED=false,
      DEBUG_SHOW_PREFAB=false,
      alt_only_information=false,
      appeasement_value="undefined",
      armor="undefined",
      attack_range_type="undefined",
      battlesong_range="both",
      blink_range=false,
      boss_indicator=true,
      bottle_indicator=true,
      crash_reporter=false,
      danger_announcements="undefined",
      death_indicator=false,
      display_attack_range="undefined",
      display_cawnival="undefined",
      display_compostvalue="undefined",
      display_crafting_lookup_button=true,
      display_fertilizer="undefined",
      display_finiteuses=true,
      display_food="undefined",
      display_gyminfo="undefined",
      display_harvestable=true,
      display_health="undefined",
      display_hunger="undefined",
      display_insight_menu_button=true,
      display_mob_attack_damage="undefined",
      display_oceanfishing="undefined",
      display_perishable="undefined",
      display_pickable=true,
      display_plant_stressors="undefined",
      display_pollination="undefined",
      display_sanity="undefined",
      display_sanity_interactions="undefined",
      display_sanityaura="undefined",
      display_shared_stats="undefined",
      display_shelter_info="undefined",
      display_simplefishing="undefined",
      display_spawner_information="undefined",
      display_tackle_information="undefined",
      display_timers="undefined",
      display_unwrappable="undefined",
      display_upgradeable="undefined",
      display_weather="undefined",
      display_weighable="undefined",
      display_world_events="undefined",
      display_worldmigrator="undefined",
      display_yotb_appraisal="undefined",
      display_yotb_winners="undefined",
      domestication_information="undefined",
      experimental_highlighting=true,
      extended_info_indicator=true,
      follower_info="undefined",
      followtext_insight_font_size=28,
      food_effects=true,
      food_memory="undefined",
      food_order="interface",
      food_style="long",
      food_units=true,
      fuel_highlighting=false,
      fuel_highlighting_color="RED",
      fuel_verbosity="undefined",
      growth_verbosity="undefined",
      herd_information="undefined",
      highlighting=true,
      highlighting_color="GREEN",
      hover_range_indicator=true,
      hoverer_insight_font_size=30,
      hunt_indicator="undefined",
      info_preload="undefined",
      info_style="text",
      insight_font="UIFONT",
      inventorybar_insight_font_size=25,
      item_worth="undefined",
      itemtile_display="percentages",
      klaus_sack_info="undefined",
      klaus_sack_markers="undefined",
      language="automatic",
      lightningrod_range=1,
      miniboss_indicator=true,
      naughtiness_verbosity="undefined",
      nightmareclock_display="undefined",
      notable_indicator=true,
      orchestrina_indicator="undefined",
      pipspook_indicator=true,
      refresh_delay="undefined",
      repair_values="undefined",
      sinkhole_marks=2,
      soil_moisture=2,
      soil_nutrients="undefined",
      soil_nutrients_needs_hat="undefined",
      stewer_chef="undefined",
      suspicious_marble_indicator=false,
      temperature_units="game",
      text_coloring=true,
      time_style="realtime_short",
      tumbleweed_info="undefined",
      weapon_damage="undefined",
      weather_detail="undefined",
      wortox_soul_range=true,
      wx78_scanner_info="undefined",
      ["信息控制"]=0,
      ["指示器"]=0,
      ["杂项"]=0,
      ["格式"]=0,
      ["调试"]=0,
      ["食物相关"]=0 
    },
    enabled=true 
  },
  ["workshop-2467694029"]={ configuration_options={ Language="AUTO", MaxNum=0 }, enabled=true },
  ["workshop-2678400698"]={
    configuration_options={
      BUILD_RESTRICTION="all",
      CLOCK_RATE=0.25,
      CLOCK_RATE_DISTANT=0,
      KEY_AUTO_BUILD=110,
      PATHFINDING_TIME_STEP=1,
      SEE_WORK_DIST=16 
    },
    enabled=true 
  },
  ["workshop-3235319974"]={
    configuration_options={
      set0=false,
      set1=true,
      set10=5,
      set2=true,
      set3=true,
      set4=false,
      set5=true,
      set6=true,
      set7=false,
      set8=1500,
      set9=false,
      wukongkey=114 
    },
    enabled=true 
  },
  ["workshop-375850593"]={ configuration_options={  }, enabled=true },
  ["workshop-378160973"]={
    configuration_options={
      ENABLEPINGS=true,
      FIREOPTIONS=2,
      OVERRIDEMODE=false,
      SHAREMINIMAPPROGRESS=true,
      SHOWFIREICONS=true,
      SHOWPLAYERICONS=true,
      SHOWPLAYERSOPTIONS=2 
    },
    enabled=true 
  },
  ["workshop-661253977"]={
    configuration_options={ amudiao=true, baodiao=1, kong=0, nillots=0, rendiao=2, zbdiao=true },
    enabled=true 
  },
  ["workshop-818739975"]={ configuration_options={ DFV_Language="EN" }, enabled=true },
  ["workshop-831523966"]={ configuration_options={ soul_stack=20, stack_size=999 }, enabled=true } 
}
'''

# 提取模组编号
mod_numbers = extract_mod_numbers(input_string)

# 格式化输出
output_result = format_output(mod_numbers)

# 打印结果
print(output_result)
