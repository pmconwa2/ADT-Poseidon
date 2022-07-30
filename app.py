from flask import Flask, render_template
from dbconnect import connection
# import sqlalchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://btifnirlvheggd:456dae0c256c66d5f8b454351412c5dedd3cfa6f9e696a8c229954549fe2c166@ec2-44-208-88-195.compute-1.amazonaws.com:5432/d20atckuunjd6a"


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


@app.route('/data/', methods=["GET", "POST"])
def data_page():
    try:
        c, conn = connection()

        query = "SELECT * from team"
        c.execute(query)

        data = c.fetchall()
        conn.close()

        return render_template("basic_table.html", title='NFL Teams', data=data)

    except Exception as e:
        return str(e)


@app.route('/teamO/', methods=["GET", "POST"])
def offense_page():
    try:
        c, conn = connection()

        query = """SELECT "Year", "Team", "Games", "Points", "Yards", "Plays", "YardsPerPlay", "PassYards", "PassTD", "RushYds", "RushTD" FROM teamoffense"""
        c.execute(query)

        teamO = c.fetchall()
        conn.close()

        return render_template("team_offense.html",
                               title='Team Offense',
                               data=teamO)

    except Exception as e:
        return str(e)


@app.route('/ints/', methods=["GET", "POST"])
def interception_page():
    try:
        c, conn = connection()

        query = """SELECT "Team", "Year", "PointsAgainst", "YardsAgainst", "PassYdsAgainst", "PassTDAgainst", "RushYdsAgainst", "RushTDAgainst", "FumblesRecovered", "Interceptions" FROM teamdefense"""
        c.execute(query)

        ints = c.fetchall()
        conn.close()

        return render_template("interceptions.html",
                               title='Team Defense',
                               data=ints)

    except Exception as e:
        return str(e)


@app.route('/kick/', methods=["GET", "POST"])
def kick_page():
    try:
        c, conn = connection()

        query = """SELECT "Year", "Team", "FGA", "FGM", "FGLong", "XPA", "XPM", "Punts", "PuntYards", "PuntLong" FROM kick"""
        c.execute(query)

        kicks = c.fetchall()
        conn.close()

        return render_template("kick.html", title='Team Kicking', data=kicks)

    except Exception as e:
        return str(e)


@app.route('/advd/', methods=["GET", "POST"])
def advd_page():
    try:
        c, conn = connection()

        query = """SELECT "Year", "Team", "AverageTargetDepth", "AirYardsAgainst", "YdsAfterContact", "Blitzes", "QBHurries", "Sacks", "Pressures", "MissedTackles" FROM advanceddefense"""
        c.execute(query)

        vance = c.fetchall()
        conn.close()

        return render_template("advanced_def.html",
                               title='Advanced Defense',
                               data=vance)

    except Exception as e:
        return str(e)


@app.route('/chi/', methods=["GET", "POST"])
def chi_page():
    try:
        c, conn = connection()
        query = """SELECT "Year", "Team", "Games", "Points", "Yards", "YardsPerPlay",
                "PassYards", "PassTD", "RushYds", "RushTD", "Turnovers", "1stDowns",
                "Penalties", "PenaltyYards" FROM teamoffense WHERE "Team"='Chicago Bears'"""
        c.execute(query)
        bears = c.fetchall()
        conn.close()

        c, conn = connection()
        query = """SELECT "Team", "Year", "PointsAgainst", "YardsAgainst", "PassYdsAgainst",
                "PassTDAgainst", "RushYdsAgainst", "RushTDAgainst", "FumblesRecovered",
                "1stDownsAgainst", "Interceptions", "DefPenalties",
                "DefPenaltyYds" FROM teamdefense WHERE "Team"='Chicago Bears'"""
        c.execute(query)
        bearsD = c.fetchall()
        conn.close()

        return render_template("chi.html", title='Chicago Bears', data=bears, data2=bearsD)

    except Exception as e:
        return str(e)


@app.route('/team/<team_id>', methods=["GET", "POST"])
def teampage(team_id):
    team_id = team_id.replace("_", " ")

    c, conn = connection()
    query = f"""SELECT "Year", "Team", "Games", "Points", "Yards", "YardsPerPlay",
            "PassYards", "PassTD", "RushYds", "RushTD", "Turnovers", "1stDowns", "Penalties",
            "PenaltyYards" FROM teamoffense WHERE "Team" LIKE '%{team_id}%'"""
    c.execute(query)
    off = c.fetchall()
    conn.close()

    c, conn = connection()
    query = f"""SELECT "Team", "Year", "PointsAgainst", "YardsAgainst", "PassYdsAgainst",
                "PassTDAgainst", "RushYdsAgainst", "RushTDAgainst", "FumblesRecovered",
                "1stDownsAgainst", "Interceptions", "DefPenalties",
                "DefPenaltyYds" FROM teamdefense WHERE "Team" LIKE '%{team_id}%'"""
    c.execute(query)
    defense = c.fetchall()
    conn.close()

    return render_template('team_page.html',
                           title=team_id,
                           data=off,
                           data2=defense)


if __name__ == '__main__':
    app.run()

