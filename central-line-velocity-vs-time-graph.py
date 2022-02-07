#Importing modules, packages, libraries, etc
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.interpolate import make_interp_spline
import numpy as np
import math


def plot_graph():
    plt.style.use('classic')
    # Data for x-axis = time and y-axis = centre-line velocity
    x_time = ['0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1.0']
    y_SICKLE = [
        calc_pressure_gradient_coronary(0.1,'SICKLE'),
        calc_pressure_gradient_coronary(0.2,'SICKLE'),
        calc_pressure_gradient_coronary(0.3,'SICKLE'),
        calc_pressure_gradient_coronary(0.4,'SICKLE'),
        calc_pressure_gradient_coronary(0.5,'SICKLE'),
        calc_pressure_gradient_coronary(0.6,'SICKLE'),
        calc_pressure_gradient_coronary(0.7,'SICKLE'),
        calc_pressure_gradient_coronary(0.8,'SICKLE'),
        calc_pressure_gradient_coronary(0.9,'SICKLE'),
        calc_pressure_gradient_coronary(1.0,'SICKLE'),
    ]
    y_PLASMA = [
        calc_pressure_gradient_coronary(0.1,'PLASMA'),
        calc_pressure_gradient_coronary(0.2,'PLASMA'),
        calc_pressure_gradient_coronary(0.3,'PLASMA'),
        calc_pressure_gradient_coronary(0.4,'PLASMA'),
        calc_pressure_gradient_coronary(0.5,'PLASMA'),
        calc_pressure_gradient_coronary(0.6,'PLASMA'),
        calc_pressure_gradient_coronary(0.7,'PLASMA'),
        calc_pressure_gradient_coronary(0.8,'PLASMA'),
        calc_pressure_gradient_coronary(0.9,'PLASMA'),
        calc_pressure_gradient_coronary(1.0,'PLASMA'),
    ]
    y_POLYCYTHEMIA = [
        calc_pressure_gradient_coronary(0.1,'POLYCYTHEMIA'),
        calc_pressure_gradient_coronary(0.2,'POLYCYTHEMIA'),
        calc_pressure_gradient_coronary(0.3,'POLYCYTHEMIA'),
        calc_pressure_gradient_coronary(0.4,'POLYCYTHEMIA'),
        calc_pressure_gradient_coronary(0.5,'POLYCYTHEMIA'),
        calc_pressure_gradient_coronary(0.6,'POLYCYTHEMIA'),
        calc_pressure_gradient_coronary(0.7,'POLYCYTHEMIA'),
        calc_pressure_gradient_coronary(0.8,'POLYCYTHEMIA'),
        calc_pressure_gradient_coronary(0.9,'POLYCYTHEMIA'),
        calc_pressure_gradient_coronary(1.0,'POLYCYTHEMIA'),
    ]
    y_NORMAL = [
        calc_pressure_gradient_coronary(0.1,'NORMAL'),
        calc_pressure_gradient_coronary(0.2,'NORMAL'),
        calc_pressure_gradient_coronary(0.3,'NORMAL'),
        calc_pressure_gradient_coronary(0.4,'NORMAL'),
        calc_pressure_gradient_coronary(0.5,'NORMAL'),
        calc_pressure_gradient_coronary(0.6,'NORMAL'),
        calc_pressure_gradient_coronary(0.7,'NORMAL'),
        calc_pressure_gradient_coronary(0.8,'NORMAL'),
        calc_pressure_gradient_coronary(0.9,'NORMAL'),
        calc_pressure_gradient_coronary(1.0,'NORMAL'),
    ]

    # Plotting lines and assigning a unique color
    plt.plot(y_SICKLE, color='green')
    plt.plot(y_PLASMA, color='red')
    plt.plot(y_POLYCYTHEMIA, color='orange')
    plt.plot(y_NORMAL, color='purple')

    plt.title("Centre-line Velocity VS Time graph")

    plt.xlabel('Time(s)')
    plt.ylabel('Centre-line Velocity')
    plt.xticks(np.arange(len(x_time)), x_time, rotation=90)

    # Adding legend for different Arteries
    green_patch = mpatches.Patch(color='green', label='SICKLE CELL')
    red_patch = mpatches.Patch(color='red', label='PLASMA CELL')
    orange_patch = mpatches.Patch(color='orange', label='POLYCYTHEMIA CELL')
    purple_patch = mpatches.Patch(color='purple', label='NORMAL BLOOD CELL')
    plt.legend(handles=[green_patch, red_patch, orange_patch, purple_patch])

    plt.grid(True)
    plt.gca().invert_yaxis()
    plt.show()

def calc_pressure_gradient_coronary(time, type):
    An_Femoral = ["285.7314","-129.0962","-228.4915","51.8916","231.5986","-257.8969","-83.1624","10.2941","9.8959","-8.0418","-0.0481","3.1985","1.1922","-1.8612","-0.3136","1.1593","2.7302","-3.0642","4.6452","2.9388","-6.5784","3.2710","8.8252","-4.2634","3.5135","6.1367","-4.1843","0.1013","4.4836","0.0197","0.1449","-1.5150","4.1805","2.1611","-5.3132","2.3175","7.7625","-6.5698","-1.2518","6.4584","-0.3714","-1.0762","0.1864","2.0003","2.2200","-2.9155","-0.5914","4.9380","-1.0953","-1.8957"]
    Bn_Femoral = ["31.6574", "379.8315", "-90.3741", "-92.9544", "102.6494", "165.5609", "-162.7442", "-1.8481", "7.1957", "6.8170", "-7.3512", "-7.3512", "3.4779", "0.5524", "0.3664", "-3.5030", "4.2242", "-2.9325", "-3.3349", "2.3709", "3.2721", "-11.0000", "4.4926", "0.4568", "-5.6891", "4.3685", "0.9790", "-3.1224", "0.7288", "1.0156", "0.2900", "0.2900", "-2.4227", "4.0966", "-0.3749", "-7.8178", "4.4732", "4.0971", "-7.4902", "-0.3660", "3.2635", "-0.8456", "-0.8431", "-1.3000", "2.7129", "1.2549", "-4.3481", "0.1853", "3.8484", "-2.0993"]
    An_Pulmonary = ["1322.1", "852.1", "-160.3", "-417.1", "-868", "-610.9", "-437.5", "-612.7", "-612.7", "-204.6",   "110.3", "-64.8", "207.8", "175", "140.7", "35.3", "-31.6", "141.9", "-48.1", "-2.4", "67.2", "-31.8", "4.1","-18.8", "-4.7", "-10.9", "-102.4", "28.1", "-7.8", "-22.7", "21.4", "15.6", "29", "-24.8", "22.6", "32.2", "-24.6", "22.6", "10.7", "8.6", "11.1", "-19.9", "33.7", "-22.3", "-14.5", "24.2", "-13.7", "12.5", "4.8", "11.4"]
    Bn_Pulmonary = ["-542.6", "5.6", "936.4", "1231.6", "723", "489.2", "-179.2", "0.1", "-282.2", "-680", "-190.4", "-129.2", "-139.5", "17.8", "47.9", "136.8", "-20.3", "40.9", "129.6", "-63.9", "56.7", "50.1", "37.1", "36.2", "-9.2", "65.3", "-19.6", "-49.3", "37.9", "-49.4", "-32.8", "-18", "13.2", "5.6", "-33.9", "36.3", "4.8", "-23.2", "14.3", "-5.3", "32.9", "-7.3", "1.9", "31.7", "-35.1", "8.4", "-0.1", "-15.2", "5.5", "-18.3"]
    An_Coronary = ["2124.7338", "-513.7472", "-77.9321", "165.7688", "-435.3311", "-87.8924", "-1.3272", "-121.8126", "60.3047", "51.5078", "29.6615", "23.0370", "23.7804", "17.4804", "29.3202", "31.3152", "21.0945", "25.3082", "17.9130", "20.1894", "14.7966", "18.5829", "6.6717", "11.0004", "5.3708", "9.5004", "7.4897", "3.2099", "6.8229", "0.7970", "1.4501", "3.3212", "-5.4243", "-4.7271", "-1.4700", "-5.6648", "-3.6477", "-5.3823", "-8.7455", "-5.5398", "-6.0953", "-6.7116", "-4.7765", "-6.2822", "-7.4666", "-5.2332", "-8.3591", "-4.3271", "-5.2805", "-5.6532"]
    Bn_Coronary = ["1453.0751", "-314.0834", "650.9328", "108.3926", "-158.2025", "120.2019", "-42.1155", "-23.4507", "7.7228", "-11.7642", "-17.4899", "-19.3200", "-25.5780", "-11.9417", "-16.9995", "-14.8397", "-18.5798", "-10.0380", "-13.9818", "-11.8724", "-17.4426", "-15.3552", "-16.8378", "-15.9537", "-18.4244", "-17.5907", "-19.0008", "-17.4248", "-13.5114", "-18.7698", "-12.8268", "-12.2714", "-18.7698", "-18.7698", "-11.9942", "-10.3226", "-11.4450", "-6.5919", "-6.0932", "-8.7413", "-3.2582", "-7.4246", "-5.3886", "-2.4224", "-2.0738", "-3.1280", "-0.1439", "-1.7094", "1.5866", "-0.8988"]
    An_Brachial = ["191.6383", "218.9791", "268.1564", "224.3540", "145.9238", "103.1281", "74.0993", "57.0934", "36.8736", "16.2201", "0.2299", "-18.6542", "-28.4889", "-46.9507", "-45.4633", "-55.5101", "-64.8284", "-68.0315", "-71.2238", "-67.9262", "-70.7426", "-67.2803", "-66.4062", "-59.1810", "-57.6494", "-53.7718", "-48.0437","-42.4643", "-41.1287", "-33.9490", "-30.2650", "-24.4485", "-20.8442", "-17.5611", "-12.3196", "-9.2091", "-7.9124", "-7.7500", "-4.6640", "-2.8875", "-1.6893", "0.0577", "1.4701", "0.3349", "3.7993", "1.3974", "3.7970", "2.0775", "1.0691","1.0863", "11.1", "-19.9", "33.7", "-22.3", "-14.5", "24.2", "-13.7", "12.5", "4.8", "11.4"]
    Bn_Brachial = ["-253.0965", "-65.9683", "16.1377", "107.7265", "141.5211", "138.2621", "145.0011", "146.7079", "151.2893", "131.4338", "130.3422", "122.3305", "115.0491", "98.3526", "94.4473", "80.0819", "75.3471", "60.5751", "48.4956", "38.3485", "27.2166", "18.5114", "11.9816", "8.0941", "-0.5086", "-6.6034", "-12.4996", "-16.7447", "-18.8979", "-19.7601", "-24.5299", "-21.8377", "-24.1316", "-20.9204", "-21.0125", "-19.1784", "-18.5020", "-17.2335", "-15.2416", "-15.4263", "-11.7592", "-10.4825", "-10.5018", "-7.9252", "-6.7515", "-4.6179", "-2.7875", "-3.0679", "-2.5105", "-0.6775", "-0.7986", "0.1097", "0.9671", "0.7818", "2.2293", "2.6181", "3.1057", "1.2236", "2.0984", "0.7317"]

    w = 2 * 3.14159 * 1.2 #Hz
    u_o = 0.004
    T = 310.15
    a0 = -1474.0373
    R = 0.0015
    r = 0
    Pf = 1050
    Pp = 1125
    n = len(An_Femoral)
    Io = 1
    an = float(An_Femoral[-1])
    if type == "SICKLE":
        c = 0.248
        m = 0.07 * (math.exp(2.49 * c) + ((1107/T) * math.exp(-1.69 * c)))
        u_s = u_o / (1 - m * c)
        # u_f = - ((a0 * R)/(1-c) * u_s * w) * (r*r - 1)
        S = 4.5 * (u_o / R*R) * (4 + 3 * math.sqrt(c * 8 * c - 2 * c * c) + 3 * c)/((2 - 3 * c) * (2 - 3 * c))
        En = - (an * R)/(u_s * w) * (c/(1-c) * (S/(S + n * w * Pp)))
        Gn = -R*R * (c * S * n * w * Pp + n * w * Pf * (1 - c) * S - n * n * Pp * Pf * (1 - c)) / ((1 - c) * ( S * n * w * Pp) * u_s)
        u_f = ((-a0 * R) / (1-c) * u_s * w) * (r * r - 1)
        for n in range(len(An_Femoral)):
            newAn = float(An_Femoral[n])
            newBn = float(Bn_Femoral[n])
            u_f = u_f + (En/Gn * ((Io * (r * math.sqrt(Gn))) / (Io * math.sqrt(Gn))) * math.exp(c * n * w * time - math.atan(newBn/newAn)))
        return u_f
    if type == "PLASMA":
        c = 0.28
        m = 0.07 * (math.exp(2.49 * c) + ((1107/T) * math.exp(-1.69 * c)))
        u_s = u_o / (1 - m * c)
        S = 4.5 * (u_o / R*R) * (4 + 3 * math.sqrt(c * 8 * c - 2 * c * c) + 3 * c)/((2 - 3 * c) * (2 - 3 * c))
        En = - (an * R)/(u_s * w) * (c/(1-c) * (S/(S + n * w * Pp)))
        Gn = -R*R * (c * S * n * w * Pp + n * w * Pf * (1 - c) * S - n * n * Pp * Pf * (1 - c)) / ((1 - c) * ( S * n * w * Pp) * u_s)
        u_f = ((-a0 * R) / (1-c) * u_s * w) * (r * r - 1)
        for n in range(len(An_Femoral)):
            newAn = float(An_Femoral[n])
            newBn = float(Bn_Femoral[n])
            u_f = u_f + (En/Gn * ((Io * (r * math.sqrt(Gn))) / (Io * math.sqrt(Gn))) * math.exp(c * n * w * time - math.atan(newBn/newAn)))
        return u_f
    if type == "POLYCYTHEMIA":
        c = 0.632
        m = 0.07 * (math.exp(2.49 * c) + ((1107/T) * math.exp(-1.69 * c)))
        u_s = u_o / (1 - m * c)
        S = 4.5 * (u_o / R*R) * (4 + 3 * math.sqrt(c * 8 * c - 2 * c * c) + 3 * c)/((2 - 3 * c) * (2 - 3 * c))
        En = - (an * R)/(u_s * w) * (c/(1-c) * (S/(S + n * w * Pp)))
        Gn = -R*R * (c * S * n * w * Pp + n * w * Pf * (1 - c) * S - n * n * Pp * Pf * (1 - c)) / ((1 - c) * ( S * n * w * Pp) * u_s)
        u_f = ((-a0 * R) / (1-c) * u_s * w) * (r * r - 1)
        for n in range(len(An_Femoral)):
            newAn = float(An_Femoral[n])
            newBn = float(Bn_Femoral[n])
            u_f = u_f + (En/Gn * ((Io * (r * math.sqrt(Gn))) / (Io * math.sqrt(Gn))) * math.exp(c * n * w * time - math.atan(newBn/newAn)))
        return u_f
    if type == "NORMAL":
        c = 0.426
        m = 0.07 * (math.exp(2.49 * c) + ((1107/T) * math.exp(-1.69 * c)))
        u_s = u_o / (1 - m * c)
        S = 4.5 * (u_o / R*R) * (4 + 3 * math.sqrt(c * 8 * c - 2 * c * c) + 3 * c)/((2 - 3 * c) * (2 - 3 * c))
        En = - (an * R)/(u_s * w) * (c/(1-c) * (S/(S + n * w * Pp)))
        Gn = -R*R * (c * S * n * w * Pp + n * w * Pf * (1 - c) * S - n * n * Pp * Pf * (1 - c)) / ((1 - c) * ( S * n * w * Pp) * u_s)
        u_f = ((-a0 * R) / (1-c) * u_s * w) * (r * r - 1)
        for n in range(len(An_Femoral)):
            newAn = float(An_Femoral[n])
            newBn = float(Bn_Femoral[n])
            u_f = u_f + (En/Gn * ((Io * (r * math.sqrt(Gn))) / (Io * math.sqrt(Gn))) * math.exp(c * n * w * time - math.atan(newBn/newAn)))
        return u_f

plot_graph()