# 🌾 Indian Agriculture Data Analytics & Visualization Platform

## 📌 Problem Statement
India's agricultural sector is vital for the economy, but managing agricultural data remains a challenge due to its complexity, fragmentation, and lack of easy access. Stakeholders such as farmers, policymakers, and researchers often face difficulties in accessing, analyzing, and making data-driven decisions.

**Goal:**  
Create a data visualization platform that integrates agricultural data from different states and districts in India. The platform will provide insights into crop production, yields, and areas under cultivation — helping users identify trends, gaps, and regional disparities.

---

## 💼 Business Use Cases

### **Farmers**
- **UC1:** Explore historical crop production & yield data to decide what to grow each season.
- **UC2:** Identify regions with higher productivity and learn best practices for soil, irrigation, and crop selection.

### **Policymakers**
- **UC1:** Locate low-productivity regions to allocate resources or subsidies effectively.
- **UC2:** Identify crops with fluctuating yields to improve crop insurance and risk management policies.

### **Researchers**
- **UC1:** Study the impact of climate, soil, and irrigation on crop yields over time.
- **UC2:** Identify opportunities for agricultural innovation (e.g., high-yield varieties, pest control).

---

## 🔍 Approach

### **1. Data Collection & Cleaning**
- Gather data from government sources, surveys, and agricultural reports.
- Standardize units (ha, tons, kg/ha) and handle missing values.

### **2. Data Analysis**
- Perform **Exploratory Data Analysis (EDA)** to identify trends & correlations.
- Use statistical methods for insights on productivity, crop patterns, and yield optimization.

### **3. Visualization**
- Build **interactive dashboards** (Plotly, Power BI).
- Charts: Line graphs (time series), bar charts (regional comparisons), heatmaps (crop concentration).

### **4. User Interface**
- Filters for crop, state, district, year, and yield.
- Interactive elements: dropdowns, slicers, tooltips.

### **5. Advanced Analytics**
- Machine learning for yield prediction, crop recommendations, and cultivation planning.

---

## 📊 Power BI Integration Steps

1. **Prepare Data**: Structured format with clear headers (`Crop Name`, `State`, `District`, `Year`, `Area (ha)`, `Production (tons)`, `Yield (kg/ha)`).
2. **Load Data**: Import CSV/Excel/SQL into Power BI and clean using **Power Query Editor**.
3. **Model Data**: Create relationships between crop, location, and production tables.
4. **Design Dashboard**:
   - **Maps** for geographical performance.
   - **Line Charts** for production trends.
   - **Bar Charts** for crop comparisons.
   - **KPIs** for total area, production, and yield.
5. **Add Filters & Slicers**: Crop type, region, year.
6. **Enhance Visuals**: Color themes, tooltips, dynamic titles, interactivity.

---

## 📈 Exploratory Data Analysis (EDA)

- **Top 7 Rice Producing States** (Bar plot)
- **Top 5 Wheat Producing States & % Share** (Bar + Pie chart)
- **Oilseed Production** by top states
- **Sunflower Production** (Top 7 states)
- **India’s Sugarcane Production** (50-year trend line)
- **Rice vs Wheat Production** (50-year comparison)
- **Rice Production in West Bengal Districts**
- **Top Wheat Production Years from Uttar Pradesh**
- **Millet & Sorghum Production Trends**
- **Groundnut Production** (Top states)
- **Soybean Yield Efficiency**
- **Area vs Production Correlation** (Rice, Wheat, Maize)

---

## 📜 SQL Analysis Questions

1. Year-wise Trend of Rice Production Across States (Top 3)
2. Top 5 Districts by Wheat Yield Increase Over the Last 5 Years
3. States with the Highest Growth in Oilseed Production (5-Year Growth Rate)
4. District-wise Correlation Between Area and Production for Major Crops (Rice, Wheat, Maize)
5. Yearly Production Growth of Cotton in Top 5 Cotton Producing States
6. Districts with the Highest Groundnut Production in 2020
7. Annual Average Maize Yield Across All States
8. Total Area Cultivated for Oilseeds in Each State
9. Districts with the Highest Rice Yield
10. Compare Wheat vs Rice Production in Top 5 States Over 10 Years

---

## 🎯 Results

- **Interactive Visualizations**: Explore key metrics (area, production, yield) for crops across time and regions.
- **Trend Identification**: Discover patterns in production & yield, identify top and low performers.
- **Actionable Recommendations**: Crop selection, diversification strategies, and best practices for productivity improvement.

---

## 📏 Project Evaluation Metrics

- **Accuracy**: Visualizations are clear and true to the data.
- **Engagement**: Users interact with filters & visuals.
- **Performance**: Dashboards load quickly and respond instantly to filters.
- **Data Completeness**: All key metrics (area, production, yield) are present and consistent.
- **User Satisfaction**: Positive feedback from farmers, policymakers, researchers.

---

## 📦 Project Deliverables

- **Source Code**: Python scripts for ETL and analysis.
- **Database**: MySQL/PostgreSQL with normalized schema.
- **SQL Scripts**: Table creation, data loading, and queries.
- **Power BI Reports**: Interactive dashboards.
- **Documentation**: Setup instructions, methodology, and data dictionary.

---

## 🛠️ Tech Stack

- **Data Processing**: Python (Pandas, NumPy)
- **Database**: MySQL / PostgreSQL
- **Visualization**: Power BI, Plotly
- **Deployment**: GitHub

---

## 🚀 How to Run

1. Clone this repository:
  ```bash
git clone https://github.com/ThilagavathyVenkatesan/Indian_agricultural.git
cd Indian_agricultural
```
2. Import the dataset into your MySQL database.

3. Run Python ETL scripts to clean & load data.

4. Open Power BI, connect to your database, and load the dashboard.
