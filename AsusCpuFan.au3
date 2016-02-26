#Region ;**** Directives created by AutoIt3Wrapper_GUI ****
#AutoIt3Wrapper_UseX64=y
#AutoIt3Wrapper_Res_Description=AsusCpuFan - EcmaXp
#AutoIt3Wrapper_Res_Language=1042
#AutoIt3Wrapper_Res_requestedExecutionLevel=requireAdministrator
#EndRegion ;**** Directives created by AutoIt3Wrapper_GUI ****
#NoTrayIcon
#include <Misc.au3>
#include <MsgBoxConstants.au3>

AutoItWinSetTitle("AsusCpuFan - EcmaXp")

If _Singleton("AsusCpuFan_EcmaXp", 1) = 0 Then
    MsgBox($MB_SYSTEMMODAL, "Warning", "AsusCpuFan - EcmaXp are already running.")
    Exit
EndIf

$Py = DllOpen("Python35")
DllCall($Py, "int", "Py_Initialize")
DllCall($Py, "int", "PyRun_SimpleString", "str", "from main import main; main()")
