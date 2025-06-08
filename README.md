# 💰 Virgil Financial Simulator

A comprehensive financial simulation tool for analyzing the business model of Virgil, an AI-powered health assistant for autoimmune conditions. This Streamlit application helps model subscription-based revenue, costs, and profitability over time.

## 🚀 Features

- **Interactive Parameter Adjustment**: Easily modify key business parameters through an intuitive sidebar interface
- **Real-time Financial Modeling**: Calculate MRR, profit/loss, break-even points, and more
- **Visual Dashboard**: Interactive charts showing key metrics over time
- **Scenario Analysis**: Test different pricing strategies and growth assumptions
- **Detailed Data Export**: View and analyze monthly financial data in tabular format

## 📊 Key Metrics Calculated

- **Monthly Recurring Revenue (MRR)**
- **Active Subscribers Growth**
- **Break-Even Analysis**
- **Cumulative Profit/Loss**
- **Gross Profit Margins**
- **Customer Churn Impact**
- **Net Profit Margins**

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/virgil-financial-simulator.git
   cd virgil-financial-simulator
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser** to `http://localhost:8501`

## 🌐 Deployment

### Streamlit Cloud Deployment

1. **Fork this repository** to your GitHub account

2. **Visit [Streamlit Cloud](https://share.streamlit.io/)**

3. **Deploy your app**:
   - Click "New app"
   - Connect your GitHub account
   - Select this repository
   - Set the main file path to `app.py`
   - Click "Deploy"

### Alternative Deployment Options

- **Heroku**: Follow the [Streamlit Heroku deployment guide](https://docs.streamlit.io/knowledge-base/tutorials/deploy/heroku)
- **AWS/GCP/Azure**: Use container deployment with the provided requirements
- **Local Network**: Run locally and access via network IP

## 📈 Usage Guide

### Basic Operation

1. **Adjust Parameters**: Use the sidebar to modify:
   - Initial Investment
   - Monthly Fixed Costs
   - Variable Cost per User
   - Subscription Price
   - New Users per Month
   - Monthly Churn Rate
   - Simulation Duration

2. **Run Simulation**: Click the "🚀 Run Simulation" button

3. **Analyze Results**: Review the key metrics and interactive charts

### Parameter Definitions

| Parameter | Description | Default Value |
|-----------|-------------|---------------|
| Initial Investment | Upfront development & setup costs | $150,000 |
| Monthly Fixed Costs | Recurring costs (salaries, rent, etc.) | $15,000 |
| Variable Cost/User | Per-user monthly costs (servers, support) | $5.00 |
| Subscription Price | Monthly price per user | $25.00 |
| New Users/Month | Monthly user acquisition rate | 200 |
| Monthly Churn Rate | Percentage of users lost monthly | 3% |
| Simulation Duration | Analysis timeframe in months | 48 |

## 🧮 Financial Model Details

### Core Calculations

1. **Churned Users** = Active Subscribers × Monthly Churn Rate
2. **Active Subscribers** = Previous Month + New Users - Churned Users
3. **MRR** = Active Subscribers × Monthly Subscription Price
4. **Monthly Costs** = Fixed Costs + (Active Subscribers × Variable Cost)
5. **Monthly Profit** = MRR - Monthly Costs
6. **Cumulative Profit** = Running total including initial investment
7. **Gross Margin** = (MRR - Variable Costs) / MRR

### Break-Even Analysis

The simulation identifies the exact month when cumulative profit becomes positive, accounting for:
- Initial investment recovery
- Ongoing operational costs
- Subscriber growth and churn dynamics

## 📊 Visualization Features

- **Cumulative Profit/Loss**: Track overall financial performance
- **Monthly Recurring Revenue**: Monitor subscription revenue growth
- **Active Subscribers**: Visualize user base evolution
- **Gross Margin Trends**: Analyze profitability efficiency

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Use Cases

- **Startup Financial Planning**: Model different pricing strategies
- **Investor Presentations**: Demonstrate financial projections
- **Business Strategy**: Analyze impact of churn and acquisition rates
- **Funding Requirements**: Calculate investment needs for break-even
- **Sensitivity Analysis**: Test various market scenarios

## 🔍 Technical Details

### Built With
- **Streamlit**: Web application framework
- **Plotly**: Interactive data visualization
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations

### Architecture
- **Modular Design**: Separate simulation logic from UI
- **Object-Oriented**: Clean class-based structure
- **Responsive UI**: Adapts to different screen sizes
- **Real-time Updates**: Interactive parameter changes

## 📞 Support

- **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/yourusername/virgil-financial-simulator/issues)
- **Discussions**: Join conversations in [GitHub Discussions](https://github.com/yourusername/virgil-financial-simulator/discussions)
- **Email**: Contact us at support@virgil-simulator.com

## 🗺️ Roadmap

- [ ] Multi-scenario comparison
- [ ] Monte Carlo simulation
- [ ] Advanced sensitivity analysis
- [ ] Export to Excel/PDF reports
- [ ] API integration for real-time data
- [ ] Team collaboration features

---

**Made with ❤️ for the Virgil Health Assistant Project** 