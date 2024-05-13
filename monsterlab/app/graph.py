from altair import Chart, Tooltip, Scale,Color
from pandas import DataFrame

def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    # Drop the '_id' column
    df = df.drop('_id', axis=1)

    graph = Chart(
        df,
        title=f"{y} by {x} for {target}",
    ).mark_circle(size=100).encode(
        x=x,
        y=y,
        color=Color(target, scale=Scale(range=["red", "blue", "yellow", "green","black"])),
        tooltip=Tooltip(df.columns.to_list())
    ).properties(
        width=800,
        height=600,
        background='white',
        padding=10
    )
    return graph
