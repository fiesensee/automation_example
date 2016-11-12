## Example for automating ERPNext workflow between documents

This small example app tries to show how a simple automation of the worklflow from purchase order to a finished manufacturing could be done. 

#### This is not a production ready automation app!

Nevertheless, here is how to install it:
1. _from your frappe-bench folder:_ `bench get-app automation_example https://github.com/fiesensee/automation_example`
2. `bench --site [site_name] install-app automation-example
3. go into `apps/erpnext/erpnext/hooks.py` and under doc_events add the following hooks:
```
"Sales Order": {
    "on_submit": "automation_example.automation_example.automation.make_manufacture_order"
},
"Material Request": {
    "on_submit" "automation_example.automation_example.automation.make_production_orders"
},
"Production Order": {
    "on_submit": "automation_example.automation_example.automation.start_production_order"
}
```

Now when you submit a purchase order, either from the desk or after a customer orders a item from your shop, it will automatically create and submit a stock entry with the "manufacture" purpose. This will start to make all needed production orders, assuming that the item that was just bought is one that gets manufactured with the bom-feature. Then the production orders also will get finished while also creating all needed stock entries.
As I said, this is not a ready-for-production app, it's a mere example to show how automation can look.

#### Further reading

[hooks](https://frappe.github.io/frappe/user/en/guides/basics/hooks)

[database](https://frappe.github.io/frappe/current/api/frappe.database)

[document](https://frappe.github.io/frappe/current/api/model/frappe.model.document)

#### License

MIT
