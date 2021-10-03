from app_consts import PURCHASE_EVENT
def calculate_total_revenue(event_list_str, product_list_str):
    """
    Function to calculate revenue from list of events and list of products.

    Parameters
    ----------
    event_list_str : str
        comma separated events string.
    product_list_str : TYPE
        comma separated products string..

    Returns
    -------
    total_revenue : float
        total revenue for a product.

    """
    total_revenue = 0.0
    if event_list_str is None:
        print()
        return total_revenue
    
    event_list = event_list_str.split(',')
    if PURCHASE_EVENT in event_list:
        products = product_list_str.split(',')
        for product in products:
            product_information_list = product.split(';')
            if product_information_list[2] != '' and product_information_list[3] != '':
                total_revenue += (float(product_information_list[2]) * float(product_information_list[3]))
        
        return total_revenue
    
    return total_revenue