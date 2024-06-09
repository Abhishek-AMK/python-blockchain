from block import Block

# Description: A simple blockchain implementation in Python
class Blockchain:
    """
    Blockchain: A public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions
    """
    def __init__(self):
        self.chain = []
        
    def add_block(self, data):
        self.chain.append(Block(data))
        
    def __repr__(self):
        return f'Blockchain: {self.chain}'

def main():        
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')

    print(blockchain)

    print(f'blockchain.py __name__: {__name__}')
    
if __name__ == '__main__':
    main()

