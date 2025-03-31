import streamlit as st

# Set page config
st.set_page_config(page_title="Baseball Stats Calculator", layout="wide")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Basic Stats Calculator", "wRC+ Calculator", "Glossary"])

# Park factors data
park_factors = {
    "American Family Field (Brewers)": 100,
    "Angel Stadium (Los Angeles Angels)": 102,
    "Busch Stadium (St. Louis Cardinals)": 98,
    "Chase Field (Arizona Diamondbacks)": 101,
    "Citi Field (New York Mets)": 96,
    "Citizens Bank Park (Philadelphia Phillies)": 100,
    "Comerica Park (Detroit Tigers)": 99,
    "Coors Field (Colorado Rockies)": 113,
    "Daikin Park (Houston Astros)": 99,
    "Dodger Stadium (Los Angeles Dodgers)": 98,
    "Fenway Park (Boston Red Sox)": 106,
    "Tropicana Field (Tampa Bay Rays)": 96,
    "Globe Life Field (Texas Rangers)": 100,
    "Great American Ballpark (Cincinnati Reds)": 106,
    "Kauffman Stadium (Kansas City Royals)": 105,
    "LoanDepot Park (Miami Marlins)": 102,
    "Nationals Park (Washington Nationals)": 99,
    "Oracle Park (San Francisco Giants)": 97,
    "Oriole Park at Camden Yards (Baltimore Orioles)": 98,
    "Petco Park (San Diego Padres)": 96,
    "PNC Park (Pittsburgh Pirates)": 102,
    "Progressive Field (Cleveland Guardians)": 99,
    "Rate Field (Chicago White Sox)": 101,
    "Rogers Centre (Toronto Blue Jays)": 99,
    "Oakland Coliseum (Oakland Athletics)": 96,
    "T-Mobile Park (Seattle Mariners)": 94,
    "Target Field (Minnesota Twins)": 100,
    "Truist Park (Atlanta Braves)": 101,
    "Wrigley Field (Chicago Cubs)": 97,
    "Yankee Stadium (New York Yankees)": 100
} 

# Tab 1: Basic Stats Calculator
with tab1:
    st.header("Basic Baseball Stats Calculator")
    
    # Create columns for input
    col1, col2 = st.columns(2)
    
    with col1:
        pa = st.number_input("Plate Appearances (PA)", min_value=0, value=600)
        ab = st.number_input("At-Bats (AB)", min_value=0, value=550)
        ubb = st.number_input("Unintentional Walks (UBB)", min_value=0, value=50)
        ibb = st.number_input("Intentional Walks (IBB)", min_value=0, value=5)
        hbp = st.number_input("Hit By Pitch (HBP)", min_value=0, value=10)
        sf = st.number_input("Sacrifice Flies (SF)", min_value=0, value=5)
    
    with col2:
        k = st.number_input("Strikeouts (K)", min_value=0, value=150)
        singles = st.number_input("Singles (1B)", min_value=0, value=100)
        doubles = st.number_input("Doubles (2B)", min_value=0, value=30)
        triples = st.number_input("Triples (3B)", min_value=0, value=5)
        hr = st.number_input("Home Runs (HR)", min_value=0, value=25)
    
    if st.button("Calculate Stats"):
        # Calculate basic stats
        bb_pct = (ubb + ibb) / pa * 100 if pa > 0 else 0
        k_pct = k / pa * 100 if pa > 0 else 0
        avg = (singles + doubles + triples + hr) / ab if ab > 0 else 0
        obp = (singles + doubles + triples + hr + ubb + ibb + hbp) / (ab + ubb + ibb + hbp + sf) if (ab + ubb + ibb + hbp + sf) > 0 else 0
        slg = (singles + doubles*2 + triples*3 + hr*4) / ab if ab > 0 else 0
        ops = obp + slg
        woba = ((.69 * ubb) + (.72 * hbp) + (.88 * singles) + (1.25 * doubles) + (1.59 * triples) + (2.05 * hr))/(ab + ubb + sf + hbp)
        
        # Display results
        st.subheader("Results")
        st.markdown(f"**Walk% (BB%):** {bb_pct:.1f}%")
        st.markdown(f"**Strikeout% (K%):** {k_pct:.1f}%")
        st.markdown(f"**Batting Average (AVG):** {avg:.3f}")
        st.markdown(f"**On-base Percentage (OBP):** {obp:.3f}")
        st.markdown(f"**Slugging Percentage (SLG):** {slg:.3f}")
        st.markdown(f"**On-base Plus Slugging (OPS):** {ops:.3f}")
        st.markdown(f"**Weighted On-base Average (wOBA):** {woba:.3f}")

# Tab 2: wRC+ Calculator
with tab2:
    st.header("wRC+ Calculator") 
    
    # Only two inputs needed
    col1, col2 = st.columns(2)
    with col1:
        player_woba = st.number_input("Player's wOBA", min_value=0.0, max_value=1.0, value=0.350, step=0.001, format="%.3f")
    with col2:
        park = st.selectbox("Home Ballpark", options=list(park_factors.keys()))
    
    park_factor = park_factors[park]
    
    if st.button("Calculate wRC+"):
        
        # wRC+ formula
        wrc_plus = (((((player_woba - 0.310) / 1.242) + 0.11698) + (0.11698 - ((park_factor / 100) * 0.11698))) / (0.117)) * 100
        
        # Display results
        st.metric("wRC+", value=f"{wrc_plus:.0f}")
        st.caption(f"Park Factor: {park_factor} (Higher park factor means that park favors hitters, and vice versa for a lower number. 100 is average. For example, if a player has a 110 park factor, their wRC+ will not be as high as someone with the same stats playing in a 100 park factor stadium.)")
    
# Tab 3: Glossary
with tab3:
    st.header("Baseball Statistics Glossary")
    
    stats_info = {
        "Walk% (BB%)": {
            "description": "Percentage of plate appearances resulting in walks",
            "url": "https://library.fangraphs.com/offense/rate-stats/"
        },
        "Strikeout% (K%)": {
            "description": "Percentage of plate appearances resulting in strikeouts",
            "url": "https://library.fangraphs.com/offense/rate-stats/"
        },
        "Batting Average (AVG)": {
            "description": "Hits divided by at-bats",
            "url": "https://library.fangraphs.com/offense/offensive-statistics-list/"
        },
        "On-base Percentage (OBP)": {
            "description": "How often a batter reaches base",
            "url": "https://library.fangraphs.com/offense/offensive-statistics-list/"
        },
        "Slugging Percentage (SLG)": {
            "description": "Total bases divided by at-bats",
            "url": "https://library.fangraphs.com/offense/offensive-statistics-list/"
        },
        "On-base Plus Slugging (OPS)": {
            "description": "OBP plus SLG",
            "url": "https://www.fangraphs.com/library/offense/ops/"
        },
        "Weighted On-base Average (wOBA)": {
            "description": "Advanced offensive metric that properly weights outcomes",
            "url": "https://library.fangraphs.com/offense/woba/"
        },
        "Weighted Runs Created Plus (wRC+)": {
            "description": "Takes wOBA and adjusts it based on league and park factors, where 100 is average",
            "url": "https://library.fangraphs.com/offense/wrc/"
        }
    }
    
    for stat, info in stats_info.items():
        st.subheader(stat)
        st.markdown(info["description"])
        st.markdown(f"[Read more on FanGraphs]({info['url']})")
        st.write("---")