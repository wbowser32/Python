import pandas as pd
#ChannelOrderID	ChannelName	FulfillmentDate	Carrier	ShippingTrackingNumber	ShippingMethod	ShippingTrackingURL	ChannelOrderItemID	MerchantOrderItemID	SKU	Quantity

path = "C:\\Users\\BowDa001\\Desktop\\New File\\BaseFile.xlsx"
data = pd.read_excel(path)

for label, row in data.iterrows():
    A = row["ChannelOrderID"]
    B = row["ChannelName"]
    C = row["FulfillmentDate"]
    D = row["Carrier"]
    E = row["ShippingTrackingNumber"]
    F = row["ShippingMethod"]
    G = row["ShippingTrackingURL"]
    H = row["ChannelOrderItemID"]
    I = row["MerchantOrderItemID"]
    J = row["SKU"]
    K = row["Quantity"]
    template = "<?xml version=""1.0"" encoding=""UTF-8""?> \n\
        <MercentFeed> \n\
         <OrderFulfillment> \n\
         <ChannelOrderID>{}</ChannelOrderID> \n\
         <ChannelName>{}</ChannelName> \n\
         <FulfillmentDate>{}-06:00</FulfillmentDate> \n\
         <FulfillmentData> \n\
          <Carrier>{}</Carrier> \n\
          <ShippingTrackingNumber>{}</ShippingTrackingNumber> \n\
          <ShippingMethod>{}</ShippingMethod> \n\
          <ShippingTrackingURL>{}</ShippingTrackingURL> \n\
         </FulfillmentData> \n\
         <Item> \n\
           <ChannelOrderItemID>{}</ChannelOrderItemID> \n\
           <MerchantOrderItemID>{}</MerchantOrderItemID> \n\
           <SKU>{}</SKU> \n\
           <Quantity>{}</Quantity> \n\
          </Item> \n\
         </OrderFulfillment> \n\
        </MercentFeed>".format(A, B, C, D, E, F, G, H, I, J, K)
    filename = "C:\\Users\\BowDa001\\Desktop\\New File\\OrderAdjustment_{}_{}_{}.xml".format(B, A, C)
    file = open(filename, "x")
    file.write(template)
    file.close