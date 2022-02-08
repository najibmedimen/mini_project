
from mini_project_functions import file_opener, display_list_by_index, file_writer, file_writer2, print_products_menu, print_main_menu
from mini_project_functions import print_product_sub_menu, print_couriers_menu, print_orders_menu
from mini_project_functions import return_list, delete_item_from_list, update_listitem_by_name
products  = file_opener("products.txt")
couriers = file_opener("couriers.txt")

def update_listitem_by_name(products, product_name,new_name):
        earlier_index_of_product = return_list(products).index(product_name)
        print(earlier_index_of_product)
        products[earlier_index_of_product] = new_name
        print(products)
courier_name  = "john sena"
new_name  = "james burke"
update_listitem_by_name(couriers, courier_name,new_name)