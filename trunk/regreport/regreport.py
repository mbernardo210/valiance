import os
from time import gmtime, strftime

class RegistryReport(object):
	def __init__(self, system='system', sam='sam', software='software', security='security', ntusers=None, base_hive_path=None, base_report_path=None, report_timestamp=strftime("%Y%m%d%H%M%S"), regripper_path=None, report_path=None, report_path_execution=None, report_path_autoruns=None, version_info='1.0'):
		self.system = system
		self.sam = sam
		self.software = software
		self.security = security
		self.ntusers = ntusers
		self.base_hive_path = base_hive_path
		self.base_report_path = base_report_path	
		self.report_timestamp = report_timestamp
		self.regripper_path = regripper_path
		self.report_path = report_path
		self.version_info = version_info
		
	def get_version(self):
		print 'RegistryReport v' + self.version_info
	
	def set_hives_ntuser(self, hives_ntuser):
		self.ntusers = hives_ntuser
		
	def set_paths(self, base_hive_path, base_report_path, regripper_path):
		self.base_hive_path = base_hive_path
		self.base_report_path = base_report_path
		self.regripper_path = regripper_path
		self.report_path = base_report_path + '\\regreport_' + self.report_timestamp
	
	def report_all(self):
		self.report_mod_os()
		self.report_mod_users()
		self.report_mod_software()
		self.report_mod_network()
		self.report_mod_storage()
		self.report_mod_execution()
		self.report_mod_autoruns()
		self.report_mod_log()
		self.report_mod_web()
		self.report_mod_user_config()
		self.report_mod_user_act()
		self.report_mod_user_network()
		self.report_mod_user_file()
		self.report_mod_user_virtual()
		self.report_mod_comm()
	
	def report_mod_os(self):
		report_path_os = self.report_path + '\\os'
		os.system('mkdir ' + report_path_os)
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p winnt_cv >> " + report_path_os + "\\winnt_cv" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p producttype >> " + report_path_os + "\\producttype" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p win_cv >> " + report_path_os + "\\win_cv" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p timezone >> " + report_path_os + "\\timezone" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p shutdown >> " + report_path_os + "\\shutdown" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p shutdowncount >> " + report_path_os + "\\shutdowncount" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.security + "\" -p polacdms >> " + report_path_os + "\\polacdms" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p winlogon >> " + report_path_os + "\\winlogon" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p uac >> " + report_path_os + "\\uac" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p disablesr >> " + report_path_os + "\\disablesr" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p diag_sr >> " + report_path_os + "\\diag_sr" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p spp_clients >> " + report_path_os + "\\spp_clients" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p backuprestore >> " + report_path_os + "\\backuprestore" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p winbackup >> " + report_path_os + "\\winbackup" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p bitbucket >> " + report_path_os + "\\bitbucket" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p disablelastaccess >> " + report_path_os + "\\disablelastaccess" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p dfrg >> " + report_path_os + "\\dfrg" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p secctr >> " + report_path_os + "\\secctr" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p pagefile >> " + report_path_os + "\\pagefile" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p hibernate >> " + report_path_os + "\\hibernate" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p crashcontrol >> " + report_path_os + "\\crashcontrol" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p regback >> " + report_path_os + "\\regback" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p ctrlpnl >> " + report_path_os + "\\ctrlpnl" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p banner >> " + report_path_os + "\\banner" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p nolmhash >> " + report_path_os + "\\nolmhash" + ".txt")		
	
	def report_mod_users(self):
		report_path_users = self.report_path + '\\users'
		os.system('mkdir ' + report_path_users)
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.sam + "\" -p samparse >> " + report_path_users + "\\samparse" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p profilelist >> " + report_path_users + "\\profilelist" + ".txt")
		
	def report_mod_software(self):
		report_path_software = self.report_path + '\\software'
		os.system('mkdir ' + report_path_software)
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p uninstall >> " + report_path_software + "\\uninstall" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p apppaths >> " + report_path_software + "\\apppaths" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p assoc >> " + report_path_software + "\\assoc" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p installedcomp >> " + report_path_software + "\\installedcomp" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p msis >> " + report_path_software + "\\msis" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p product >> " + report_path_software + "\\product" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p installer >> " + report_path_software + "\\installer" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p clsid >> " + report_path_software + "\\clsid" + ".txt")
		for i in range(len(self.ntusers)):
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p listsoft >> " + report_path_software + "\\listsoft_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p fileexts >> " + report_path_software + "\\fileexts_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p arpcache >> " + report_path_software + "\\arpcache_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p appcompatflags >> " + report_path_software + "\\appcompatflags_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p startpage >> " + report_path_software + "\\startpage_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
	
	def report_mod_network(self):
		report_path_network = self.report_path + '\\network'
		os.system('mkdir ' + report_path_network)
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p compname >> " + report_path_network + "\\compname" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p networkcards >> " + report_path_network + "\\networkcards" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p nic >> " + report_path_network + "\\nic" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p nic2 >> " + report_path_network + "\\nic2" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p macaddr >> " + report_path_network + "\\macaddr" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p shares >> " + report_path_network + "\\shares" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p fw_config >> " + report_path_network + "\\fw_config" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p routes >> " + report_path_network + "\\routes" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p networklist >> " + report_path_network + "\\networklist" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p ssid >> " + report_path_network + "\\ssid" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p networkuid >> " + report_path_network + "\\networkuid" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p network >> " + report_path_network + "\\network" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p termserv >> " + report_path_network + "\\termserv" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p termcert >> " + report_path_network + "\\termcert" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p rdpport >> " + report_path_network + "\\rdpport" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p sql_lastconnect >> " + report_path_network + "\\sql_lastconnect" + ".txt")
	
	def report_mod_storage(self):
		report_path_storage = self.report_path + '\\storage'
		os.system('mkdir ' + report_path_storage)
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p mountdev2 >> " + report_path_storage + "\\mountdev2" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p ide >> " + report_path_storage + "\\ide" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p usbdevices >> " + report_path_storage + "\\usbdevices" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p usbstor >> " + report_path_storage + "\\usbstor" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p devclass >> " + report_path_storage + "\\devclass" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p emdmgmt >> " + report_path_storage + "\\emdmgmt" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p wpdbusenum >> " + report_path_storage + "\\wpdbusenum" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p bthport >> " + report_path_storage + "\\bthport" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p btconfig >> " + report_path_storage + "\\btconfig" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p imagedev >> " + report_path_storage + "\\imagedev" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p stillimage >> " + report_path_storage + "\\stillimage" + ".txt")
		
	def report_mod_execution(self):
		report_path_execution = self.report_path + '\\execution'
		os.system('mkdir ' + report_path_execution)
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p prefetch >> " + report_path_execution + "\\prefetch_config" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p appcompatcache >> " + report_path_execution + "\\appcompatcache" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p legacy >> " + report_path_execution + "\\legacy" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p tracing >> " + report_path_execution + "\\tracing" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p direct >> " + report_path_execution + "\\direct" + ".txt")
		for i in range(len(self.ntusers)):
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p muicache >> " + report_path_execution + "\\muicache_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p userassist >> " + report_path_execution + "\\userassist_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p compatassist >> " + report_path_execution + "\\compatassist_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p streams >> " + report_path_execution + "\\streams_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			
	def report_mod_autoruns(self):
		report_path_autoruns = self.report_path + '\\autoruns'
		os.system('mkdir ' + report_path_autoruns)
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p soft_run >> " + report_path_autoruns + "\\soft_run" + ".txt")
		for i in range(len(self.ntusers)):
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p user_run >> " + report_path_autoruns + "\\user_run_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p services >> " + report_path_autoruns + "\\services" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p svc >> " + report_path_autoruns + "\\svc" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p svcdll >> " + report_path_autoruns + "\\svcdll" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p userinit >> " + report_path_autoruns + "\\userinit" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p appinitdlls >> " + report_path_autoruns + "\\appinitdlls" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p init_dlls >> " + report_path_autoruns + "\\init_dlls" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p bho >> " + report_path_autoruns + "\\bho" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p installedcomp >> " + report_path_autoruns + "\\installedcomp" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p imagefile >> " + report_path_autoruns + "\\imagefile" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p winlogon >> " + report_path_autoruns + "\\winlogon" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p svchost >> " + report_path_autoruns + "\\svchost" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p drivers32 >> " + report_path_autoruns + "\\drivers32" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p cmd_shell >> " + report_path_autoruns + "\\cmd_shell" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p shellexec >> " + report_path_autoruns + "\\shellexec" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p shellext >> " + report_path_autoruns + "\\shellext" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p schedagent >> " + report_path_autoruns + "\\schedagent" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p appcertdlls >> " + report_path_autoruns + "\\appcertdlls" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p lsa_packages >> " + report_path_autoruns + "\\lsa_packages" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p safeboot >> " + report_path_autoruns + "\\safeboot" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p dllsearch >> " + report_path_autoruns + "\\dllsearch" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p securityproviders >> " + report_path_autoruns + "\\securityproviders" + ".txt")
		for i in range(len(self.ntusers)):
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p load >> " + report_path_autoruns + "\\load_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p winlogon_u >> " + report_path_autoruns + "\\winlogon_u_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p cmdproc >> " + report_path_autoruns + "\\cmdproc_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			
	def report_mod_log(self):
		report_path_log = self.report_path + '\\log'
		os.system('mkdir ' + report_path_log)
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p mrt >> " + report_path_log + "\\mrt" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.security + "\" -p auditpol >> " + report_path_log + "\\auditpol" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p eventlog >> " + report_path_log + "\\eventlog" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p eventlogs >> \"" + report_path_log + "\\eventlogs" + ".txt\"")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.system + "\" -p auditfail >> " + report_path_log + "\\auditfail" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p drwatson >> " + report_path_log + "\\drwatson" + ".txt")
			
	def report_mod_web(self):
		report_path_web = self.report_path + '\\web'
		os.system('mkdir ' + report_path_web)
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p defbrowser >> " + report_path_web + "\\defbrowser" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p startmenuinternetapps_lm >> " + report_path_web + "\\startmenuinternetapps_lm" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p ie_version >> " + report_path_web + "\\ie_version" + ".txt")
		os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.software + "\" -p javasoft >> " + report_path_web + "\\javasoft" + ".txt")
		for i in range(len(self.ntusers)):
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p startmenuinternetapps_cu >> " + report_path_web + "\\startmenuinternetapps_cu_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p proxysettings >> " + report_path_web + "\\proxysettings_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p menuorder >> " + report_path_web + "\\menuorder_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p ie_settings >> " + report_path_web + "\\ie_settings_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p internet_settings_cu >> " + report_path_web + "\\internet_settings_cu_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p internet_explorer_cu >> " + report_path_web + "\\internet_explorer_cu_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p domains >> " + report_path_web + "\\domains_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p typedurls >> " + report_path_web + "\\typedurls_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			
	def report_mod_user_config(self):
		report_path_user_config = self.report_path + '\\user_config'
		os.system('mkdir ' + report_path_user_config)
		for i in range(len(self.ntusers)):
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p shellfolders >> " + report_path_user_config + "\\shellfolders_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p policies_u >> " + report_path_user_config + "\\policies_u_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p environment >> " + report_path_user_config + "\\environment_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p userinfo >> " + report_path_user_config + "\\userinfo_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p vista_bitbucket >> " + report_path_user_config + "\\vista_bitbucket_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p autorun >> " + report_path_user_config + "\\autorun_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p attachmgr >> " + report_path_user_config + "\\attachmgr_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p autoendtasks >> " + report_path_user_config + "\\autoendtasks_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p winlogon_u >> " + report_path_user_config + "\\winlogon_u_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p user_win >> " + report_path_user_config + "\\user_win_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p ccleaner >> " + report_path_user_config + "\\ccleaner_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p sysinternals >> " + report_path_user_config + "\\sysinternals_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p logonusername >> " + report_path_user_config + "\\logonusername_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p ntusernetwork >> " + report_path_user_config + "\\ntusernetwork_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p printers >> " + report_path_user_config + "\\printers_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p winvnc >> " + report_path_user_config + "\\winvnc_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p userlocsvc >> " + report_path_user_config + "\\userlocsvc_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			
	def report_mod_user_act(self):
		report_path_user_act = self.report_path + '\\user_act'
		os.system('mkdir ' + report_path_user_act)
		for i in range(len(self.ntusers)):
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p typedpaths >> " + report_path_user_act + "\\typedpaths_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p mmc >> " + report_path_user_act + "\\mmc_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p runmru >> " + report_path_user_act + "\\runmru_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p applets >> " + report_path_user_act + "\\applets_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p acmru >> " + report_path_user_act + "\\acmru_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p wordwheelquery >> " + report_path_user_act + "\\wordwheelquery_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p gthist >> " + report_path_user_act + "\\gthist_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			
	def report_mod_user_network(self):
		report_path_user_network = self.report_path + '\\user_network'
		os.system('mkdir ' + report_path_user_network)
		for i in range(len(self.ntusers)):
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p mndmru >> " + report_path_user_network + "\\mndmru_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p compdesc >> " + report_path_user_network + "\\compdesc_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p tsclient >> " + report_path_user_network + "\\tsclient_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p rdphint >> " + report_path_user_network + "\\rdphint_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p ssh_host_keys >> " + report_path_user_network + "\\ssh_host_keys_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p winscp_sessions >> " + report_path_user_network + "\\winscp_sessions_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p vncviewer >> " + report_path_user_network + "\\vncviewer_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p vnchooksapplicationprefs >> " + report_path_user_network + "\\vnchooksapplicationprefs_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			
	def report_mod_user_file(self):
		report_path_user_file = self.report_path + '\\user_file'
		os.system('mkdir ' + report_path_user_file)
		for i in range(len(self.ntusers)):
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p shellbags >> " + report_path_user_file + "\\shellbags_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p itempos >> " + report_path_user_file + "\\itempos_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p comdlg32 >> " + report_path_user_file + "\\comdlg32_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p recentdocs >> " + report_path_user_file + "\\recentdocs_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p winzip >> " + report_path_user_file + "\\winzip_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p winrar >> " + report_path_user_file + "\\winrar_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p sevenzip >> " + report_path_user_file + "\\sevenzip_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p mspaper >> " + report_path_user_file + "\\mspaper_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p nero >> " + report_path_user_file + "\\nero_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p officedocs >> " + report_path_user_file + "\\officedocs_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p officedocs2010 >> " + report_path_user_file + "\\officedocs2010_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p oisc >> " + report_path_user_file + "\\oisc_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p trustrecords >> " + report_path_user_file + "\\trustrecords_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p snapshot_viewer >> " + report_path_user_file + "\\snapshot_viewer_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p adoberdr >> " + report_path_user_file + "\\adoberdr_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p wallpaper >> " + report_path_user_file + "\\wallpaper_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p mpmru >> " + report_path_user_file + "\\mpmru_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p realplayer6 >> " + report_path_user_file + "\\realplayer6_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			
	def report_mod_user_virtual(self):
		report_path_user_virtual = self.report_path + '\\user_virtual'
		os.system('mkdir ' + report_path_user_virtual)
		for i in range(len(self.ntusers)):
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p vmplayer >> " + report_path_user_virtual + "\\vmplayer_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p vmware_vsphere_client >> " + report_path_user_virtual + "\\vmware_vsphere_client_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			
	def report_mod_comm(self):
		report_path_comm = self.report_path + '\\comm'
		os.system('mkdir ' + report_path_comm)
		for i in range(len(self.ntusers)):
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p outlook >> " + report_path_comm + "\\outlook_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p olsearch >> " + report_path_comm + "\\olsearch_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p unreadmail >> " + report_path_comm + "\\unreadmail_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p winlivemail >> " + report_path_comm + "\\winlivemail_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p skype >> " + report_path_comm + "\\skype_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p aim >> " + report_path_comm + "\\aim_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p winlivemsn >> " + report_path_comm + "\\winlivemsn_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p liveContactsGUID >> " + report_path_comm + "\\liveContactsGUID_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")
			os.system(self.regripper_path + '\\rip.exe -r \"' + self.base_hive_path + '\\' + self.ntusers[i] + "\" -p yahoo_cu >> " + report_path_comm + "\\yahoo_cu_" + self.ntusers[i][0:self.ntusers[i].find("\\")] + ".txt")