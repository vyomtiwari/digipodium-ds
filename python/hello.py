def smallestStockPrice(stock, valuek):
    stock.sort()
    return stock[valuek]




def main():

    stock= []
    stock_size = int(input(()))
    stock = list(map(int,input().split()))
    k = int(input())
    print(smallestStockPrice(stock,k))

if __name__ == "__main__":
    main()