
sudo add-apt-repository -y ppa:ethereum/ethereum
sudo apt-get update
sudo apt-get install ethereum


geth --rinkeby --datadir /opt/data/ethereumdata

geth --rinkeby --syncmode light --http
python publish.py