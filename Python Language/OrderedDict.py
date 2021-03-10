from collections import OrderedDict
def main():
    n = int(input())
    Ordered_Dist = OrderedDict()
    for i in range(n):
        item_price = list(map(str, input().split()))
        item_name = (" ".join(item_price[:-1]))
        if item_name not in Ordered_Dist:
            Ordered_Dist[item_name] = int(item_price[-1]) 
        else:
            Ordered_Dist[item_name] = int(item_price[-1]) + Ordered_Dist[item_name]

    for i in Ordered_Dist:
        print(i,Ordered_Dist[i])
        
    
    
if __name__ == "__main__":
    main()

