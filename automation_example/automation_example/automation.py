import frappe
import datetime
from erpnext.selling.doctype.sales_order.sales_order import make_material_request
from erpnext.stock.doctype.material_request.material_request import raise_production_orders
from erpnext.manufacturing.doctype.production_order.production_order import make_stock_entry

 
#gets called on_submit from purchase order
#leverages the make_material_request function
def make_manufacture_order(sale, method):
    print("making manufacture order")
    manufacture = make_material_request(sale.name)

    today = datetime.date.today()

    manufacture.material_request_type = "Manufacture"
    for item in manufacture.items:
        item.schedule_date = today.isoformat()

    manufacture.insert()
    manufacture.submit()
    manufacture.save()
    print("finished manufacturing order")
    #submits the created production orders
    ponames = frappe.db.get_values("Production Order", {"material_request": manufacture.name}, as_dict=True)
    for poname in ponames:
        po = frappe.get_doc("Production Order", poname["name"])
        po.submit()

#gets called on_submit from material_order 
#calls the raise_production_orders function
def make_production_orders(manufacture, method):
    if(manufacture.material_request_type == "Manufacture"):
        print("making production order") 
        production_orders = raise_production_orders(manufacture.name)

        for production_order in production_orders:
            po = frappe.get_doc("Production Order", production_order)
            po.wip_warehouse = po.fg_warehouse
            po.save()

        print("raised production orders")

#gets called on_submit from production_order
#sets the po to in process through making a "transfer for manufacture" stock entry
#here would be a good point to do some sort of external activation
def start_production_order(production_order, method):
    print("start production order")
    
    stock_entry = make_stock_entry(production_order.name, "Material Transfer for Manufacture")
    stock_entry.save()
    stock_entry.submit()

    finish_production_order(production_order)

#finish production order
#also sends signal for delivery
def finish_production_order(production_order):
    print("finishing production order")
    stock_entry = make_stock_entry(production_order.name, "Manufacture")
    stock_entry.items[1].serial_no = stock_entry.items[0].serial_no
    stock_entry.save()
    stock_entry.submit()
    #call function here to start delivery of finished goods
