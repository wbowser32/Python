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
    L = ""
    for character in C:
        if character.isalnum():
            L += character
    P = list(L)
    P[16] = "6"
    O = "".join(P)
    M = list(C)
    M[21] = "6"
    N = "".join(M)
    template = "<?xml version= \"1.0\" encoding= \"UTF-8\"?> \n\
        <MercentFeed> \n\
         <OrderFulfillment> \n\
         <ChannelOrderID>{}</ChannelOrderID> \n\
         <ChannelName>{}</ChannelName> \n\
         <FulfillmentDate>{}</FulfillmentDate> \n\
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
        </MercentFeed>".format(A, B, N, D, E, F, G, H, I, J, K)
    filename = "C:\\Users\\BowDa001\\Desktop\\New File\\OrderFulfillment_{}_{}_{}.xml".format(B, A, O)
    file = open(filename, "x")
    file.write(template)
    file.close