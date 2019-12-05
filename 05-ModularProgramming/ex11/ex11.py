from data import get_data
from results import display_raport, display_statistics, display_chart, sep
from calculations import calculate

expenses = get_data('wydatki.txt')
statistics_data = calculate(expenses)

display_raport(expenses)
sep(20)
display_statistics(statistics_data)
sep(20)
display_chart(expenses)
