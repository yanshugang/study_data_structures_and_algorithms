import votesmart

votesmart.apikey = '49024thereoncewasamanfromnantucket94040'
bills = votesmart.votes.getBillsByStateRecent()
for i in bills:
    print(i)