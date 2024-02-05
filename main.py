import machine
import utime as ut
from MCF8316A_drv import MCF8316A as drv
import uctypes

import regs
import defaults

# from layout import status as status

DEV_ID = 0x01


# ## buttons
FAULT_PIN = 3
PROBE_PIN = 16
CLEAN_PIN = 17

## fault pin IRQ setup ##
clean_flag = False
clean = machine.Pin( CLEAN_PIN, machine.Pin.IN, machine.Pin.PULL_UP )
def clean_cb(clean):
    global clean_flag
    clean_flag = True
    
clean.irq( trigger = machine.Pin.IRQ_FALLING, handler=clean_cb )


## fault pin IRQ setup ##
fault_flag = False
fault = machine.Pin( FAULT_PIN, machine.Pin.IN, machine.Pin.PULL_UP )
def fault_cb(fault):
    global fault_flag
    fault_flag = True
    
fault.irq( trigger = machine.Pin.IRQ_FALLING, handler=fault_cb )

## probe pin IRQ setup ##
probe_flag = False
probe = machine.Pin( PROBE_PIN, machine.Pin.IN, machine.Pin.PULL_UP )
def probe_cb(probe):
    global probe_flag
    probe_flag = True

probe.irq( trigger = machine.Pin.IRQ_FALLING, handler=probe_cb )


if __name__ == "__main__":
    
    drv = drv( dev_id=0x01 )
      
    drv.print_cfg(regs.ALGORITHM_CFG         )
    drv.print_cfg(regs.FAULT_CFG             )
    drv.print_cfg(regs.HARDWARE_CFG          )
    drv.print_cfg(regs.INTERNAL_ALGORITHM_CFG)

      
    ## load and print default configurations ##  
    drv.write_cfg( regs.ALGORITHM_CFG         , defaults.ALGORITHM_CFG          )
    drv.write_cfg( regs.FAULT_CFG             , defaults.FAULT_CFG              )
    drv.write_cfg( regs.HARDWARE_CFG          , defaults.HARDWARE_CFG           )
    drv.write_cfg( regs.INTERNAL_ALGORITHM_CFG, defaults.INTERNAL_ALGORITHM_CFG )
               
#     drv.print_cfg(regs.ALGORITHM_CFG         , detail=True)
#     drv.print_cfg(regs.FAULT_CFG             , detail=True)
#     drv.print_cfg(regs.HARDWARE_CFG          , detail=True)
#     drv.print_cfg(regs.INTERNAL_ALGORITHM_CFG, detail=True)
    
    

    ##################
    ##  INT_ALGO_1  ##
    ##################
    __IA1 = drv.get_struct( regs.INTERNAL_ALGORITHM_CFG )
    
    __IA1['INT_ALGO_1'].MPET_OPEN_LOOP_CURRENT_REF = 2 # 0 = 1A, 7 = 8A
    __IA1['INT_ALGO_1'].MPET_OPEN_LOOP_SLEW_RATE   = 3 # 0 = .1Hz/s, 7 = 20Hz/s
    
    IA1 = drv.cfg_from_struct(__IA1)
    
    drv.write_cfg( regs.INTERNAL_ALGORITHM_CFG, IA1 )
#     drv.print_cfg( regs.INTERNAL_ALGORITHM_CFG, detail=True  )

    ##################
    ## CLOSED_LOOP1 ##
    ##################
    __CL1 = drv.get_struct( regs.ALGORITHM_CFG )
    
    __CL1['CLOSED_LOOP1'].DEADTIME_COMP_EN = 1

    CL1 = drv.cfg_from_struct(__CL1)
    
    drv.write_cfg( regs.ALGORITHM_CFG, CL1 )
#     drv.print_cfg( regs.ALGORITHM_CFG, detail=True      )

    ##################
    ## CLOSED_LOOP2 ##
    ##################
    __CL2 = drv.get_struct( regs.ALGORITHM_CFG )
    
    __CL2['CLOSED_LOOP2'].MOTOR_IND = 0x04  # 0 to autoset
    __CL2['CLOSED_LOOP2'].MOTOR_RES = 0x37  # 0 to autoset

    CL2 = drv.cfg_from_struct(__CL2)
    
    drv.write_cfg( regs.ALGORITHM_CFG, CL2 )
#     drv.print_cfg( regs.ALGORITHM_CFG, detail=True      )

    ##################
    ## CLOSED_LOOP3 ##
    ##################
    __CL3 = drv.get_struct( regs.ALGORITHM_CFG )
    
    __CL3['CLOSED_LOOP3'].MOTOR_BEMF_CONST = 0x0F # 0 to FF
    __CL3['CLOSED_LOOP3'].CURR_LOOP_KP     = 0 # 0 to autoset
    __CL3['CLOSED_LOOP3'].CURR_LOOP_KI     = 0x93 # 0 to autoset

    CL3 = drv.cfg_from_struct(__CL3)
    
    drv.write_cfg( regs.ALGORITHM_CFG, CL3 )
#     drv.print_cfg( regs.ALGORITHM_CFG, detail=True      )
    
    ##################
    ## CLOSED_LOOP4 ##
    ##################
    __CL4 = drv.get_struct( regs.ALGORITHM_CFG )
    
    __CL4['CLOSED_LOOP4'].MAX_SPEED   = 1500 # 14 bit (0 - 32767)
    __CL4['CLOSED_LOOP4'].SPD_LOOP_KP = 0    # 0 to autoset
    __CL4['CLOSED_LOOP4'].SPD_LOOP_KI = 0    # 0 to autoset

    CL4 = drv.cfg_from_struct(__CL4)
    
    drv.write_cfg( regs.ALGORITHM_CFG, CL4 )
#     drv.print_cfg( regs.ALGORITHM_CFG, detail=True      )  
    
    ###################
    ## FAULT_CONFIG1 ##
    ###################
    __FC1 = drv.get_struct( regs.FAULT_CFG )
    
    __FC1['FAULT_CONFIG1'].LOCK_ILIMIT    = 0xF # 8A
    __FC1['FAULT_CONFIG1'].HW_LOCK_ILIMIT = 0xF # 8A
    
    FC1 = drv.cfg_from_struct(__FC1)
    
    drv.write_cfg( regs.FAULT_CFG, FC1         )
#     drv.print_cfg( regs.FAULT_CFG, detail=True )
    
    
    
    # write all cfg to EEPROM
    drv.write( regs.DEV_CTRL[0]['DEV_CTRL'], 0x80000000 )
    
    
    
    
    
    
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
            print('|------------------------------------------------------|')
            print('|###################### PROBE #########################|')
            print('|------------------------------------------------------|')
            drv.print_cfg(regs.ALGORITHM_CFG         , detail=True)
            drv.print_cfg(regs.FAULT_CFG             , detail=True)
            drv.print_cfg(regs.HARDWARE_CFG          , detail=True)
            drv.print_cfg(regs.INTERNAL_ALGORITHM_CFG, detail=True)
    
            drv.print_cfg( regs.FAULT_STATUS   , detail=True)
            drv.print_cfg( regs.SYSTEM_STATUS  , detail=True)
            drv.print_cfg( regs.ALGORITHM_CTRL , detail=True)
            drv.print_cfg( regs.DEV_CTRL       , detail=True)       
            
            probe_flag = False        
        
        if clean_flag is True:
#             while clean.value() is 0:
#                 continue
#             print(clean.value())
#             print( regs.DEV_CTRL[0]['DEV_CTRL'] )
            drv.write( regs.DEV_CTRL[0]['DEV_CTRL'], 0x20000000 )
            drv.print_cfg( regs.DEV_CTRL)
            
            clean_flag = False 
        
        