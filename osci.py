import pyvisa 

# Open a VISA resource manager
rm = pyvisa.ResourceManager()

# Connect to the device
instrument = rm.open_resource('TCPIP::169.254.105.229::inst0')

# Send a command to get the device details
#response = instrument.query('*IDN?')

instrument.write('CHAN1:STAT ON')

# Print the response
#print(response)

