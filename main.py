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
PROBE_PIN = 2
# 
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
        
#     drv.read_EEPROM()
    drv.write_cfg( regs.ALGORITHM_CFG         , defaults.ALGORITHM_CFG          )
    drv.write_cfg( regs.FAULT_CFG             , defaults.FAULT_CFG              )
    drv.write_cfg( regs.HARDWARE_CFG          , defaults.HARDWARE_CFG           )
    drv.write_cfg( regs.INTERNAL_ALGORITHM_CFG, defaults.INTERNAL_ALGORITHM_CFG )
#     
#     drv.read_EEPROM( regs.ALGORITHM_CFG          )
#     drv.read_EEPROM( regs.FAULT_CFG              )
#     drv.read_EEPROM( regs.HARDWARE_CFG           )
#     drv.read_EEPROM( regs.INTERNAL_ALGORITHM_CFG )
    
#     fault_status_struct = drv.get_struct( regs.FAULT_STATUS )
        
#     v = drv.val_from_struct(fault_status_struct)
#     print(v)
        
            
    drv.read_cfg(regs.ALGORITHM_CFG, detail=True)
    
    algo_cfg_struct = drv.get_struct( regs.ALGORITHM_CFG )
    
    algo_cfg_struct['ISD_CONFIG'].BRK_MODE = 0
    
    algo_cfg_vals = drv.val_from_struct(algo_cfg_struct)
    
    drv.write_cfg( regs.ALGORITHM_CFG, algo_cfg_vals )
    
#     drv.status(regs.ALGORITHM_CFG)
    
#     print(algo_cfg_vals)
    
#     drv.write( 0x80, 0x44638C20 )
        
#     dev_ctl_addr = uctypes.addressof( dev_ctl['DEV_CTRL'] )
    
    
#     print( dev_ctl )

#     print( drv.read( 0x80) )
#     drv.write( 0x80, 0x44638C20 )
#     print( drv.read( 0x80) )

    while True:
        if fault_flag is True:
#             print("\nfault!!!\n")
            drv.status( regs.FAULT_STATUS )
            drv.status( regs.SYSTEM_STATUS )
            drv.status( regs.ALGORITHM_CTRL )
            drv.status( regs.DEV_CTRL )       

            fault_flag = False
            
        if probe_flag is True:
            drv.status( regs.FAULT_STATUS )
            drv.status( regs.SYSTEM_STATUS )
            drv.status( regs.ALGORITHM_CTRL )
            drv.status( regs.DEV_CTRL )
            
            probe_flag = False        
        
        
        