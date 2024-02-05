
# chip defaults 
# unsigned long eeprom_regmap[24][2] = {
#     {0x80, 0x64738C20},  // ISD_CONFIG
#     {0x82, 0xA8200000},  // REV_DRIVE_CONFIG
#     {0x84, 0x0B6807D0},  // MOTOR_STARTUP1
#     {0x86, 0xA306600C},  // MOTOR_STARTUP2
#     {0x88, 0x0D3201B5},  // CLOSED_LOOP1
#     {0x8A, 0x9BAD0000},  // CLOSED_LOOP2
#     {0x8C, 0x00000000},  // CLOSED_LOOP3
#     {0x8E, 0x00000000},  // CLOSED_LOOP4
#     {0x90, 0xBEC80106},  // FAULT_CONFIG1
#     {0x92, 0xF0D00888},  // FAULT_CONFIG2
#     {0x94, 0x00000000},  // SPEED_PROFILES1
#     {0x96, 0x00000000},  // SPEED_PROFILES2
#     {0x98, 0x00000000},  // SPEED_PROFILES3
#     {0x9A, 0x800D0000},  // SPEED_PROFILES4
#     {0x9C, 0x00000000},  // SPEED_PROFILES5
#     {0x9E, 0x00000000},  // SPEED_PROFILES6
#     {0xA0, 0xA433407D},  // INT_ALGO_1
#     {0xA2, 0x000001A7},  // INT_ALGO_2
#     {0xA4, 0x00000000},  // PIN_CONFIG
#     {0xA6, 0x00101462},  // DEVICE_CONFIG1
#     {0xA8, 0xC000F00F},  // DEVICE_CONFIG2
#     {0xAA, 0xC1C01F00},  // PERI_CONFIG1
#     {0xAC, 0x9C450100},  // GD_CONFIG1
#     {0xAE, 0x80200000},  // GD_CONFIG2
# };


# internel chip defaults
CHIP_ALGORITHM_CFG = {
    "ISD_CONFIG"        : 0x64738C20,
    "REV_DRIVE_CONFIG"  : 0xA8200000,
    "MOTOR_STARTUP1"    : 0x0B6807D0,
    "MOTOR_STARTUP2"    : 0xA306600C,
    "CLOSED_LOOP1"      : 0x0D3201B5,
    "CLOSED_LOOP2"      : 0x9BAD0000,
    "CLOSED_LOOP3"      : 0x00000000,
    "CLOSED_LOOP4"      : 0x00000000,
    "SPEED_PROFILES1"   : 0x00000000,
    "SPEED_PROFILES2"   : 0x00000000,
    "SPEED_PROFILES3"   : 0x00000000,
    "SPEED_PROFILES4"   : 0x800D0000,
    "SPEED_PROFILES5"   : 0x00000000,
    "SPEED_PROFILES6"   : 0x00000000
}

CHIP_FAULT_CFG = {
    "FAULT_CONFIG1"     : 0xBEC80106,
    "FAULT_CONFIG2"     : 0xF0D00888
}

CHIP_HARDWARE_CFG = {
    "PIN_CONFIG"        : 0x00000000,
    "DEVICE_CONFIG1"    : 0x00101462,
    "DEVICE_CONFIG2"    : 0xC000F00F,
    "PERI_CONFIG1"      : 0xC1C01F00,
    "GD_CONFIG1"        : 0x9C450100,
    "GD_CONFIG2"        : 0x80200000
}

CHIP_INTERNAL_ALGORITHM_CFG = {
    "INT_ALGO_1"        : 0xA433407D,
    "INT_ALGO_2"        : 0x000001A7
}

###################################

# p6 in config guide https://www.ti.com/lit/ug/sllu335a/sllu335a.pdf?ts=1706018395326
ALGORITHM_CFG = {
    "ISD_CONFIG"      : 0x44638C20,
    "REV_DRIVE_CONFIG": 0x283AF064,
    "MOTOR_STARTUP1"  : 0x0B6807D0,
    "MOTOR_STARTUP2"  : 0x23066000,
    "CLOSED_LOOP1"    : 0x0C3181B0,
    "CLOSED_LOOP2"    : 0x1AAD0000,
    "CLOSED_LOOP3"    : 0x00000000,
    "CLOSED_LOOP4"    : 0x0000012C,
    "SPEED_PROFILES1" : 0x00000000,
    "SPEED_PROFILES2" : 0x00000000,
    "SPEED_PROFILES3" : 0x00000000,
    "SPEED_PROFILES4" : 0x000D0000,
    "SPEED_PROFILES5" : 0x00000000,
    "SPEED_PROFILES6" : 0x00000000
}

FAULT_CFG = {
    "FAULT_CONFIG1" : 0x5FE80206,
    "FAULT_CONFIG2" : 0x74000000
}

HARDWARE_CFG = {
    "PIN_CONFIG"    : 0x00000000,
    "DEVICE_CONFIG1": 0x00100000,
    "DEVICE_CONFIG2": 0x0000B000,
    "PERI_CONFIG1"  : 0x40000000,
    "GD_CONFIG1"    : 0x00000100,
    "GD_CONFIG2"    : 0x00200000
}

INTERNAL_ALGORITHM_CFG = {
    "INT_ALGO_1" : 0x00B3407D,
    "INT_ALGO_2" : 0x000001A7
}

# EEPROM_REGISTERS = [ ALGORITHM_CFG, FAULT_CFG, HARDWARE_CFG, INTERNAL_ALGORITHM_CFG ]

