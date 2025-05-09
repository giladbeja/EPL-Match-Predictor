import pandas as pd

def compute_team_cumulative(df, team_col, stat_cols):
    team_stats = {}
    cumulative_data = []
    for idx, row in df.iterrows():
        team = row[team_col]
        if team not in team_stats or team_stats[team]['count'] == 0:
            cumulative_row = {col: pd.NA for col in stat_cols}
        else:
            cumulative_row = {
                col: team_stats[team]['sum'][col] / team_stats[team]['count']
                for col in stat_cols
            }
        cumulative_data.append(cumulative_row)
        if team not in team_stats:
            team_stats[team] = {
                'count': 0,
                'sum': {col: 0.0 for col in stat_cols}
            }
        team_stats[team]['count'] += 1
        for col in stat_cols:
            val = row[col]
            if pd.notnull(val):
                team_stats[team]['sum'][col] += val
    return pd.DataFrame(cumulative_data, index=df.index)