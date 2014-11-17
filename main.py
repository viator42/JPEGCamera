# -*- coding: utf-8 -

import serial, uuid, binascii

def main():
    print 'serial test'
    
    ser = None
    opt = ''
    previous = ''
    data = ''
    
    try:
        ser = serial.Serial('/dev/ttyACM0', 38400, timeout=1)
        
    except Exception:
        print '端口未打开'
        exit()
    
    while True:
        opt = raw_input('请输入指令')
        if(opt == '1'):
            ser.write(opt)
            
            # read image from serial port
            
            output = open('./' + str(uuid.uuid1()) + '.jpg', 'wb')
            while ser.isOpen():
                previous = data
                data = ser.read()
                
                output.write(data)
                
                if binascii.b2a_hex(previous) == 'ff' and binascii.b2a_hex(data) == 'd9':
                    break
                print data

            output.close()
            
            print '文件传输完毕'
        
            ser.close()
            exit
    

if __name__ == '__main__':
    main()
