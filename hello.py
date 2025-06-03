from preswald import connect, text, table, get_df, query


connect()
df = get_df("mls")

sql = "SELECT TEAM, CITY, STATE, JOINED FROM mls ORDER BY TEAM, JOINED"
filtered_df = query(sql, "mls")

text(f"# MLS Data Analysis App")
table(filtered_df, title="Filtered Data")


from preswald import plotly
import plotly.express as px

text("# MLS Map")
fig_map = px.scatter_geo(
    df,
    lat="latitude",
    lon="longitude",
    hover_name="team",
    title="MLS Map",
)
fig_map.update_geos(
    scope="north america",  # Zoom to North America
    projection_type="natural earth",  # Optional: other options include 'orthographic', 'equirectangular'
    showland=True, landcolor="lightgray"
)

plotly(fig_map)
