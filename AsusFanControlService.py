# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)]
# From type library 'AsusFanControlService.exe'
# On Fri Jan 22 02:28:48 2016
'AsusFanControlService 1.0 Type Library'
makepy_version = '0.5.01'
python_version = 0x30501f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{DF5522FB-119C-428D-A62E-8BFE4A2FBC9B}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class IDualModeFanCurve(DispatchBaseClass):
	'IDualModeFanCurve Interface'
	CLSID = IID('{A7808A8A-F1E3-4E7B-96DA-1C51545EE988}')
	coclass_clsid = None

	def AddPoint(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg):
		'method AddPoint'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 1), (3, 1)),x
			, y)

	# Result is of type IFanCurvePoint
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{C3C24163-FC1B-431F-978D-44A9FBAC34EC}')
		return ret

	_prop_map_get_ = {
		"Count": (2, 2, (3, 0), (), "Count", None),
		# Method 'FanCurve' returns object of type 'IFanCurve'
		"FanCurve": (4, 2, (9, 0), (), "FanCurve", '{E6BB07B4-F360-45AF-814E-EB0D12D55BEC}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{C3C24163-FC1B-431F-978D-44A9FBAC34EC}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{C3C24163-FC1B-431F-978D-44A9FBAC34EC}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IFanControl(DispatchBaseClass):
	'IFanControl Interface'
	CLSID = IID('{D20E7B8F-C878-4538-B624-9BC08FE7D54F}')
	coclass_clsid = None

	def ApplyFanCurve(self, FanCurve=defaultNamedNotOptArg):
		'method ApplyFanCurve'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (19, 0), ((9, 1),),FanCurve
			)

	def ApplyFanCurveButNotSave(self, FanCurve=defaultNamedNotOptArg):
		'method ApplyFanCurveButNotSave'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (19, 0), ((9, 1),),FanCurve
			)

	def ApplyIndex(self, index=defaultNamedNotOptArg):
		'method ApplyIndex'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((3, 1),),index
			)

	# The method CalculatedDuty is actually a property, but must be used as a method to correctly pass the arguments
	def CalculatedDuty(self, Temperature=defaultNamedNotOptArg):
		'property CalculatedDuty'
		return self._oleobj_.InvokeTypes(9, LCID, 2, (17, 0), ((17, 1),),Temperature
			)

	def EnableManualMode(self, value=defaultNamedNotOptArg):
		'method EnableManualMode'
		return self._oleobj_.InvokeTypes(37, LCID, 1, (24, 0), ((11, 1),),value
			)

	def EnableRpmMode(self, value=defaultNamedNotOptArg):
		'method EnableRpmMode'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (24, 0), ((11, 1),),value
			)

	def EnableRpmModeButNotSave(self, value=defaultNamedNotOptArg):
		'method EnableRpmModeButNotSave'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (24, 0), ((11, 1),),value
			)

	def NormalizeFanCurve(self, FanCurve=defaultNamedNotOptArg):
		'method NormalizeFanCurve'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (19, 0), ((9, 1),),FanCurve
			)

	def RefreshFanCurve(self):
		'method RefreshFanCurve'
		return self._oleobj_.InvokeTypes(36, LCID, 1, (19, 0), (),)

	def SetFanDuty(self, FanCurve=defaultNamedNotOptArg):
		'method SetFanDuty'
		return self._oleobj_.InvokeTypes(35, LCID, 1, (19, 0), ((9, 1),),FanCurve
			)

	_prop_map_get_ = {
		# Method 'CurrentFanCurve' returns object of type 'IFanCurve'
		"CurrentFanCurve": (13, 2, (9, 0), (), "CurrentFanCurve", '{E6BB07B4-F360-45AF-814E-EB0D12D55BEC}'),
		"DisplayName": (14, 2, (8, 0), (), "DisplayName", None),
		"DutyCycle": (3, 2, (17, 0), (), "DutyCycle", None),
		"EcFanStop": (21, 2, (11, 0), (), "EcFanStop", None),
		"EcMode": (11, 2, (3, 0), (), "EcMode", None),
		"FanSourceIndex": (38, 2, (19, 0), (), "FanSourceIndex", None),
		"Id": (1, 2, (19, 0), (), "Id", None),
		"IsRpmMode": (19, 2, (11, 0), (), "IsRpmMode", None),
		"IsSencitiveSupported": (34, 2, (19, 0), (), "IsSencitiveSupported", None),
		"MinimalDuty": (10, 2, (17, 0), (), "MinimalDuty", None),
		"Name": (2, 2, (8, 0), (), "Name", None),
		# Method 'Profiles' returns object of type 'IFanProfileCollection'
		"Profiles": (4, 2, (9, 0), (), "Profiles", '{8CAF0DBE-D1E1-42A4-B0EC-1B365CF50982}'),
		"RpmTolerance": (20, 2, (19, 0), (), "RpmTolerance", None),
		"StartupProfileIndex": (7, 2, (19, 0), (), "StartupProfileIndex", None),
		"StepDownTime": (16, 2, (19, 0), (), "StepDownTime", None),
		"StepUnit": (22, 2, (19, 0), (), "StepUnit", None),
		"StepUnitSupported": (24, 2, (19, 0), (), "StepUnitSupported", None),
		"StepUpTime": (15, 2, (19, 0), (), "StepUpTime", None),
		"T1DelayTime": (23, 2, (19, 0), (), "T1DelayTime", None),
		"TempTolerance": (17, 2, (19, 0), (), "TempTolerance", None),
		# Method 'ThermalWeights' returns object of type 'IThermalWeights'
		"ThermalWeights": (12, 2, (9, 0), (), "ThermalWeights", '{2DFEAC64-E8E8-437E-8662-25F7AA4B0CE0}'),
		"WeightsSupported": (25, 2, (19, 0), (), "WeightsSupported", None),
	}
	_prop_map_put_ = {
		"DisplayName": ((14, LCID, 4, 0),()),
		"DutyCycle": ((3, LCID, 4, 0),()),
		"EcFanStop": ((21, LCID, 4, 0),()),
		"EcMode": ((11, LCID, 4, 0),()),
		"FanSourceIndex": ((38, LCID, 4, 0),()),
		"RpmTolerance": ((20, LCID, 4, 0),()),
		"RpmToleranceButNotSave": ((31, LCID, 4, 0),()),
		"StartupProfileIndex": ((7, LCID, 4, 0),()),
		"StepDownTime": ((16, LCID, 4, 0),()),
		"StepDownTimeButNotSave": ((28, LCID, 4, 0),()),
		"StepUnit": ((22, LCID, 4, 0),()),
		"StepUnitButNotSave": ((26, LCID, 4, 0),()),
		"StepUpTime": ((15, LCID, 4, 0),()),
		"StepUpTimeButNotSave": ((27, LCID, 4, 0),()),
		"T1DelayTime": ((23, LCID, 4, 0),()),
		"T1DelayTimeButNotSave": ((29, LCID, 4, 0),()),
		"TempTolerance": ((17, LCID, 4, 0),()),
		"ThermalWeights": ((12, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IFanControlCollection(DispatchBaseClass):
	'IFanControlCollection Interface'
	CLSID = IID('{05F22B4C-27D5-4488-A7EE-B712FE447426}')
	coclass_clsid = None

	# Result is of type IFanControl
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{D20E7B8F-C878-4538-B624-9BC08FE7D54F}')
		return ret

	_prop_map_get_ = {
		"Count": (2, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{D20E7B8F-C878-4538-B624-9BC08FE7D54F}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{D20E7B8F-C878-4538-B624-9BC08FE7D54F}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IFanControlManager(DispatchBaseClass):
	'IFanControlManager Interface'
	CLSID = IID('{BB327645-E3EC-4B7D-90EE-67FCB949E584}')
	coclass_clsid = IID('{14083C53-B8E7-48E4-9320-811F3478C4A4}')

	_prop_map_get_ = {
		"ConstraintType": (3, 2, (2, 0), (), "ConstraintType", None),
		# Method 'Controls' returns object of type 'IFanControlCollection'
		"Controls": (2, 2, (9, 0), (), "Controls", '{05F22B4C-27D5-4488-A7EE-B712FE447426}'),
		"IsSIOSupportedRPM": (6, 2, (11, 0), (), "IsSIOSupportedRPM", None),
		"MaxStepTime": (4, 2, (19, 0), (), "MaxStepTime", None),
		"MaxTolerance": (5, 2, (19, 0), (), "MaxTolerance", None),
		"OneSencitiveSupported": (9, 2, (11, 0), (), "OneSencitiveSupported", None),
		"RpmPerstep": (7, 2, (19, 0), (), "RpmPerstep", None),
		"RpmSmoothFreq": (8, 2, (19, 0), (), "RpmSmoothFreq", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IFanCurve(DispatchBaseClass):
	'IFanCurve Interface'
	CLSID = IID('{E6BB07B4-F360-45AF-814E-EB0D12D55BEC}')
	coclass_clsid = None

	def AddPoint(self, x=defaultNamedNotOptArg, y=defaultNamedNotOptArg):
		'method AddPoint'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 1), (3, 1)),x
			, y)

	# Result is of type IFanCurvePoint
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{C3C24163-FC1B-431F-978D-44A9FBAC34EC}')
		return ret

	_prop_map_get_ = {
		"Count": (2, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{C3C24163-FC1B-431F-978D-44A9FBAC34EC}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{C3C24163-FC1B-431F-978D-44A9FBAC34EC}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IFanCurvePoint(DispatchBaseClass):
	'IFanCurvePoint Interface'
	CLSID = IID('{C3C24163-FC1B-431F-978D-44A9FBAC34EC}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Speed": (2, 2, (3, 0), (), "Speed", None),
		"Temperature": (1, 2, (3, 0), (), "Temperature", None),
	}
	_prop_map_put_ = {
		"Speed": ((2, LCID, 4, 0),()),
		"Temperature": ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IFanProfile(DispatchBaseClass):
	'IFanProfile Interface'
	CLSID = IID('{DDC814D3-118A-4BC7-9E0D-8C96599E922C}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'FanCurve' returns object of type 'IFanCurve'
		"FanCurve": (4, 2, (9, 0), (), "FanCurve", '{E6BB07B4-F360-45AF-814E-EB0D12D55BEC}'),
		"Id": (3, 2, (19, 0), (), "Id", None),
		"Name": (1, 2, (8, 0), (), "Name", None),
		"Type": (2, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IFanProfileCollection(DispatchBaseClass):
	'IFanProfileCollection Interface'
	CLSID = IID('{8CAF0DBE-D1E1-42A4-B0EC-1B365CF50982}')
	coclass_clsid = None

	# Result is of type IFanProfile
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{DDC814D3-118A-4BC7-9E0D-8C96599E922C}')
		return ret

	def SaveUserProfile(self, FanCurve=defaultNamedNotOptArg):
		'method SaveUserProfile'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (19, 0), ((9, 1),),FanCurve
			)

	_prop_map_get_ = {
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Current": (4, 2, (19, 0), (), "Current", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'property Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{DDC814D3-118A-4BC7-9E0D-8C96599E922C}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{DDC814D3-118A-4BC7-9E0D-8C96599E922C}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IThermalWeights(DispatchBaseClass):
	'IThermalWeights Interface'
	CLSID = IID('{2DFEAC64-E8E8-437E-8662-25F7AA4B0CE0}')
	coclass_clsid = None

	def ApplyButNotSave(self):
		'method ApplyButNotSave'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), (),)

	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'property Item'
		return self._oleobj_.InvokeTypes(0, LCID, 2, (3, 0), ((3, 1),),index
			)

	def Save(self):
		'method Save'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), (),)

	# The method SetItem is actually a property, but must be used as a method to correctly pass the arguments
	def SetItem(self, index=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'property Item'
		return self._oleobj_.InvokeTypes(0, LCID, 4, (24, 0), ((3, 1), (3, 1)),index
			, arg1)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'property Item'
		return self._oleobj_.InvokeTypes(0, LCID, 2, (3, 0), ((3, 1),),index
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class _IFanControlManagerEvents:
	'_IFanControlManagerEvents Interface'
	CLSID = CLSID_Sink = IID('{6F71C865-D228-4B2A-9B8B-C4F979EA8998}')
	coclass_clsid = IID('{14083C53-B8E7-48E4-9320-811F3478C4A4}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnFanSettingChange",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnFanSettingChange(self, fanCtrlId=defaultNamedNotOptArg):
#		'method OnFanSettingChange'


from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'AsusFanControlService.FanControlManag.1'
class FanControlManager(CoClassBaseClass): # A CoClass
	# FanControlManager Class
	CLSID = IID('{14083C53-B8E7-48E4-9320-811F3478C4A4}')
	coclass_sources = [
		_IFanControlManagerEvents,
	]
	default_source = _IFanControlManagerEvents
	coclass_interfaces = [
		IFanControlManager,
	]
	default_interface = IFanControlManager

IDualModeFanCurve_vtables_dispatch_ = 1
IDualModeFanCurve_vtables_ = [
	(( 'FanCurve' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E6BB07B4-F360-45AF-814E-EB0D12D55BEC}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IFanControl_vtables_dispatch_ = 1
IFanControl_vtables_ = [
	(( 'Id' , 'pVal' , ), 1, (1, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'DutyCycle' , 'pVal' , ), 3, (3, (), [ (16401, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'DutyCycle' , 'pVal' , ), 3, (3, (), [ (17, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Profiles' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{8CAF0DBE-D1E1-42A4-B0EC-1B365CF50982}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ApplyFanCurve' , 'FanCurve' , 'retVal' , ), 5, (5, (), [ (9, 1, None, "IID('{E6BB07B4-F360-45AF-814E-EB0D12D55BEC}')") ,
			 (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'NormalizeFanCurve' , 'FanCurve' , 'retVal' , ), 6, (6, (), [ (9, 1, None, "IID('{E6BB07B4-F360-45AF-814E-EB0D12D55BEC}')") ,
			 (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'StartupProfileIndex' , 'pVal' , ), 7, (7, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'StartupProfileIndex' , 'pVal' , ), 7, (7, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ApplyIndex' , 'index' , ), 8, (8, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'CalculatedDuty' , 'Temperature' , 'pVal' , ), 9, (9, (), [ (17, 1, None, None) ,
			 (16401, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'MinimalDuty' , 'pVal' , ), 10, (10, (), [ (16401, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'EcMode' , 'pVal' , ), 11, (11, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'EcMode' , 'pVal' , ), 11, (11, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ThermalWeights' , 'pVal' , ), 12, (12, (), [ (16393, 10, None, "IID('{2DFEAC64-E8E8-437E-8662-25F7AA4B0CE0}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ThermalWeights' , 'pVal' , ), 12, (12, (), [ (9, 1, None, "IID('{2DFEAC64-E8E8-437E-8662-25F7AA4B0CE0}')") , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'CurrentFanCurve' , 'pVal' , ), 13, (13, (), [ (16393, 10, None, "IID('{E6BB07B4-F360-45AF-814E-EB0D12D55BEC}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'DisplayName' , 'pVal' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'DisplayName' , 'pVal' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'StepUpTime' , 'pVal' , ), 15, (15, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'StepDownTime' , 'pVal' , ), 16, (16, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'StepDownTime' , 'pVal' , ), 16, (16, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'TempTolerance' , 'pVal' , ), 17, (17, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'TempTolerance' , 'pVal' , ), 17, (17, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'EnableRpmMode' , 'value' , ), 18, (18, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'IsRpmMode' , 'pVal' , ), 19, (19, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'RpmTolerance' , 'pVal' , ), 20, (20, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'RpmTolerance' , 'pVal' , ), 20, (20, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'EcFanStop' , 'pVal' , ), 21, (21, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'EcFanStop' , 'pVal' , ), 21, (21, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'StepUnit' , 'pVal' , ), 22, (22, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'StepUnit' , 'pVal' , ), 22, (22, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'T1DelayTime' , 'pVal' , ), 23, (23, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'T1DelayTime' , 'pVal' , ), 23, (23, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'StepUnitSupported' , 'pVal' , ), 24, (24, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'WeightsSupported' , 'pVal' , ), 25, (25, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'StepUnitButNotSave' , ), 26, (26, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'StepUpTimeButNotSave' , ), 27, (27, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'StepDownTimeButNotSave' , ), 28, (28, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'T1DelayTimeButNotSave' , ), 29, (29, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'RpmToleranceButNotSave' , ), 31, (31, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'EnableRpmModeButNotSave' , 'value' , ), 32, (32, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'ApplyFanCurveButNotSave' , 'FanCurve' , 'retVal' , ), 33, (33, (), [ (9, 1, None, "IID('{E6BB07B4-F360-45AF-814E-EB0D12D55BEC}')") ,
			 (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'IsSencitiveSupported' , 'pVal' , ), 34, (34, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'SetFanDuty' , 'FanCurve' , 'retVal' , ), 35, (35, (), [ (9, 1, None, "IID('{E6BB07B4-F360-45AF-814E-EB0D12D55BEC}')") ,
			 (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'RefreshFanCurve' , 'retVal' , ), 36, (36, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'EnableManualMode' , 'value' , ), 37, (37, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'FanSourceIndex' , 'pVal' , ), 38, (38, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'FanSourceIndex' , 'pVal' , ), 38, (38, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
]

IFanControlCollection_vtables_dispatch_ = 1
IFanControlCollection_vtables_ = [
	(( '_NewEnum' , 'pVal' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'pVal' , ), 0, (0, (), [ (3, 1, None, None) ,
			 (16393, 10, None, "IID('{D20E7B8F-C878-4538-B624-9BC08FE7D54F}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IFanControlManager_vtables_dispatch_ = 1
IFanControlManager_vtables_ = [
	(( 'Controls' , 'value' , ), 2, (2, (), [ (16393, 10, None, "IID('{05F22B4C-27D5-4488-A7EE-B712FE447426}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ConstraintType' , 'pVal' , ), 3, (3, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'MaxStepTime' , 'pVal' , ), 4, (4, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'MaxTolerance' , 'pVal' , ), 5, (5, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'IsSIOSupportedRPM' , 'pVal' , ), 6, (6, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'RpmPerstep' , 'pVal' , ), 7, (7, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'RpmSmoothFreq' , 'pVal' , ), 8, (8, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'OneSencitiveSupported' , 'pVal' , ), 9, (9, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IFanCurve_vtables_dispatch_ = 1
IFanCurve_vtables_ = [
	(( '_NewEnum' , 'pVal' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'pVal' , ), 0, (0, (), [ (3, 1, None, None) ,
			 (16393, 10, None, "IID('{C3C24163-FC1B-431F-978D-44A9FBAC34EC}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'AddPoint' , 'x' , 'y' , ), 3, (3, (), [ (3, 1, None, None) ,
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IFanCurvePoint_vtables_dispatch_ = 1
IFanCurvePoint_vtables_ = [
	(( 'Temperature' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Temperature' , 'pVal' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Speed' , 'pVal' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Speed' , 'pVal' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IFanProfile_vtables_dispatch_ = 1
IFanProfile_vtables_ = [
	(( 'Name' , 'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'pVal' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Id' , 'pVal' , ), 3, (3, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FanCurve' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{E6BB07B4-F360-45AF-814E-EB0D12D55BEC}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IFanProfileCollection_vtables_dispatch_ = 1
IFanProfileCollection_vtables_ = [
	(( '_NewEnum' , 'pVal' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'pVal' , ), 0, (0, (), [ (3, 1, None, None) ,
			 (16393, 10, None, "IID('{DDC814D3-118A-4BC7-9E0D-8C96599E922C}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Current' , 'pVal' , ), 4, (4, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'SaveUserProfile' , 'FanCurve' , 'result' , ), 5, (5, (), [ (9, 1, None, "IID('{E6BB07B4-F360-45AF-814E-EB0D12D55BEC}')") ,
			 (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IThermalWeights_vtables_dispatch_ = 1
IThermalWeights_vtables_ = [
	(( '_NewEnum' , 'pVal' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'pVal' , ), 0, (0, (), [ (3, 1, None, None) ,
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'pVal' , ), 0, (0, (), [ (3, 1, None, None) ,
			 (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Save' , ), 2, (2, (), [ ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ApplyButNotSave' , ), 3, (3, (), [ ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{C3C24163-FC1B-431F-978D-44A9FBAC34EC}' : IFanCurvePoint,
	'{6F71C865-D228-4B2A-9B8B-C4F979EA8998}' : _IFanControlManagerEvents,
	'{A7808A8A-F1E3-4E7B-96DA-1C51545EE988}' : IDualModeFanCurve,
	'{DDC814D3-118A-4BC7-9E0D-8C96599E922C}' : IFanProfile,
	'{05F22B4C-27D5-4488-A7EE-B712FE447426}' : IFanControlCollection,
	'{E6BB07B4-F360-45AF-814E-EB0D12D55BEC}' : IFanCurve,
	'{14083C53-B8E7-48E4-9320-811F3478C4A4}' : FanControlManager,
	'{2DFEAC64-E8E8-437E-8662-25F7AA4B0CE0}' : IThermalWeights,
	'{BB327645-E3EC-4B7D-90EE-67FCB949E584}' : IFanControlManager,
	'{8CAF0DBE-D1E1-42A4-B0EC-1B365CF50982}' : IFanProfileCollection,
	'{D20E7B8F-C878-4538-B624-9BC08FE7D54F}' : IFanControl,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{C3C24163-FC1B-431F-978D-44A9FBAC34EC}' : 'IFanCurvePoint',
	'{A7808A8A-F1E3-4E7B-96DA-1C51545EE988}' : 'IDualModeFanCurve',
	'{DDC814D3-118A-4BC7-9E0D-8C96599E922C}' : 'IFanProfile',
	'{05F22B4C-27D5-4488-A7EE-B712FE447426}' : 'IFanControlCollection',
	'{E6BB07B4-F360-45AF-814E-EB0D12D55BEC}' : 'IFanCurve',
	'{2DFEAC64-E8E8-437E-8662-25F7AA4B0CE0}' : 'IThermalWeights',
	'{BB327645-E3EC-4B7D-90EE-67FCB949E584}' : 'IFanControlManager',
	'{8CAF0DBE-D1E1-42A4-B0EC-1B365CF50982}' : 'IFanProfileCollection',
	'{D20E7B8F-C878-4538-B624-9BC08FE7D54F}' : 'IFanControl',
}


NamesToIIDMap = {
	'IFanControlManager' : '{BB327645-E3EC-4B7D-90EE-67FCB949E584}',
	'IDualModeFanCurve' : '{A7808A8A-F1E3-4E7B-96DA-1C51545EE988}',
	'IFanControlCollection' : '{05F22B4C-27D5-4488-A7EE-B712FE447426}',
	'IFanCurve' : '{E6BB07B4-F360-45AF-814E-EB0D12D55BEC}',
	'IFanProfile' : '{DDC814D3-118A-4BC7-9E0D-8C96599E922C}',
	'IFanProfileCollection' : '{8CAF0DBE-D1E1-42A4-B0EC-1B365CF50982}',
	'IThermalWeights' : '{2DFEAC64-E8E8-437E-8662-25F7AA4B0CE0}',
	'IFanControl' : '{D20E7B8F-C878-4538-B624-9BC08FE7D54F}',
	'_IFanControlManagerEvents' : '{6F71C865-D228-4B2A-9B8B-C4F979EA8998}',
	'IFanCurvePoint' : '{C3C24163-FC1B-431F-978D-44A9FBAC34EC}',
}


