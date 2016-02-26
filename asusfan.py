from AsusFanControlService import FanControlManager
import ctypes
import time
import atexit
import wmi
import contextlib

__all__ = ["FanManager", "FanControl", "get_cpu_fan"]


class FanManager():
    def __init__(self):
        self.mgr = FanControlManager()

    def __getitem__(self, key):
        obj = self.get_control(key)
        if obj is None:
            raise KeyError(key)

        return obj

    def get_control(self, key):
        for control in self.mgr.Controls:
            if control.Name == key:
                return FanControl(self, control)

        return None

class FanControl():
    def __init__(self, parent, raw_control):
        self.parent = parent
        self.name = raw_control.Name
        self.control = raw_control

    def __enter__(self):
        self.setup()
        return self

    def __exit__(self, a, b, c):
        self.restore()

    def setup(self):
        self.setEnable(True)
        self.StepUpTimeButNotSave = 0
        self.StepDownTimeButNotSave = 0

    def restore(self):
        self.setEnable(False)
        self.set_profile(self["User"])

    def __getitem__(self, key):
        obj = self.get_profile(key)
        if obj is None:
            raise KeyError(key)

        return obj

    def get_profile(self, key):
        for profile in self.control.Profiles:
            if profile.Name == key:
                return profile

        return None

    def set_profile(self, profile):
        if profile.Name == "User":
            target = self["Standard"].FanCurve
            for x, y in zip(target, profile.FanCurve):
                x.Temperature = y.Temperature
                x.Speed = y.Speed

            self.control.SetFanDuty(target)
        else:
            self.control.SetFanDuty(profile.FanCurve)

    def setEnable(self, value:bool):
        self.control.EnableManualMode(value)

    def getCycle(self) -> float:
        return self.control.DutyCycle / 255 * 100

    def setCycle(self, value:float):
        self.control.DutyCycle = value


def get_cpu_fan():
    mgr = FanManager()
    fan = mgr["CPU fan"]
    return fan
