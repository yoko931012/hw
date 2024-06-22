import csv

# Function to extract win-loss percentage from the record
def win_loss_pct(record):
    wins, losses = [int(x) for x in record.split('-')]
    return wins / (wins + losses)

try:
    # Read the CSV file
    with open('nba_standings.csv', mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

    # Question 1: Eastern teams with Home win-loss percentage lower than Away win-loss percentage
    try:
        eastern_teams = [row for row in data if row['Conference'] == 'Eastern']
        teams_home_away = [
            row['Team'] for row in eastern_teams
            if win_loss_pct(row['HOME']) < win_loss_pct(row['AWAY'])
        ]
        print("Eastern Conference teams with Home win-loss percentage lower than Away win-loss percentage:")
        print(teams_home_away)
    except Exception as e:
        print("Error processing Question 1:", str(e))

    # Question 2: Which conference had a higher average difference of PF minus PA?
    try:
        conference_diff = {'Eastern': [], 'Western': []}
        for row in data:
            pf_minus_pa = float(row['PF']) - float(row['PA'])
            conference_diff[row['Conference']].append(pf_minus_pa)
        
        avg_diff = {conf: sum(diff) / len(diff) for conf, diff in conference_diff.items()}
        higher_avg_diff_conference = max(avg_diff, key=avg_diff.get)
        print("Conference with higher average PF minus PA:", higher_avg_diff_conference)
    except Exception as e:
        print("Error processing Question 2:", str(e))

    # Question 3: Generate a ranking list based on wins against the other conference
    try:
        interconf_win_percentage = []
        for row in data:
            home_pct = win_loss_pct(row['HOME'])
            away_pct = win_loss_pct(row['AWAY'])
            interconf_win_pct = home_pct if row['Conference'] == 'Western' else away_pct
            interconf_win_percentage.append((row['Team'], interconf_win_pct))

        ranking_list = sorted(interconf_win_percentage, key=lambda x: x[1], reverse=True)
        print("Ranking list of teams based on win percentage against the other conference:")
        for team, pct in ranking_list:
            print(team, pct)
    except Exception as e:
        print("Error processing Question 3:", str(e))

except FileNotFoundError:
    print("Error: The file 'nba_standings.csv' was not found.")
except Exception as e:
    print("An unexpected error occurred:", str(e))
