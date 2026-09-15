def convert2range(value, f_min, f_max, t_min, t_max):
    return round(t_min + (t_max - t_min) * ((value - f_min) / (f_max - f_min)), 2)