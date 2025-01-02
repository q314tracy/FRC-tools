#used to calculate theoretical values for drivetrain characterization.
#kS, kV, and kA are used to develop a motor model that may be used for finer controls of mechanisms.
#kS must be measured.
# kV can be accurately calculated.
# kA can also be calculated but is only approximate.
#kA must be accurately calculated from resulting acceleration from a given voltage and using linear regression.

from math import pi

#constants
number_motors = 4
max_volts = 12 #volts
free_speed_rpm = 6784 #RPM
stall_torque = 2.65 #Nm
final_ratio = 4.71
mass = 65.77 #kg
wheel_radius = 0.0762 / 2 #meters
wheel_conv_factor = wheel_radius * 2*pi / 60

#linear calculations
def calc_linear_vel_m() -> float:
    vel = (free_speed_rpm / final_ratio) * wheel_conv_factor
    return vel
def calc_linear_acl_m() -> float:
    acl = ((stall_torque * final_ratio * number_motors) / wheel_radius) / mass
    return acl

#values
max_vel = calc_linear_vel_m()
max_acl = calc_linear_acl_m()
kV = max_volts / max_vel
kA = max_volts / max_acl

print(f"calculated max vel is {max_vel} m/s")
print(f"calculated max acceleration is {max_acl} m/s^2")
print(f"calculated kV is {kV} volts per m/s")
print(f"calcualted kA is {kA} volts per m/s^2")