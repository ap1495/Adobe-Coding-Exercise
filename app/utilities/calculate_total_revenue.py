def calculate_total_revenue(event_list_str, product_list_str):
    total_revenue = 0.0
    if event_list_str is None:
        print('ts', total_revenue)
        return total_revenue
    
    event_list = event_list_str.split(',')
    if '1' in event_list:
        products = product_list_str.split(',')
        for product in products:
            product_information_list = product.split(';')
            print(product_information_list)
            if product_information_list[2] != '' and product_information_list[3] != '':
                total_revenue += (float(product_information_list[2]) * float(product_information_list[3]))
        
        return total_revenue