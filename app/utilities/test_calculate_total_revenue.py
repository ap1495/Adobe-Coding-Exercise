from app.utilities.calculate_total_revenue import calculate_total_revenue

def test_calculate_total_revenue_when_purchase_is_set():
    event_list = "1"
    product_list = "Electronics;Ipod - Touch - 32GB;1;290;"
    
    assert 290 == calculate_total_revenue(event_list, product_list)
    
def test_calculate_total_revenue_when_purchase_event_is_not_set():
    event_list = "2"
    product_list = "Electronics;Ipod - Touch - 32GB;1;290;"
    
    assert 0 == calculate_total_revenue(event_list, product_list)