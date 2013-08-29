from regreport import RegistryReport

if  __name__ =='__main__':
	reg1 = RegistryReport()
	reg1.set_hives_ntuser(['02515250\\ntuser.dat','Administrator\\ntuser.dat','Default\\ntuser.dat','st00599\\ntuser.dat','ST00810\\ntuser.dat'])
	reg1.set_paths('C:\\INVENTORY\\Cases\\021-DEECEDU01_PC03\\Registry Hives', 'C:\\INVENTORY\\Cases\\021-DEECEDU01_PC03\\temp', 'C:\\INVENTORY\\Code\\rrv2.8')
	reg1.report_all()