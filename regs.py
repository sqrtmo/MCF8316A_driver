from micropython import const
import uctypes

def _b(start, end=-1):
#     print( start, ((end-start)+1) )

   if end == -1:
      end = start             # lengh is 1
   elif end < start:
      print('ERR --> _b(', start, ',', end, ')')   # if I enteren wrong value order

   return start << uctypes.BF_POS | abs((end-start)+1) << uctypes.BF_LEN | uctypes.BFUINT32 

#########################
## EEPROM REGISTER MAP ##
#########################

ALGORITHM_CFG = [
    {"ISD_CONFIG"                      : 0x80,
     'LAYOUT':{
        'REV_DRV_OPEN_LOOP_CURRENT'    :_b( 0, 1),
        'REV_DRV_HANDOFF_THR'          :_b( 2, 5),
        'STAT_DETECT_THR'              :_b( 6, 8),
        'HIZ_TIME'                     :_b( 9,12),
        'BRK_TIME'                     :_b(13,16),
        'BRK_MODE'                     :_b(21),
        'FW_DRV_RESYN_THR'             :_b(22,25),
        'RESYNC_EN'                    :_b(26),
        'RVS_DR_EN'                    :_b(27),
        'HIZ_EN'                       :_b(28),
        'BRAKE_EN'                     :_b(29),
        'ISD_EN'                       :_b(30),
        'PARITY'                       :_b(31)
        }
    },    
    {"REV_DRIVE_CONFIG"                : 0x82,
     'LAYOUT':{
        'ACTIVE_BRAKE_KI'              :_b( 0, 9),
        'ACTIVE_BRAKE_KP'              :_b(10,19),
        'ACTIVE_BRAKE_CURRENT_LIMIT'   :_b(20,22),
        'REV_DRV_OPEN_LOOP_ACCEL_A2'   :_b(23,26),
        'REV_DRV_OPEN_LOOP_ACCEL_A1'   :_b(27,30),
        'PARITY'                       :_b(31)
        }
    },    
    {"MOTOR_STARTUP1"                  : 0x84,
     'LAYOUT':{
        'REV_DRV_CONFIG'               :_b(0),
        'ACTIVE_BRAKE_EN'              :_b(1),
        'IQ_RAMP_EN'                   :_b(2),
        'OL_ILIMIT_CONFIG'             :_b(3),
        'IPD_REPEAT'                   :_b( 4, 5),
        'IPD_ADV_ANGLE'                :_b( 6, 7),
        'IPD_RLS_MODE'                 :_b(8),
        'IPD_CURR_THR'                 :_b( 9,13),
        'IPD_CLK_FREQ'                 :_b(14,16),
        'ALIGN_OR_SLOW_CURRENT_ILIMIT' :_b(17,20),
        'ALIGN_TIME'                   :_b(21,24),
        'ALIGN_SLOW_RAMP_RATE'         :_b(25,28),
        'MTR_STARTUP'                  :_b(29,30),
        'PARITY'                       :_b(31) 
        }
    },    
    {"MOTOR_STARTUP2"                  : 0x86,
     'LAYOUT':{
        'THETA_ERROR_RAMP_ RATE'       :_b( 0, 2),
        'FIRST_CYCLE_FREQ_SEL'         :_b( 3),
        'SLOW_FIRST_CYC_FREQ'          :_b( 4, 7),
        'ALIGN_ANGLE'                  :_b( 8,12),
        'OPN_CL_HANDOFF_THR'           :_b(13,17),
        'AUTO_HANDOFF_EN'              :_b(18),
        'OL_ACC_A2'                    :_b(19,22),
        'OL_ACC_A1'                    :_b(23,26),
        'OL_ILIMIT'                    :_b(27,30),
        'PARITY'                       :_b(31) 
        }
    },    
    {"CLOSED_LOOP1"                    : 0x88,
     'LAYOUT':{
        'LOW_SPEED_RECIRC_BRAKE_EN'    :_b(0),
        'SPEED_LOOP_DIS'               :_b(1), 
        'DEADTIME_COMP_EN'             :_b(2),
        'AVS_EN'                       :_b(3),
        'FG_BEMF_THR'                  :_b( 4, 6),
        'FG_CONFIG'                    :_b(7),
        'FG_DIV'                       :_b( 8,11),
        'FG_SEL'                       :_b(12,13),
        'PWM_MODE'                     :_b(14),
        'PWM_FREQ_OUT'                 :_b(15,18),
        'CL_DEC'                       :_b(19,23),
        'CL_DEC_CONFIG'                :_b(24),
        'CL_ACC'                       :_b(25,29),
        'OVERMODULATION_ENABLE'        :_b(30),
        'PARITY'                       :_b(31) 
        }
    },    
    {"CLOSED_LOOP2"                    : 0x8A,
     'LAYOUT':{
        'MOTOR_IND'                    :_b( 0, 7),
        'MOTOR_RES'                    :_b( 8,15),
        'BRAKE_SPEED_THRESHOLD'        :_b(16,19),
        'ACT_SPIN_THR'                 :_b(20,23),
        'MTR_STOP_BRK_TIME'            :_b(24,27),
        'MTR_STOP'                     :_b(28,30),
        'PARITY'                       :_b(31) 
        }
    },    
    {"CLOSED_LOOP3"                    : 0x8C,
     'LAYOUT':{
        'SPD_LOOP_KP'                  :_b( 0, 2),
        'CURR_LOOP_KI'                 :_b( 3,12),
        'CURR_LOOP_KP'                 :_b(13,22),
        'MOTOR_BEMF_CONST'             :_b(23,30),
        'PARITY'                       :_b(31) 
        }
    },    
    {"CLOSED_LOOP4"                    : 0x8E,
     'LAYOUT':{
        'MAX_SPEED'                    :_b( 0,13),
        'SPD_LOOP_KI'                  :_b(14,23), 
        'SPD_LOOP_KP'                  :_b(24,30), 
        'PARITY'                       :_b(31) 
        }
    },    
    {"SPEED_PROFILES1"                 : 0x94,
     'LAYOUT':{
        'DUTY_A'                       :_b( 0, 4), 
        'DUTY_CLAMP1'                  :_b( 5,12),
        'DUTY_OFF1'                    :_b(13,20),
        'DUTY_ON1'                     :_b(21,28),
        'SPEED_PROFILE_CONFIG'         :_b(29,30),
        'PARITY'                       :_b(31) 
        }
    },    
    {"SPEED_PROFILES2"                 : 0x96,
     'LAYOUT':{
        'DUTY_E'                       :_b( 0, 3), 
        'DUTY_D'                       :_b( 4,11),
        'DUTY_C'                       :_b(12,19),
        'DUTY_B'                       :_b(20,27),
        'DUTY_A'                       :_b(28,30),
        'PARITY'                       :_b(31) 
        }
    },    
    {"SPEED_PROFILES3"                 : 0x98,
     'LAYOUT':{
        'DUTY_CLAMP2'                  :_b( 3,10),
        'DUTY_OFF2'                    :_b(11,18),
        'DUTY_ON2'                     :_b(19,26),
        'DUTY_E'                       :_b(27,30),
        'PARITY'                       :_b(31) 
        }
    },    
    {"SPEED_PROFILES4"                 : 0x9A,
     'LAYOUT':{
        'SPEED_B'                      :_b( 0, 6),
        'SPEED_A'                      :_b( 7,14),
        'SPEED_CLAMP1'                 :_b(15,22),
        'SPEED_OFF1'                   :_b(23,30),
        'PARITY'                       :_b(31) 
        }
    },    
    {"SPEED_PROFILES5"                 : 0x9C,
     'LAYOUT':{
        'SPEED_E'                      :_b( 6,13),
        'SPEED_D'                      :_b(14,21),
        'SPEED_C'                      :_b(22,29),
        'SPEED_B'                      :_b(30),
        'PARITY'                       :_b(31) 
        }
    },    
    {"SPEED_PROFILES6"                 : 0x9E,
     'LAYOUT':{
        'SPEED_CLAMP2'                 :_b(15,22),
        'SPEED_OFF2'                   :_b(23,30),
        'PARITY'                       :_b(31) 
        }
    }     
]

FAULT_CFG = [
   {"FAULT_CONFIG1"                    : 0x90,
     'LAYOUT':{
        'SATURATION_FLAGS_EN'          :_b(0),
        'IPD_FREQ_FAULT_EN'            :_b(1),
        'IPD_TIMEOUT_FAULT_EN'         :_b(2),
        'MTR_LCK_MODE'                 :_b( 3, 6),
        'LCK_RETRY'                    :_b( 7,10),
        'LOCK_ILIMIT_DEG'              :_b(11,14),
        'LOCK_ILIMIT_MODE'             :_b(15,18),
        'LOCK_ILIMIT'                  :_b(19,22),
        'HW_LOCK_ILIMIT'               :_b(23,26),
        'ILIMIT'                       :_b(27,30),
        'PARITY'                       :_b(31) 
        }
    },    
    {"FAULT_CONFIG2"                   : 0x92,
     'LAYOUT':{
        'AUTO_RETRY_TIMES'             :_b( 0, 2),     
        'MAX_VM_MODE'                  :_b(3),
        'MAX_VM_MOTOR'                 :_b( 4, 6),
        'MIN_VM_MODE'                  :_b(7),     
        'MIN_VM_MOTOR'                 :_b( 8,10),
        'HW_LOCK_ILIMIT_DEG'           :_b(11,14),
        'HW_LOCK_ILIMIT_MODE'          :_b(15,18),
        'NO_MTR_THR'                   :_b(19,21),
        'ABNORMAL_BEMF_THR'            :_b(22,24),
        'LOCK_ABN_SPEED'               :_b(25,27),
        'LOCK3_EN'                     :_b(28),
        'LOCK2_EN'                     :_b(29),
        'LOCK1_EN'                     :_b(30),
        'PARITY'                       :_b(31)          
        }
    },    
]

HARDWARE_CFG = [
    {"PIN_CONFIG"                      : 0xA4,
     'LAYOUT':{
        'SPEED_MODE'                   :_b(0,1),
        'BRAKE_INPUT'                  :_b(2,3),
        'ALIGN_BRAKE_ANGLE_SEL'        :_b(4),
        'BRAKE_PIN_MODE'               :_b(5),
        'PARITY'                       :_b(31)                   
         }
     },
    {"DEVICE_CONFIG1"                  : 0xA6,
     'LAYOUT':{
        'BUS_VOLT'                     :_b(0 ,1),
        'I2C_TARGET_ADDR'              :_b(20,26),
        'PIN_38_CONFIG'                :_b(28,29),
        'PARITY'                       :_b(31)                        
         }
     },
    {"DEVICE_CONFIG2"                  : 0xA8,
     'LAYOUT':{
        'EXT_WD_FAULT'                 :_b( 0),
        'EXT_WD_INPUT'                 :_b( 1),
        'EXT_WD_CONFIG'                :_b( 2, 3),     
        'EXT_WD_EN'                    :_b( 4),
        'EXT_CLK_CONFIG'               :_b( 5, 7),
        'EXT_CLK_EN'                   :_b( 8),
        'CLK_SEL'                      :_b( 9,10),
        'DEV_MODE'                     :_b(11),
        'DYNAMIC_VOLTAGE_GAIN_EN'      :_b(12),
        'DYNAMIC_CSA_GAIN_EN'          :_b(13),
        'SLEEP_ENTRY_TIME'             :_b(14,15),
        'INPUT_MAXIMUM_FREQ'           :_b(30,36),
        'PARITY'                       :_b(31)                   
         }
     },
    {"PERI_CONFIG1"                       : 0xAA,
     'LAYOUT':{
        'ALARM_PIN_DIS'                   :_b( 8),     
        'SPEED_RANGE_SEL'                 :_b( 9),
        'ACTIVE_BRAKE_MOD_INDEX_LIMIT'    :_b(10,12),
        'ACTIVE_BRAKE_SPEED_DELTA_LIMIT'  :_b(13,16),
        'SELF_TEST_ENABLE'                :_b(17),
        'DIR_CHANGE_MODE'                 :_b(18),
        'DIR_INPUT'                       :_b(19,20),
        'BUS_CURRENT_LIMIT_ENABLE'        :_b(21),
        'BUS_CURRENT_LIMIT'               :_b(22,25),
        'SPREAD_SPECTRUM_MODULATION_DIS'  :_b(30),
        'PARITY'                          :_b(31)                            
         }
     },
    {"GD_CONFIG1"                      : 0xAC,
     'LAYOUT':{
        'CSA_GAIN'                     :_b( 0, 1),
        'OCP_MODE'                     :_b( 8, 9),
        'OCP_LVL'                      :_b(10),
        'TRETRY'                       :_b(11),
        'OCP_DEG'                      :_b(12,13),
        'OTW_REP'                      :_b(16),
        'OVP_EN'                       :_b(18),
        'OVP_SEL'                      :_b(19),
        'SLEW_RATE'                    :_b(26,27),
        'PARITY'                       :_b(31)                                     
        }
     },
    {"GD_CONFIG2"                      : 0xAE,
     'LAYOUT':{
        'BUCK_DIS'                     :_b(20),
        'BUCK_SEL'                     :_b(21,22),
        'BUCK_CL'                      :_b(23),
        'BUCK_PS_DIS'                  :_b(24),
        'BUCK_SR'                      :_b(25),
        'TARGET_DELAY'                 :_b(26,29),
        'DELAY_COMP_EN'                :_b(30),
        'PARITY'                       :_b(31)                                              
        }
    } 
]

INTERNAL_ALGORITHM_CFG = [ 
    {"INT_ALGO_1"                      : 0xA0,
     'LAYOUT':{
        'REV_DRV_OPEN_LOOP_DEC'        :_b( 0, 2),     
        'MPET_OPEN_LOOP_SLEW_RATE'     :_b( 3, 5),
        'MPET_OPEN_LOOP_SPEED_REF'     :_b( 6, 7),     
        'MPET_OPEN_LOOP_CURRENT_REF'   :_b( 8,10),     
        'MPET_IPD_FREQ'                :_b(11,12),
        'MPET_IPD_CURRENT_LIMIT'       :_b(13,14),
        'AUTO_HANDOFF_MIN_BEMF'        :_b(17,19),
        'ISD_TIMEOUT'                  :_b(20,21),
        'ISD_RUN_TIME'                 :_b(22,23),
        'ISD_STOP_TIME'                :_b(24,25),
        'FAST_ISD_EN'                  :_b(26),
        'SPEED_PIN_GLITCH_FILTER'      :_b(27,28),
        'FG_ANGLE_INTERPOLATE_EN'      :_b(29),
        'PARITY'                       :_b(31)                                     
        }
    },
    {"INT_ALGO_2"                            : 0xA2,
     'LAYOUT':{
        'IPD_HIGH_RESOLUTION_EN'             :_b( 0),
        'MPET_KE_MEAS_PARAMETER_SELECT'      :_b( 1),
        'MPET_IPD_SELECT'                    :_b( 2),
        'ACTIVE_BRAKE_BUS_CURRENT_SLEW_RATE' :_b( 3, 5),
        'CL_SLOW_ACC'                        :_b( 6, 9),
        'PARITY'                             :_b(31)                                              
        }
    }
]

# EEPROM_REGISTERS = [ ALGORITHM_CFG, FAULT_CFG, HARDWARE_CFG, INTERNAL_ALGORITHM_CFG ]

# def ISD_CONFIG():
    


######################
## RAM REGISTER MAP ##
######################



FAULT_STATUS = [
    {'GATE_DRIVER_FAULT_STATUS'        : 0xE0,
     'LAYOUT' : {
            'VCP_UV'                   :_b(11),
            'BUCK_UV'                  :_b(12),
            'BUCK_OCP'                 :_b(13),
            'OTP_ERR'                  :_b(14),
            'OCP_LA'                   :_b(16),
            'OCP_HA'                   :_b(17),
            'OCP_LB'                   :_b(18),
            'OCP_HB'                   :_b(19),
            'OCP_LC'                   :_b(20),
            'OCP_HC'                   :_b(21),
            'TSD'                      :_b(22), 
            'OTW'                      :_b(23),
            'OT'                       :_b(25), 
            'OVP'                      :_b(26),
            'NPOR'                     :_b(27),
            'OCP'                      :_b(28),
            'BK_FLT'                   :_b(30),
            'DRIVER_FAULT'             :_b(31)
        }
      },
    {'CONTROLLER_FAULT_STATUS'         : 0xE2,
     'LAYOUT' : {
            'CURRENT_LOOP_SATURATION'  :_b(14),
            'SPEED_LOOP_SATURATION'    :_b(15),
            'MTR_OVER_VOLTAGE'         :_b(16),
            'MTR_UNDER_VOLTAGE'        :_b(17),
            'HW_LOCK_ILIMIT'           :_b(18),
            'LOCK_ILIMIT'              :_b(19),
            'MTR_LCK'                  :_b(20),
            'NO_MTR'                   :_b(21),
            'ABN_BEMF'                 :_b(22),
            'ABN_SPEED'                :_b(23),
            'MPET_BEMF_FAULT'          :_b(24),
            'MPET_IPD_FAULT'           :_b(25),
            'BUS_CURRENT_LIMIT_STATUS' :_b(26),
            'IPD_T2_FAULT'             :_b(27),
            'IPD_T1_FAULT'             :_b(28),
            'IPD_FREQ_FAULT'           :_b(29),
            'CONTROLLER_FAULT'         :_b(31)
        }
    }
]

SYSTEM_STATUS = [
    {"ALGO_STATUS"                     : 0xE4,
     'LAYOUT':{
             'VOLT_MAG'                :_b(16,31)
         }
      },
    {"MTR_PARAMS"                      : 0xE6,
     'LAYOUT':{
             'MOTOR_L'                 :_b( 8,15),
             'MOTOR_BEMF_CONST'        :_b(16,23),             
             'MOTOR_R'                 :_b(24,31)             
         }
      }, 
    {'ALGO_STATUS_MPET'                : 0xE8,
     'LAYOUT':{
             'MPET_PWM_FREQ'           :_b(24,27),
             'MPET_MECH_STATUS'        :_b(28),
             'MPET_KE_STATUS'          :_b(29),
             'MPET_L_STATUS'           :_b(30),
             'MPET_R_STATUS'           :_b(31)
        }
    }
]

DEV_CTRL = [
    {'DEV_CTRL'                        : 0xEA,
     'LAYOUT':{
             'WATCHDOG_TICKLE'         :_b(10),
             'FORCED_ALIGN_ANGLE'      :_b(11,19),
             'EEPROM_WRITE_ACCESS_KEY' :_b(20,27),
             'CLR_FLT_RETRY_COUNT'     :_b(28),
             'CLR_FLT'                 :_b(29),
             'EEPROM_READ'             :_b(30),
             'EEPROM_WRT'              :_b(31)
        }
    }
]

ALGORITHM_CTRL =[
    {'ALGO_CTRL1'                         : 0xEC,
     'LAYOUT':{
             'FORCE_IQ_REF_SPEED_LOOP_DIS':_b( 0, 9),
             'FORCE_ALIGN_ANGLE_SRC_SEL'  :_b(10),
             'FORCE_ISD_EN'               :_b(11),
             'FORCE_IPD_EN'               :_b(12),
             'FORCE_SLOW_FIRST_CYCLE_EN'  :_b(13),
             'FORCE_ALIGN_EN'             :_b(14),
             'CLOSED_LOOP_DIS'            :_b(15),
             'DIGITAL_SPEED_CTRL'         :_b(16,30),
             'OVERRIDE'                   :_b(31)
    }},
    {'ALGO_CTRL2'                         : 0xEE,
     'LAYOUT':{
             'MPET_WRITE_SHADOW'          :_b( 0),
             'MPET_MECH'                  :_b( 1),
             'MPET_KE'                    :_b( 2),
             'MPET_L'                     :_b( 3),
             'MPET_R'                     :_b( 4),
             'MPET_CMD'                   :_b( 5),
             'FORCE_VQ_CURRENT_LOOP_DIS'  :_b( 6,15),
             'FORCE_VD_CURRENT_LOOP_DIS'  :_b(16,25),
             'CURRENT_LOOP_DIS'           :_b(26)
    }},
    {'CURRENT_PI' : 0xF0,
     'LAYOUT':{
             'CURRENT_LOOP_KI'            :_b(12,21),
             'CURRENT_LOOP_KP'            :_b(22,31)
    }},
    {'SPEED_PI' : 0xF2,
     'LAYOUT':{
             'SPEED_LOOP_KI'              :_b(12,21),
             'SPEED_LOOP_KP'              :_b(22,31)
        }
    }
]



ALGORITHM_VAR = {
    "ALGORITHM_STATE"       : 0x210,
    "FG_SPEED_FDBK"         : 0x216,
    'BUS_CURRENT'           : 0x410,
    'PHASE_CURRENT_A'       : 0x43E,
    "PHASE_CURRENT_B"       : 0x440,
    "PHASE_CURRENT_C"       : 0x442,
    'CSA_GAIN_FEEDBACK'     : 0x466,
    'VOLTAGE_GAIN_FEEDBACK' : 0x476,
    "VM_VOLTAGE"            : 0x478,
    "PHASE_VOLTAGE_VA"      : 0x47E,
    'PHASE_VOLTAGE_VB'      : 0x480,
    'PHASE_VOLTAGE_VC'      : 0x482,
    "SIN_COMMUTATION_ANGLE" : 0x4BA,
    "COS_COMMUTATION_ANGLE" : 0x4BC,
    'IALPHA'                : 0x4D4,
    'IBETA'                 : 0x4D6,
    "VALPHA"                : 0x4D8,
    "VBETA"                 : 0x4DA,
    'ID'                    : 0x4E4,
    'IQ'                    : 0x4E6,
    "VD"                    : 0x4E8,
    "VQ"                    : 0x4EA,
    'IQ_REF_ROTOR_ALIGN'    : 0x524,
    'SPEED_REF_OPEN_LOOP'   : 0x53A,
    'IQ_REF_OPEN_LOOP'      : 0x548,
    'SPEED_REF_CLOSED_LOOP' : 0x5CC,
    "ID_REF_CLOSED_LOOP"    : 0x5FC,
    "IQ_REF_CLOSED_LOOP"    : 0x5FE,
    'ISD_STATE'             : 0x67A,
    'ISD_SPEED'             : 0x684,
    "IPD_STATE"             : 0x6B8,
    "IPD_ANGLE"             : 0x6FC,
    'ED'                    : 0x742,
    'EQ'                    : 0x744,
    "SPEED_FDBK"            : 0x752,
    "THETA_EST"             : 0x756
}





