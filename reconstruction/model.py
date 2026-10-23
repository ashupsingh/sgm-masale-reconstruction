"""New reconstruction, 2026-10-23. Demo inputs are synthetic, not historical results."""
class OrderLedger:
    def __init__(self):self.prices={'turmeric':10000,'cumin':8000};self.orders={}
    def create(self,order_id,cart):
        if order_id in self.orders:raise ValueError('Duplicate order')
        if not cart:raise ValueError('Empty cart')
        total=0
        for sku,quantity in cart.items():
            if sku not in self.prices or type(quantity) is not int or not 1<=quantity<=100:raise ValueError('Invalid cart')
            total+=self.prices[sku]*quantity
        self.orders[order_id]={'paise':total,'status':'pending'}
        return dict(self.orders[order_id])
    def settle(self,order_id,amount,signature_verified=False):
        order=self.orders[order_id]
        if not signature_verified or amount!=order['paise']:raise PermissionError('Payment not verified')
        order['status']='paid';return dict(order)
def demo():
    c=OrderLedger();assert c.create('demo',{'turmeric':2})['paise']==20000
    try:c.settle('demo',1,True);raise AssertionError('Wrong amount accepted')
    except PermissionError:pass
    assert c.settle('demo',20000,True)['status']=='paid'
    return {'illustrative_prices_only':True,'real_payment_integration':False}

if __name__ == "__main__":
    import json
    print(json.dumps(demo(), indent=2))
