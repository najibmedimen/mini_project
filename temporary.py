from mini_project_functions import file_opener, display_list, file_writer, file_writer2, print_products_menu, print_main_menu
from mini_project_functions import print_product_sub_menu, print_couriers_menu, print_orders_menu
products = file_opener("products.txt")

#items = file_opener("products.txt")
#display_list(items)
#display_list(file_opener("products.txt"))
#file_writer('products.txt', 'milkoo')
#file_writer2('products.txt', 'milkoo')
print_main_menu()
print_products_menu()
print_product_sub_menu()
print_couriers_menu()
print_orders_menu()
#display_list(products)
#
#product_list_length = len(products)
#product_input = int(input(f'\n Choose an Index Position to Add New Product.\n'))
#new_product_suggestion = input(f'\nSuggest a Name for The New Product.\n')
#file_writer("products.txt", new_product_suggestion)
##products.insert(product_input-1, new_product_suggestion)
#display_list(products)
