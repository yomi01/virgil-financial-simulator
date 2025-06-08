import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import FuncFormatter
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page configuration
st.set_page_config(
    page_title="Virgil Financial Simulator",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

class FinancialSimulator:
    """Class to handle the financial simulation logic"""
    
    def __init__(self):
        self.results = None
    
    def run_simulation(self, initial_investment, monthly_fixed_costs, variable_cost_per_user,
                      monthly_subscription_price, new_users_per_month, monthly_churn_rate,
                      simulation_timeframe_months):
        """
        Runs the MVP financial simulation for the AI health assistant app.
        
        Returns:
            dict: A dictionary containing simulation results.
        """
        
        active_subscribers = 0
        cumulative_profit_loss = -initial_investment
        total_revenue = 0
        
        # Lists to store monthly data
        months = list(range(1, simulation_timeframe_months + 1))
        mrr_monthly = []
        profit_loss_monthly = []
        cumulative_profit_loss_monthly = [cumulative_profit_loss]
        active_subscribers_monthly = [0]
        gross_margin_monthly = []
        
        break_even_month = None
        subscribers_at_break_even = None
        reached_break_even = False
        
        for month in months:
            # Calculate churned users
            churned_users = round(active_subscribers * monthly_churn_rate)
            
            # Update active subscribers
            active_subscribers = active_subscribers + new_users_per_month - churned_users
            if active_subscribers < 0:
                active_subscribers = 0
            
            # Calculate MRR
            mrr = active_subscribers * monthly_subscription_price
            total_revenue += mrr
            
            # Calculate costs
            total_variable_costs = active_subscribers * variable_cost_per_user
            total_monthly_costs = monthly_fixed_costs + total_variable_costs
            
            # Calculate profit/loss
            monthly_profit_loss = mrr - total_monthly_costs
            cumulative_profit_loss += monthly_profit_loss
            
            # Calculate gross margin
            gross_profit = mrr - total_variable_costs
            monthly_gross_margin = (gross_profit / mrr) if mrr > 0 else 0
            
            # Store data
            mrr_monthly.append(mrr)
            profit_loss_monthly.append(monthly_profit_loss)
            cumulative_profit_loss_monthly.append(cumulative_profit_loss)
            active_subscribers_monthly.append(active_subscribers)
            gross_margin_monthly.append(monthly_gross_margin)
            
            # Check break-even
            if not reached_break_even and cumulative_profit_loss >= 0:
                reached_break_even = True
                break_even_month = month
                subscribers_at_break_even = active_subscribers
        
        # Calculate final metrics
        final_active_subscribers = active_subscribers_monthly[-1]
        final_mrr = mrr_monthly[-1] if mrr_monthly else 0
        final_cumulative_profit = cumulative_profit_loss_monthly[-1]
        final_net_margin = (final_cumulative_profit / total_revenue) if total_revenue > 0 else 0
        
        self.results = {
            "break_even_month": break_even_month,
            "subscribers_at_break_even": subscribers_at_break_even,
            "reached_break_even": reached_break_even,
            "final_active_subscribers": final_active_subscribers,
            "final_mrr": final_mrr,
            "final_cumulative_profit": final_cumulative_profit,
            "final_net_margin": final_net_margin,
            "total_revenue": total_revenue,
            "monthly_data": {
                "months": months,
                "mrr": mrr_monthly,
                "profit_loss": profit_loss_monthly,
                "cumulative_profit_loss": cumulative_profit_loss_monthly[1:],
                "active_subscribers": active_subscribers_monthly[1:],
                "gross_margin": gross_margin_monthly
            }
        }
        
        return self.results
    
    def create_plots(self):
        """Create interactive plots using Plotly"""
        if not self.results:
            return None
        
        data = self.results["monthly_data"]
        
        # Create subplots
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Cumulative Profit/Loss', 'Monthly Recurring Revenue', 
                          'Active Subscribers', 'Monthly Gross Margin'),
            specs=[[{"secondary_y": False}, {"secondary_y": False}],
                   [{"secondary_y": False}, {"secondary_y": False}]]
        )
        
        # Cumulative Profit/Loss
        fig.add_trace(
            go.Scatter(x=data["months"], y=data["cumulative_profit_loss"],
                      mode='lines+markers', name='Cumulative P&L', line=dict(color='blue')),
            row=1, col=1
        )
        
        # Break-even line
        fig.add_hline(y=0, line_dash="dash", line_color="red", row=1, col=1)
        
        # MRR
        fig.add_trace(
            go.Scatter(x=data["months"], y=data["mrr"],
                      mode='lines+markers', name='MRR', line=dict(color='green')),
            row=1, col=2
        )
        
        # Active Subscribers
        fig.add_trace(
            go.Scatter(x=data["months"], y=data["active_subscribers"],
                      mode='lines+markers', name='Subscribers', line=dict(color='purple')),
            row=2, col=1
        )
        
        # Gross Margin
        gross_margin_percent = [m * 100 for m in data["gross_margin"]]
        fig.add_trace(
            go.Scatter(x=data["months"], y=gross_margin_percent,
                      mode='lines+markers', name='Gross Margin %', line=dict(color='orange')),
            row=2, col=2
        )
        
        fig.update_layout(height=600, showlegend=False, title_text="Financial Simulation Dashboard")
        fig.update_xaxes(title_text="Month")
        fig.update_yaxes(title_text="Amount ($)", row=1, col=1)
        fig.update_yaxes(title_text="Amount ($)", row=1, col=2)
        fig.update_yaxes(title_text="Count", row=2, col=1)
        fig.update_yaxes(title_text="Percentage (%)", row=2, col=2)
        
        return fig

def main():
    # Header
    st.title("💰 Virgil Financial Simulator")
    st.markdown("---")
    st.markdown("### AI Health Assistant - Business Model Analysis")
    
    # Initialize simulator
    simulator = FinancialSimulator()
    
    # Sidebar for inputs
    st.sidebar.header("📊 Simulation Parameters")
    st.sidebar.markdown("Adjust the parameters below to run different scenarios:")
    
    # Input widgets
    initial_investment = st.sidebar.number_input(
        "Initial Investment ($)", 
        min_value=0.0, 
        value=150000.0, 
        step=1000.0,
        help="Total upfront development & setup cost"
    )
    
    monthly_fixed_costs = st.sidebar.number_input(
        "Monthly Fixed Costs ($)", 
        min_value=0.0, 
        value=15000.0, 
        step=500.0,
        help="Combined recurring fixed costs per month (salaries, rent, etc.)"
    )
    
    variable_cost_per_user = st.sidebar.number_input(
        "Variable Cost per User/Month ($)", 
        min_value=0.0, 
        value=5.0, 
        step=0.5,
        help="Combined variable cost per active user per month"
    )
    
    monthly_subscription_price = st.sidebar.number_input(
        "Subscription Price/Month ($)", 
        min_value=0.0, 
        value=25.0, 
        step=1.0,
        help="Price per user per month"
    )
    
    new_users_per_month = st.sidebar.number_input(
        "New Users per Month", 
        min_value=0, 
        value=200, 
        step=10,
        help="Number of new paying users acquired each month"
    )
    
    monthly_churn_rate = st.sidebar.number_input(
        "Monthly Churn Rate", 
        min_value=0.0, 
        max_value=1.0, 
        value=0.03, 
        step=0.001, 
        format="%.3f",
        help="Percentage of users lost each month (e.g., 0.03 = 3%)"
    )
    
    simulation_timeframe_months = st.sidebar.number_input(
        "Simulation Duration (Months)", 
        min_value=1, 
        value=48, 
        step=1,
        help="Duration of the simulation in months"
    )
    
    # Run simulation button
    if st.sidebar.button("🚀 Run Simulation", type="primary"):
        # Validation
        if monthly_subscription_price <= variable_cost_per_user:
            st.warning("⚠️ Warning: Subscription price should ideally be greater than variable cost per user.")
        
        # Run simulation
        with st.spinner("Running simulation..."):
            results = simulator.run_simulation(
                initial_investment=initial_investment,
                monthly_fixed_costs=monthly_fixed_costs,
                variable_cost_per_user=variable_cost_per_user,
                monthly_subscription_price=monthly_subscription_price,
                new_users_per_month=new_users_per_month,
                monthly_churn_rate=monthly_churn_rate,
                simulation_timeframe_months=simulation_timeframe_months
            )
        
        # Display results
        st.success("✅ Simulation completed!")
        
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Final Subscribers", 
                f"{results['final_active_subscribers']:,}",
                help="Total active subscribers at end of simulation"
            )
        
        with col2:
            st.metric(
                "Final MRR", 
                f"${results['final_mrr']:,.0f}",
                help="Monthly Recurring Revenue at end of simulation"
            )
        
        with col3:
            profit_color = "normal" if results['final_cumulative_profit'] >= 0 else "inverse"
            st.metric(
                "Cumulative Profit", 
                f"${results['final_cumulative_profit']:,.0f}",
                help="Total profit/loss over simulation period"
            )
        
        with col4:
            if results['reached_break_even']:
                st.metric(
                    "Break-Even Month", 
                    f"{results['break_even_month']}",
                    help="Month when cumulative profit becomes positive"
                )
            else:
                st.metric("Break-Even", "Not Reached", help="Break-even not achieved in timeframe")
        
        # Additional metrics
        st.markdown("### 📈 Additional Metrics")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "Net Profit Margin", 
                f"{results['final_net_margin']:.1%}",
                help="Final cumulative profit as % of total revenue"
            )
        
        with col2:
            st.metric(
                "Total Revenue", 
                f"${results['total_revenue']:,.0f}",
                help="Total revenue generated over simulation period"
            )
        
        with col3:
            if results['reached_break_even']:
                st.metric(
                    "Subscribers at Break-Even", 
                    f"{results['subscribers_at_break_even']:,}",
                    help="Number of subscribers when break-even was reached"
                )
        
        # Charts
        st.markdown("### 📊 Financial Dashboard")
        fig = simulator.create_plots()
        if fig:
            st.plotly_chart(fig, use_container_width=True)
        
        # Data table
        with st.expander("📋 View Detailed Monthly Data"):
            df = pd.DataFrame({
                'Month': results['monthly_data']['months'],
                'Active Subscribers': results['monthly_data']['active_subscribers'],
                'MRR ($)': results['monthly_data']['mrr'],
                'Monthly P&L ($)': results['monthly_data']['profit_loss'],
                'Cumulative P&L ($)': results['monthly_data']['cumulative_profit_loss'],
                'Gross Margin (%)': [f"{m:.1%}" for m in results['monthly_data']['gross_margin']]
            })
            st.dataframe(df, use_container_width=True)
    
    # About section
    with st.expander("ℹ️ About This Simulation"):
        st.markdown("""
        This financial simulation models the performance of Virgil, an AI-powered health assistant 
        for autoimmune conditions, as a subscription-based service.
        
        **Key Calculations:**
        - **Churned Users**: Active Subscribers × Monthly Churn Rate
        - **Active Subscribers**: Previous + New Users - Churned Users
        - **Monthly Recurring Revenue (MRR)**: Active Subscribers × Subscription Price
        - **Monthly Profit/Loss**: MRR - (Fixed Costs + Variable Costs)
        - **Cumulative Profit/Loss**: Running total including initial investment
        - **Gross Margin**: (MRR - Variable Costs) / MRR
        
        **Break-Even Point**: When cumulative profit/loss becomes positive
        """)

if __name__ == "__main__":
    main() 