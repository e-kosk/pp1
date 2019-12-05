import statistics as s


def calculate(data):
    mean = s.mean(data)
    median = s.median(data)
    min_value = min(data)
    max_value = max(data)
    return [mean, median, min_value, max_value]
