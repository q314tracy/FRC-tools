#used to calculate theoretical values for drivetrain characterization.
#kS, kV, and kA are used to develop a motor model that may be used for finer controls of mechanisms.
#kS must be measured.
# kV can be accurately calculated.
# kA can also be calculated but is only approximate.
#kA must be accurately calculated from resulting acceleration from a given voltage and using linear regression.

from math import pi

#constants, all must be in metric units
number_motors = 1
max_volts = 12 #volts
free_speed_rpm = 11004 #RPM
stall_torque = 0.97 #Nm
final_ratio = 46.42 
mass = 2.26 #kg
approxmate_radius = 0.1016 #meters
mom_of_inertia = 0.5 * mass * approxmate_radius**2

#angular calculations
def calc_angular_vel_rad() -> float:
    vel = (free_speed_rpm / final_ratio) * 2*pi / 60
    return vel
def calc_angular_acl_rad() -> float:
    acl = (stall_torque * final_ratio) / mom_of_inertia
    return acl

#values
max_vel = calc_angular_vel_rad()
max_acl = calc_angular_acl_rad()
kV = max_volts / max_vel
kA = max_volts / max_acl

print(f"calculated max vel is {max_vel} rad/s")
print(f"calculated max acceleration is {max_acl} rad/s^2")
print(f"calculated kV is {kV} volts per rad/s")
print(f"calcualted kA is {kA} volts per rad/s^2")