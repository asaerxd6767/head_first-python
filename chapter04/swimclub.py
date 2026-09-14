import statistics
FOLDER = 'swimdata/'

def read_swim_data(filename: str):
    swimmer, age, distance, stroke = filename.removesuffix('.txt').split('-')
    with open(FOLDER + filename) as f:
        lines = f.readlines()
        times = lines[0].strip().split(',')
        
    converts = []
    for time in times:
        minutes, rest = time.split(':')
        seconds, hundreds = rest.split('.')
        converted_time = (int(minutes) * 100 * 60) + (int(seconds) * 100) + int(hundreds)
        converts.append(converted_time)

    average = statistics.mean(converts)
    mins_secs, hundredths = str(round(average / 100, 2)).split('.')
    minutes = int(mins_secs) // 60
    seconds = int(mins_secs) - minutes * 60
    average = str(minutes) + ":" + str(seconds) + '.' + str(hundredths)
    return swimmer, age, distance, stroke, times, average