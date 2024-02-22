import streamlit as st
import requests

_name_ = "_main_"

currency = {
    "IDR" : {
        "Rupiah" : {
            "Seratus Ribu" : {100000 : 0},
            "Lima Puluh Ribu" :{50000 : 0},
            "Dua Puluh Ribu" : {20000 : 0},
            "Sepuluh Ribu" : {10000 : 0},
            "Lima Ribu" : {5000 : 0},
            "Dua Ribu" : {2000 : 0},
            "Seribu" : {1000 : 0},
            "Lima Ratus" : {500 : 0},
            "Dua Ratus" : {200 : 0},
            "Seratus" : {100 : 0},
        },
    },
    "USD" :  { 
        "Dollar" : {
            "Seratus" : {100 : 0},
            "Lima Puluh" :{50 : 0},
            "Dua Puluh" : {20 : 0},
            "Sepuluh" : {10 : 0},
            "Lima" : {5 : 0},
            "Dua" : {2 : 0},
            "Satu" : {1 : 0}
        },
    },
    "AUD" : {
        "Dollar" : {
            "Seratus" : {100 : 0},
            "Lima Puluh" :{50 : 0},
            "Dua Puluh" : {20 : 0},
            "Sepuluh" : {10 : 0},
            "Lima" : {5 : 0},
            "Dua" : {2 : 0},
            "Satu" : {1 : 0}
        },
    },
    "JPY" : {
        "Yen" : {
            "Sepuluh Ribu" : {10000 : 0},
            "Lima Ribu" : {5000 : 0},
            "Dua Ribu" : {2000 : 0},
            "Seribu" : {1000 : 0},
            "Lima Ratus" : {500 : 0},
            "Seratus" : {100 : 0},
            "Lima Puluh" : {50 : 0},
            "Sepuluh" : {10 : 0},
            "Lima" : {5 : 0},
            "Satu" : {1 : 0}
        }
    },
    "SGD" : {
        "Dollar" : {
            "Sepuluh Ribu" : {10000 : 0},
            "Seribu" : {1000 : 0},
            "Seratus" : {100 : 0},
            "Lima Puluh" :{50 : 0},
            "Dua Puluh" : {20 : 0},
            "Sepuluh" : {10 : 0},
            "Lima" : {5 : 0},
            "Dua" : {2 : 0},
            "Satu" : {1 : 0}
        },
    },
    "CAD" : {
        "Dollar" : {
            "Seratus" : {100 : 0},
            "Lima Puluh" :{50 : 0},
            "Dua Puluh" : {20 : 0},
            "Sepuluh" : {10 : 0},
            "Lima" : {5 : 0},
            "Dua" : {2 : 0},
            "Satu" : {1 : 0}
        },
    },
    "EUR" : {
        "Euro" : {
            "Dua Ratus" : {200 : 0},
            "Seratus" : {100 : 0},
            "Lima Puluh" :{50 : 0},
            "Dua Puluh" : {20 : 0},
            "Sepuluh" : {10 : 0},
            "Lima" : {5 : 0},
            "Dua" : {2 : 0},
            "Satu" : {1 : 0}
        },
    },
    "GBP" : {
       "Pound" : {
            "Seratus" : {100 : 0},
            "Lima Puluh" :{50 : 0},
            "Dua Puluh" : {20 : 0},
            "Sepuluh" : {10 : 0},
            "Lima" : {5 : 0},
            "Dua" : {2 : 0},
            "Satu" : {1 : 0}
       } ,
    },
    "CNY" : {
        "Yuan" : {
            "Seratus" : {100 : 0},
            "Lima Puluh" :{50 : 0},
            "Dua Puluh" : {20 : 0},
            "Sepuluh" : {10 : 0},
            "Lima" : {5 : 0},
            "Dua" : {2 : 0},
            "Satu" : {1 : 0},
        }
    },
    "KRW" : {
        "Won" : {
            "Lima Puluh Ribu" : {50000 : 0},
            "Sepuluh Ribu" : {10000 : 0},
            "Lima Ribu" : {5000 : 0},
            "Seribu" : {1000 : 0},
            "Lima Ratus" : {500 : 0},
            "Seratus" : {100 : 0},
            "Lima Puluh" : {50 : 0},
            "Sepuluh" : {10 : 0}
        }
    }
}

def getExchangeRate (fromCurrency, toCurrency) :
    api_url = (f'https://api.frankfurter.app/latest?amount=1&from={fromCurrency}&{toCurrency}')
    response = requests.get(api_url)
    exchangeRate = float(response.json()['rates'][toCurrency])
    return exchangeRate

def convertMoney():
    currencyList = list(currency.keys())
    jumlah = 0

    st.title("Konversi Uang")

    fromCurrency = st.selectbox("Pilih mata uang asal:", currencyList)
    toCurrency = st.selectbox("Pilih mata uang tujuan:", currencyList)

    for x in currency[fromCurrency]:
        for y in currency[fromCurrency][x]:
            for z in currency[fromCurrency][x][y]:
                currency[fromCurrency][x][y][z] = st.number_input(
                    f"Jumlah pecahan {y} {x}: ", step=1
                )

    for x in currency[fromCurrency]:
        for y in currency[fromCurrency][x]:
            for z in currency[fromCurrency][x][y]:
                jumlah = float(jumlah) + float(
                    float(z) * float(currency[fromCurrency][x][y][z])
                )
                currency[fromCurrency][x][y][z] = 0

    exchangeRate = getExchangeRate(fromCurrency, toCurrency)
    hasil = round(jumlah * exchangeRate, 2)

    st.write(f"Exchange Rate dari {fromCurrency} ke {toCurrency} :", "{:f}".format(exchangeRate))
    st.write(f"Hasil konversi {jumlah} {fromCurrency} ke {toCurrency} adalah {hasil}")
    minChanges(hasil, toCurrency)


def minChanges(hasil, toCurrency):
    denoList = []
    denoListNames = []
    ans = []

    for x in currency[toCurrency]:
        for y in currency[toCurrency][x]:
            for z in currency[toCurrency][x][y]:
                denoListNames.append(y)
                denoList.append(z)

    n = len(denoList)
    i = 0

    while (i < n):
        while (hasil >= denoList[i]):
            hasil -= denoList[i]
            ans.append(denoListNames[i])
        i += 1

    for x in currency[toCurrency]:
        for y in currency[toCurrency][x]:
            for z in currency[toCurrency][x][y]:
                for i in range(len(ans)):
                    if (ans[i] == y):
                        currency[toCurrency][x][y][z] += 1

    st.write("Uang yang diberikan : ")
    for x in currency[toCurrency]:
        for y in currency[toCurrency][x]:
            for z in currency[toCurrency][x][y]:
                if (currency[toCurrency][x][y][z] != 0):
                    st.write(f"Pecahan {y} {x} sebanyak : {currency[toCurrency][x][y][z]}")
                    currency[toCurrency][x][y][z] = 0


def showExchangeRate():
    st.header("Cek Exchange Rate")
    
    currency_list = list(currency.keys())
    currency_list.remove(RateCurrency)
    
    for toCurrency in currency_list:
        exchange_rate = getExchangeRate(RateCurrency, toCurrency)
        exchange_rate = float(exchange_rate)
        st.write(f"Exchange rate dari {RateCurrency} ke {toCurrency} adalah :","{:f}".format(exchange_rate))

if __name__ == "__main__":
    st.title("Money Changer")


    menu_option = st.sidebar.radio("Select Option", ["Convert Money", "Check Exchange Rate"])

    if menu_option == "Convert Money":  
        convertMoney()
    elif menu_option == "Check Exchange Rate":
        RateCurrency = st.selectbox("Pilih mata uang asal Exchange Rate:", list(currency.keys()))
        showExchangeRate()