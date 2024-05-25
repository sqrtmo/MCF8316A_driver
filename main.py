import machine
import utime as ut
from MCF8316A_drv import MCF8316A as drv
import uctypes

import regs
import defaults

# from layout import status as status



# ## buttons
FAULT_PIN = 3
PROBE_PIN = 16
CLEAN_PIN = 17

SPEED_PIN = 15

speed_pwm = machine.PWM( machine.Pin(SPEED_PIN) )
speed_pwm.freq(1000)

ADC_PIN = 28
adc_val = machine.ADC(ADC_PIN)


## fault pin IRQ setup ##
clean_flag = False
clean = machine.Pin( CLEAN_PIN, machine.Pin.IN, machine.Pin.PULL_UP )
def clean_cb(c):
    if clean.value() is 0:
        global clean_flag
        clean_flag = True
    
clean.irq( trigger = machine.Pin.IRQ_FALLING, handler=clean_cb )


## probe pin IRQ setup ##
probe_flag = False
probe = machine.Pin( PROBE_PIN, machine.Pin.IN, machine.Pin.PULL_UP )
def probe_cb(p):
    if probe.value() is 0:
        global probe_flag
        probe_flag = True

probe.irq( trigger = machine.Pin.IRQ_FALLING, handler=probe_cb )


## fault pin IRQ setup ##
fault_flag = False
fault = machine.Pin( FAULT_PIN, machine.Pin.IN, machine.Pin.PULL_UP )
def fault_cb(f):
    if fault.value() is 0:
        global fault_flag
        fault_flag = True
    
fault.irq( trigger = machine.Pin.IRQ_FALLING, handler=fault_cb )


def _map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


if __name__ == "__main__":
    
    drv = drv( dev_id=0xA )
    
    # clear fault flags
    drv.clear_fault()
    
    
#     drv.i2c_scan()
    
#     drv.EEPROM_read()
        
#     drv.print_cfg(regs.ALGORITHM_CFG         )
#     drv.print_cfg(regs.FAULT_CFG             )
#     drv.print_cfg(regs.HARDWARE_CFG          )
#     drv.print_cfg(regs.INTERNAL_ALGORITHM_CFG)

      
    ## load and print default configurations ##  
#     drv.write_cfg( regs.ALGORITHM_CFG         , defaults.CHIP_ALGORITHM_CFG          )
#     drv.write_cfg( regs.FAULT_CFG             , defaults.CHIP_FAULT_CFG              )
#     drv.write_cfg( regs.HARDWARE_CFG          , defaults.CHIP_HARDWARE_CFG           )
#     drv.write_cfg( regs.INTERNAL_ALGORITHM_CFG, defaults.CHIP_INTERNAL_ALGORITHM_CFG )
               
    drv.write_cfg( regs.ALGORITHM_CFG         , defaults.MY["ALGORITHM_CFG"]          )
    drv.write_cfg( regs.FAULT_CFG             , defaults.MY["FAULT_CFG"]              )
    drv.write_cfg( regs.HARDWARE_CFG          , defaults.MY["HARDWARE_CFG"]           )
    drv.write_cfg( regs.INTERNAL_ALGORITHM_CFG, defaults.MY["INTERNAL_ALGORITHM_CFG"] )
    
#     drv.print_cfg(regs.ALGORITHM_CFG         , detail=True)
#     drv.print_cfg(regs.FAULT_CFG             , detail=True)
#     drv.print_cfg(regs.HARDWARE_CFG          , detail=True)
#     drv.print_cfg(regs.INTERNAL_ALGORITHM_CFG, detail=True)



    ##################
    ##  PIN_CONFIG  ##
    ##################
    __PC = drv.get_struct( regs.HARDWARE_CFG )
    
    __PC['PIN_CONFIG'].SPEED_MODE = 0x01 # PWM control
    
    drv.write_cfg( regs.HARDWARE_CFG, drv.cfg_from_struct(__PC) )

    ##################
    ## HARDWARE_CFG ##
    ##################
    __HC = drv.get_struct( regs.HARDWARE_CFG )
    
    __HC['PERI_CONFIG1'].SPEED_RANGE_SEL = 0x00 # 0h = 325 Hz to 95 kHz, PWM frequency
    
    __HC['GD_CONFIG1'].SLEW_RATE = 0x03 # 200 V/μs increasing efficiency and EMI noise
        
    drv.write_cfg( regs.HARDWARE_CFG, drv.cfg_from_struct(__HC) )

    ##############################
    ##  INTERNAL_ALGORITHM_CFG  ##
    ##############################
    __IA = drv.get_struct( regs.INTERNAL_ALGORITHM_CFG )
    
    __IA['INT_ALGO_1'].MPET_OPEN_LOOP_CURRENT_REF = 3 # 0 = 1A, 7 = 8A
    __IA['INT_ALGO_1'].MPET_OPEN_LOOP_SPEED_REF   = 3 # 0 = 1A, 7 = 8A
    __IA['INT_ALGO_1'].MPET_OPEN_LOOP_SLEW_RATE   = 2 # 0 = .1Hz/s, 7 = 20Hz/s
    __IA['INT_ALGO_1'].AUTO_HANDOFF_MIN_BEMF      = 0 #
    __IA['INT_ALGO_1'].MPET_IPD_CURRENT_LIMIT     = 3 # 2A 
    
#     __IA['INT_ALGO_2'].CL_SLOW_ACC                = 0x0A # 100hZ/s
    
    drv.write_cfg( regs.INTERNAL_ALGORITHM_CFG, drv.cfg_from_struct(__IA) )

    ###################
    ## ALGORITHM_CFG ##
    ###################
    __AC = drv.get_struct( regs.ALGORITHM_CFG )
    
    __AC['CLOSED_LOOP1'].DEADTIME_COMP_EN       = 1
    __AC['CLOSED_LOOP1'].OVERMODULATION_ENABLE  = 1
    __AC['CLOSED_LOOP1'].AVS_EN                 = 1
    __AC['CLOSED_LOOP1'].CL_ACC                 = 0x13 # 1000 hZ/s
    __AC['CLOSED_LOOP1'].CL_DEC_CONFIG          = 1    # CL_DEC same as CL_ACC
    __AC['CLOSED_LOOP1'].PWM_MODE               = 0    # Continuous Space Vector Modulation    
    
    __AC['CLOSED_LOOP2'].MOTOR_IND         = 0x0A  # 0 to autoset
    __AC['CLOSED_LOOP2'].MOTOR_RES         = 0x42  # 0 to autoset    
    
    __AC['CLOSED_LOOP3'].MOTOR_BEMF_CONST = 0x0F # 0 to FF
    __AC['CLOSED_LOOP3'].CURR_LOOP_KP     = 0 # 0 to autoset
    __AC['CLOSED_LOOP3'].CURR_LOOP_KI     = 0 # 0 to autoset

    __AC['CLOSED_LOOP4'].MAX_SPEED        = 2600    # 14 bit (0 - 32767)
    __AC['CLOSED_LOOP4'].SPD_LOOP_KP      = 0x4E    # 0 to autoset
    __AC['CLOSED_LOOP4'].SPD_LOOP_KI      = 0x24E   # 0 to autoset
    
    __AC['MOTOR_STARTUP1'].MTR_STARTUP         = 0x02 # IPD
    __AC['MOTOR_STARTUP1'].IPD_CURR_THR        = 0x07 # 2.5A
    __AC['MOTOR_STARTUP1'].IPD_CLK_FREQ        = 0x05 # 2000 Hz
    __AC['MOTOR_STARTUP1'].IPD_REPEAT          = 0x00 # 1 time
    __AC['MOTOR_STARTUP1'].IPD_ADV_ANGLE       = 0x03 # 90 deg
    __AC['MOTOR_STARTUP1'].ALIGN_TIME          = 0x02 # 100 mS
    __AC['MOTOR_STARTUP1'].OL_ILIMIT_CONFIG    = 0x01 # Open loop current limit defined by ILIMIT
#     __AC['MOTOR_STARTUP1'].IQ_RAMP_EN          = 0x01 # Enable Iq ramp down
    

    __AC['MOTOR_STARTUP2'].OL_ACC_A1             = 0x07 # 50 hZ
    __AC['MOTOR_STARTUP2'].OL_ACC_A2             = 0x07 # 50 hZ
    __AC['MOTOR_STARTUP2'].AUTO_HANDOFF_EN       = 0    # 
    __AC['MOTOR_STARTUP2'].THETA_ERROR_RAMP_RATE = 0x04 #  .2 deg/ms 

#     __AC['MOTOR_STARTUP2'].SLOW_FIRST_CYC_FREQ = 0x05 
    
#     __AC['ALGO_CTRL2'].MPET_KE           = 1
#     __AC['ALGO_CTRL2'].MPET_R            = 1
#     __AC['ALGO_CTRL2'].MPET_L            = 1
#     __AC['ALGO_CTRL2'].MPET_WRITE_SHADOW = 1    
    
#     __AC['SPEED_PROFILES1'].SPEED_PROFILE_CONFIG = 0x1 # linear speed profile
#     __AC['SPEED_PROFILES4'].SPEED_CLAMP1 = 0x1         # 
#     __AC['SPEED_PROFILES6'].SPEED_CLAMP2 = 0x64        #
    
    drv.write_cfg( regs.ALGORITHM_CFG, drv.cfg_from_struct(__AC) )
    
    ###################
    ## FAULT_CONFIG1 ##
    ###################
    __FC = drv.get_struct( regs.FAULT_CFG )
    
    __FC['FAULT_CONFIG1'].LOCK_ILIMIT     = 0xF # 8A
    __FC['FAULT_CONFIG1'].HW_LOCK_ILIMIT  = 0xF # 8A
    __FC['FAULT_CONFIG1'].LOCK_ILIMIT_DEG = 0x4 # 1mS Lock detection current limit deglitch time
    __FC['FAULT_CONFIG1'].MTR_LCK_MODE    = 0x4 # Fault automatically cleared after LCK_RETRY time
    __FC['FAULT_CONFIG1'].LCK_RETRY       = 0x2 # 1 sec

    __FC['FAULT_CONFIG2'].LOCK_ABN_SPEED      = 0x7 # 170 % of max speed
    __FC['FAULT_CONFIG2'].MIN_VM_MODE         = 0x1 # if a VM undervoltage event appears clear the flag automatically when V level restores
    __FC['FAULT_CONFIG2'].HW_LOCK_ILIMIT_MODE = 0x8 # Hardware Ilimit lock detection is in report only but no action is taken
    __FC['FAULT_CONFIG2'].AUTO_RETRY_TIMES    = 0x5 # 10
    
    drv.write_cfg( regs.FAULT_CFG, drv.cfg_from_struct(__FC) )
    
    ###################
    ## HARDWARE_CFG  ##
    ###################
    __HC = drv.get_struct( regs.HARDWARE_CFG )
    
    __HC['DEVICE_CONFIG1'].PIN_38_CONFIG   = 0x2 # SOA\
#     __HC['DEVICE_CONFIG1'].I2C_TARGET_ADDR = 0xA # 
    
    drv.write_cfg( regs.HARDWARE_CFG, drv.cfg_from_struct(__HC) )

        
#     drv.status(regs.ALGORITHM_CFG)
    
#     print(algo_cfg_vals)
    
#     drv.write( 0x80, 0x44638C20 )
        
#     dev_ctl_addr = uctypes.addressof( dev_ctl['DEV_CTRL'] )
    
    
#     print( dev_ctl )

#     print( drv.read( 0x80) )
#     drv.write( 0x80, 0x44638C20 )
#     print( drv.read( 0x80) )

    print('init ready ')
    while True:
        
        v = _map( adc_val.read_u16(), 600, 65100, 0, 65535)
        if v < 0:
            v = 0
        elif v > 65535:
            v = 65535
#         print( v )
        speed_pwm.duty_u16(v)
        
        ut.sleep_ms(100)
        
#         v = _map( adc_val.read_u16(), 600, 65100, 0, 1000)
#         
#         ut.sleep_ms(v)
#         speed_pwm.duty_u16(1000)
#         ut.sleep_ms(v)
#         speed_pwm.duty_u16(50000)
#         
#         print(v)
        
        if fault_flag is True:
            print('|------------------------------------------------------|')
            print('|###################### FAULT #########################|')
            print('|------------------------------------------------------|')
            
            drv.print_cfg( regs.FAULT_STATUS   , detail=True)
            drv.print_cfg( regs.SYSTEM_STATUS  , detail=True)
            drv.print_cfg( regs.ALGORITHM_CTRL , detail=True)
            drv.print_cfg( regs.DEV_CTRL       , detail=True)       

            fault_flag = False
            
        if probe_flag is True:
            det = True
            print('|------------------------------------------------------|')
            print('|###################### PROBE #########################|')
            print('|------------------------------------------------------|')
            drv.print_cfg(regs.ALGORITHM_CFG         , detail=det)
            drv.print_cfg(regs.FAULT_CFG             , detail=det)
            drv.print_cfg(regs.HARDWARE_CFG          , detail=det)
            drv.print_cfg(regs.INTERNAL_ALGORITHM_CFG, detail=det)
    
            drv.print_cfg( regs.FAULT_STATUS   , detail=det)
            drv.print_cfg( regs.SYSTEM_STATUS  , detail=det)
            drv.print_cfg( regs.ALGORITHM_CTRL , detail=det)
            drv.print_cfg( regs.DEV_CTRL       , detail=det)       
            
            probe_flag = False        
        
        if clean_flag is True:
            
            print('---> in clean')
#             machine.disable_irq()
#             while clean.value() is 0:
#                 continue
#             print(clean.value())
#             print( regs.DEV_CTRL[0]['DEV_CTRL'] )
#             drv.write( regs.DEV_CTRL[0]['DEV_CTRL'], 0x80000000 )
#             drv.print_cfg( regs.DEV_CTRL)
            
#             dev.clear_fault()
            
            drv.EEPROM_write()
#             drv.print_cfg(regs.ALGORITHM_CFG         )
#             drv.print_cfg(regs.FAULT_CFG             )
#             drv.print_cfg(regs.HARDWARE_CFG          )
#             drv.print_cfg(regs.INTERNAL_ALGORITHM_CFG)
            
            clean_flag = False
            
#             machine.enable_irq()
        
        