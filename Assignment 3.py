def analyze_data(data_points):
    # 1. Print the total number of data points
    print("Total number of data points:", len(data_points))

    # 2. Identify and print the data point with the highest 'value'
    max_data_point = max(data_points, key=lambda x: x['value'])
    print("Data point with the highest value:", max_data_point)

    # 3. Calculate and print the average 'value' for each 'category'
    category_values = {}
    category_counts = {}
    for data_point in data_points:
        category = data_point['category']
        value = data_point['value']

        if category in category_values:
            category_values[category] += value
            category_counts[category] += 1
        else:
            category_values[category] = value
            category_counts[category] = 1

    average_values = {category: category_values[category] / category_counts[category] for category in category_values}
    print("Average value for each category:", average_values)

    # 4. Check if there are any data points where 'value' is greater than 100
    high_value_data_points = [dp for dp in data_points if dp['value'] > 100]
    if high_value_data_points:
        print("High-value data points found:", high_value_data_points)
    else:
        print("No high-value data points found")

# Example usage
data_points = [
    {'name': 'A', 'value': 75, 'category': 'X'},
    {'name': 'B', 'value': 120, 'category': 'Y'},
    {'name': 'C', 'value': 90, 'category': 'X'},
    {'name': 'D', 'value': 150, 'category': 'Z'},
    {'name': 'E', 'value': 80, 'category': 'Y'}
]

analyze_data(data_points)
nnbbbbxhjhddtbmkjxxdhnjjj
