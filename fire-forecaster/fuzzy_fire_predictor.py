import numpy as np
from skfuzzy import control as ctrl
from skfuzzy import membership as mf
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import FWI_Calculator
import tkinter as tk
from matplotlib.figure import Figure
from tkinter import messagebox



# Define the antecedents and consequents using skfuzzy
fwi = ctrl.Antecedent(np.arange(0, 150, 0.1), 'fwi')
ndvi = ctrl.Antecedent(np.arange(0, 1, 0.001), 'ndvi')
settlement_dist = ctrl.Antecedent(np.arange(0, 10000, 1), 'distance of settlement')
fire_spread_rate = ctrl.Consequent(np.arange(0, 5000, 0.5), 'rate of fire spread')
fire_risk = ctrl.Consequent(np.arange(0, 100, 0.5), 'risk of fire')

# Membership functions for FWI
fwi['very low'] = mf.trimf(fwi.universe, [0, 0, 8.2])
fwi['low'] = mf.trimf(fwi.universe, [2.6, 8.2, 16.25])
fwi['moderate'] = mf.trimf(fwi.universe, [8.2, 16.25, 29.65])
fwi['high'] = mf.trimf(fwi.universe, [16.25, 29.65, 44.0])
fwi['very high'] = mf.trimf(fwi.universe, [29.65, 44.0, 55.0])
fwi['extremely high'] = mf.trapmf(fwi.universe, [44.0, 50, 150, 150])

# Membership functions for NDVI
ndvi['very low'] = mf.trimf(ndvi.universe, [0, 0, 0.32])
ndvi['low'] = mf.trimf(ndvi.universe, [0.125, 0.32, 0.425])
ndvi['moderate'] = mf.trimf(ndvi.universe, [0.32, 0.425, 0.53])
ndvi['high'] = mf.trimf(ndvi.universe, [0.425, 0.53, 0.8])
ndvi['very high'] = mf.trapmf(ndvi.universe, [0.53, 0.8, 1, 1])

# Membership functions for Settlement Distance
settlement_dist['very low'] = mf.trimf(settlement_dist.universe, [0, 0, 1100])
settlement_dist['low'] = mf.trimf(settlement_dist.universe, [450, 1100, 1500])
settlement_dist['moderate'] = mf.trimf(settlement_dist.universe, [1100, 1500, 1900])
settlement_dist['high'] = mf.trimf(settlement_dist.universe, [1500, 1900, 6050])
settlement_dist['very high'] = mf.trapmf(settlement_dist.universe, [1900, 6050, 10000, 10000])

# Membership functions for Fire Risk
fire_risk['very low'] = mf.trimf(fire_risk.universe, [0, 0, 33.33])
fire_risk['low'] = mf.trimf(fire_risk.universe, [0, 33.33, 66.66])
fire_risk['moderate'] = mf.trimf(fire_risk.universe, [33.33, 66.66, 100])
fire_risk['high'] = mf.trimf(fire_risk.universe, [66.66, 100, 100])

# Membership functions for Fire Spread Rate
fire_spread_rate['very low'] = mf.trimf(fire_spread_rate.universe, [0, 0, 40])
fire_spread_rate['low'] = mf.trimf(fire_spread_rate.universe, [20, 65, 110])
fire_spread_rate['moderate'] = mf.trimf(fire_spread_rate.universe, [60, 330, 600])
fire_spread_rate['high'] = mf.trimf(fire_spread_rate.universe, [300, 650, 1000])
fire_spread_rate['very high'] = mf.trimf(fire_spread_rate.universe, [700, 1850, 3000])
fire_spread_rate['extremely high'] = mf.trapmf(fire_spread_rate.universe, [2000, 3000, 5000, 5000])

fwi.view()
ndvi.view()
settlement_dist.view()
fire_spread_rate.view()
fire_risk.view()


        
# Define Rules
rule1 = ctrl.Rule(fwi['very low'] & ndvi['very low'] & settlement_dist['very low'], (fire_risk['very low'], fire_spread_rate['very low']))
rule2 = ctrl.Rule(fwi['very low'] & ndvi['very low'] & settlement_dist['low'], (fire_risk['very low'], fire_spread_rate['very low']))
rule3 = ctrl.Rule(fwi['very low'] & ndvi['very low'] & settlement_dist['moderate'], (fire_risk['very low'], fire_spread_rate['very low']))
rule4 = ctrl.Rule(fwi['very low'] & ndvi['very low'] & settlement_dist['high'], (fire_risk['very low'], fire_spread_rate['very low']))
rule5 = ctrl.Rule(fwi['very low'] & ndvi['very low'] & settlement_dist['very high'], (fire_risk['very low'], fire_spread_rate['very low']))

rule6 = ctrl.Rule(fwi['very low'] & ndvi['low'] & settlement_dist['very low'], (fire_risk['very low'], fire_spread_rate['very low']))
rule7 = ctrl.Rule(fwi['very low'] & ndvi['low'] & settlement_dist['low'], (fire_risk['very low'], fire_spread_rate['very low']))
rule8 = ctrl.Rule(fwi['very low'] & ndvi['low'] & settlement_dist['moderate'], (fire_risk['very low'], fire_spread_rate['very low']))
rule9 = ctrl.Rule(fwi['very low'] & ndvi['low'] & settlement_dist['high'], (fire_risk['very low'], fire_spread_rate['very low']))
rule10 = ctrl.Rule(fwi['very low'] & ndvi['low'] & settlement_dist['very high'], (fire_risk['very low'], fire_spread_rate['very low']))

rule11 = ctrl.Rule(fwi['very low'] & ndvi['moderate'] & settlement_dist['very low'], (fire_risk['very low'], fire_spread_rate['very low']))
rule12 = ctrl.Rule(fwi['very low'] & ndvi['moderate'] & settlement_dist['low'], (fire_risk['very low'], fire_spread_rate['very low']))
rule13 = ctrl.Rule(fwi['very low'] & ndvi['moderate'] & settlement_dist['moderate'], (fire_risk['very low'], fire_spread_rate['very low']))
rule14 = ctrl.Rule(fwi['very low'] & ndvi['moderate'] & settlement_dist['high'], (fire_risk['very low'], fire_spread_rate['very low']))
rule15 = ctrl.Rule(fwi['very low'] & ndvi['moderate'] & settlement_dist['very high'], (fire_risk['very low'], fire_spread_rate['very low']))

rule16 = ctrl.Rule(fwi['very low'] & ndvi['high'] & settlement_dist['very low'], (fire_risk['very low'], fire_spread_rate['low']))
rule17 = ctrl.Rule(fwi['very low'] & ndvi['high'] & settlement_dist['low'], (fire_risk['very low'], fire_spread_rate['low']))
rule18 = ctrl.Rule(fwi['very low'] & ndvi['high'] & settlement_dist['moderate'], (fire_risk['very low'], fire_spread_rate['low']))
rule19 = ctrl.Rule(fwi['very low'] & ndvi['high'] & settlement_dist['high'], (fire_risk['very low'], fire_spread_rate['low']))
rule20 = ctrl.Rule(fwi['very low'] & ndvi['high'] & settlement_dist['very high'], (fire_risk['very low'], fire_spread_rate['low']))

rule21 = ctrl.Rule(fwi['very low'] & ndvi['very high'] & settlement_dist['very low'], (fire_risk['very low'], fire_spread_rate['low']))
rule22 = ctrl.Rule(fwi['very low'] & ndvi['very high'] & settlement_dist['low'], (fire_risk['very low'], fire_spread_rate['low']))
rule23 = ctrl.Rule(fwi['very low'] & ndvi['very high'] & settlement_dist['moderate'], (fire_risk['very low'], fire_spread_rate['low']))
rule24 = ctrl.Rule(fwi['very low'] & ndvi['very high'] & settlement_dist['high'], (fire_risk['very low'], fire_spread_rate['low']))
rule25 = ctrl.Rule(fwi['very low'] & ndvi['very high'] & settlement_dist['very high'], (fire_risk['very low'], fire_spread_rate['low']))

rule26 = ctrl.Rule(fwi['low'] & ndvi['very low'] & settlement_dist['very low'], (fire_risk['low'], fire_spread_rate['very low']))
rule27 = ctrl.Rule(fwi['low'] & ndvi['very low'] & settlement_dist['low'], (fire_risk['very low'], fire_spread_rate['very low']))
rule28 = ctrl.Rule(fwi['low'] & ndvi['very low'] & settlement_dist['moderate'], (fire_risk['very low'], fire_spread_rate['very low']))
rule29 = ctrl.Rule(fwi['low'] & ndvi['very low'] & settlement_dist['high'], (fire_risk['very low'], fire_spread_rate['very low']))
rule30 = ctrl.Rule(fwi['low'] & ndvi['very low'] & settlement_dist['very high'], (fire_risk['very low'], fire_spread_rate['very low']))

rule31 = ctrl.Rule(fwi['low'] & ndvi['low'] & settlement_dist['very low'], (fire_risk['low'], fire_spread_rate['very low']))
rule32 = ctrl.Rule(fwi['low'] & ndvi['low'] & settlement_dist['low'], (fire_risk['very low'], fire_spread_rate['very low']))
rule33 = ctrl.Rule(fwi['low'] & ndvi['low'] & settlement_dist['moderate'], (fire_risk['very low'], fire_spread_rate['very low']))
rule34 = ctrl.Rule(fwi['low'] & ndvi['low'] & settlement_dist['high'], (fire_risk['very low'], fire_spread_rate['very low']))
rule35 = ctrl.Rule(fwi['low'] & ndvi['low'] & settlement_dist['very high'], (fire_risk['very low'], fire_spread_rate['very low']))

rule36 = ctrl.Rule(fwi['low'] & ndvi['moderate'] & settlement_dist['very low'], (fire_risk['low'], fire_spread_rate['low']))
rule37 = ctrl.Rule(fwi['low'] & ndvi['moderate'] & settlement_dist['low'], (fire_risk['very low'], fire_spread_rate['low']))
rule38 = ctrl.Rule(fwi['low'] & ndvi['moderate'] & settlement_dist['moderate'], (fire_risk['very low'], fire_spread_rate['low']))
rule39 = ctrl.Rule(fwi['low'] & ndvi['moderate'] & settlement_dist['high'], (fire_risk['very low'], fire_spread_rate['low']))
rule40 = ctrl.Rule(fwi['low'] & ndvi['moderate'] & settlement_dist['very high'], (fire_risk['very low'], fire_spread_rate['low']))

rule41 = ctrl.Rule(fwi['low'] & ndvi['high'] & settlement_dist['very low'], (fire_risk['low'], fire_spread_rate['low']))
rule42 = ctrl.Rule(fwi['low'] & ndvi['high'] & settlement_dist['low'], (fire_risk['very low'], fire_spread_rate['low']))
rule43 = ctrl.Rule(fwi['low'] & ndvi['high'] & settlement_dist['moderate'], (fire_risk['very low'], fire_spread_rate['low']))
rule44 = ctrl.Rule(fwi['low'] & ndvi['high'] & settlement_dist['high'], (fire_risk['very low'], fire_spread_rate['low']))
rule45 = ctrl.Rule(fwi['low'] & ndvi['high'] & settlement_dist['very high'], (fire_risk['very low'], fire_spread_rate['low']))

rule46 = ctrl.Rule(fwi['low'] & ndvi['very high'] & settlement_dist['very low'], (fire_risk['low'], fire_spread_rate['moderate']))
rule47 = ctrl.Rule(fwi['low'] & ndvi['very high'] & settlement_dist['low'], (fire_risk['very low'], fire_spread_rate['moderate']))
rule48 = ctrl.Rule(fwi['low'] & ndvi['very high'] & settlement_dist['moderate'], (fire_risk['very low'], fire_spread_rate['moderate']))
rule49 = ctrl.Rule(fwi['low'] & ndvi['very high'] & settlement_dist['high'], (fire_risk['very low'], fire_spread_rate['moderate']))
rule50 = ctrl.Rule(fwi['low'] & ndvi['very high'] & settlement_dist['very high'], (fire_risk['very low'], fire_spread_rate['moderate']))

rule51 = ctrl.Rule(fwi['moderate'] & ndvi['very low'] & settlement_dist['very low'], (fire_risk['low'], fire_spread_rate['low']))
rule52 = ctrl.Rule(fwi['moderate'] & ndvi['very low'] & settlement_dist['low'], (fire_risk['low'], fire_spread_rate['low']))
rule53 = ctrl.Rule(fwi['moderate'] & ndvi['very low'] & settlement_dist['moderate'], (fire_risk['very low'], fire_spread_rate['low']))
rule54 = ctrl.Rule(fwi['moderate'] & ndvi['very low'] & settlement_dist['high'], (fire_risk['very low'], fire_spread_rate['low']))
rule55 = ctrl.Rule(fwi['moderate'] & ndvi['very low'] & settlement_dist['very high'], (fire_risk['very low'], fire_spread_rate['low']))

rule56 = ctrl.Rule(fwi['moderate'] & ndvi['low'] & settlement_dist['very low'], (fire_risk['low'], fire_spread_rate['low']))
rule57 = ctrl.Rule(fwi['moderate'] & ndvi['low'] & settlement_dist['low'], (fire_risk['low'], fire_spread_rate['low']))
rule58 = ctrl.Rule(fwi['moderate'] & ndvi['low'] & settlement_dist['moderate'], (fire_risk['low'], fire_spread_rate['low']))
rule59 = ctrl.Rule(fwi['moderate'] & ndvi['low'] & settlement_dist['high'], (fire_risk['very low'], fire_spread_rate['low']))
rule60 = ctrl.Rule(fwi['moderate'] & ndvi['low'] & settlement_dist['very high'], (fire_risk['very low'], fire_spread_rate['low']))

rule61 = ctrl.Rule(fwi['moderate'] & ndvi['moderate'] & settlement_dist['very low'], (fire_risk['moderate'], fire_spread_rate['moderate']))
rule62 = ctrl.Rule(fwi['moderate'] & ndvi['moderate'] & settlement_dist['low'], (fire_risk['low'], fire_spread_rate['moderate']))
rule63 = ctrl.Rule(fwi['moderate'] & ndvi['moderate'] & settlement_dist['moderate'], (fire_risk['low'], fire_spread_rate['moderate']))
rule64 = ctrl.Rule(fwi['moderate'] & ndvi['moderate'] & settlement_dist['high'], (fire_risk['low'], fire_spread_rate['moderate']))
rule65 = ctrl.Rule(fwi['moderate'] & ndvi['moderate'] & settlement_dist['very high'], (fire_risk['very low'], fire_spread_rate['moderate']))

rule66 = ctrl.Rule(fwi['moderate'] & ndvi['high'] & settlement_dist['very low'], (fire_risk['moderate'], fire_spread_rate['high']))
rule67 = ctrl.Rule(fwi['moderate'] & ndvi['high'] & settlement_dist['low'], (fire_risk['moderate'], fire_spread_rate['high']))
rule68 = ctrl.Rule(fwi['moderate'] & ndvi['high'] & settlement_dist['moderate'], (fire_risk['low'], fire_spread_rate['high']))
rule69 = ctrl.Rule(fwi['moderate'] & ndvi['high'] & settlement_dist['high'], (fire_risk['low'], fire_spread_rate['high']))
rule70 = ctrl.Rule(fwi['moderate'] & ndvi['high'] & settlement_dist['very high'], (fire_risk['low'], fire_spread_rate['high']))

rule71 = ctrl.Rule(fwi['moderate'] & ndvi['very high'] & settlement_dist['very low'], (fire_risk['moderate'], fire_spread_rate['high']))
rule72 = ctrl.Rule(fwi['moderate'] & ndvi['very high'] & settlement_dist['low'], (fire_risk['moderate'], fire_spread_rate['high']))
rule73 = ctrl.Rule(fwi['moderate'] & ndvi['very high'] & settlement_dist['moderate'], (fire_risk['moderate'], fire_spread_rate['high']))
rule74 = ctrl.Rule(fwi['moderate'] & ndvi['very high'] & settlement_dist['high'], (fire_risk['low'], fire_spread_rate['high']))
rule75 = ctrl.Rule(fwi['moderate'] & ndvi['very high'] & settlement_dist['very high'], (fire_risk['low'], fire_spread_rate['high']))

rule76 = ctrl.Rule(fwi['high'] & ndvi['very low'] & settlement_dist['very low'], (fire_risk['moderate'], fire_spread_rate['moderate']))
rule77 = ctrl.Rule(fwi['high'] & ndvi['very low'] & settlement_dist['low'], (fire_risk['moderate'], fire_spread_rate['moderate']))
rule78 = ctrl.Rule(fwi['high'] & ndvi['very low'] & settlement_dist['moderate'], (fire_risk['low'], fire_spread_rate['moderate']))
rule79 = ctrl.Rule(fwi['high'] & ndvi['very low'] & settlement_dist['high'], (fire_risk['low'], fire_spread_rate['moderate']))
rule80 = ctrl.Rule(fwi['high'] & ndvi['very low'] & settlement_dist['very high'], (fire_risk['low'], fire_spread_rate['moderate']))

rule81 = ctrl.Rule(fwi['high'] & ndvi['low'] & settlement_dist['very low'], (fire_risk['moderate'], fire_spread_rate['moderate']))
rule82 = ctrl.Rule(fwi['high'] & ndvi['low'] & settlement_dist['low'], (fire_risk['moderate'], fire_spread_rate['moderate']))
rule83 = ctrl.Rule(fwi['high'] & ndvi['low'] & settlement_dist['moderate'], (fire_risk['moderate'], fire_spread_rate['moderate']))
rule84 = ctrl.Rule(fwi['high'] & ndvi['low'] & settlement_dist['high'], (fire_risk['low'], fire_spread_rate['moderate']))
rule85 = ctrl.Rule(fwi['high'] & ndvi['low'] & settlement_dist['very high'], (fire_risk['low'], fire_spread_rate['moderate']))

rule86 = ctrl.Rule(fwi['high'] & ndvi['moderate'] & settlement_dist['very low'], (fire_risk['high'], fire_spread_rate['high']))
rule87 = ctrl.Rule(fwi['high'] & ndvi['moderate'] & settlement_dist['low'], (fire_risk['moderate'], fire_spread_rate['high']))
rule88 = ctrl.Rule(fwi['high'] & ndvi['moderate'] & settlement_dist['moderate'], (fire_risk['moderate'], fire_spread_rate['high']))
rule89 = ctrl.Rule(fwi['high'] & ndvi['moderate'] & settlement_dist['high'], (fire_risk['moderate'], fire_spread_rate['high']))
rule90 = ctrl.Rule(fwi['high'] & ndvi['moderate'] & settlement_dist['very high'], (fire_risk['low'], fire_spread_rate['high']))

rule91 = ctrl.Rule(fwi['high'] & ndvi['high'] & settlement_dist['very low'], (fire_risk['high'], fire_spread_rate['very high']))
rule92 = ctrl.Rule(fwi['high'] & ndvi['high'] & settlement_dist['low'], (fire_risk['high'], fire_spread_rate['very high']))
rule93 = ctrl.Rule(fwi['high'] & ndvi['high'] & settlement_dist['moderate'], (fire_risk['moderate'], fire_spread_rate['very high']))
rule94 = ctrl.Rule(fwi['high'] & ndvi['high'] & settlement_dist['high'], (fire_risk['moderate'], fire_spread_rate['very high']))
rule95 = ctrl.Rule(fwi['high'] & ndvi['high'] & settlement_dist['very high'], (fire_risk['moderate'], fire_spread_rate['very high']))

rule96 = ctrl.Rule(fwi['high'] & ndvi['very high'] & settlement_dist['very low'], (fire_risk['high'], fire_spread_rate['very high']))
rule97 = ctrl.Rule(fwi['high'] & ndvi['very high'] & settlement_dist['low'], (fire_risk['high'], fire_spread_rate['very high']))
rule98 = ctrl.Rule(fwi['high'] & ndvi['very high'] & settlement_dist['moderate'], (fire_risk['high'], fire_spread_rate['very high']))
rule99 = ctrl.Rule(fwi['high'] & ndvi['very high'] & settlement_dist['high'], (fire_risk['moderate'], fire_spread_rate['very high']))
rule100 = ctrl.Rule(fwi['high'] & ndvi['very high'] & settlement_dist['very high'], (fire_risk['moderate'], fire_spread_rate['very high']))

rule101 = ctrl.Rule(fwi['very high'] & ndvi['very low'] & settlement_dist['very low'], (fire_risk['high'], fire_spread_rate['high']))
rule102 = ctrl.Rule(fwi['very high'] & ndvi['very low'] & settlement_dist['low'], (fire_risk['high'], fire_spread_rate['high']))
rule103 = ctrl.Rule(fwi['very high'] & ndvi['very low'] & settlement_dist['moderate'], (fire_risk['high'], fire_spread_rate['high']))
rule104 = ctrl.Rule(fwi['very high'] & ndvi['very low'] & settlement_dist['high'], (fire_risk['high'], fire_spread_rate['high']))
rule105 = ctrl.Rule(fwi['very high'] & ndvi['very low'] & settlement_dist['very high'], (fire_risk['moderate'], fire_spread_rate['high']))

rule106 = ctrl.Rule(fwi['very high'] & ndvi['low'] & settlement_dist['very low'], (fire_risk['high'], fire_spread_rate['very high']))
rule107 = ctrl.Rule(fwi['very high'] & ndvi['low'] & settlement_dist['low'], (fire_risk['high'], fire_spread_rate['very high']))
rule108 = ctrl.Rule(fwi['very high'] & ndvi['low'] & settlement_dist['moderate'], (fire_risk['high'], fire_spread_rate['very high']))
rule109 = ctrl.Rule(fwi['very high'] & ndvi['low'] & settlement_dist['high'], (fire_risk['high'], fire_spread_rate['very high']))
rule110 = ctrl.Rule(fwi['very high'] & ndvi['low'] & settlement_dist['very high'], (fire_risk['moderate'], fire_spread_rate['very high']))

rule111 = ctrl.Rule(fwi['very high'] & ndvi['moderate'] & settlement_dist['very low'], (fire_risk['high'], fire_spread_rate['very high']))
rule112 = ctrl.Rule(fwi['very high'] & ndvi['moderate'] & settlement_dist['low'], (fire_risk['high'], fire_spread_rate['very high']))
rule113 = ctrl.Rule(fwi['very high'] & ndvi['moderate'] & settlement_dist['moderate'], (fire_risk['high'], fire_spread_rate['very high']))
rule114 = ctrl.Rule(fwi['very high'] & ndvi['moderate'] & settlement_dist['high'], (fire_risk['high'], fire_spread_rate['very high']))
rule115 = ctrl.Rule(fwi['very high'] & ndvi['moderate'] & settlement_dist['very high'], (fire_risk['moderate'], fire_spread_rate['very high']))

rule116 = ctrl.Rule(fwi['very high'] & ndvi['high'] & settlement_dist['very low'], (fire_risk['high'], fire_spread_rate['extremely high']))
rule117 = ctrl.Rule(fwi['very high'] & ndvi['high'] & settlement_dist['low'], (fire_risk['high'], fire_spread_rate['extremely high']))
rule118 = ctrl.Rule(fwi['very high'] & ndvi['high'] & settlement_dist['moderate'], (fire_risk['high'], fire_spread_rate['extremely high']))
rule119 = ctrl.Rule(fwi['very high'] & ndvi['high'] & settlement_dist['high'], (fire_risk['high'], fire_spread_rate['extremely high']))
rule120 = ctrl.Rule(fwi['very high'] & ndvi['high'] & settlement_dist['very high'], (fire_risk['moderate'], fire_spread_rate['extremely high']))

rule121 = ctrl.Rule(fwi['very high'] & ndvi['very high'] & settlement_dist['very low'], (fire_risk['high'], fire_spread_rate['extremely high']))
rule122 = ctrl.Rule(fwi['very high'] & ndvi['very high'] & settlement_dist['low'], (fire_risk['high'], fire_spread_rate['extremely high']))
rule123 = ctrl.Rule(fwi['very high'] & ndvi['very high'] & settlement_dist['moderate'], (fire_risk['high'], fire_spread_rate['extremely high']))
rule124 = ctrl.Rule(fwi['very high'] & ndvi['very high'] & settlement_dist['high'], (fire_risk['high'], fire_spread_rate['extremely high']))
rule125 = ctrl.Rule(fwi['very high'] & ndvi['very high'] & settlement_dist['very high'], (fire_risk['moderate'], fire_spread_rate['extremely high']))

# Duplicate rules for validation purposes
rule126 = ctrl.Rule(fwi['extremely high'] & ndvi['very low'] & settlement_dist['very low'], (fire_risk['high'], fire_spread_rate['very high']))
rule127 = ctrl.Rule(fwi['extremely high'] & ndvi['very low'] & settlement_dist['low'], (fire_risk['high'], fire_spread_rate['very high']))
rule128 = ctrl.Rule(fwi['extremely high'] & ndvi['very low'] & settlement_dist['moderate'], (fire_risk['high'], fire_spread_rate['very high']))
rule129 = ctrl.Rule(fwi['extremely high'] & ndvi['very low'] & settlement_dist['high'], (fire_risk['high'], fire_spread_rate['very high']))
rule130 = ctrl.Rule(fwi['extremely high'] & ndvi['very low'] & settlement_dist['very high'], (fire_risk['high'], fire_spread_rate['very high']))

rule131 = ctrl.Rule(fwi['extremely high'] & ndvi['low'] & settlement_dist['very low'], (fire_risk['high'], fire_spread_rate['very high']))
rule132 = ctrl.Rule(fwi['extremely high'] & ndvi['low'] & settlement_dist['low'], (fire_risk['high'], fire_spread_rate['very high']))
rule133 = ctrl.Rule(fwi['extremely high'] & ndvi['low'] & settlement_dist['moderate'], (fire_risk['high'], fire_spread_rate['very high']))
rule134 = ctrl.Rule(fwi['extremely high'] & ndvi['low'] & settlement_dist['high'], (fire_risk['high'], fire_spread_rate['very high']))
rule135 = ctrl.Rule(fwi['extremely high'] & ndvi['low'] & settlement_dist['very high'], (fire_risk['high'], fire_spread_rate['very high']))

rule136 = ctrl.Rule(fwi['extremely high'] & ndvi['moderate'] & settlement_dist['very low'], (fire_risk['high'], fire_spread_rate['extremely high']))
rule137 = ctrl.Rule(fwi['extremely high'] & ndvi['moderate'] & settlement_dist['low'], (fire_risk['high'], fire_spread_rate['extremely high']))
rule138 = ctrl.Rule(fwi['extremely high'] & ndvi['moderate'] & settlement_dist['moderate'], (fire_risk['high'], fire_spread_rate['extremely high']))
rule139 = ctrl.Rule(fwi['extremely high'] & ndvi['moderate'] & settlement_dist['high'], (fire_risk['high'], fire_spread_rate['extremely high']))
rule140 = ctrl.Rule(fwi['extremely high'] & ndvi['moderate'] & settlement_dist['very high'], (fire_risk['high'], fire_spread_rate['extremely high']))

rule141 = ctrl.Rule(fwi['extremely high'] & ndvi['high'] & settlement_dist['very low'], (fire_risk['high'], fire_spread_rate['extremely high']))
rule142 = ctrl.Rule(fwi['extremely high'] & ndvi['high'] & settlement_dist['low'], (fire_risk['high'], fire_spread_rate['extremely high']))
rule143 = ctrl.Rule(fwi['extremely high'] & ndvi['high'] & settlement_dist['moderate'], (fire_risk['high'], fire_spread_rate['extremely high']))
rule144 = ctrl.Rule(fwi['extremely high'] & ndvi['high'] & settlement_dist['high'], (fire_risk['high'], fire_spread_rate['extremely high']))
rule145 = ctrl.Rule(fwi['extremely high'] & ndvi['high'] & settlement_dist['very high'], (fire_risk['high'], fire_spread_rate['extremely high']))

rule146 = ctrl.Rule(fwi['extremely high'] & ndvi['very high'] & settlement_dist['very low'], (fire_risk['high'], fire_spread_rate['extremely high']))
rule147 = ctrl.Rule(fwi['extremely high'] & ndvi['very high'] & settlement_dist['low'], (fire_risk['high'], fire_spread_rate['extremely high']))
rule148 = ctrl.Rule(fwi['extremely high'] & ndvi['very high'] & settlement_dist['moderate'], (fire_risk['high'], fire_spread_rate['extremely high']))
rule149 = ctrl.Rule(fwi['extremely high'] & ndvi['very high'] & settlement_dist['high'], (fire_risk['high'], fire_spread_rate['extremely high']))
rule150 = ctrl.Rule(fwi['extremely high'] & ndvi['very high'] & settlement_dist['very high'], (fire_risk['high'], fire_spread_rate['extremely high']))

rules = []

for i in range(1, 151):
    rules.append(eval(f'rule{i}'))


#Construct the fuzzy control system
forest_fire_ctrl = ctrl.ControlSystem(rules=rules)
forest_fire = ctrl.ControlSystemSimulation(control_system=forest_fire_ctrl)

#GUI
# Set up Tkinter window
window = Tk()
window.geometry("850x800")
window.title("Forest Fire Forecast")
window.configure(bg="#2A2F4F")

# To keep track of the canvas for the gauge chart
gauge_chart_canvas = None
gauge_chart_rate_canvas = None

# Title Label
title_label = Label(window, text="Forest Fire Forecast", font=("Inter Bold", 30), fg="white", bg="#2A2F4F")
title_label.pack(pady=20)

# Input Frame for organizing all input fields
input_frame = Frame(window, bg="#2A2F4F")
input_frame.pack(pady=20)

Label(input_frame, text="Temperature:", font=('Arial', 12), fg='white', bg="#2A2F4F").grid(row=0, column=0, sticky="w", padx=10, pady=5)
temp_entry = Entry(input_frame, font=('Arial', 14))
temp_entry.grid(row=1, column=0, padx=10, pady=5)

Label(input_frame, text="Precipitation (mm):", font=('Arial', 12), fg='white', bg="#2A2F4F").grid(row=2, column=0, sticky="w", padx=10, pady=5)
prcp_entry = Entry(input_frame, font=('Arial', 14))
prcp_entry.grid(row=3, column=0, padx=10, pady=5)

Label(input_frame, text="Distance of Settlement:", font=('Arial', 12), fg='white', bg="#2A2F4F").grid(row=4, column=0, sticky="w", padx=10, pady=5)
settlement_entry = Entry(input_frame, font=('Arial', 14))
settlement_entry.grid(row=5, column=0, padx=10, pady=5)

Label(input_frame, text="Humidity (%):", font=('Arial', 12), fg='white', bg="#2A2F4F").grid(row=0, column=1, sticky="w", padx=10, pady=5)
rhum_entry = Entry(input_frame, font=('Arial', 14))
rhum_entry.grid(row=1, column=1, padx=10, pady=5)

Label(input_frame, text="Wind Speed (km/h):", font=('Arial', 12), fg='white', bg="#2A2F4F").grid(row=2, column=1, sticky="w", padx=10, pady=5)
wind_entry = Entry(input_frame, font=('Arial', 14))
wind_entry.grid(row=3, column=1, padx=10, pady=5)

Label(input_frame, text="NDVI:", font=('Arial', 12), fg='white', bg="#2A2F4F").grid(row=4, column=1, sticky="w", padx=10, pady=5)
ndvi_entry = Entry(input_frame, font=('Arial', 14))
ndvi_entry.grid(row=5, column=1, padx=10, pady=5)

# Function to compute and display fire risk
def compute_fire_risk():
    try:
        # Get input values from user
        temp = float(temp_entry.get())
        rhum = float(rhum_entry.get())
        wind = float(wind_entry.get())
        prcp = float(prcp_entry.get())
        ndvi_value = float(ndvi_entry.get())
        settlement_dist_value = float(settlement_entry.get())
        
        
        # Check if inputs are within acceptable ranges
        if not (-30 <= temp <= 50):
            messagebox.showwarning("Input Error", "Temperature must be between -30 and 50 °C.")
            return
        if not (0 <= rhum <= 100):
            messagebox.showwarning("Input Error", "Humidity must be between 0 and 100%.")
            return
        if not (0 <= wind <= 150):
            messagebox.showwarning("Input Error", "Wind Speed must be between 0 and 150 km/h.")
            return
        if not (0 <= prcp <= 500):
            messagebox.showwarning("Input Error", "Precipitation must be between 0 and 500 mm.")
            return
        if not (0 <= ndvi_value <= 1):
            messagebox.showwarning("Input Error", "NDVI must be between 0 and 1.")
            return
        if not (0 <= settlement_dist_value <= 10000):
            messagebox.showwarning("Input Error", "Distance of Settlement must be between 0 and 100 km.")
            return
        
        fwi_values = FWI_Calculator.calculate_fwi(temp, rhum, wind, prcp)
        fwi = fwi_values['fwi']
        
        # Set inputs to the fuzzy system (these lines assume you have a working fuzzy system called forest_fire)
        forest_fire.input['fwi'] = fwi
        forest_fire.input['ndvi'] = ndvi_value
        forest_fire.input['distance of settlement'] = settlement_dist_value

        # Perform computation
        forest_fire.compute()

        # Obtain outputs
        risk_output = forest_fire.output['risk of fire']
        spread_rate_output = forest_fire.output['rate of fire spread']

        #Draw gauge charts with updated values
        draw_gauge_chart(risk_output)
        draw_gauge_chart_rate(spread_rate_output)
        #risk_label.config(text=f"Risk of Fire: {risk_output:.2f}")
        #spread_label.config(text=f"Rate of Fire Spread: {spread_rate_output:.2f}")
        risk_label.config(text=f"Risk of Fire: {risk_output:.2f}")
        spread_label.config(text=f"Rate of Fire Spread: {spread_rate_output:.2f}")
        risk_label.grid()  # Show label after computation
        spread_label.grid()  # Show label after computation
        
    except ValueError:
        print("Please enter valid numerical values.")

# Button to run the computation
compute_button = Button(window, text="Compute", command=compute_fire_risk, padx=10, pady=5)
compute_button.pack(pady=10)

# Output Frame to display computed results
output_frame = Frame(window, bg="#2A2F4F")
output_frame.pack(pady=10)
output_frame = Frame(window, bg="#2A2F4F")
output_frame.pack(pady=10)

# Labels to show computed output (initially hidden)
risk_label = Label(output_frame, text="", font=('Arial', 14), fg="white", bg="#2A2F4F")
spread_label = Label(output_frame, text="", font=('Arial', 14), fg="white", bg="#2A2F4F")
'''
# Labels to show computed output
risk_label = Label(output_frame, text="Risk of Fire: ", font=('Arial', 14), fg="white", bg="#2A2F4F")
risk_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

spread_label = Label(output_frame, text="Rate of Fire Spread: ", font=('Arial', 14), fg="white", bg="#2A2F4F")
spread_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
'''
# Main container for charts
charts_frame = Frame(window, bg="#2A2F4F")
charts_frame.pack(pady=20)

# Separate frames for each chart
risk_chart_frame = Frame(charts_frame)
risk_chart_frame.pack(side=LEFT, padx=20)

spread_chart_frame = Frame(charts_frame)
spread_chart_frame.pack(side=RIGHT, padx=20)

# Gauge chart functions
#https://coderzcolumn.com/tutorials/data-science/gauge-chart-using-matplotlib
def draw_gauge_chart(risk_value):
    global gauge_chart_canvas
    #Clear any previous chart if it exists
    if gauge_chart_canvas:
        gauge_chart_canvas.get_tk_widget().destroy()

    fig = plt.figure(figsize=(5, 4))
    fig.subplots_adjust(top=1, bottom=0, left=0, right=1)
    ax = fig.add_subplot(projection="polar")
    max_theta = 180
    ax.set_thetamax(max_theta)

    #Define colors, values, and x-axis positions for four ranges
    colors = ['#4dab6d', "#c1da64", "#fabd57", "#ee4d55"]
    values = [0, 33.33, 66.66, 100]
    x_axis_vals = [0, 0.8, 1.6, 2.4]

    # Create four bars for each performance range
    ax.bar(x=x_axis_vals, width=0.8, height=0.5, bottom=2,
           linewidth=0, edgecolor="white", color=colors, align="edge")

    #Add labels for each of the four ranges
    plt.annotate("Very Low", xy=(0.22, 2.0), rotation=-75, color="white", fontweight="bold")
    plt.annotate("Low", xy=(1.3, 2.1), rotation=-20, color="white", fontweight="bold")
    plt.annotate("Moderate", xy=(2.2, 2.2), rotation=30, color="white", fontweight="bold")
    plt.annotate("High", xy=(2.90, 2.25), rotation=75, color="white", fontweight="bold")

    for loc, val in zip(x_axis_vals, values):
        plt.annotate(val, xy=(loc, 2.5), ha="right" if val >= 60 else "left")

    plt.annotate(round(risk_value), xytext=(0, 0), xy=(1.1, 2.0),
                 arrowprops=dict(arrowstyle="wedge, tail_width=0.5", color="black", shrinkA=0),
                 bbox=dict(boxstyle="circle", facecolor="black", linewidth=2.0),
                 fontsize=15, color="white", ha="center")
    

    plt.title("Risk of Fire", loc="center", pad=20, fontsize=20, fontweight="bold")
    ax.set_axis_off()
    
    gauge_chart_canvas = FigureCanvasTkAgg(fig, master=risk_chart_frame)
    gauge_chart_canvas.draw()
    gauge_chart_canvas.get_tk_widget().pack()



def draw_gauge_chart_rate(rate_value):
    global gauge_chart_rate_canvas  
    
    #Clear any previous chart if it exists
    if gauge_chart_rate_canvas:
        gauge_chart_rate_canvas.get_tk_widget().destroy()

    fig = plt.figure(figsize=(5, 4))
    fig.subplots_adjust(top=1, bottom=0, left=0, right=1)
    ax = fig.add_subplot(projection="polar")
    max_theta = 180
    ax.set_thetamax(max_theta)

    #Define colors, values, and x-axis positions for six ranges
    colors = ['#4dab6d', "#c1da64", "#f6ee54", "#fabd57", "#f36d54", "#ee4d55"]
    values = [0, 40, 110, 600, 1000, 3000, 5000]
    x_axis_vals = [0, 0.53, 1.06, 1.59, 2.12, 2.65]

    ax.bar(x=x_axis_vals, width=0.67, height=0.5, bottom=2,
           linewidth=0, edgecolor="white", color=colors, align="edge")

    plt.annotate("Very Low", xy=(0.16, 2.0), rotation=-75, color="white", fontweight="bold", fontsize=8)
    plt.annotate("Low", xy=(0.80, 2.05), rotation=-45, color="white", fontweight="bold", fontsize=8)
    plt.annotate("Moderate", xy=(1.45, 2.1), rotation=-20, color="white", fontweight="bold", fontsize=8)
    plt.annotate("High", xy=(1.95, 2.2), rotation=10, color="white", fontweight="bold", fontsize=8)
    plt.annotate("Very High", xy=(2.55, 2.25), rotation=45, color="white", fontweight="bold", fontsize=8)
    plt.annotate("Extremely High", xy=(3.1, 2.25), rotation=80, color="white", fontweight="bold", fontsize=6)


    for loc, val in zip(x_axis_vals, values):
        plt.annotate(val, xy=(loc, 2.5), ha="right" if val >= 500 else "left")

    plt.annotate(round(rate_value), xytext=(0, 0), xy=(1.1, 2.0),
                 arrowprops=dict(arrowstyle="wedge, tail_width=0.5", color="black", shrinkA=0),
                 bbox=dict(boxstyle="circle", facecolor="black", linewidth=2.0),
                 fontsize=15, color="white", ha="center")

    plt.title("Rate of Fire Spread", loc="center", pad=20, fontsize=20, fontweight="bold")
    ax.set_axis_off()
    
    gauge_chart_rate_canvas = FigureCanvasTkAgg(fig, master=spread_chart_frame)
    gauge_chart_rate_canvas.draw()
    gauge_chart_rate_canvas.get_tk_widget().pack()
    
window.mainloop() #close window


fire_risk.view(sim=forest_fire)
fire_spread_rate.view(sim=forest_fire)


x1, y1 = np.meshgrid(np.linspace(fwi.universe.min(), fwi.universe.max(), 50),
                   np.linspace(ndvi.universe.min(), ndvi.universe.max(), 50))
z1_fire_risk = np.zeros_like(x1, dtype=float)
z1_fire_spread_rate = np.zeros_like(x1, dtype=float)

for i,r in enumerate(x1):
  for j,c in enumerate(r):
    forest_fire.input['fwi'] = x1[i,j]
    forest_fire.input['ndvi'] = y1[i,j]
    try:
      forest_fire.compute()
    except:
      z1_fire_risk[i,j] = float('inf')
      z1_fire_spread_rate[i,j] = float('inf')
    z1_fire_risk[i,j] = forest_fire.output['risk of fire']
    z1_fire_spread_rate[i,j] = forest_fire.output['rate of fire spread']
    
x2, y2 = np.meshgrid(np.linspace(fwi.universe.min(), fwi.universe.max(), 50),
                   np.linspace(settlement_dist.universe.min(), settlement_dist.universe.max(), 50))
z2_fire_risk = np.zeros_like(x2, dtype=float)
z2_fire_spread_rate = np.zeros_like(x2, dtype=float)

for i,r in enumerate(x2):
  for j,c in enumerate(r):
    forest_fire.input['fwi'] = x2[i,j]
    forest_fire.input['distance of settlement'] = y2[i,j]
    try:
      forest_fire.compute()
    except:
      z2_fire_risk[i,j] = float('inf')
      z2_fire_spread_rate[i,j] = float('inf')
    z2_fire_risk[i,j] = forest_fire.output['risk of fire']
    z2_fire_spread_rate[i,j] = forest_fire.output['rate of fire spread']
    
x3, y3 = np.meshgrid(np.linspace(settlement_dist.universe.min(), settlement_dist.universe.max(), 50),
                   np.linspace(ndvi.universe.min(), ndvi.universe.max(), 50))
z3_fire_risk = np.zeros_like(x3, dtype=float)
z3_fire_spread_rate = np.zeros_like(x3, dtype=float)

for i,r in enumerate(x3):
  for j,c in enumerate(r):
    forest_fire.input['distance of settlement'] = x3[i,j]
    forest_fire.input['ndvi'] = y3[i,j]
    try:
      forest_fire.compute()
    except:
      z3_fire_risk[i,j] = float('inf')
      z3_fire_spread_rate[i,j] = float('inf')
    z3_fire_risk[i,j] = forest_fire.output['risk of fire']
    z3_fire_spread_rate[i,j] = forest_fire.output['rate of fire spread']


def plot3d(x,y,z):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')

  ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis', linewidth=0.4, antialiased=True)

  
  """ax.contourf(x, y, z, zdir='z', offset=-2.5, cmap='viridis', alpha=0.5)
  ax.contourf(x, y, z, zdir='x', offset=x.max()*1.5, cmap='viridis', alpha=0.5)
  ax.contourf(x, y, z, zdir='y', offset=y.max()*1.5, cmap='viridis', alpha=0.5)"""

  ax.view_init(30, 200)

plot3d(x1, y1, z1_fire_risk)
plot3d(x1, y1, z1_fire_spread_rate)
plot3d(x2, y2, z2_fire_risk)
plot3d(x2, y2, z2_fire_spread_rate)
plot3d(x3, y3, z3_fire_risk)
plot3d(x3, y3, z3_fire_spread_rate)
