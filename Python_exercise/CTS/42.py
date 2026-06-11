import statistics

def analyze_data():
    sales = [100, 200, 300, 400, 500]

    mean_value = statistics.mean(sales)
    median_value = statistics.median(sales)

    print("Mean:", mean_value)
    print("Median:", median_value)

analyze_data()