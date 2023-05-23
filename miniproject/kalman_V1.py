import numpy as np



class Kalman_filter:
    def __init__(self,x=0,y=0,z=0,yaw=0,vx=0,vy=0,vz=0,yaw_rate=0):
        self.x = x
        self.y = y
        self.z = z
        self.yaw = yaw
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.yaw_rate = yaw_rate
        self.is_initialized = False
        pass
    
    def get_vehicle_state():
        pass
    
    def get_vehicle_state_posecovariance():
        pass
    
    def prediction_step(pose,dt):
        pass
    
    def handle_wheelenco_measurement(wheel_pose,dt):
        pass
    
    def handle_amcl_measurement(amcl_pose,dt):
        pass
    
    def handle_indoorgps_measurement(gps_pose,dt):
        pass
    def handle_gazebo_odom_measurement(gazebo_pose,dt):
        pass
    
    def is_kf_initialized():
        return self.is_initialized
        
print("hello world")

kf =Kalman_filter()