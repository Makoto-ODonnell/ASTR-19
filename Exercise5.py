import numpy as np


def main():
    from astropy.table import Table
    mytable = Table()
    x = np.linspace(0, 2*np.pi, 1000)
    mytable['x'] = x
    mytable['sin x'] = np.sin(x)
    print(mytable)
    
    
if __name__ == "__main__":
    main()
