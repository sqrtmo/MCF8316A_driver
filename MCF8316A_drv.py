import machine
import utime as ut
import uctypes

import regs as register

# @micropython.asm_thumb
# def __reverse(r0, r1):               # bytearray, len(bytearray)
#     add(r4, r0, r1)
#     sub(r4, 1) # end address
#     label(LOOP)
#     ldrb(r5, [r0, 0])
#     ldrb(r6, [r4, 0])
#     strb(r6, [r0, 0])
#     strb(r5, [r4, 0])
#     add(r0, 1)
#     sub(r4, 1)
#     cmp(r4, r0)
#     bpl(LOOP)
# 
# 
class MCF8316A:
    def __init__(self, dev_id):
#     RESET_PIN = 1
#         ALERT_PIN = 0
#     SDA_PIN = 2
#     SCL_PIN = 3
    
        self.i2c = machine.I2C( 0, scl=machine.Pin(9), sda=machine.Pin(8), freq=50000 ) # default assignment: scl=Pin(9), sda=Pin(8)
        self.dev_id = dev_id
    
    def read( self, ctl_word ):
        _cw = bytearray( b'\x90\x00' )
        _cw.append(ctl_word)
        
        self.i2c.writeto(self.dev_id, _cw)

        ut.sleep_us(200)
        
        msg = bytearray(4)
        self.i2c.readfrom_into(self.dev_id, msg, 4)
        
        return hex(int.from_bytes(msg, 'little'))
    
    def write( self, ctl_word, data):
        _cw = bytearray( b'\x10\x00' )
        _cw.append(ctl_word)
        
        data = data.to_bytes(4, 'little')    
#         __reverse( _data, 4)
        
        ut.sleep_us(200)
        
        self.i2c.writeto(self.dev_id, _cw, False)
        self.i2c.writeto(self.dev_id, data)
        
#         print(err)
        
        
    
#     def read_cfg( self, reg ):
# #         for d in register.EEPROM_REGISTERS:
#         for d in reg:
#             for key, val in d.items():
#                 if key is not 'LAYOUT':
#                     print( f'{key:<17}{self.read(val)}' )
    
    def write_cfg( self, dest, source ):
        for d in dest:
            for key, val in d.items():
                if key is not 'LAYOUT':
#                     print( val, source[key] )
                    self.write( val, source[key] )
                
    
#     def read_D( self, d ):
#         for key, val in d.items():
#             v = self.read(val)
#             if int(v) != 0:
#                 print( f'{key:<26}{v}' ) # {bin(int(v))}            
#                 for b in range(32):
#                     print( f' --> {b:<3}{(int(v) >> int(b)) & 0x01}' )
                    
    def print_cfg(self, reg, detail=False):
        
#         res = {}
        
        for i in reg:
            reg = 0
            reg_name = ''
            layout = {}
            for key, val in i.items():
                # >>> shitty code <<<
                if key is not 'LAYOUT':
                    reg = int( self.read(val) )
                    reg_name = key
                else:
                    layout = val
                
            reg_addr = uctypes.addressof( reg.to_bytes(4, 'big') )
            s = uctypes.struct( reg_addr, layout, uctypes.BIG_ENDIAN )

#             res.update({reg_name:s})

#             if detail is True:
            print('|------------------------------------------------------|')
                
            print( f'|{reg_name:<42}{hex(reg):<12}|' )
            
            if detail is True:
                for key, val in layout.items():
                    flag = getattr( s, key )
                    print( f'|\t{key:<35}{hex(flag):<12}|' )
        print('|------------------------------------------------------|')
#         return res
                        
    def get_struct(self, reg):
    # reads registers and returns it in dict format
        res = {}
        
        for i in reg:
            reg = 0
            reg_name = ''
            layout = {}
            for key, val in i.items():
                # >>> shitty code <<<
                if key is not 'LAYOUT':
                    reg = int( self.read(val) )
                    reg_name = key
                else:
                    layout = val
                
            reg_addr = uctypes.addressof( reg.to_bytes(4, 'big') )
            s = uctypes.struct( reg_addr, layout, uctypes.BIG_ENDIAN )

            res.update({reg_name:s})
                
        return res
    
    def cfg_from_struct( self, s ):
        # reads struct format an returns values in dict format
        res = {}
                  
        for key, val in s.items():
            
            addr = uctypes.addressof(val)
            __val = int.from_bytes(uctypes.bytes_at(addr, uctypes.sizeof(val)), 'big')
            
            res.update({key: __val})
        # (uctypes.bytes_at(addr, 4)) byte array
        
        return res





