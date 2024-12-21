import plotly.express as px

def plot_types_bar_chart(qs):
    x_vals = ['Income','Expenditure']
    total_income = qs.get_total_income()
    total_expense = qs.get_total_expenses()
    fig = px.bar( x=x_vals, y=[total_income,total_expense])
    return fig