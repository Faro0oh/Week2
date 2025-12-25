# Summary of Findings and Caveats

This document summarizes the key analytical findings, definitions, data quality considerations, and future questions based on the analytics pipeline and exploratory analysis.

---

## Key Findings

1. **Revenue concentration by country**  
   A small number of countries account for a large share of total revenue. This indicates that business performance is highly dependent on specific geographic markets.

2. **Seasonal and temporal patterns**  
   Revenue shows variation across months and hours of the day, suggesting that user purchasing behavior is influenced by time-based factors such as seasonality and daily routines.

3. **Order amount distribution is skewed**  
   The raw distribution of order amounts is right-skewed with extreme high values. Winsorization was applied to cap extreme values and improve robustness of summary statistics.

4. **User cohorts differ in behavior**  
   Users grouped by signup year show different average order amounts, suggesting that newer and older cohorts may have different purchasing patterns.

5. **Statistical comparison between groups**  
   A bootstrap comparison between selected user groups (for example, by country or status) shows that observed differences in mean values are statistically meaningful when the confidence interval does not cross zero.

---

## Definitions

- **Order**: A transaction recorded in the orders dataset representing a purchase made by a user.
- **Revenue**: The total monetary value of orders, calculated as the sum of the `amount` field.
- **Winsorization**: A method to limit the influence of extreme values by capping data at specified quantiles (e.g., 1st and 99th percentiles).
- **Outlier**: A value that falls outside the interquartile range (IQR) bounds defined by Q1 − 1.5×IQR and Q3 + 1.5×IQR.
- **Cohort**: A group of users defined by a shared characteristic, such as the year they signed up.

---

## Data Quality Caveats

- **Missing timestamps**: Approximately 20% of `created_at` values could not be parsed into valid datetimes and were converted to missing values (`NaT`).
- **Missing or invalid numeric values**: Some numeric fields contained missing or invalid entries that required cleaning and coercion.
- **Potential reporting delays**: Some orders may appear later than their actual transaction time due to system or ingestion delays.
- **Join assumptions**: The analysis assumes that each user has a unique `user_id` and that orders reference valid users.

---

## Next Questions

1. How does customer lifetime value differ across cohorts and regions?
2. Are there differences in refund or cancellation rates between user groups?
3. Can we predict high-value customers early in their lifecycle?
4. How do marketing campaigns or promotions affect order behavior?
5. Are there long-term trends indicating growth or decline in specific markets?


