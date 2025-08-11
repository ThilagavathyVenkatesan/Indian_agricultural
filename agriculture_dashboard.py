import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Page config
st.set_page_config(page_title="🌾 Agriculture Data Insights", layout="wide")
st.title("🌾 Agriculture Data Analytics Dashboard")

# Connection (cached)
@st.cache_resource
def get_connection():
    try:
        engine = create_engine("mysql+pymysql://root:@localhost/agri")
        conn = engine.connect()
        st.success("✅ Connected to database successfully!")
        return conn
    except Exception as e:
        st.error(f"❌ Connection failed: {e}")
        return None

connection = get_connection()

# SQL queries list
queries = [
    # 1️⃣
    ("""
    SELECT `Year`, `State Name`, total_rice_production
    FROM (
        SELECT 
            `Year`, 
            `State Name`, 
            SUM(`RICE PRODUCTION (1000 tons)`) AS total_rice_production,
            RANK() OVER (
                PARTITION BY `Year` 
                ORDER BY SUM(`RICE PRODUCTION (1000 tons)`) DESC
            ) AS rank_per_year
        FROM crop_production
        GROUP BY `Year`, `State Name`
    ) ranked
    WHERE rank_per_year <= 3
    ORDER BY `Year`, total_rice_production DESC;
    """, "1️⃣ Year-wise Trend of Rice Production Across States (Top 3)"),

    # 2️⃣
    ("""
    WITH latest_years AS (
        SELECT MAX(`Year`) AS max_year FROM crop_production
    ),
    wheat_yield_trend AS (
        SELECT 
            `Dist Name`, 
            `Year`, 
            AVG(`WHEAT YIELD (Kg per ha)`) AS avg_wheat_yield
        FROM crop_production
        WHERE `Year` IN (
            (SELECT max_year FROM latest_years),
            (SELECT max_year - 4 FROM latest_years)
        )
        GROUP BY `Dist Name`, `Year`
    )
    SELECT 
        wy1.`Dist Name`,
        wy2.avg_wheat_yield - wy1.avg_wheat_yield AS yield_increase
    FROM 
        wheat_yield_trend wy1
    JOIN 
        wheat_yield_trend wy2 
        ON wy1.`Dist Name` = wy2.`Dist Name` 
        AND wy1.`Year` = (SELECT max_year - 4 FROM latest_years)
        AND wy2.`Year` = (SELECT max_year FROM latest_years)
    ORDER BY 
        yield_increase DESC
    LIMIT 5;
    """, "2️⃣ Top 5 Districts by Wheat Yield Increase Over the Last 5 Years"),

    # 3️⃣
    ("""
    WITH latest_years AS (
        SELECT MAX(`Year`) AS max_year FROM crop_production
    ),
    oilseed_by_year AS (
        SELECT 
            `State Name`, 
            `Year`, 
            SUM(`OILSEEDS PRODUCTION (1000 tons)`) AS total_production
        FROM crop_production
        GROUP BY `State Name`, `Year`
    )
    SELECT 
        recent.`State Name`,
        ((recent.total_production - past.total_production) / NULLIF(past.total_production, 0)) * 100 AS growth_percent
    FROM 
        oilseed_by_year recent
    JOIN 
        oilseed_by_year past 
        ON recent.`State Name` = past.`State Name`
    JOIN 
        latest_years ly
        ON recent.`Year` = ly.max_year 
        AND past.`Year` = ly.max_year - 4
    ORDER BY 
        growth_percent DESC
    LIMIT 5;
    """, "3️⃣ States with Highest Growth in Oilseed Production (5-Year Growth Rate)"),

    # 4️⃣
    ("""
    WITH rice_corr AS (
    SELECT 
        `Dist Name`,
        (
            COUNT(*) * SUM(`RICE AREA (1000 ha)` * `RICE PRODUCTION (1000 tons)`) -
            SUM(`RICE AREA (1000 ha)`) * SUM(`RICE PRODUCTION (1000 tons)`)
        ) /
        (
            SQRT(COUNT(*) * SUM(POWER(`RICE AREA (1000 ha)`, 2)) - POWER(SUM(`RICE AREA (1000 ha)`), 2)) *
            SQRT(COUNT(*) * SUM(POWER(`RICE PRODUCTION (1000 tons)`, 2)) - POWER(SUM(`RICE PRODUCTION (1000 tons)`), 2))
        ) AS rice_correlation
    FROM crop_production
    WHERE `RICE AREA (1000 ha)` IS NOT NULL AND `RICE PRODUCTION (1000 tons)` IS NOT NULL
    GROUP BY `Dist Name`
),

wheat_corr AS (
    SELECT 
        `Dist Name`,
        (
            COUNT(*) * SUM(`WHEAT AREA (1000 ha)` * `WHEAT PRODUCTION (1000 tons)`) -
            SUM(`WHEAT AREA (1000 ha)`) * SUM(`WHEAT PRODUCTION (1000 tons)`)
        ) /
        (
            SQRT(COUNT(*) * SUM(POWER(`WHEAT AREA (1000 ha)`, 2)) - POWER(SUM(`WHEAT AREA (1000 ha)`), 2)) *
            SQRT(COUNT(*) * SUM(POWER(`WHEAT PRODUCTION (1000 tons)`, 2)) - POWER(SUM(`WHEAT PRODUCTION (1000 tons)`), 2))
        ) AS wheat_correlation
    FROM crop_production
    WHERE `WHEAT AREA (1000 ha)` IS NOT NULL AND `WHEAT PRODUCTION (1000 tons)` IS NOT NULL
    GROUP BY `Dist Name`
),

maize_corr AS (
    SELECT 
        `Dist Name`,
        (
            COUNT(*) * SUM(`MAIZE AREA (1000 ha)` * `MAIZE PRODUCTION (1000 tons)`) -
            SUM(`MAIZE AREA (1000 ha)`) * SUM(`MAIZE PRODUCTION (1000 tons)`)
        ) /
        (
            SQRT(COUNT(*) * SUM(POWER(`MAIZE AREA (1000 ha)`, 2)) - POWER(SUM(`MAIZE AREA (1000 ha)`), 2)) *
            SQRT(COUNT(*) * SUM(POWER(`MAIZE PRODUCTION (1000 tons)`, 2)) - POWER(SUM(`MAIZE PRODUCTION (1000 tons)`), 2))
        ) AS maize_correlation
    FROM crop_production
    WHERE `MAIZE AREA (1000 ha)` IS NOT NULL AND `MAIZE PRODUCTION (1000 tons)` IS NOT NULL
    GROUP BY `Dist Name`
)

SELECT 
    r.`Dist Name`,
    ROUND(r.rice_correlation, 3) AS rice_corr,
    ROUND(w.wheat_correlation, 3) AS wheat_corr,
    ROUND(m.maize_correlation, 3) AS maize_corr
FROM rice_corr r
LEFT JOIN wheat_corr w ON r.`Dist Name` = w.`Dist Name`
LEFT JOIN maize_corr m ON r.`Dist Name` = m.`Dist Name`
ORDER BY rice_corr DESC;
""", "4️⃣ District-wise Correlation Between Area and Production"),

    # 5️⃣
    ("""
    WITH top_states AS (
        SELECT `State Name`
        FROM crop_production
        GROUP BY `State Name`
        ORDER BY SUM(`COTTON PRODUCTION (1000 tons)`) DESC
        LIMIT 5
    )
    SELECT Year, `State Name`, SUM(`COTTON PRODUCTION (1000 tons)`) AS total_cotton_production
    FROM crop_production
    WHERE `State Name` IN (SELECT `State Name` FROM top_states)
    GROUP BY Year, `State Name`
    ORDER BY Year, total_cotton_production DESC;
    """, "5️⃣ Yearly Cotton Production Growth in Top 5 States"),

    # 6️⃣
    ("""
    SELECT `Dist Name`, `GROUNDNUT PRODUCTION (1000 tons)`
    FROM crop_production
    WHERE Year = 2020
    ORDER BY `GROUNDNUT PRODUCTION (1000 tons)` DESC
    LIMIT 5;
    """, "6️⃣ Districts with Highest Groundnut Production in 2020"),

    # 7️⃣
    ("""
    SELECT Year, ROUND(AVG(`MAIZE YIELD (Kg per ha)`), 2) AS avg_maize_yield
    FROM crop_production
    GROUP BY Year
    ORDER BY Year;
    """, "7️⃣ Annual Average Maize Yield Across States"),

    # 8️⃣
    ("""
    SELECT `State Name`, SUM(`OILSEEDS AREA (1000 ha)`) AS total_oilseed_area
    FROM crop_production
    GROUP BY `State Name`
    ORDER BY total_oilseed_area DESC;
    """, "8️⃣ Total Oilseeds Area Cultivated in Each State"),

    # 9️⃣
    ("""
    SELECT `Dist Name`, MAX(`RICE YIELD (Kg per ha)`) AS max_rice_yield
    FROM crop_production
    GROUP BY `Dist Name`
    ORDER BY max_rice_yield DESC
    LIMIT 5;
    """, "9️⃣ Districts with Highest Rice Yield"),

    # 🔟
    ("""
    WITH top_states AS (
        SELECT `State Name`
        FROM crop_production
        GROUP BY `State Name`
        ORDER BY SUM(`WHEAT PRODUCTION (1000 tons)` + `RICE PRODUCTION (1000 tons)`) DESC
        LIMIT 5
    )
    SELECT 
        Year, 
        `State Name`, 
        SUM(`WHEAT PRODUCTION (1000 tons)`) AS wheat_production,
        SUM(`RICE PRODUCTION (1000 tons)`) AS rice_production
    FROM crop_production
    WHERE `State Name` IN (SELECT `State Name` FROM top_states)
    GROUP BY Year, `State Name`
    ORDER BY Year, `State Name`;
    """, "🔟 Wheat vs Rice Production in Top 5 States (10-Year View)")
]

# Run Queries
if connection:
    for sql, title in queries:
        with st.expander(title, expanded=False):
            try:
                df = pd.read_sql(sql, connection)
                st.dataframe(df, use_container_width=True)
            except Exception as e:
                st.error(f"❌ Error loading data: {e}")
else:
    st.warning("🛑 No connection to the database.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit and MySQL")
