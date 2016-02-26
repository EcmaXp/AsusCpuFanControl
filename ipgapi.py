# -*- coding: utf-8 -*-
"""Intel® Power Gadget 3.0 API for Python

https://software.intel.com/blogs/2014/01/07/using-the-intel-power-gadget-30-api-on-windows
"""

import functools
import os
import platform
import time
from ctypes import *
from ctypes import _Pointer as PrototypePointer

__all__ = ["ipg_ver", "ipg_dir", "load_ipg", "IPGError", "IPGCallFailure"]

ipg_func_prototypes = dict(
    # 1: bool IntelEnergyLibInitialize();
    IntelEnergyLibInitialize = WINFUNCTYPE(c_bool),
    # 2: bool ReadSample();
    ReadSample = WINFUNCTYPE(c_bool),
    # 3: bool GetNumNodes(int *nNodes);
    GetNumNodes = WINFUNCTYPE(c_bool, POINTER(c_int)),
    # 4: bool GetNumMsrs(int *nMsrs);
    GetNumMsrs = WINFUNCTYPE(c_bool, POINTER(c_int)),
    # 5: bool GetMsrName(int iMsr, wchar_t *szName);
    GetMsrName = None,
    # 6: bool GetMsrFunc(int iMsr, int *pFuncID);
    GetMsrFunc = None,
    # 7: bool GetPowerData(int iNode, int iMSR, double *pResult, int *nResult);
    GetPowerData = None,
    # 8: bool IsGTAvailable();
    IsGTAvailable = WINFUNCTYPE(c_bool),
    # 9: bool GetGTFrequency(int *freq);
    GetGTFrequency = WINFUNCTYPE(c_bool, c_int, POINTER(c_int)),
    # 10: bool GetSysTime(void *pSysTime);
    GetSysTime =  WINFUNCTYPE(c_bool, c_int, POINTER(c_int64)),
    # 11: bool GetTimeInterval(double *pOffset);
    GetTimeInterval =  WINFUNCTYPE(c_bool, c_int, POINTER(c_double)),
    # 12: bool GetIAFrequency(int iNode, int *freqInMHz);
    GetIAFrequency = WINFUNCTYPE(c_bool, c_int, POINTER(c_int)),
    # 13: bool GetTDP(int iNode, double *TDP);
    GetTDP = WINFUNCTYPE(c_bool, c_int, POINTER(c_double)),
    # 14: bool GetMaxTemperature(int iNode, int *degreeC);
    GetMaxTemperature = WINFUNCTYPE(c_bool, c_int, POINTER(c_int)),
    # 15: bool GetTemperature(int iNode, int *degreeC);
    GetTemperature = WINFUNCTYPE(c_bool, c_int, POINTER(c_int)),
    # 16: bool GetBaseFrequency(int iNode, double *pBaseFrequency);
    GetBaseFrequency = WINFUNCTYPE(c_bool, c_int, POINTER(c_int)),
    # 17: bool StartLog(wchar_t *szFileName);
    StartLog = None,
    # 18: bool StopLog();
    StopLog = None,
)


class IPGError(Exception):
    pass


class IPGCallFailure(IPGError):
    pass


def ipg_errcheck(result, func, arguments):
    if not result:
        raise IPGCallFailure("function return false (that's all)")


def build_func(funcname, prototype, dllfunc):
    rawfunc = prototype(dllfunc)
    if funcname.startswith("Get"):
        last_arg_type = rawfunc.argtypes[-1]
        if issubclass(last_arg_type, PrototypePointer):
            unboxed_type = last_arg_type._type_

            @functools.wraps(rawfunc)
            def func(*args):
                box = unboxed_type(0)
                args = args + (box,)
                result = rawfunc(*args)
                return box.value

            rawfunc.errcheck = ipg_errcheck
            return func
    elif funcname.startswith("Is"):
        pass
    else:
        rawfunc.errcheck = ipg_errcheck

    return rawfunc


def setup_dll(dll):
    for funcname, prototype in ipg_func_prototypes.items():
        if not prototype:
            setattr(dll, funcname, NotImplemented)
            continue

        rawfunc = getattr(dll, funcname)
        func = build_func(funcname, prototype, rawfunc)
        setattr(dll, funcname, func)


def ipg_ver():
    return os.environ.get("IPG_Ver")


def ipg_dir():
    return os.environ.get("IPG_Dir")


def find_dllpath():
    ver = ipg_ver()
    if not ver or ver < "3.0":
        raise EnvironmentError("Require IPG 3.0+")

    archbit, name = platform.architecture()
    if name != "WindowsPE":
        raise EnvironmentError("Require Windows for running: ".format(name))

    dllname = None
    if archbit == "64bit":
        dllname = "EnergyLib64.dll"
    elif archbit == "32bit":
        dllname = "EnergyLib32.dll"
    else:
        raise EnvironmentError("Incorrect Arch: {}".format(archbit))

    ipg_path = ipg_dir()
    if not ipg_path:
        raise EnvironmentError("IPG Dir are empty")

    dllpath = os.path.join(ipg_path, dllname)
    return dllpath


def load_ipg(*, auto_init=True):
    dll = WinDLL(find_dllpath())
    setup_dll(dll)

    if auto_init:
        dll.IntelEnergyLibInitialize()

    return dll


def main():
    dll = load_ipg()

    while True:
        dll.ReadSample()
        print(dll.GetTemperature(0))
        time.sleep(0.5)


if __name__ == "__main__":
    main()
