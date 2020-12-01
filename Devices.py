class Device :
    ipAddress=""
    port = ""
    
    def findDevices() :
            devices=[]

            d= Device()
            d.ipAddress= "192.168.1.1"
            d.port="80"

            devices.append(d)
            
            d= Device()
            d.ipAddress= "192.168.1.2"
            d.port="443"
            
            devices.append(d)

            d= Device()
            d.ipAddress= "192.168.1.3"
            d.port="23"
            
            devices.append(d)

            return devices





class DevicesView :
    def showDevices(self , devices):
        for d in devices :
            print( "------------------------" ) 
            print ("Ip address : " + str(d.ipAddress) )
            print ("Port : " + str(d.port))
            print( "------------------------" ) 







class DevicesController : 
    def __init__(self) :
        devices = Device.findDevices()

        v= DevicesView()
        v.showDevices(devices)





c =DevicesController()


 

            






        
