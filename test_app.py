import unittest
from app import FinancialSimulator

class TestFinancialSimulator(unittest.TestCase):
    
    def setUp(self):
        self.simulator = FinancialSimulator()
    
    def test_basic_simulation(self):
        """Test basic simulation with default parameters"""
        results = self.simulator.run_simulation(
            initial_investment=150000,
            monthly_fixed_costs=15000,
            variable_cost_per_user=5,
            monthly_subscription_price=25,
            new_users_per_month=200,
            monthly_churn_rate=0.03,
            simulation_timeframe_months=48
        )
        
        # Check that results are returned
        self.assertIsNotNone(results)
        
        # Check required keys exist
        required_keys = [
            'break_even_month', 'subscribers_at_break_even', 'reached_break_even',
            'final_active_subscribers', 'final_mrr', 'final_cumulative_profit',
            'final_net_margin', 'total_revenue', 'monthly_data'
        ]
        
        for key in required_keys:
            self.assertIn(key, results)
        
        # Check monthly data structure
        monthly_data = results['monthly_data']
        self.assertIn('months', monthly_data)
        self.assertIn('mrr', monthly_data)
        self.assertIn('profit_loss', monthly_data)
        self.assertIn('cumulative_profit_loss', monthly_data)
        self.assertIn('active_subscribers', monthly_data)
        self.assertIn('gross_margin', monthly_data)
        
        # Check data consistency
        self.assertEqual(len(monthly_data['months']), 48)
        self.assertEqual(len(monthly_data['mrr']), 48)
        
    def test_break_even_logic(self):
        """Test break-even detection logic"""
        # Test scenario that should reach break-even quickly
        results = self.simulator.run_simulation(
            initial_investment=10000,  # Lower initial investment
            monthly_fixed_costs=5000,   # Lower fixed costs
            variable_cost_per_user=2,
            monthly_subscription_price=30,  # Higher price
            new_users_per_month=300,    # More users
            monthly_churn_rate=0.01,    # Lower churn
            simulation_timeframe_months=24
        )
        
        # Should reach break-even in this scenario
        self.assertTrue(results['reached_break_even'])
        self.assertIsNotNone(results['break_even_month'])
        self.assertIsNotNone(results['subscribers_at_break_even'])
        
    def test_no_break_even_scenario(self):
        """Test scenario that doesn't reach break-even"""
        results = self.simulator.run_simulation(
            initial_investment=500000,  # Very high initial investment
            monthly_fixed_costs=50000,  # Very high fixed costs
            variable_cost_per_user=20,  # High variable costs
            monthly_subscription_price=10,  # Low price
            new_users_per_month=50,     # Few users
            monthly_churn_rate=0.1,     # High churn
            simulation_timeframe_months=12
        )
        
        # Should not reach break-even
        self.assertFalse(results['reached_break_even'])
        self.assertIsNone(results['break_even_month'])
        self.assertIsNone(results['subscribers_at_break_even'])
        
    def test_edge_cases(self):
        """Test edge cases and boundary conditions"""
        # Test zero churn rate
        results = self.simulator.run_simulation(
            initial_investment=100000,
            monthly_fixed_costs=10000,
            variable_cost_per_user=5,
            monthly_subscription_price=25,
            new_users_per_month=100,
            monthly_churn_rate=0.0,  # No churn
            simulation_timeframe_months=12
        )
        
        # Should have growing subscriber base with no churn
        final_subscribers = results['final_active_subscribers']
        expected_subscribers = 100 * 12  # 100 users per month for 12 months
        self.assertEqual(final_subscribers, expected_subscribers)
        
    def test_financial_calculations(self):
        """Test accuracy of financial calculations"""
        results = self.simulator.run_simulation(
            initial_investment=0,  # No initial investment for easier testing
            monthly_fixed_costs=1000,
            variable_cost_per_user=5,
            monthly_subscription_price=20,
            new_users_per_month=100,
            monthly_churn_rate=0.0,  # No churn for predictable results
            simulation_timeframe_months=3
        )
        
        monthly_data = results['monthly_data']
        
        # Month 1: 100 subscribers
        # MRR = 100 * 20 = 2000
        # Costs = 1000 + (100 * 5) = 1500
        # Profit = 2000 - 1500 = 500
        self.assertEqual(monthly_data['active_subscribers'][0], 100)
        self.assertEqual(monthly_data['mrr'][0], 2000)
        self.assertEqual(monthly_data['profit_loss'][0], 500)
        
        # Month 2: 200 subscribers
        self.assertEqual(monthly_data['active_subscribers'][1], 200)
        self.assertEqual(monthly_data['mrr'][1], 4000)
        self.assertEqual(monthly_data['profit_loss'][1], 2000)

if __name__ == '__main__':
    unittest.main() 